incoming_file = open('Assorted/testdoc.txt','r')

for i in incoming_file:
    if i != "\n":
        print(i, end = "")
        print("-" * 8)