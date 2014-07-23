from math import sqrt


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
        return (sum_xy - (sum_x * sum_y) / number_of_items) / denominator-
