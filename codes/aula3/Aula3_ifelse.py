x = 15

if(x>10):
    print("O meu x é maior que 10: ",x)
if(x>5):
    print("O meu x é maior que 5: ",x)
if(x>2):
    print("O meu x é maior que 2: ",x)
else:
    print("Não é uma opção acima: ",x)

saldo=15

if(saldo>=10):
    print("Da pra comprar Bolo")
elif(saldo>5):
    print("Da pra comprar Tapioca")
elif(saldo>2):
    print("Da pra comprar pão")
else:
    print("Bebe água pra passar a fome")


saldo1= 80.00
cheque_especial= 200.00
preco_tablet = 120.00

if(saldo1>=preco_tablet):
    print("Venda autorizada")
    troco=saldo1-preco_tablet
    print("Troco: R$",troco)
else:
    print("Saldo insuficiente")
    diferenca=preco_tablet-saldo1
    if(cheque_especial>=diferenca):
        autorizacao=input("Permite usar o cheque especial?(s/n) ")
        if(autorizacao == "s"):
            print("Venda autorizada")
            cheque_especial=cheque_especial-diferenca
            print("Seu novo saldo do cheque especial é: R$",cheque_especial)
    else:
        print("Deposite R$",diferenca," para comprar")
