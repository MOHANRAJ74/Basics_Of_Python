class Calculator:

    def add(self, a, b):
        c=a+b
        print("Addition: ",c)
    def sub(self, a,b):
        c=a-b
        print("Subtraction: ",c)
    def mul(self, a, b):
        c=a*b
        print("Multiplication: ",c)
    def div(self, a, b):
        c=a/b
        print("Division: ",c)

if __name__=="__main__":

    obj = Calculator()

    x=float(input("Enter value of A: "))
    y=float(input("Enter value of B: "))

    obj.add(x,y)
    obj.sub(x,y)
    obj.mul(x,y)
    obj.div(x,y)


