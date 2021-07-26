import string
from random import random, choice

#print (string.ascii_letters) #todas as letras + string.dig
#print (string.digits) #numeros de 0 a 9
#print (string.punctuation) # caracteres especiais
valores = string.ascii_letters
valores += string.digits
valores += string.punctuation
tamanho = 7
senha = ""
#print (valores)

for i in range(tamanho):
    senha += choice(valores)
print(senha)
