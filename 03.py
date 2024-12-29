array=[]
# print("Enter List Items:")

while True:
    line=input()
    if line:
        array.append(line)
    else:
        break
    # print(array)
    out='\n'.join(array)
    print("Fruits Item: ", out)
