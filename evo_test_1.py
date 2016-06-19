import random

# range to generate: [START_RANGE, END_RANGE]
START_RANGE = 0
END_RANGE = 9

# size of each edge of the cube
SIZE = 10

# generate array of size n x n x n, using random float numbers from range [start, end]
def generate_array(start, end, n):
	return [[[ random.uniform(start, end) for k in xrange(n)] for j in xrange(n)] for i in xrange(n)]

# returns coords of 3 perpendicular columns - 3 dictionaries consisting of 2 elements
# 1-st dictionary - coords of column where you can iterate over 1-st coordinate in matrix[x][y][z]
# 2-nd dictionary - coords of column where you can iterate over 2-nd coordinate in matrix[x][y][z]
# 3-rd dictionary - coords of column where you can iterate over 3-rd coordinate in matrix[x][y][z]
def find_koords(matrix, n):
	max_x, max_y, max_z = 0, 0, 0
	col_on_x, col_on_y, col_on_z = {'y': 0, 'z': 0}, {'x': 0, 'z':0}, {'x': 0, 'y': 0}

	for i in range(n):
		for j in range(n):
			m_x, m_y, m_z = 0, 0, 0
			for k in range(n):
				m_x += matrix[k][i][j]
				m_y += matrix[i][k][j]
				m_z += matrix[i][j][k]
			if m_x > max_x:
				max_x = m_x
				col_on_x['y'], col_on_x['z'] = i, j
			if m_y > max_y:
				max_y = m_y
				col_on_y['x'], col_on_y['z'] = i, j
			if m_z > max_z:
				max_z = m_z
				col_on_z['x'], col_on_z['y'] = i, j

	return col_on_x, col_on_y, col_on_z


matrix = generate_array(START_RANGE, END_RANGE, SIZE)
print find_koords(matrix, SIZE)
