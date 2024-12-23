import random

def gerarCodigoProfessor():

    letrasAlfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    numero = random.randint(1, 99999);
    letra = random.choice(letrasAlfabeto)

    return f"{letra}{numero}"