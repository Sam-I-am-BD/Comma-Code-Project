# Comma Code
spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']
def commaCode(someList):
    try:
        someString = ''
        for i in range(len(someList) - 1):
            someString += str(someList[i]) + ', '
        someString = someString + 'and ' + str(someList[-1])
        print(someString)
    except IndexError:
        return print('The list is empty')
commaCode(spam)


