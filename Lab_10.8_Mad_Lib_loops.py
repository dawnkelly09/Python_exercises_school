#get the input from the user
user_text = input()
#split the input into tokens
tokens = user_text.split() #[apples, 5]

# while the first token is not 'quit' -> print the mad lib with the variables
while tokens[0] != 'quit':
    print(f'Eating {tokens[1]} {tokens[0]} a day keeps the doctor away.')
    #get new user input and split into tokens -> will repeat until 'quit'
    user_text = input()
    tokens = user_text.split()
