class person():
	def say_hi(self):    # Class method taking self as argument since 
			     # default argument is passed while calling a method
		print("Hello, how are you?")

print (person()) # This prints the memory location (address) for object 
		 # of class person. It could also be written as:
		 # a = person()
		 # print (a)
person().say_hi()
#p = person()
#p.say_hi()
