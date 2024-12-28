def add_discipline(name, id, prof, workload):
    disciplines.append({'name': name, 'id': id, 'professor': prof, 'workload': workload})
    return disciplines

disciplines = []

while True:
    print('Escolha uma opção')
    print('1 - Lista das disciplinas')
    print('2 - Adcionar a lista de disciplinas')
    print('3 - Sair')
    option = input('Insita o número da opção desejada: ')

    if option == '1':
        for discipline in disciplines:
            print(discipline)
    elif option == '2':
        name = input('Digite o nome da disciplina: ')
        id = int(input('Digite o id da disciplina: '))
        prof = input('Digite o nome do professor da disciplina: ')
        workload = int(input('Digite a carga horaria da disciplina: '))
        add_discipline(name, id, prof, workload)
    elif option == '3':
        break
    else:
        print('Opção inválida. Tente novamente.')