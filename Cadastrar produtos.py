def cadastrar_evento():
    nome = input("Digite o nome do evento: ")
    data = input("Digite a data do evento (DD/MM/AAAA): ")
    descricao = input("Digite a descrição do evento: ")
    vagas = int(input("Digite o número máximo de participantes: "))
    evento = {
        'nome': nome,
        'data': data,
        'descricao': descricao,
        'vagas': vagas,
        'inscritos': []
    }
    eventos.append(evento)
