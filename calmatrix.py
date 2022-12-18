#--------------------------> Input Matrix
R = int(input("Enter Row:"))
C = int(input("Enter Column:"))

matrixAQ = []
newMatrix = []
for i in range(R):
    a = []
    b = []
    for j in range(C):
        a.append(int(input()))
        b.append(0)
    matrixAQ.append(a)
    newMatrix.append(b)
    
matrixSQ = []
R1 = int(input("Enter Row:"))
C1 = int(input("Enter Column:"))
for i in range(R1):
    a = []
    for j in range(C1):
        a.append(int(input()))
    matrixSQ.append(a)


#-------------------------> Sum of Column
def SumCol(matrix, k, C):
    sum = 0
    for i in range(C):
        sum += matrix[k][i]
    return sum


#-------------------------> VF - Affinity Measure Function
for i in range(R):
    for j in range(C):
        if i == j:
            sum = 0
            for k in range(R1):
                if matrixAQ[k][i] == 1:
                    sum += SumCol(matrixSQ, k, C1)
            newMatrix[i][i] = sum
        else:
            sum = 0
            for k in range(R1):
                if matrixAQ[k][i] == 1 and matrixAQ[k][j] == 1:
                    sum += SumCol(matrixSQ, k, C1)
            newMatrix[i][j] = newMatrix[j][i] = sum

for i in range(R):
    for j in range(C):
        print(newMatrix[i][j], end=" ")
    print()
    
    
    
#-----------------------> BOND CALCULATE FUNCTION
def bond(Ax,Ay):
    if Ax==-1 or Ay==-1:
        return 0
    ans = 0
    for i in range(R):
        ans = ans + (newMatrix[i][Ax]*newMatrix[i][Ay])
    return ans



#-----------------------> CONT CALCULATE FUNCTION
def cont(Ai,Ak,Aj):
    print("Bond(A",Ai+1, ", A", Ak+1, ") = ", bond(Ai,Ak))
    print("Bond(A",Ak+1, ", A", Aj+1, ") = ", bond(Ak,Aj))
    print("Bond(A",Ai+1, ", A", Aj+1, ") = ", bond(Ai,Aj))
    return 2*bond(Ai,Ak) + 2*bond(Ak,Aj) - 2*bond(Ai,Aj)

def BEA():
    Ca = []
    Ca.append(0)
    Ca.append(1)
    index = 2
    while index < R:
        maxi = -1 
        maxc = -100000
        for i in range(1,index):
                con = cont(Ca[i-1],index,Ca[i])
                print("Index A", i+1, " ", "cont ", Ca[i],index+1,Ca[i]+1, con)
                if con > maxc:
                    maxi = i
                    maxc = con
                    
                    
        #If Index in left array
        con = cont(-1,index,Ca[0])
        print("Index A", i+1, " ", "cont ", 0,index+1,Ca[0]+1, con)
        if con > maxc:
            maxi = 0
            maxc = con
        #If Index in right array
        con = cont(Ca[index-1],index,-1)
        print("Index ", i+1, " ", "cont ", Ca[index-1]+1,index+1,index+2, con)
        if con > maxc:
            maxi = index
        if maxi==index:
            Ca.append(index)
        else:
            Ca.append(0)
            for j in range(index,maxi,-1):
                Ca[j]=Ca[j-1]
            Ca[maxi] = index
        print(Ca)
        index = index + 1
    print("The clustered affinity matrix Ca: ")
    print(Ca)
    return Ca


CA = BEA()
Ca = [[0 for i in range(R)] for j in range(C)]
for i in range(R):
    for j in range(C):
        Ca[i][j] = newMatrix[CA[i]][CA[j]]
        
for i in range(R):
    for j in range(C):
        print(Ca[i][j], end=" ")
    print()
    
