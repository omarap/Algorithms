class DriverMatch:
	def __init__(self,match):
		self.match = match
		self.users = len(match)
		self.drivers = len(match[0])
 
	# A DFS based recursive function that returns true if a
	# matching for vertex u is possible
	def bpm(self, u, matchR, seen):
 
		# Try every driver one by one
		for v in range(self.drivers):
 
			# If user u is assigned to driver v and v is
        	# not seen
			if self.match[u][v] and seen[v] == False:
				seen[v] = True # Mark v as visited
 
				'''If driver 'v' is not assigned to an user OR
            	previously assigned user for driver v (which is matchR[v]) 
            	has an alternate job available. 
            	Since v is marked as assigned in the above line, matchR[v] 
            	in the following recursive call will not get driver 'v' again'''
				if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen):
					matchR[v] = u
					return True
		return False
 
	# Returns maximum number of matching 
	def maxBPM(self):
		'''An array to keep track of the users assigned to
    	drivers. The value of matchR[i] is the user number
    	assigned to driver i, the value -1 indicates nobody is
    	assigned.'''
		matchR = [-1] * self.drivers
		result = 0 # Count of drivers assigned to users
		for i in range(self.users):
			# Mark all drivers as not seen for next user.
			seen = [False] * self.drivers
			# Find if the user 'u' can get a driver
			if self.bpm(i, matchR, seen):
				result += 1
 
		print ("Matching are :")
		for driver, user in enumerate(matchR):
			if user != -1 :
				print ("Driver%d --> User%d " % (driver+1, user+1))   
 
		return result
 
 
list =[[0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1]]
 
g = DriverMatch(list)
 
print ("Maximum number of users that can get a driver is %d " % g.maxBPM())
