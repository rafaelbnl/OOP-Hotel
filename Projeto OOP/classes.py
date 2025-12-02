import random

class Cliente():
    def __init__(self, nome: str, telefone: str, email:str, id: str):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__id = id

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone
    
    def get_email(self):
        return self.__email
    
    def get_id(self):
        return self.__id
    
    def set_nome(self):
        novo_nome = input("\nDigite o novo nome: ")
        self.__nome = novo_nome
    def set_telefone(self):
        novo_telefone = input("\nDigite o novo telefone: ")
        self.__telefone = novo_telefone

    def set_email(self):
        novo_email = input("\nDigite o novo email: ")
        self.__email = novo_email

    def set_id(self):
        """Não é possível editar o ID"""
        return None

class Quarto():
    def __init__(self, numero:int, tipo:str, diaria:float, status:str):
        self.numero = numero
        self.tipo = tipo
        self.diaria = diaria
        self.status = status

class Hotel():
    def __init__(self, nome:str, logradouro:str, numero:int, rede:str):
        self.nome = nome
        self.logradouro = logradouro
        self.numero = numero
        self.rede = rede
        self.lista_de_quartos = []

    def cadastrar_quarto(self, numero:int, tipo:str, diaria:float, status:str):
        quarto = Quarto(numero, tipo, diaria, status)
        self.lista_de_quartos.append(quarto)

    def editar_quarto(self):
        if not self.lista_de_quartos:
            return "\nNenhum quarto cadastrado."
        quarto_editado = int(input("\nDigite o número do quarto que deseja editar: "))
        for quarto in self.lista_de_quartos:
            if quarto.numero == quarto_editado:
                alterar_diaria = input("\nDeseja alterar a diária do quarto? (s/n)")
                if alterar_diaria == "s":
                    nova_diaria = float(input("\nDigite o novo valor da diária: "))
                    quarto.diaria = nova_diaria
                    return "\nValor da diária atualizado"
                elif alterar_diaria == "n":
                    pass
                else:
                    return "\nResponda apenas sim ou não"
                alterar_status = input("\nDeseja alterar o status do quarto? (s/n)")
                if alterar_status == "s":
                    novo_status = input("\nO quarto está disponível? (s/n)")
                    if novo_status == "s":
                        quarto.status = "Disponível"
                        return print(f"Quarto {quarto.numero} disponibilizado")
                    elif novo_status == "n":
                        quarto.status = "Indisponível"
                        return print(f"Quarto {quarto.numero} reservado")
                    else:
                        return "\nResponda apenas sim ou não"
                    
    def excluir_quarto(self):
        if not self.lista_de_quartos:
            return "\nNenhum quarto cadastrado."
        quarto_excluido = int(input("\nDigite o número do quarto a ser excluído: "))
        for quarto in self.lista_de_quartos:
            if quarto.numero == quarto_excluido:
                self.lista_de_quartos.remove(quarto)
                print("\nQuarto excluído")

    def listar_quartos(self):
        for quarto in self.lista_de_quartos:
            if quarto.status == "Disponível":
                print("\nQuartos disponíveis: ")
                print("----------------------------------------")
                print(f"Número: {quarto.numero} | Tipo: {quarto.tipo.title()} | Diária: R${quarto.diaria:.2f}")
            elif quarto.status == "Indisponível":
                print("\nQuartos indisponíveis: ")
                print("----------------------------------------")
                print(f"Número: {quarto.numero} | Tipo: {quarto.tipo.title()} | Diária: R${quarto.diaria:.2f}")
        return "----------------------------------------"

class Gerenciador():
    def __init__(self, hotel:str):
        self.hotel = hotel
        self.lista_de_reservas = []
        self.lista_de_ids = []
    
    def verificar_disponibilidade(self):
        print(self.hotel.listar_quartos())

    def criar_reserva(self, cliente: Cliente, numero_quarto: int, checkin: str, checkout: str, status:str):

        id = random.randint(1000, 9999)
        while id in self.lista_de_ids:
            id = random.randint(1000, 9999)

        reserva = {
            "nome": cliente.get_nome(),
            "telefone": cliente.get_telefone(),
            "email": cliente.get_email(),
            "quarto": numero_quarto,
            "id": id,
            "checkin": checkin,
            "checkout": checkout,
            "status": status
        }

        self.lista_de_reservas.append(reserva)

    def listar_reservas(self):
        print("Reservas confirmadas")
        print("--------------------")
        if not self.lista_de_reservas:
            return "Não há reservas cadastradas"
        for reserva in self.lista_de_reservas:
            print(f"Nome: {reserva['nome']} | ID: {reserva['id']} | Quarto: {reserva['quarto']} | Check-in: {reserva["checkin"]} | Check-out: {reserva["checkout"]} | Status: {reserva["status"]}")

    def editar_dados_reserva(self, reserva):
        print("""
        O que deseja modificar?
        1 - Nome do hóspede
        2 - Quarto alocado
        3 - Data de check-in
        4 - Data de check-out
        5 - Status da reserva
        """)
        opt_reserva = int(input("Digite a opção desejada: "))
        
        match opt_reserva:
            case 1:
                novo_nome = input("Digite o novo nome do hóspede: ")
                reserva["nome"] = novo_nome
                return "Nome alterado com sucesso"
            case 2:
                novo_quarto = int(input("Digite o novo quarto alocado: "))
                reserva["quarto"] = novo_quarto
                return "Quarto alterado com sucesso"
            case 3:
                novo_checkin = input("Digite a nova data de check-in: ")
                reserva["checkin"] = novo_checkin
                return "Data de check-in alterada com sucesso"
            case 4:
                novo_checkout = input("Digite a nova data de check-out: ")
                reserva["checkout"] = novo_checkout
                return "Data de check-out alterada com sucesso"
            case 5:
                novo_status = input("Digite o novo status da reserva: ")
                reserva["status"] = novo_status
                return "Status da reserva alterado com sucesso"
            case _:
                return "Opção inválida"

    def modificar_reserva(self):
        opt = int(input("Buscar reserva por ID (1) ou número do quarto (2)? "))
        
        match opt:
            case 1:
                id = int(input("Digite o ID do hóspede: "))
                for reserva in self.lista_de_reservas:
                    if reserva["id"] == id:
                        return self.editar_dados_reserva(reserva)
                return "Reserva não encontrada"
            
            case 2:
                quarto = int(input("Digite o número do quarto: "))
                for reserva in self.lista_de_reservas:
                    if reserva["quarto"] == quarto:
                        return self.editar_dados_reserva(reserva)
                return "Reserva não encontrada"
            
            case _:
                return "Opção inválida"
            
    def cancelar_reserva(self):
        opt = int(input("Buscar reserva por ID (1) ou número do quarto (2)? "))
        
        match opt:
            case 1:
                id = int(input("Digite o ID do hóspede: "))
                for reserva in self.lista_de_reservas:
                    if reserva["id"] == id:
                        self.lista_de_reservas.remove(reserva)
                        return "Reserva cancelada"
                return "Reserva não encontrada"
            
            case 2:
                quarto = int(input("Digite o número do quarto: "))
                for reserva in self.lista_de_reservas:
                    if reserva["quarto"] == quarto:
                        self.lista_de_reservas.remove(reserva)
                        return "Reserva cancelada"
                return "Reserva não encontrada"
            
            case _:
                return "Opção inválida"
            
    def listar_informacoes(self):
        for reserva in self.lista_de_reservas:
            print(f"Nome: {reserva['nome']} | Telefone: {reserva['telefone']} | E-mail: {reserva['email']}")
