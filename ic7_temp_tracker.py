class TempTracker:
	""" Track temperatures between 0 and 110
		Create functions to return min, max, mean, mode
		Note: if exercise didn't require these functions, could
		      replace functions with retrieval of attributes
	"""
	def __init__(self):
		# For min and max
		self.max = None
		self.min = None

		# For mean
		self.mean = None
		self.sum_temps = 0
		self.temps_count = 0

		#For mode
		self.mode = None
		self.mode_count = 0
		self.temps = {}

	def insert(self, temp):
		# For mean
		self.temps_count += 1
		self.sum_temps += temp
		self.mean = self.sum_temps / self.temps_count

		# First temperature inserted
		if self.max == None:
			self.max = temp
			self.min = temp
			# For mode
			self.temps[temp] = 1
			self.mode_count = 1
			self.mode = temp
		else:
			self.max = max(self.max, temp)
			self.min = min(self.min, temp)
			# For mode
			self.temps[temp] = self.temps.get(temp, 0) + 1
			if self.temps[temp] > self.mode_count:
				self.mode_count = self.temps[temp]
				self.mode = temp

	def get_max(self):
		return (self.max)

	def get_min(self):
		return self.min

	def get_mean(self):
		return self.mean

	def get_mode(self):
		return self.mode

my_temp_tracker = TempTracker()
print("No temperatures inserted:", my_temp_tracker.temps)
print("Max: ", my_temp_tracker.get_max())
print("Min: ", my_temp_tracker.get_min())
print("Mean: ", my_temp_tracker.get_mean())
print("Mode: ", my_temp_tracker.get_mode())

my_temp_tracker.insert(8)

print()
print("1 temperature inserted:", my_temp_tracker.temps)
print("Max: ", my_temp_tracker.get_max())
print("Min: ", my_temp_tracker.get_min())
print("Mean: ", my_temp_tracker.get_mean())
print("Mode: ", my_temp_tracker.get_mode())

my_temp_tracker.insert(6)
my_temp_tracker.insert(10)
my_temp_tracker.insert(8)
my_temp_tracker.insert(10)
my_temp_tracker.insert(4)

print()
print("Multiple temps inserted, 2 temps match mode:", my_temp_tracker.temps)
print("Max: ", my_temp_tracker.get_max())
print("Min: ", my_temp_tracker.get_min())
print("Mean: ", my_temp_tracker.get_mean())
print("Mode: ", my_temp_tracker.get_mode())

my_temp_tracker.insert(10)

print()
print("Multiple temps inserted, 1 temp matches mode:", my_temp_tracker.temps)
print("Max: ", my_temp_tracker.get_max())
print("Min: ", my_temp_tracker.get_min())
print("Mean: ", my_temp_tracker.get_mean())
print("Mode: ", my_temp_tracker.get_mode())
