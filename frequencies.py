"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    counter = 0
    for i in items:
        i = str(i)
        for item in items:
            item = str(item)
            if item == i:
                counter +=1
        frequencies.update({i: counter})
        counter = 0
    return frequencies


# testList = ['a','a','b','c']
# print(frequencies(testList))

