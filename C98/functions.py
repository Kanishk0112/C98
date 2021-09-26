def wordcount():
    filename=input("Enter The File Name")
    numberofwords=0
    file=open(filename,"r")
    for i in file:
        words=i.split()
        numberofwords=numberofwords+len(words)
    print(numberofwords)
wordcount()            