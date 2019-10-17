data = [2, 34, 12, 29, 37, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]

# def mean(any_list):
#     my_mean = sum(int(any_list) / len(any_list))
#     return my_mean

# def median(any_list):
#     my_median = (any_list[10] + any_list [11]) / 2
#     return my_median

# def mode(any_list):
#     from collections import Counter
#     occurence = Counter(any_list)
#     my_mode = occurence.most_common(1)
#     return my_mode

# def basic_stats(any_list):
#     data_mean = mean(any_list)
#     print("mean: " + data_mean)
#     data_median = median(any_list)
#     print("median: " + data_median)
#     data_mode = mode(any_list)
#     print("mode: " + data_mode)
#     return



def basic_stats(any_list):
    my_mean = sum(any_list) / len(any_list)
    print("mean: " + str(my_mean))
    any_list.sort()
    my_median = (any_list[10] + any_list [11]) / 2
    my_median = int(my_median)
    print("median: " + str(my_median))
    from collections import Counter
    occurence = Counter(any_list)
    my_mode = occurence.most_common(1)
    my_mode = my_mode[0][0]
    print("mode: " + str(my_mode))

basic_stats(data)
