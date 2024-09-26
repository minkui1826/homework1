def add(x, y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

a,b = map(float, input().split())

print(f"Add: {add(a,b)}")
print(f"Sub: {sub(a,b)}")
print(f"Mul: {mul(a,b)}")
print(f"Div: {div(a,b)}")