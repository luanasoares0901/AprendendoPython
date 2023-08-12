#potência tradicional: eu elevo um número a uma base comum
#potência função  
#potência math
#potência numpy

a=2
b=2
c=2
d=2
resultado=a*b*c*d
print(resultado)

x=2 #base comum 
y=4 #potencia
potencia=x**y
print(potencia)

print(pow(2,5)) #base,expoente

import math
print(math.pow(2,5)) # a diferença é que aqui eu consigo trabalhar com o float

import numpy as np #numpy consome menos processamento
print(np.power(2,6))

import time #analisar tempo de processamento
start = time.process_time()
x = 1000 ** 99999
print("O tempo de processamento usando ** é",time.process_time()-start,"ms")
