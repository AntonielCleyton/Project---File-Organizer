import os

# Get the current working directory
os.getcwd()

# List files in the specified directories
os.listdir('C:\\Users\\Cleyton\\Desktop\\Curso de Python\\Projetos\\Projeto - Organizador de arquivos\\Arquivos Txt')
os.listdir('C:\\Users\\Cleyton\\Desktop\\Curso de Python\\Projetos\\Projeto - Organizador de arquivos\\Arquivos PDF')
os.listdir('C:\\Users\\Cleyton\\Desktop\\Curso de Python\\Projetos\\Projeto - Organizador de arquivos\\Arquivos DOC')
os.listdir('C:\\Users\\Cleyton\\Desktop\\Curso de Python\\Projetos\\Projeto - Organizador de arquivos\\Arquivos Img PNG')

# Create lists of files in the specified directories
txt_files = list(os.listdir('C:\\Users\\Cleyton\\Desktop\\Curso de Python\\Projetos\\Projeto - Organizador de arquivos\\Arquivos Txt'))
pdf_files = list(os.listdir('C:\\Users\\Cleyton\\Desktop\\Curso de Python\\Projetos\\Projeto - Organizador de arquivos\\Arquivos PDF'))
doc_files = list(os.listdir('C:\\Users\\Cleyton\\Desktop\\Curso de Python\\Projetos\\Projeto - Organizador de arquivos\\Arquivos DOC'))
png_files = list(os.listdir('C:\\Users\\Cleyton\\Desktop\\Curso de Python\\Projetos\\Projeto - Organizador de arquivos\\Arquivos Img PNG'))

# Organize files by moving them to the root directory
while True:
    for file in txt_files:
        if ".txt" in file:
            os.rename(os.path.join('Arquivos Txt/', file), file)
    for file in pdf_files:
        if ".pdf" in file:
            os.rename(os.path.join('Arquivos PDF/', file), file)
    for file in doc_files:
        if ".docx" in file:
            os.rename(os.path.join('Arquivos DOC/', file), file)            
    for file in png_files:
        if ".png" in file:
            os.rename(os.path.join('Arquivos Img Png/', file), file)            
    
    # Move back to the parent directory and remove the subdirectories
    os.chdir('C:\\Users\\Cleyton\\Desktop\\Curso de Python\\Projetos\\Projeto - Organizador de arquivos')
    os.rmdir('Arquivos Txt')
    os.rmdir('Arquivos PDF')
    os.rmdir('Arquivos DOC')
    os.rmdir('Arquivos Img PNG')
