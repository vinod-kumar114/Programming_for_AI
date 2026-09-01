"""4.A university has two groups of students enrolled in two different courses.
 Course A contains one group of student IDs.
 Course B contains another group of student IDs.

The university wants to determine:
 Students enrolled in both courses
 Students enrolled only in Course A
 Students enrolled only in Course B
 All unique students across both courses
Requirement: Choose a data structure that naturally supports these operations."""



# According to the given requirment, there is a suitable option of usinf Set and its methods

# intersection gives us similar corses in both
# difference A-B give us values of A tht are not in B
# union gives us all the unique vlaues of both A and B collectively


A = {1,2,3,4,5,6,7,8}
B = {2,7,4,9,10,11,12,13}

print("Students enrolled in both courses: ", A.intersection(B))
print("Students enrolled in A: ", A.difference(B))
print("Students enrolled in B: ", B.difference(A))
print("unique students accross both courses: ", A.union(B))