x=0

for x  in range(5):
    print(x)

for x in range(1,10,2): #pula de 2 em 2 
    print(x)


for x in range(1,10): #vai direto do 1 ao 10
    print(x)


#Entrada do trabalho:08h e Saída: 18h
for h_trabalho in range(8,18,1): #range(inicio,fim,passo)
    print("Trabalho das",h_trabalho, "até às",h_trabalho+1)


################################################################
linguagens=['Python','C++','PHP','JavaScript','Java']
for i in range(len(linguagens)):
    print(linguagens[i])


for linguagem in linguagens:
    print(linguagem)

linguagens.append('Angular')

for linguagem in linguagens:
    print(linguagem)
