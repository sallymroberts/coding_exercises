#123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 
def condense_meeting_times(meeting_times):
	"""
	Condense meeting times to time ranges with at least one meeting occurring

		Arguments: 
		meeting_times [List] tuples of integers for meeting start time, end time
		    start/end times are integers representing 30-minute blocks past 9 a.m.
		    i.e., meeting time (2, 3) starts at 10 a.m., ends at 10:30 a.m.

		Returns: [List] tuples of integers for start time, end time of ranges
		                when meetings are taking place

        >>> meeting_times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
		>>> print(condense_meeting_times(meeting_times))
		[(0, 1), (3, 8), (9, 12)]

		>>> meeting_times = [(0, 1), (0, 1), (1, 4), (2, 3), (9, 10)]
		>>> print(condense_meeting_times(meeting_times))
		[(0, 4), (9, 10)]
	"""

	meeting_times.sort()
	mtg_ranges = []

	for i, mtg in enumerate(meeting_times):
		cur_mtg_start = mtg[0]
		cur_mtg_end = mtg[1]

		if i == 0:
			cur_range_start = mtg[0]
			cur_range_end = mtg[1]

		elif cur_mtg_start <= cur_range_end:
			cur_range_end = max(cur_mtg_end, cur_range_end)

		else:
			mtg_ranges.append((cur_range_start, cur_range_end))
			cur_range_start = mtg[0]
			cur_range_end = mtg[1]

	if mtg_ranges[-1] != (cur_range_start, cur_range_end):
		mtg_ranges.append((cur_range_start, cur_range_end))

	return mtg_ranges

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT!\n")