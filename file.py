import os
from posixpath import splitext
import shutil

path, dirs, files = next(os.walk('/Users/tokyo/Downloads'))


img_extensions = ['.jpeg', '.jpg', '.png', 'gif', '.tiff']
document_extensions = ['.pdf', '.doc', 'docx', '.txt', '.xml']
software_extensions = ['.exe']
zip_extensions = ['.zip']

folders = ['documents', 'images', 'others', 'python', 'softwares', 'zip']
for dir in dirs:
    if dir in folders:
        pass
    else:
        current_path = path + '/' + dir

        new_path = path + '/' + 'softwares' + '/' + dir
        shutil.move(current_path, new_path)


for file in files:
    split = splitext(file)
    file_name = split[0]
    file_extension = split[1]
    current_path = path + '/' + file
    new_path = ''
    if file_extension == '.py':
        P
        print('python file')
        current_name = file
        new_name = 'new_name1'
        new_file = new_name + file_extension
        new_path = path + '/' + 'python' + '/' + new_file

    elif file_extension in zip_extensions:
        print('zip file')
        new_path = path + '/' + 'zip' + '/' + file
        os.replace(current_path, new_path)
    elif file_extension in software_extensions:
        print('software file')
        new_path = path + '/' + 'softwares' + '/' + file
    elif file_extension in document_extensions:
        print('document file')
        new_path = path + '/' + 'documents' + '/' + file

    elif file_extension in img_extensions:
        print('image')
        new_path = path + '/' + 'images' + '/' + file
    else:
        new_path = path + '/' + 'others' + '/' + file

    if new_path != '':
        os.replace(current_path, new_path)
