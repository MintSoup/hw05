#!/usr/bin/env python3

from math import sqrt

def distance(a, b):
	q = 0
	for x in range(len(a)):
		q += (a[x] - b[x]) ** 2
	return sqrt(q)

if __name__ == "__main__":
	print(distance([0, 0], [3, 4]))
	print(distance([-7, -4], [17, 6]))
	print(distance([3, 6, 12], [-15, 8, 5]))
	print(distance([3, 6, 12, 24], [-15, 8, 5, 52]))
