#Pascal's triangle is a triangular array of integers constructed with the following formula:
#The first row consists of the number 1.
#For each subsequent row, each element is the sum of the numbers directly above it, on either side.
#Given an input k, return the kth row of Pascal's triangle.

k = int(input())
triangle = []
lastrow =[]
for i in range(k+1):
    row = []
    for j in range(i+1):
        if j != 0:
            try:
                row.append(lastrow[j] + lastrow[j-1])
            except:
                row.append(1)
        else:
            row.append(1)
    lastrow = row
    triangle.append(row)
print(triangle[k-1])