
def soma(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1-num2)
def mul(num1,num2):
    print(num1*num2)
def div(num1,num2):
    if num2==0:
        print("Impossível dividir por zero")
    else:
        print(num1/num2)

soma(8,7)
sub(5,3)
mul(2,2)
div(8,2)
div(8,0)


x= int(input("Digite o primeiro numero:"))
y=int(input("Digite o segundo numero:"))
soma(x,y)
sub(int(input("Digite o primeiro numero:")),int(input("Digite o segundo numero:")))


def soma1(num1,num2):
    return(num1+num2)
def sub1(num1,num2):
    return(num1-num2)
def mul1(num1,num2):
    return(num1*num2)
def div1(num1,num2):
    if num2==0:
        print("Impossível dividir por zero")
    else:
        return(num1/num2)

print(soma1(2,3))
soma1(1,2)
sub1(3,2)
mul1(2,2)
div1(4,2)

result= sub1(4,3)
print(result)
