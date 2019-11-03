import os

def createfile (target=None):
	if target is None:
		target = input("Provide file name:")
	if os.path.exists(target) and os.path.isfile(target):
		print("File already exists")
	else:
		open(target, "a").close()

createfile()

