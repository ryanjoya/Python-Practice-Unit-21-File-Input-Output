with open("text.txt", "w") as textfile:
    textfile.write("TSM TSM TSM!")

if textfile.closed != True:
    textfile.close()

print textfile.closed
