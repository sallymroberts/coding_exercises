def get_max_profit(stock_prices_yesterday):
	best_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
	low_price = stock_prices_yesterday[0]
	print("best_profit, low_price: ", best_profit, low_price)

	for i in range(1, len(stock_prices_yesterday)):
		cur_price = stock_prices_yesterday[i]

		if cur_price - low_price > best_profit:
			best_profit = cur_price - low_price

		if cur_price < low_price:
			low_price = cur_price

	return best_profit

prices = [10, 7, 5, 8, 11, 9, 4, 6, 12, 2, 6]
best_prof = get_max_profit(stock_prices_yesterday = prices)
print(best_prof)

prices = [12, 10, 9, 3]
best_prof = get_max_profit(stock_prices_yesterday = prices)
print(best_prof)