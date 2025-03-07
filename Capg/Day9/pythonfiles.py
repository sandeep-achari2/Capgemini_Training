file=open("sample1.txt","w")
file.write("Hello, this is sample text")
file.close()

# with open("sample1.txt","w") as file:
#     file.write("hello world")
    
#reading file
with open("sample1.txt",'r') as file:
    content=file.read()
    print(content)
    
with open("sample1.txt","r") as file:
    for line in file:
        print(line.strip())
