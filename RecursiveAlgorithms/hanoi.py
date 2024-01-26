def solveHanoi(n, source, dest, aux):
	if(n<=0): return #Cannot have 0 disks

	solveHanoi(n-1, source, aux, dest) #RFC before(move disks to aux first)
	print(f"Moved Disk {n} from {source} to {dest}")
	solveHanoi(n-1, aux, dest, source) #RFC after(move disks over to destination, after largest disk is there)

#Main(Driver) Code
solveHanoi(3, "Rod A", "Rod C", "Rod B")
print('\n')
solveHanoi(6, "Rod A", "Rod C", "Rod B")

input() #Wait Line