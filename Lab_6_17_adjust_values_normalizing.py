'''When analyzing data sets, such as data for human heights or for human weights, a common step is to adjust the data. This adjustment can be done by normalizing to values between 0 and 1, or throwing away outliers.

For this program, adjust the values by dividing all values by the largest value. The input begins with an integer indicating the number of floating-point values that follow.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')
Ex: If the input is:

5
30.0
50.0
10.0
100.0
65.0
the output is:

0.30
0.50
0.10
1.00
0.65
The 5 indicates that there are five floating-point values in the list, namely 30.0, 50.0, 10.0, 100.0, and 65.0. 100.0 is the largest value in the list, so each value is divided by 100.0.'''

#My solution
#input:
#integer how many float values are listed
how_many_values = int(input())
#float -> get input from user same number of times as how_many_values
#assign a blank list to hold the inputs
inputs_from_user = []

#assign 1 to the num_of_inputs to start the count
num_of_inputs = 1
#as long as num_of_inputs is less than or equal how_many_values
while num_of_inputs <= how_many_values:
    #get next input, add it to the list, incriment num_of_inputs
    next_value = float(input())
    inputs_from_user.append(next_value)
    num_of_inputs += 1
    
#determine the max number from the provided inputs
max_of_inputs = max(inputs_from_user)

#loop over all the values in the list, div by the max, output
for input in inputs_from_user:
    input = input / max_of_inputs
    #output: each floating-point value with two digits after the decimal point
    print('{:.2f}'.format(input))
