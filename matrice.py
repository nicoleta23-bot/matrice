#Sa se creeze o matrice patratica cu dimensiunile 5:5.
#  Sa se calculeze suma elementelor de pe fiecare linie, 
# sa se calculeze suma elementelor de pe fiecare coloana.
#sa se afiseze diagonala principala si secundara.
A=[[1, 4, 5, 3, 6],
[-6, 7, 2, 6, 9],
[12, 34, 14, 8, 23],
[24, 67, 45, 13, 22],
[44, 33, 11, 15, 10]]
print("A=", A)
print(sum(A[0]))
print(sum(A[1]))
print(sum(A[2]))
print(sum(A[3]))
print(sum(A[4]))
col1 = [];
for rind1 in A:
    col1.append(rind1[0])
print(col1)
print(sum(col1))

col2 = [];
for rind2 in A:
    col2.append(rind2[1])
print(col2)
print(sum(col2))

col3 = [];
for rind3 in A:
    col3.append(rind3[2])
print(col3)
print(sum(col3))

col4 = [];
for rind4 in A:
    col4.append(rind4[3])
print(col4)
print(sum(col4))

col5 = [];
for rind5 in A:
    col5.append(rind5[4])
print(col5)
print(sum(col5))

#diagonala principala
D1= [A[0][0], A[1][1], A[2][2], A[3][3], A[4][4]]
print(D1)
#diagonala secundara
D2= [A[0][4], A[1][3], A[2][2], A[3][1], A[4][0]]
print(D2)