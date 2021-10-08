file_path = 'e:/zzc/learning_python.txt'
with open(file_path) as file_object:
    file = file_object.read()
    print(file.replace('Python','c'))
