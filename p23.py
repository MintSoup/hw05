#!/usr/bin/env python3

def getMatrixType(m):
	if not isinstance(m, list):
		return -1

	q = None

	for x in m:
		if not isinstance(x, list):
			return -1

		for y in x:
			if not (isinstance(y, float) or isinstance(y, int)):
				return -1

		if q == None:
			q = len(x)
		elif q != len(x):
			return 0

	if q == len(m):
		return 2
	else:
		return 1

def transpose(m):
	if getMatrixType(m) < 1:
		return None

	ret = []
	for _ in range(len(m[0])):
		q = []
		for _ in range(len(m)):
			q.append(0)
		ret.append(q)

	for y in range(len(m)):
		for x in range(len(m[0])):
			ret[x][y] = m[y][x]

	return ret

if __name__ == "__main__":
	print(getMatrixType([1]))
	print(getMatrixType("test"))
	print(getMatrixType(
		[[8, 5, 6, 7, 9],
		[2, "test", 5, 9, 7],
		[6, 2, 6, 9, 9],
		[9, 3, 8, "hello", 2],
		[4, 6, 2, 5, 8]]))

	print(getMatrixType([[1], [2, 4, 5], [3, 5]]))
	print(getMatrixType([[5, 6, 7], [2, 4, 5], [6, 2, 6, 2]]))

	print(getMatrixType(
		[[8, 5, 6, 7],
		[2, 4, 5, 9],
		[6, 2, 6, 9]]))

	print(getMatrixType(
		[[8, 5],
		[2, 4],
		[6, 2]]))

	print(getMatrixType(
		[[8, 5, 6, 7],
		[2, 4, 5, 9],
		[6, 2, 6, 9],
		[9, 3, 8, 3]]))

	print(getMatrixType(
		[[8.5, 5, 6.4, 7, 9],
		[2, 4.8, 5.7, 9, 7],
		[6, 2.1, 6.2, 9, 9],
		[9, 3, 8.3, 3, 2.2],
		[4, 6, 2, 5.2, 8.1]]))

	print()

	print(transpose(
		[[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12]]))
