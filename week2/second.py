import zipfile

with zipfile.ZipFile('my_archive.zip', 'w') as my_zip:
    my_zip.write('first.py')
    my_zip.write('text.txt')
