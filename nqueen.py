import sys

def exactly_one(A):
    return atleast_one(A) + atmost_one(A)

def atleast_one(A):
    return " ".join(map(str, A)) + " 0\n"

def atmost_one(A):
    temp = ""
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            temp += f" -{A[i]} -{A[j]} 0\n"
    return temp

def varmap(r, c, N):
    return r * N + c + 1

if len(sys.argv) > 1:
    N = int(sys.argv[1])
else:
    N = 4

if N < 1:
    print("Error N<1")
    sys.exit(0)

print(f"c SAT Expression for N={N}")
spots = N * N
print(f"c Board has {spots} positions")

temp = ""
for row in range(N):
    A = [varmap(row, column, N) for column in range(N)]
    temp += exactly_one(A)

for column in range(N):
    A = [varmap(row, column, N) for row in range(N)]
    temp += exactly_one(A)

for row in range(N - 1, -1, -1):
    A = [varmap(row + x, x, N) for x in range(N - row)]
    temp += atmost_one(A)

for column in range(1, N):
    A = [varmap(x, column + x, N) for x in range(N - column)]
    temp += atmost_one(A)

for row in range(N - 1, -1, -1):
    A = [varmap(row + x, N - 1 - x, N) for x in range(N - row)]
    temp += atmost_one(A)

for column in range(N - 2, -1, -1):
    A = [varmap(x, column - x, N) for x in range(column + 1)]
    temp += atmost_one(A)

print( 'p cnf ' + str(N*N) + ' ' + str(temp.count('\n')) + '\n')
print(temp)
