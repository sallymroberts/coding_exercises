def get_max_profit(stock_prices_yesterday):
	""" Get max profit by buying and selling stock

		Arguments: 
		stock_prices_yesterday [List] Apple stock prices yesterday
		    indices: minutes after market opening
		    values:  price in dollars of Apple stock

		Returns: [Integer] Max profit from 1 purchase and 1 sale of Apple stock yesterday: 
		    Note: if stock prices declined all day, return value is negative 
	"""
	best_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
	low_price = stock_prices_yesterday[0]

	for i in range(1, len(stock_prices_yesterday)):
		cur_price = stock_prices_yesterday[i]
		cur_profit = cur_price - low_price

		if cur_profit > best_profit:
			best_profit = cur_profit

		if cur_price < low_price:
			low_price = cur_price

	return best_profit

# Test cases
# Max profit is positive (price increased at least once)
prices = [10, 7, 5, 8, 11, 9, 4, 6, 12, 2, 6]
best_prof = get_max_profit(stock_prices_yesterday = prices)
print("Expected max profit is 8: ", best_prof)

# Test max profit is negative (prices decline all day)
prices = [12, 10, 9, 3]
best_prof = get_max_profit(stock_prices_yesterday = prices)
print("Expected max profit is -1: ", best_prof)

# Test max profit is zero (no increase in price, one price stays level)
prices = [12, 10, 9, 9, 3]
best_prof = get_max_profit(stock_prices_yesterday = prices)
print("Expected max profit is zero: ", best_prof)