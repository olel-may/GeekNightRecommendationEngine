from math import sqrt


users = {
    'Daniel': {'m300': 2.5, 'Lord of the Rings': 3.5, 'Django Unchained': 3.5, 'Madagascar': 4.5},
    'Lloyd': {'m300': 4.5, 'Lord of the Rings': 4.5, 'Django Unchained': 4.0, 'Madagascar': 4.0},
    'Steve': {'m300': 4.5, 'Lord of the Rings': 4.5, 'Django Unchained': 4.5, 'Madagascar': 4.0},
    'Lenny': {'m300': 4.0, 'Lord of the Rings': 4.0, 'Django Unchained': 3.5, 'Madagascar': 3.5}
}


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


if __name__ == "__main__":
    print "Cosine Similarity between Users"
    print "\nDaniel and Lloyd: ", cosine_similarity(users['Daniel'], users['Lloyd'])
    print "\nDaniel and Steve: ", cosine_similarity(users['Daniel'], users['Steve'])
    print "\nDaniel and Lenny: ", cosine_similarity(users['Daniel'], users['Lenny'])
    print "\nLloyd and Steve: ", cosine_similarity(users['Lloyd'], users['Steve'])
    print "\nLloyd and Lenny: ", cosine_similarity(users['Lloyd'], users['Lenny'])
    print "\nSteve and Lenny: ", cosine_similarity(users['Steve'], users['Lenny'])
