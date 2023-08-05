#AND, NOT,OR

matricula= 120
aluno= "Sandro"
administrador = False

senha= input("Digite a senha do administrador: ")
if(senha==2563):
    administrador=True
if(matricula== 123) and (aluno=="Sandro"):
    print("Seja bem vindo",aluno)
elif(matricula==123) or (administrador==True):
    print("Seja bem vindo")
else:
    print("Usuário incorreto")