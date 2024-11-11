import zipfile

# Creating a ZIP file
with zipfile.ZipFile('archive.zip', 'w') as zipf:
    zipf.write('file.txt')

# Extracting a ZIP file
with zipfile.ZipFile('archive.zip', 'r') as zipf:
    zipf.extractall('extracted_files')
