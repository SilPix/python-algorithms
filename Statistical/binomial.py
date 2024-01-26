#f(x) = [nCx].p[x].(1-p)[n-x]
#f(x) = [nCx].p[x].q[n-x]
successPercent = float(input("Input Percentage Chance of Success: "))

successChance = successPercent / 100
failureChance = 1 - successChance

x = float(input("Input x: "))
n = int(input("How many trials were taken? "))

p = successChance
q = failureChance

pmf = (p**x) * (q**(n-x))
print("Probability Mass Function = ", pmf)

input()