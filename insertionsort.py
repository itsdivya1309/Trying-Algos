"""
Solves the sorting problem

Sorting Problem:-
Input: A sequence of n numbers <a1,a2,...an>
Output: A permutation (reordering) <a1',a2',...an'> of the input sequence such that a1'<a2'<...an'.
"""

A = list(map(float,input().split()))
n = len(A)

#Function to sort the sequence in ascending order
def ascend():

    for j in range(1,n):
        key = A[j]
        #Inserting key into the sorted sequence A[0,...,j-1]

        i = j-1
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

    print(A)

#Function to sort the sequence in descending order
def descend():

    for j in range(1,n):
        key = A[j]
        #Inserting key into the sorted sequence A[0,...,j-1]

        i = j-1
        while i>=0 and A[i]<key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

    print(A)

ascend()
descend()