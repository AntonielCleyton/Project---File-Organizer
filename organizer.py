import os

# Get the current working directory
os.getcwd()

# List files in the current working directory
os.listdir(os.getcwd())

# Create a list of files in the current working directory
file_list = list(os.listdir(os.getcwd()))

# Iterate through each file in the list and organize them into respective directories
for file in file_list:
    if ".txt" in file:
        # Check if the directory for .txt files exists; if not, create it
        if not os.path.exists('Arquivos Txt'):
            os.mkdir('Arquivos Txt')
            # Move the file to the directory for .txt files
            os.rename(file, os.path.join('Arquivos Txt/', file))
        else:
            # Move the file to the directory for .txt files
            os.rename(file, os.path.join('Arquivos Txt/', file))
    if ".pdf" in file:
        if not os.path.exists('Arquivos PDF'):
            os.mkdir("Arquivos PDF")
            os.rename(file, os.path.join('Arquivos PDF/', file))
        else:
            os.rename(file, os.path.join('Arquivos PDF/', file))
    if ".docx" in file:
        if not os.path.exists('Arquivos DOC'):
            os.mkdir('Arquivos DOC')
            os.rename(file,  os.path.join('Arquivos DOC/', file))
        else:
            os.rename(file,  os.path.join('Arquivos DOC/', file))
    if ".png" in file:
        if not os.path.exists('Arquivos Img PNG'):
            os.mkdir('Arquivos Img PNG')
            os.rename(file, os.path.join('Arquivos Img PNG/', file)) 
        else:
            os.rename(file, os.path.join('Arquivos Img PNG/', file))
