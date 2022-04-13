# Return keyword
def fun():
	S = 0
	
	for i in range(10):
		S += i
	return S

# fun()
print(fun())

print()

# Yield Keyword
def fun():
	S = 0
	
	for i in range(10):
		S += i
		yield S

for i in fun():
	print(i)
