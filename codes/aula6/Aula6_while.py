num = 0 
while num <= 10:
    print("Contando:",num)
    num = num+1
print("Acabei a contagem")
num= int(input("Digite um numero: "))
while num< 10:
    print("Numero digitado:",num)
    num = int(input("Digite um numero: "))
print("Numero digitado maior que 10:",num)

while int (input("Digite um numero: ")) >10:
    print("O numero digitado é maior a 10")
print("O numero digitado é menor que 10")


num=0
while True:
    print(num)
    num=num+1
    cont=(input("Deseja continuar?(s/n)"))
    if cont == "n":
        print("Encerrando o código")
        break
print("Codigo encerrado")


