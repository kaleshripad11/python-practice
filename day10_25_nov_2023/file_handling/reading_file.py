print("Reading the contents of existing file 'Existing_File.txt' in read mode.....")
file = open("files/Existing_File1.txt", "r")
print("\n", file.read())
file.close()
print("\nDone...")