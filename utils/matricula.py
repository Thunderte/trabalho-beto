import random

def gerarMatricula():

    letrasAlfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    numero = random.randint(1, 9999);
    letra = random.choice(letrasAlfabeto)

    return f"{numero}-{letra}"