#!/usr/bin/env python3

def print_matrix(m):
	for x in m:
		print("[", end="")
		for y in x[:-1]:
			print(y, end="\t")
		print(x[-1], end="]\n")

def spiral(size):
	m = []
	for _ in range(size):
		q = []
		for _ in range(size):
			q.append(0)
		m.append(q)

	for x in range(size // 2):
		q = (size - x * 2)
		sq = q ** 2
		for y in range(x, size - x):
			m[y][x] = sq + x - y
			m[y][-x - 1] = (sq - 3 * q + 3) + y - x

	for y in range(size // 2):
		x = -2 - y
		while m[y][x] == 0:
			m[y][x] = m[y][x + 1] - 1
			m[-y - 1][x] = m[-y - 1][x + 1] + 1
			x -= 1

	m[size // 2][size // 2] = 1

	return m

if __name__ == "__main__":
	for x in range(1, 16, 2):
		print_matrix(spiral(x))
		print()

# Using numpy and PIL export the spiral matrix
# as an image where each number is a brightness value
def export_image(k):
	from PIL import Image
	import numpy as np

	g = spiral(k)
	ks = k * k
	g = [[(x / ks * 255 , x / ks * 255, x / ks * 255) for x in q] for q in g]
	array = np.array(g, dtype=np.uint8)
	new_image = Image.fromarray(array)
	new_image.save("img.png")
