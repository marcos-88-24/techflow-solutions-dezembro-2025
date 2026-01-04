eventos = []  # Lista para armazenar os eventos
inscricoes = []  # Lista para armazenar as inscrições

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
print(f"Evento '{nome}' cadastrado com sucesso!")

def atualizar_evento():
    nome = input("Digite o nome do evento que deseja atualizar: ")
    evento_encontrado = False
    
    for evento in eventos:
        if evento['nome'] == nome:
            evento_encontrado = True
            nova_data = input(f"Digite a nova data do evento (atualmente {evento['data']}): ")
            evento['data'] = nova_data
            novas_vagas = int(input(f"Digite o novo número de vagas (atualmente {evento['vagas']}): "))
            evento['vagas'] = novas_vagas
            print(f"Evento '{nome}' atualizado com sucesso!")
            break
    
    if not evento_encontrado:
        print("Evento não encontrado!")

def visualizar_eventos():
    if not eventos:
        print("Não há eventos cadastrados.")
        return
    
    print("\n--- Lista de Eventos Disponíveis ---")
    for evento in eventos:
        print(f"Nome: {evento['nome']}, Data: {evento['data']}, Descrição: {evento['descricao']}, Vagas Restantes: {evento['vagas'] - len(evento['inscritos'])}")

