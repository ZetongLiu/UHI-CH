from shapely.geometry import Polygon

# Create a square polygon with edges of length 4
original_square = Polygon([(0, 0), (4, 0), (4, 4), (0, 4)])

# Apply a buffer of 2 units
buffered_square = original_square.buffer(2)

# Print the coordinates of the original and buffered squares
print("Original Square:", original_square.exterior.coords.xy)
print("Buffered Square:", buffered_square.exterior.coords.xy)
