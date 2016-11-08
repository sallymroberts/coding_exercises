class TempTracker:
	def __init__(self):
		self.max = None
		self.min = None
		self.mean = None
		self.mode = None
		self.sum_temps = 0
		self.temps_count =0
		self.temps = {}

	def insert(self, temp):
		self.temps_count += 1
		self.sum_temps += temp
		self.mean = self.sum_temps / self.temps_count

		if self.max == None:
			self.max = temp
			self.min = temp
			self.mode = temp

		else:
			self.max = max(self.max, temp)
			self.min = min(self.max, temp)
			self.temps[temp] = self.temps.get(temp, 0) + 1
			# self.mode = max(self.temps.values())

		print(self.max)
		print(self.min)
		print(self.mode)
		print(self.mean)

	def get_max(self):
		print(self.max)
		max_temp = self.max
		return max_temp

	def get_min(self):
		return self.min

	def get_mean(self):
		return self.mean

	def get_mode(self):
		return self.mode()

my_temp_tracker = TempTracker()
my_temp_tracker.insert(10)
my_temp_tracker.insert(6)
my_temp_tracker.insert(10)

print("Max: ", my_temp_tracker.get_max)
