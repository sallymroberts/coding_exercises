# TODO This is work in progress, to be completed
def get_coin_combos(amount_left, denoms, cur_index=0, num_way_hash = {}):

	# Base cases
	# hit the amount left exactly, have a valid combo
	if amount_left == 0:
		print("returning 1")
		return 1

	# went past the amount left, not a valid combo
	if amount_left < 0:
		return 0

	# finished checking all denominations, no more valid combos
	if cur_index == len(denoms):
		return 0

	print("checking ways to make", amount_left, "with", denoms[cur_index:])

	cur_coin = denoms[cur_index]

	num_possibilities = 0

	while amount_left >= 0:
		num_possibilities += get_coin_combos(amount_left, denoms, cur_index + 1)
		amount_left	-= cur_coin

	print("returning num_possibilities:", num_possibilities)
	return num_possibilities

print(get_coin_combos(4, [1, 2, 3]))
