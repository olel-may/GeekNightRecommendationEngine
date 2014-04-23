from math import sqrt


users = {
    'Daniel': {'m300': 2.5, 'Lord of the Rings': 3.5, 'Django Unchained': 3.5, 'Madagascar': 4.5},
    'Lloyd': {'m300': 4.5, 'Lord of the Rings': 4.5, 'Django Unchained': 4.0, 'Madagascar': 4.0},
    'Steve': {'m300': 4.5, 'Lord of the Rings': 4.5, 'Django Unchained': 4.5, 'Madagascar': 4.0},
    'Lenny': {'m300': 4.0, 'Lord of the Rings': 4.0, 'Django Unchained': 3.5, 'Madagascar': 3.5}
}


def pearson_correlation(ratings1, ratings2):
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


if __name__ == "__main__":
    print "Pearson\'s Correlation\'s Coefficient between Users"
    print "\nDaniel and Lloyd: ", pearson_correlation(users['Daniel'], users['Lloyd'])
    print "\nDaniel and Steve: ", pearson_correlation(users['Daniel'], users['Steve'])
    print "\nDaniel and Lenny: ", pearson_correlation(users['Daniel'], users['Lenny'])
    print "\nLloyd and Steve: ", pearson_correlation(users['Lloyd'], users['Steve'])
    print "\nLloyd and Lenny: ", pearson_correlation(users['Lloyd'], users['Lenny'])
    print "\nSteve and Lenny: ", pearson_correlation(users['Steve'], users['Lenny'])
	
