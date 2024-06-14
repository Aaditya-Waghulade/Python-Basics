x = input("Enter number 1: ")
y = input("Enter number 2: ")

try: 
    z = int(x)/int(y)
except Exception as e:
    print("the error is here : ",e)
    z=None
print("Division is : ",z)