A = input().split()
B = []
B.append (A[-1])
for i in range (len (A) - 1):
    B.append (A[i])
A = B
for j in range (len (A)):
    print (A[j], " ", sep ="", end = "")