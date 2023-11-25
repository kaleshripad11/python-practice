# In python use open("File Path", "Mode") to write/read files
print("Opening the existing file 'Existing_File.txt' in write mode.....")
existing_file = open("files/Existing_File1.txt", "w")
existing_file.write("This is an existing file.\nContent is written using python code\n")
existing_file.close()


