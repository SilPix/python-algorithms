def divider(bign, smalln):
	if(bign < smalln):
		return 0
	else:
		return (1 + divider(bign - smalln, smalln)) #Decrement by smaller number, but still compare by smaller number

print(divider(40,5))

input() #Wait Line