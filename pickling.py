import pickle

text = """Hello there,
this is a sample text 
to test

Python serializability
via Pickling...
"""

#opening file with 'with' closes it when done with indented block.
#Always open file in binary mode else data may get corrupted while writing.
with open('pickle.file', 'wb') as f:
	pickle.dump(text, f)

#To read (unpickling) file load it to some object.
#This recreates serialized data into new Python object.
with open('pickle.file', 'rb') as f:
	storedData = pickle.load(f)

print storedData
