import os
files = os.listdir("submission")
count = 0
other_type = 0
py_type = 0
file_format = []
for file in files:
    f = file.split(".")
    print(f[-1])
    file_format.append(f[-1])
    if f[-1] == "py":
        count += 1
        py_type += 1
    else:
        other_type =+ 1
print(f"There are {py_type} type file")    
print(f"There are {other_type} type file") 
print(file_format)
print(f"Total file submitted: {count}")

    