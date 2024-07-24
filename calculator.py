def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if a == 0 or b==0:
        print("Division is error")
    else:
        return a/b
print(f"Answer of Add = {add(4,6)}")
print(f"Answer of Minus = {substract(7,18)}")
print(f"Answer of Multiplied = {multiply(4,6)}")
print(f"Answer of Divide = {divide(4,6)}")