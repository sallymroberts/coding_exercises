def get_intersecting_rectangle(rect_1, rect_2):
	""" Get intersecting rectangle from 2 rectangles
		Arguments: 
		rect_1 [Dictionary] Rectangle 1 defined by specifying
			bottom left corner coordinates, width, and height. Example:
			{
			'left_x': 1,
			'bottom_y:', 5,
			'width': 10,
			'height': 4
			} 
		rect_2 [Dictionary] Same structure as rect_1


		Returns: [Dictionary] Rectangle that is the intersection of
		    rect_1 and rect_2. Returns None if there is no overlap.
	"""
	intersect_rect_axis_info = get_intersect_rect_axis(rect_1_min_coord = rect_1['left_x'],
					   rect_1_max_coord = rect_1['left_x'] + rect_1['width'],
					   rect_2_min_coord = rect_2['left_x'],
					   rect_2_max_coord = rect_2['left_x'] + rect_2['width'])
	
	if intersect_rect_axis_info:
		(intersect_rect_min_coord, intersect_rect_length) = intersect_rect_axis_info
		intersect_rectangle = {
							  'left_x': intersect_rect_min_coord,
							  'width': intersect_rect_length
		}

		intersect_rect_axis_info = get_intersect_rect_axis(rect_1_min_coord = rect_1['bottom_y'],
					   rect_1_max_coord = rect_1['bottom_y'] + rect_1['height'],
					   rect_2_min_coord = rect_2['bottom_y'],
					   rect_2_max_coord = rect_2['bottom_y'] + rect_2['height'])
		(intersect_rect_min_coord, intersect_rect_length) = intersect_rect_axis_info
		intersect_rectangle['bottom_y'] = intersect_rect_min_coord
		intersect_rectangle['height'] = intersect_rect_length

		return intersect_rectangle
	else:
		return None

def get_intersect_rect_axis(rect_1_min_coord, 
							 rect_1_max_coord, 
							 rect_2_min_coord, 
							 rect_2_max_coord):
	# Rectangles have same minimum coordinate
	if rect_1_min_coord == rect_2_min_coord:
		intersect_rect_min_coord = rect_1_min_coord
		intersect_rect_length = min(rect_1_max_coord,  rect_2_max_coord) - intersect_rect_min_coord

		return (intersect_rect_min_coord, 
				intersect_rect_length)

	# Set min and max rectangle values based on unequal coordinates
	if rect_1_min_coord < rect_2_min_coord:
		min_rect_min_coord = rect_1_min_coord
		min_rect_max_coord = rect_1_max_coord
		max_rect_min_coord = rect_2_min_coord
		max_rect_max_coord = rect_2_max_coord
	else:
		min_rect_min_coord = rect_2_min_coord
		min_rect_max_coord - rect_2_max_coord
		max_rect_min_coord = rect_1_min_coord
		max_rect_max_coord = rect_1_max_coord

	# Check if min and max rectangles overlap
	if max_rect_min_coord < min_rect_max_coord:
		intersect_rect_min_coord = max_rect_min_coord
		intersect_rect_length = max_rect_max_coord - max_rect_min_coord
		return (intersect_rect_min_coord, 
				intersect_rect_length) 
	else:
		return None

 # Define rectangles for tests
rect_1 = {
	'left_x': 1,
	'bottom_y': 5,
	'width': 10,
	'height': 4
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
	"Expect: {'left_x': 8, 'bottom_y': 6, 'width': 7, 'height': 3}", "\n", 
	"Actual:", get_intersecting_rectangle(rect_1, rect_2))

# Rectangle 3 contained within rectangle 1
print("Contained within", "\n", 
	"Expect: {'left_x': 2,'bottom_y': 6,'width': 3,'height': 1}", "\n", 
	"Actual:", get_intersecting_rectangle(rect_1, rect_3))

# Rectangles overlap, with same minimum x-coordinate
rect_2['left_x'] = 1
print()
print("Same minimum x coordinate", "\n", 
	"Expect: {'left_x': 1,'bottom_y': 6,'width': 7,'height': 10}", "\n", 
	"Actual:", get_intersecting_rectangle(rect_1, rect_2))

rect_2['left_x'] = 11
print()
print("No overlap, min rect max coord == max rect min coord", "\n", 
	"Expect: None", "\n",
	"Actual:", get_intersecting_rectangle(rect_1, rect_2))

rect_2['left_x'] = 20
print()
print("No overlap, min rect max coord < max rect min coord", "\n", 
	"Expect: None", "\n",
	"Actual:", get_intersecting_rectangle(rect_1, rect_2))


