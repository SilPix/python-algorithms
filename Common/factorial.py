def factorial(num):
    total = 1

    for x in range(1, num):
        total *= (x+1)

    return total

print(factorial(7))
input()