from math import sqrt


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
