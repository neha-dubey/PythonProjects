class schoolMember:
  def __init__(self, name, age):
	self.name = name
	self.age = age
	print "\n\nInitializing school member: {0}".format(self.name)
  def tell(self):
	print "Name: {0}  Age: {1}".format(self.name, self.age),

class teacher(schoolMember):
  def __init__(self, name, age, salary):
	schoolMember.__init__(self, name, age)
	self.salary = salary
	print "Initializing teacher: {0}".format(self.name)

  def tell(self):
	schoolMember.tell(self)  ##Python does not automatically call the constructor of the base class, we have to explicitly call it.
	print "Salary: {0}".format(self.salary)


class student(schoolMember):
  def __init__(self, name, age, grade):
	schoolMember.__init__(self, name, age)
	self.grade = grade
	print "Initializing student: {0}".format(self.name)

  def tell(self):
	schoolMember.tell(self)
	print "Grade: {0}".format(self.grade)


t = teacher('Tom', 40, 100000)
s = student('Neha', 26, 10)

print

members = [t, s]
for member in members:
  member.tell()
