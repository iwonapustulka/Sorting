import numpy as np
from timeit import default_timer
np.random.seed()
A = np.random.randint(1, 1001, 5000)
B = [x for x in range(4999, -1, -1)]

with open ("zbiorA.txt", "w")as file :
    for i in range (0,len(A)):
        pom = A[i]
        if i % 25 == 0:
            pom=str(pom)+ "\n"
        file.write(str(pom)+" ")

with open ("zbiorB.txt", "w")as file :
    for i in range (0,len(B)):
        pom = B[i]
        if i % 25 == 0:
            pom= str(pom)+"\n"
        file.write(str(pom)+" ")

def SelectSort (D):
    for i in range(0,len(D)-1):
        min =D[i]
        imin =i
        for j in range(i+1,len(D)):
            if D[j]< min:
                min =D[j]
                imin =j
        if i != imin:
            tmp= D[i]
            D[i]=D[imin]
            D[imin]=tmp

def InsertSort(D):
    for i in range(1,len(D)):
        key = D[i]
        j = i - 1
        while j>=0 and D[j]>key:
            D[j + 1] = D[j]
            j = j - 1
        D[j + 1] = key

def BubbleSort(D):
    for i in range(len(D) - 1, 0, -1):
        for j in range(i):
            if D[j] > D[j + 1]:
                D[j] =D [j + 1]
                D[j + 1] = D[j]


def CountingSort(D):
    pom = []
    for i in range(0, len(D)):
        pom.append(0);
    for x in D:
        pom[x] = pom[x] + 1
    j = 0
    for x in range(0, len(D)):
        for y in range(0, pom[x]):
            D[j] = x
            j = j + 1




with open ("inesrtSortA.txt", "w")as file :
    InsertSort(A)
    for i in range (0,len(A)):
        pom = A[i]
        if i % 25 == 0:
            pom=str(pom)+ "\n"
        file.write(str(pom)+" ")

with open ("inesrtSortB.txt", "w")as file :
    InsertSort(B)
    for i in range (0,len(B)):
        pom = B[i]
        if i % 25 == 0:
            pom= str(pom)+"\n"
        file.write(str(pom)+" ")

with open ("BubbleSortA.txt", "w")as file :
    BubbleSort(A)
    for i in range (0,len(A)):
        pom = A[i]
        if i % 25 == 0:
            pom=str(pom)+ "\n"
        file.write(str(pom)+" ")

with open ("BubbleSortB.txt", "w")as file :
    BubbleSort(B)
    for i in range (0,len(B)):
        pom = B[i]
        if i % 25 == 0:
            pom= str(pom)+"\n"
        file.write(str(pom)+" ")

with open ("SelectSortA.txt", "w")as file :
    SelectSort(A)
    for i in range (0,len(A)):
        pom = A[i]
        if i % 25 == 0:
            pom=str(pom)+ "\n"
        file.write(str(pom)+" ")

with open ("SelectSortB.txt", "w")as file :
    SelectSort(B)
    for i in range (0,len(B)):
        pom = B[i]
        if i % 25 == 0:
            pom= str(pom)+"\n"
        file.write(str(pom)+" ")

with open ("CountingSortA.txt", "w")as file :
    CountingSort(A)
    for i in range (0,len(A)):
        pom = A[i]
        if i % 25 == 0:
            pom=str(pom)+ "\n"
        file.write(str(pom)+" ")

with open ("CountingSortB.txt", "w")as file :
    CountingSort(B)
    for i in range (0,len(B)):
        pom = B[i]
        if i % 25 == 0:
            pom= str(pom)+"\n"
        file.write(str(pom)+" ")

with open ("SortA.txt", "w")as file :
    A.sort()
    for i in range (0,len(A)):
        pom = A[i]
        if i % 25 == 0:
            pom=str(pom)+ "\n"
        file.write(str(pom)+" ")

with open ("SortB.txt", "w")as file :
    B.sort()
    for i in range (0,len(B)):
        pom = B[i]
        if i % 25 == 0:
            pom= str(pom)+"\n"
        file.write(str(pom)+" ")


with open ("czas.txt","w") as file:
    start1A = default_timer()
    BubbleSort(A)
    end1A= default_timer()
    pom1A=end1A-start1A

    start1B = default_timer()
    BubbleSort(B)
    end1B = default_timer()
    pom1B = end1B - start1B

    start2A = default_timer()
    CountingSort(A)
    end2A = default_timer()
    pom2A = end2A - start2A

    start2B = default_timer()
    CountingSort(B)
    end2B = default_timer()
    pom2B = end2B - start2B

    start3A = default_timer()
    InsertSort(A)
    end3A = default_timer()
    pom3A = end3A - start3A

    start3B = default_timer()
    InsertSort(B)
    end3B = default_timer()
    pom3B = end3B - start3B

    start4A = default_timer()
    SelectSort(A)
    end4A = default_timer()
    pom4A = end4A - start4A

    start4B = default_timer()
    SelectSort(B)
    end4B = default_timer()
    pom4B = end4B - start4B

    start5A = default_timer()
    A.sort()
    end5A = default_timer()
    pom5A = end5A - start5A

    start5B = default_timer()
    B.sort()
    end5B = default_timer()
    pom5B = end5B - start5B

    file.write("BubbleSort A: "+str(pom1A)+"\n"+"BubbleSort B: "+str(pom1B)+"\n"+
               "CountingSort A: "+str(pom2A)+"\n"+"CountingSort B: "+str(pom2B)+"\n"+
               "InsertSort A: "+str(pom3A)+"\n"+"InsertSort B: "+str(pom3B)+"\n"+
               "SelectSort A: "+str(pom4A)+"\n"+"SelectSort B: "+str(pom4B)+"\n"+
               "Sort A: "+str(pom5A)+"\n"+"SortB: "+str(pom5B))
