input = open(file = 'input.txt', mode = 'r')
output = open(file = 'output.txt', mode = 'w')
A = int (input.readline())
B = int (input.readline())
C = str(A + B)
output.write(C)
input.close()
output.close()