import random

def gerarCodigoProfessor():

    letrasAlfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    numero = random.randint(1, 99999);
    letra = random.choice(letrasAlfabeto)

    return f"{letra}{numero}"

def gerarCodigoDisciplina():
    letrasAlfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    numero = random.randint(1, 99999);
    letra = random.choice(letrasAlfabeto)

    return f"{letra}{numero}"


def gerarCodigoTurma():
    letrasAlfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    numero = random.randint(1, 99999);
    letra = random.choice(letrasAlfabeto)

    return f"{letra}{numero}"