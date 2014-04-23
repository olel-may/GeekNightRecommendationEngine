from math import sqrt

users = {
	'Daniel': {'m300': 2.5, 'Lord of the Rings': 3.5, 'Django Unchained': 3.5, 'Madagascar': 4.5},
	'Lloyd':  {'m300': 4.5, 'Django Unchained': 4.0, 'Madagascar': 4.0},
	'Steve':  {'m300': 4.5, 'Lord of the Rings': 4.5, 'Django Unchained': 4.5, 'Madagascar': 4.0},
	'Lenny':  {'m300': 4.0, 'Lord of the Rings': 4.0}
}


def convert_product_id_to_name(id):
    """
    Given product id number, return product name
    """
    product_id_to_name = {}
    if id in product_id_to_name:
        return product_id_to_name[id]
    else:
        return id


def cosine_similarity(rating1, rating2):
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

def compute_nearest_neighbor(username):
        """
        Creates a sorted list of users based on their distance to the username
        """
        distances = []
        for instance in users:
            if instance != username:
                distance = cosine_similarity(users[username], users[instance])
                distances.append((instance, distance))
        distances.sort(key=lambda artist_tuple: artist_tuple[1], reverse=True)
        return distances

def recommend(user):
    """Give list of recommendations"""
    user = user
    k_nearest_neighbor_value = 3
    recommendations = {}
    nearest_neighbors = compute_nearest_neighbor(user)
    # now get the ratings for the user
    user_ratings = users[user]
    # determine the total distance
    total_distance = 0.0
    for i in range(k_nearest_neighbor_value):
        total_distance += nearest_neighbors[i][1]
    # Iterate through the k nearest neighbors accumulating their ratings
    for i in range(k_nearest_neighbor_value):
        weight = nearest_neighbors[i][1] / total_distance
        nearest_neighbor_name = nearest_neighbors[i][0]
        nearest_neighbor_ratings = users[nearest_neighbor_name]
        # now find bands neighbor rated that user didn't
        for artist in nearest_neighbor_ratings:
            if not artist in user_ratings:
                if artist not in recommendations:
                    recommendations[artist] = (nearest_neighbor_ratings[artist] * weight)
                else:
                    recommendations[artist] = (recommendations[artist] + nearest_neighbor_ratings[artist] * weight)
    # now make list from dictionary
    recommendations = list(recommendations.items())
    recommendations = [(convert_product_id_to_name(k), v) for (k, v) in recommendations]
    # finally sort and return
    recommendations.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
    return recommendations
    

if __name__ == "__main__":
	print recommend('Lenny')
