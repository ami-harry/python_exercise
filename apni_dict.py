# make a dict and take input from the user and give the output of the entered word
# if word is not found give a reply message that the word is not available in the dict try these keys form the dict

dict1 = {'apple': 'fruit', 'mutable': 'it can be modified',
         'immutable': 'we cant modify its element', 'name': 'harry', 'hii': 'bye'}

usr_inp = input("Enter your word: ")


if usr_inp not in dict1:
    print("word not avilable in the dict\n")
    print('try any one of these\n')
    print(dict1.keys())
else:
    print("the answer is ", end=' ')
    print(dict1[usr_inp])
