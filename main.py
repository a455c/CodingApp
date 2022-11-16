import sys, time

#cool typewriter animation
def print(sentence):
  for c in sentence:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)

# easy code transfer dictionary
dict = {
    'if' : 'if',
    'less' : '<',
    'more' : '>',
    'equals': '=',
    'is': '==',
    'than': ' ',
    'do' : ':',
    'for': 'for',
    'and' : 'and',
    'or' : 'or',
    'while': 'while',
    'not' : 'not',
    'plus': '+',
    'minus': '-', 
    'divided': '/',
    'times': '*',
    'by' : ' ',
    "isn't": '!=',
}

def switch(w): # acts as a switch statement
    try:
        var = dict.get(w) #finds the easycode -> python value and stores it
        if var: # if var is not 'None' is returns the new python syntax
            return var
        else: # if var is 'None' it returns the original word and keeps it as a variable
            return w
    except:
        print('exception')


if len(sys.argv) == 3:

    easycodelst = [] # creates a list for the easycode sentences
    with open(sys.argv[1], 'r') as file: # opens text file as variable 'file'
        for sentence in file: # for sentence in file
            easycodelst.append(sentence) # add the sentence to the list

    pylist = []

    for sentence in easycodelst:
        if not sentence:# if there is no sentence, continue
            continue

        split = sentence.split() # split the sentences into singular word

        for word in split: # for each word in the wordlist
            word = switch(word) # use the switch function to get the python syntax
            print(str(word) + ' ') # print the syntax

            pylist.append(word)

        print('\n') # start a new line for every new sentence
        pylist.append('_')


    with open(sys.argv[2], 'w') as f:
        for word in pylist:
            if word == '_':
                f.write('\n')
                continue


            f.write(word + ' ')

