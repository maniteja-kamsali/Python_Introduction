X = "aieef"
Y = "klaief"

m = len(X)
n = len(Y)

L = [[0 for i in range(n + 1)]
			for j in range(m + 1)]
ls = list()
ls1=list()
count = 0
for i in range(n+1):
	ls.append(0)
	for j in range(m+1):
		ls1.append(ls)

for i in ls1:
	print(len(i))
	if len(i)==7:
		count+=1
print(count)


