
def divisor_data(num):
    data = []
    divisors = [divisor for divisor in range(1,(num + 1)) if (num % divisor == 0)]
    data.append(divisors)
    sum_of_divisors = sum(divisors)
    data.append(sum_of_divisors)
    number_of_divisors = len(divisors)
    data.append(number_of_divisors)
    return data

print(divisor_data(60))

