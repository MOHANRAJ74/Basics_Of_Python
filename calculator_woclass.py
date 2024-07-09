
def add(a, b):
    c=a+b
    print("Addition: ",c)
def sub(a, b):
    c=a-b
    print("Subtraction: ",c)
def mul(a, b):
    c=a*b
    print("Multiplication: ",c)
def div(a, b):
    c=a/b
    print("Division: ",c)

def main():
    x=int(input("Enter value of A: "))
    y=int(input("Enter value of B: "))

    add(x,y)
    sub(x,y)
    mul(x,y)
    div(x,y)


if __name__=="__main__":
    main()