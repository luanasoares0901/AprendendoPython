#Aula 2: Operações matemáticas e input

x=5
y=6
soma= x+y
soma2= soma + 5.0 #o que prevalece é o float
soma3= float(soma) + 6.1  #float(soma) transforma o int em um float
sub= y-x
mult= x*y
div=x/y #o resultado de uma divisão sempre é float

print(soma)
print(sub)
print(mult)
print(type(soma2),soma2)
print(soma3)
print(type(div), div)