#!/usr/bin/python3

import matrixf
import p4
import p23

# Create a 17x17 spiral matrix
mat = p4.spiral(17)

p4.print_matrix(mat)

# Save mat to a file called matrix.json
matrixf.save_matrix(mat, "matrix.json")

# Load matrix.json back into a new matrix

mat2 = matrixf.load_matrix("matrix.json")

if p23.getMatrixType(mat2) == 2:
	# Add 1 to all numbers in the matrix
	for y in range(len(mat2)):
		for x in range(len(mat2[0])):
			mat2[y][x] += 1

	# Print mat2
	p4.print_matrix(mat2)
else:
	print("Error while reading/writing matrix.json")
