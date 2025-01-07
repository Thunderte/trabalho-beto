from utils.formatador import formartarTelefone
from utils.codigo import gerarCodigoProfessor
from models.professor import criarUmProfessor
import sqlite3

def criarProfessor():
    print('------------ INFORMAÇÕES PESSOAIS ------------')
    print('\n Bem vindo ao servidor de cadastro do IFMS \n')

    nome = str(input("Digite o nome do professor para começar:\n"))
    diaNascimento = int(input("Qual o dia de nascimento do professor?\n"))

    if diaNascimento > 31:
        print('Error: digite um dia de nascimento válido')
        exit()
    
    mesNascimento = int(input("Qual o mês de nascimento do professor? \n"))

    if mesNascimento > 12:
        print('Error: digite um mês de nascimento válido')
        exit()

    anoNascimento = int(input("Digite o ano de nascimento do professor: ex: (2001) \n"))

    if(anoNascimento < 1900):
        print('Error: ano de nascimento inválido!')
        exit()

    dataNascimento = f"{diaNascimento}/{mesNascimento}/{anoNascimento}"

    sexoInput = str(input("Qual o sexo do professor? (masculino) ou (feminino)\n"))

    sexo = ""

    if sexoInput != "masculino" and sexoInput != "Masculino" and sexoInput != "M" and sexoInput != "m" and sexoInput != "feminino" and sexoInput != "Feminino" and sexoInput != "F" and sexoInput != "f":
        print("Error: sexo do professor inválido")
        exit()
    elif sexoInput == "masculino" or sexoInput == "Masculino" or sexoInput == "M" or sexoInput == "m":
        sexo = "M"
    elif sexoInput == "feminino" or sexoInput == "Feminino" or sexoInput == "F" or sexoInput == "f":
        sexo = "F"
    
    print("\n ---------- ENDEREÇO ----------\n\n")

    rua = str(input("Qual nome da rua que o professor mora? Ex: (Manoel Pedro de Campos)\n"))
    bairro = str(input("Qual o bairro que o professor mora? Ex: Santa Rita\n"))
    numero = str(input("Qual número da casa que o professor mora? Ex: (1551)\n"))

    endereco = f"Rua {rua}, Bairro {bairro} - N° {numero}"


    print("\n ---------- Comunicação ---------- \n")

    telefoneInput = str(input("Digite o telefone do professor: Ex: 6799999999 \n"))
    email = str(input("Digite o email do professor: Ex: jonathan@ifms.edu.br \n"))

    telefone = formartarTelefone(telefoneInput);
    codigo = gerarCodigoProfessor();
    
    professor = criarUmProfessor(nome, codigo, dataNascimento, sexo, endereco, telefone, email)
    if not professor:
        raise SystemError("Ops... Ocorreu um erro inesperado")
    
    return fprint("professor {nome} criado com sucesso! \n N° do código: {codigo}")

def pesquisarProfessor():
    print('------------ DISCIPLINAS ------------')
    print('\n Bem vindo ao servidor de cadastro de disciplinas \n')

    nome = input("Digite o nome do professor: ")
    conexao = sqlite3.connect("escola.db")
    conn = conexao.cursor()
    conn.execute("SELECT * FROM professores WHERE nome = ?", (nome,))
    resultado = conn.fetchone()

    if resultado:
        if isinstance(resultado, (list, tuple)):
            print(f"Nome: {resultado[1]}, Matrrícula: {resultado[2]}")
        else:
            print("Resultado inesperado:", resultado)

    else:
        print("Professor nao encontrado.");
    
