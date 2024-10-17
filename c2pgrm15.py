words=input("enter the list of word seprated by spaces:").split()
max_length=0
for word in words:
    if len(word)>max_length:
        max_length=len(word)
print("The length of the largest word is:",max_length)
