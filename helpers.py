# Extract vectors from a SVG path
def get_vectors(path):
	vectors = []
	prev_point = (0, 0)
	i = 0

	# Split path on whitespace
	split = path.split()
	while(True):
		try:	
			# Set a new start point if this is a "M" command
			if split[i] == "M":
				start = (split[i + 1], split[i + 2])
				i = i + 3
			else:
				start = prev_point

			# Skip over the "L"
			i = i + 1

			end = (split[i], split[i + 1])
			prev_point = end
			i = i + 2

			vectors.append((start, end))

		# If end of path, stop	
		except IndexError:
			break
		
	return vectors

# Construct a raster image "bitmap" (not actually bitmap format)
def make_image(path):
	SIDE_LENGTH = 10000

	# Make a 2D array to represent image
	# Start with white image, all pixels 0
	image = [[0 for i in range(SIDE_LENGTH)] for j in range(SIDE_LENGTH)]

	vectors = get_vectors(path)

	for vector in vectors:

		# Extract basic info
		start_x = vector[0][0]
		start_y = vector[0][1]
		end_x = vector[1][0]
		end_y = vector[1][1]

		# Scale info from the 200x200 dimensions of the SVG
		# to the dimensions of the bitmap
		start_x = start_x / 200 * SIDE_LENGTH
		start_y = start_y / 200 * SIDE_LENGTH
		end_x = end_x / 200 * SIDE_LENGTH
		end_y = end_y / 200 * SIDE_LENGTH

		slope = (end_y - start_y)/(end_x - start_x)

		# Change all the pixels the vector "touches" to black
		for x in range(start_x, end_x):
			y = round(int(x + slope(x - x_start))
			image[y][x] = 1
	return image
	