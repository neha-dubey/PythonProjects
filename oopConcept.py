class robot:
  """Represents a robot with a name."""
  #Class varible counting number of robots
  population = 0
  

  def __init__(self, name):
	"""Initializes the data"""
	self.name = name
	print "\n(Initializing {0})".format(self.name)
	robot.population += 1

  def die(self):
	"""I am dying."""
	print "({0} is being destroyed)".format(self.name)
	robot.population -= 1

	if robot.population == 0:
	  print "{0} was the last one.".format(self.name)
	else:
	  print "There are still {0} robots working.".format(robot.population)

  def say_hi(self):
	"""Greetings from robot."""
	print "Greetings !!! People call me {0}".format(self.name)

  @classmethod
  def how_many(self):
	"""Prints the current population."""
	print "We have {0} robots !!!".format(self.population)

droid1 = robot("R2-D2")
droid1.say_hi()
robot.how_many()

droid2 = robot("R3-D3")
droid2.say_hi()
robot.how_many()

print "\nrobots busy doing their work !!!\n"

print "robots finished their work and good to be destroyed now.\n"

droid1.die()
droid2.die()
robot.how_many()

#print robot.__doc__
