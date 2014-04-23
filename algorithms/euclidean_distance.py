from math import sqrt


users = {
	'Daniel': {'m300': 2.5, 'Lord of the Rings': 3.5, 'Django Unchained': 3.5, 'Madagascar': 4.5},
	'Lloyd':  {'m300': 4.5, 'Lord of the Rings': 4.5, 'Django Unchained': 4.0, 'Madagascar': 4.0},
	'Steve':  {'m300': 4.5, 'Lord of the Rings': 4.5, 'Django Unchained': 4.5, 'Madagascar': 4.0},
	'Lenny':  {'m300': 4.0, 'Lord of the Rings': 4.0, 'Django Unchained': 3.5, 'Madagascar': 3.5}
}


def euclidean_distance(rating1, rating2):
    sum_of_squares = 0
    for key in rating1:
        if key in rating2:
            sum_of_squares += pow((rating1[key] - rating2[key]), 2)
    return 1/(1+(sum_of_squares))
    
    
if __name__ == "__main__":
	print "Euclidean Distance between Users"
	print "\nDaniel and Lloyd: ", euclidean_distance(users['Daniel'], users['Lloyd'])
	print "\nDaniel and Steve: ", euclidean_distance(users['Daniel'], users['Steve'])
	print "\nDaniel and Lenny: ", euclidean_distance(users['Daniel'], users['Lenny'])
	print "\nLloyd and Steve: ", euclidean_distance(users['Lloyd'], users['Steve'])
	print "\nLloyd and Lenny: ", euclidean_distance(users['Lloyd'], users['Lenny'])
	print "\nSteve and Lenny: ", euclidean_distance(users['Steve'], users['Lenny'])
	
