#f(x) = p[x].(1-p)[1-x]
#f(x) = p[x].q[1-x]
successPercent = float(input("Input Percentage Chance of Success: "))

successChance = successPercent / 100
failureChance = 1 - successChance

x = float(input("Input x: "))

p = successChance
q = failureChance

pmf = (p**x) * (q**(1-x))
print("Probability Mass Function = ", pmf)

input() #Wait Line