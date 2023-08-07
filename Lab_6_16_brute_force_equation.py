'''Numerous engineering and scientific applications require finding solutions to a set of equations. Ex: 8x + 7y = 38 and 3x - 5y = -1 have a solution x = 3, y = 2. Given integer coefficients of two linear equations with variables x and y, use brute force to find an integer solution for x and y in the range -10 to 10.

Ex: If the input is:

8
7
38
3
-5
-1
Then the output is:

x = 3 , y = 2
Use this brute force approach:

For every value of x from -10 to 10
   For every value of y from -10 to 10
      Check if the current x and y satisfy both equations. If so, output the solution, and finish.
Ex: If no solution is found, output:

There is no solution
Assume the two input equations have no more than one solution.'''

#My solution

#input: 6 integers (provided)
''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

''' Type your code here. '''
#set solution to False to start before the loop
solution = False
#step through every value btwn -10 and 10
for x in range(-10, 11, 1):
   #step through every value btwn -10 and 10
   for y in range(-10, 11, 1):
      #Check if the current x and y satisfy both equations. 
      if ((a * x) + (b * y) == c) and ((d * x) + (e * y) == f):
        #If so, output the solution, and finish.
        solution = True
        print("x = {} , y = {}".format(x, y))
#once the loop has checked all the values, if solution is still False, print the no solution statement        
if solution == False: 
    print("There is no solution")