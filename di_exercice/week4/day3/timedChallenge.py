# Perfect numbers

def is_perfect(number):
    tab = [1]
    for i in range(2, number):
        if number % i == 0:
            tab.append(i)

    return sum(tab) == number


print(is_perfect(6))
