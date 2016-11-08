def get_intersecting_rectangle(rect_1, rect_2):
	""" Get intersecting rectangle from 2 rectangles
		Arguments: 
		rect_1 [Dictionary] Rectangle 1 defined by specifying
			bottom left corner coordinates, width, and height. Example:
			{
			'left_x': 1,
			'bottom_y:' 5,
			'width': 10,
			'height': 4
			} 
		rect_2 [Dictionary] Same structure as rect_1


		Returns: [Dictionary] Rectangle that is the intersection of
		    rect_1 and rect_2. If there is no overlap, the values for 
		    each dictionary element are None.
	"""
	intersect_x, intersect_width = get_intersect_axis(\
		rect_1['left_x'], rect_1['width'], 
		rect_2['left_x'], rect_2['width'])

	intersect_y, intersect_height = get_intersect_axis(\
		rect_1['bottom_y'], rect_1['height'], 
		rect_2['bottom_y'], rect_2['height'])

	if not intersect_width or not intersect_height:
		return {
			'left_x': None,
			'bottom_y': None,
			'width': None,
			'height': None
		}
	else:
		return {
			'left_x': intersect_x,
			'bottom_y': intersect_y,
			'width': intersect_width,
			'height': intersect_height
		}

def get_intersect_axis(coord_1, length_1, coord_2, length_2):
	""" Get intersecting coordinate and length from 2 lines
		Arguments: 
		coord_1 [Integer] point coordinate
		length_w [Integer] length of line

		Returns: [Tuple] ([Integer] intersecting coordinate, 
						 [Integer] length of intersection) 
	"""	
	intersect_min_coord = max(coord_1, coord_2)
	intersect_max_coord = min(coord_1 + length_1, coord_2 + length_2)
	intersect_length = intersect_max_coord - intersect_min_coord

	if intersect_length <= 0:
		return (None, None)
	else:
		return (intersect_min_coord, intersect_length)

 # Define rectangles for tests
rect_1 = {
	'left_x': 1,
	'bottom_y': 5,
	'width': 10,
	'height': 5
}

# Rectangle 2, overlaps rectangle 1
# Note that attributes of rect_2 are modified for some tests
rect_2 = {
	'left_x': 8,
	'bottom_y': 6,
	'width': 7,
	'height': 10
}

# Rectangle 3, contained within rectangle 1
rect_3 = {
	'left_x': 2,
	'bottom_y': 6,
	'width': 3,
	'height': 1
}

# Overlapping rectangles
print("Overlapping", "\n", 
	"Expect: {'left_x': 8, 'bottom_y': 6, 'width': 3, 'height': 4}", "\n", 
	"Actual:", get_intersecting_rectangle(rect_1, rect_2))

# Rectangle 3 contained within rectangle 1
print()
print("Contained within", "\n", 
	"Expect: {'left_x': 2,'bottom_y': 6,'width': 3,'height': 1}", "\n", 
	"Actual:", get_intersecting_rectangle(rect_1, rect_3))

# Rectangles overlap, with same minimum x-coordinate
rect_2['left_x'] = 1
print()
print("Same minimum x coordinate", "\n", 
	"Expect: {'left_x': 1,'bottom_y': 6,'width': 7,'height': 4}", "\n", 
	"Actual:", get_intersecting_rectangle(rect_1, rect_2))

# Rectangles don't overlap, edge touches
rect_2['left_x'] = 11
print()
print("No overlap, edges touch", "\n", 
	"Expect: {'left_x': None,'bottom_y': None,'width': None,'height': None}", "\n",
	"Actual:", get_intersecting_rectangle(rect_1, rect_2))

# Rectangles don't overlap, edges don't touch
rect_2['left_x'] = 20
print()
print("No overlap, edges do not touch", "\n", 
	"Expect: {'left_x': None,'bottom_y': None,'width': None,'height': None}", "\n",
	"Actual:", get_intersecting_rectangle(rect_1, rect_2))