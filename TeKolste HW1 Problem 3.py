#Rebecca TeKolste
#HW 1, Problem 3

#Iterative
n=100
i=0
counter = 0
while i<(n+1):
    counter = counter + i
    i=i+1
print(counter)




#code adapted from http://www.openbookproject.net/thinkcs/python/english2e/ch06.html

#Recursive
def add2(n):
    if n == 0:
        return 0
    else:
        return n + add2(n-1)

print(add2(100))
