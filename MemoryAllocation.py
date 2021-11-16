# Python implementation of First-Fit algorithm

# Function to allocate memory to
# blocks as per First fit algorithm
def firstFit(blockSize, m, processSize, n):
	

	allocation = [-1] * n


	for i in range(n):
		for j in range(m):
			if blockSize[j] >= processSize[i]:
				
			
				allocation[i] = j

				
				blockSize[j] -= processSize[i]

				break

	print(" Process No. Process Size	 Block no.")
	for i in range(n):
		print(" ", i + 1, "		 ", processSize[i],
						"		 ", end = " ")
		if allocation[i] != -1:
			print(allocation[i] + 1)
		else:
			print("Not Allocated")


