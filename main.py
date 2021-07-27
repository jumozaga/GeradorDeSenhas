import string
from random import random, choice

valores = string.ascii_letters
valores += string.digits
valores += string.punctuation
tamanho = 11
senha = ""

for i in range(tamanho):
    senha += choice(valores)
print ("Sua senha é:")
print(senha)
