def swapFileData():
    fileName=input("Enter file name: ")
    wordCount=0
    file = open("data/names.txt", "r")
    for i in file :
        words=i.split()
        wordCount=wordCount+len(words)
    print("number of words : ")
    print(wordCount)
swapFileData()