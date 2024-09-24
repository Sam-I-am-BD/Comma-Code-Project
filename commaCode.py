# Comma Code
spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']
def commaCode(someList):
    try: # Added some error handling.
        someString = '' 
        for i in range(len(someList) - 1): # Creates a loop that iterates for however long the list is.
            someString += str(someList[i]) + ', ' # adds a list item with a comma and a space.
        someString = someString + 'and ' + str(someList[-1]) # adds a space and an "and" before the last item.
        print(someString)
    except IndexError: 
        return print('The list is empty') # Added an exception
commaCode(spam)


