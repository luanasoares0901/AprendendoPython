#IMC: peso/altura*2

imc=0
print("***********Calculadora de IMC online******************")

def calculadora(peso,altura):
    global imc
    imc= (peso/(altura**2))
    print("Seu IMC é: ",imc)
    return imc

def impressao(imc,nome):
    if imc>=40:
        print(nome, ",Você está com obesidade mórbida")

    elif imc>=35:
        print(nome,",Você está com obesidade severa")

    elif imc>=30:
        print(nome,",Você está com obesidade")

    elif imc>=25:
        print(nome,",Você está com sobrepeso")

    elif imc>=18.5:
        print(nome,",Você está saudável")

    elif imc>=17:
        print(nome,",Você está com magreza leve")

    elif imc>=16:
        print(nome,",Você está com magreza moderada")

    else:
        print(nome,",Você está com magreza grave")


while True:
    nome=input("Digite seu nome: ")
    peso=float(input("Digite o seu peso: "))
    altura=float(input("Digite a sua altura: "))
    calculadora(peso,altura)
    impressao(imc,nome)

    if input("Deseja calcular outro IMC?(s/n)").upper()=="N":
        break
    print("")
    print("============Novo cálculo===========")

print("")
print("===========Muito obrigado por usar nosso sistema===========")






