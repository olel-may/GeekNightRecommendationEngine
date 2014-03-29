__author__ = 'dolel'

from math import sqrt


class Recommender:
    def __init__(self, data, k_nearest_neighbor_value=1, max_no_of_recommendations=5):
        """
        Initialize Recommender
        Currently, if data is dictionary, the recommender is initialized to it.
        For all other types of data, no initialization occurs
        """
        self.k_nearest_neighbor_value = k_nearest_neighbor_value
        self.max_number_of_recommendations = max_no_of_recommendations
        self.username_to_id = {}
        self.user_id_to_name = {}
        self.product_id_to_name = {}
        # If data is dictionary, set recommender data to it
        if type(data).__name__ == "dict":
            self.data = data
        self.frequencies = {}
        self.deviations = {}

    def convert_product_id_to_name(self, id):
        """
        Given product id number, return product name
        """
        if id in self.product_id_to_name:
            return self.product_id_to_name[id]
        else:
            return id

    def user_ratings(self, id, number_of_top_ratings):
        print "Ratings for ", self.user_id_to_name[id]
        ratings = self.data[id]
        print len(ratings)
        ratings = list(ratings.items())
        ratings = [(self.convert_product_id_to_name(k), v) for (k, v) in ratings]
        ratings.sort(key=lambda artist_tuple: artist_tuple[1], reverse=True)
        ratings = ratings[:number_of_top_ratings]
        for rating in ratings:
            print("%s\t%i" % (rating[0], rating[1]))

    def euclidean_distance(self, rating1, rating2):
        sum_of_squares = 0
        for key in rating1:
            if key in rating2:
                sum_of_squares += pow((rating1[key] - rating2[key]), 2)
        return sqrt(sum_of_squares)

    def pearson_correlation(self, ratings1, ratings2):
        sum_xy = 0
        sum_x = 0
        sum_y = 0
        sum_x2 = 0
        sum_y2 = 0
        number_of_items = 0
        for key in ratings1:
            if key in ratings2:
                number_of_items += 1
                sum_xy += ratings1[key] * ratings2[key]
                sum_x += ratings1[key]
                sum_y += ratings2[key]
                sum_x2 += pow(ratings1[key], 2)
                sum_y2 += pow(ratings2[key], 2)
        if number_of_items == 0:
            return 0
        # now compute denominator
        denominator = (sqrt(sum_x2 - pow(sum_x, 2) / number_of_items) * sqrt(sum_y2 - pow(sum_y, 2) / number_of_items))
        if denominator == 0:
            return 0
        else:
            return (sum_xy - (sum_x * sum_y) / number_of_items) / denominator

    def cosine_similarity(self, rating1, rating2):
        dot_product = 0
        length_of_vector_x = 0
        length_of_vector_y = 0
        for key in rating1:
            if key in rating2:
                dot_product += (rating1[key] * rating2[key])
                length_of_vector_x += pow(rating1[key], 2)
                length_of_vector_y += pow(rating2[key], 2)
        if dot_product == 0 or length_of_vector_x == 0 or length_of_vector_y == 0:
            return 0
        else:
            return dot_product / ((sqrt(length_of_vector_x)) * sqrt(length_of_vector_y))

    def compute_nearest_neighbor(self, username):
        """
        Creates a sorted list of users based on their distance to the username
        """
        distances = []
        for instance in self.data:
            if instance != username:
                distance = self.cosine_similarity(self.data[username], self.data[instance])
                distances.append((instance, distance))
        distances.sort(key=lambda artist_tuple: artist_tuple[1], reverse=True)
        return distances

    def recommend(self, user):
        """Give list of recommendations"""
        recommendations = {}
        nearest_neighbors = self.compute_nearest_neighbor(user)
        # now get the ratings for the user
        user_ratings = self.data[user]
        # determine the total distance
        total_distance = 0.0
        for i in range(self.k_nearest_neighbor_value):
            total_distance += nearest_neighbors[i][1]
        # Iterate through the k nearest neighbors accumulating their ratings
        for i in range(self.k_nearest_neighbor_value):
            weight = nearest_neighbors[i][1] / total_distance
            nearest_neighbor_name = nearest_neighbors[i][0]
            nearest_neighbor_ratings = self.data[nearest_neighbor_name]
            # now find bands neighbor rated that user didn't
            for artist in nearest_neighbor_ratings:
                if not artist in user_ratings:
                    if artist not in recommendations:
                        recommendations[artist] = (nearest_neighbor_ratings[artist] * weight)
                    else:
                        recommendations[artist] = (recommendations[artist] + nearest_neighbor_ratings[artist] * weight)
        # now make list from dictionary
        recommendations = list(recommendations.items())
        recommendations = [(self.convert_product_id_to_name(k), v) for (k, v) in recommendations]
        # finally sort and return
        recommendations.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
        return recommendations[:self.max_number_of_recommendations]

    def compute_deviations(self):
        for user_ratings in self.data.values():
            #for each item & Rating in that set of strings
            for (item, rating) in user_ratings.items():
                self.frequencies.setdefault(item, {})
                self.deviations.setdefault(item, {})
                #For each item2 & rating2 in that set of strings
                for (item2, rating2) in user_ratings.items():
                    if item != item2:
                        #Add Differences between ratings to our computations
                        self.frequencies[item].setdefault(item2, 0)
                        self.deviations[item].setdefault(item2, 0.0)
                        self.frequencies[item][item2] += 1
                        self.deviations[item][item2] += rating - rating2
        for (item, user_ratings) in self.deviations.items():
            for item2 in user_ratings:
                user_ratings[item2] /= self.frequencies[item][item2]

    def slope_one_recommendations(self, user_ratings):
        self.compute_deviations()
        recommendations = {}
        frequencies = {}
        for (user_item, user_rating) in user_ratings.items():
        # for every item in dataset that the user didn't rate
            for (diff_item, diff_ratings) in self.deviations.items():
                if diff_item not in user_ratings and user_item in self.deviations[diff_item]:
                    freq = self.frequencies[diff_item][user_item]
                    recommendations.setdefault(diff_item, 0.0)
                    frequencies.setdefault(diff_item, 0)
                    # add to the running sum representing the numerator of the formula
                    recommendations[diff_item] += (diff_ratings[user_item] + user_rating) * freq
                    # keep a running sum of the frequency of diffitem
                    frequencies[diff_item] += freq
        recommendations = [(self.convert_product_id_to_name(k), v / frequencies[k])
                           for (k, v) in recommendations.items()]
        # finally sort and return
        recommendations.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
        return recommendations
