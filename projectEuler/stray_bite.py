with open("kar_05.py") as fp:
  for i, line in enumerate(fp):
    if "\xc2" in line:
	print i, repr(line)
