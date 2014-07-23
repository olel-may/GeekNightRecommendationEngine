from math import sqrt


def euclidean_distance(rating1, rating2):
    sum_of_squares = 0
    for key in rating1:
        if key in rating2:
            sum_of_squares += pow((rating1[key] - rating2[key]), 2)
    return 1/(1+(sum_of_squares))

	
