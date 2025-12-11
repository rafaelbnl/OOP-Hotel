class Cliente():
    ultimo_id = 1000

    def __init__(self, nome: str, telefone: str, email:str):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        
# cria primeiro cliente com ID único = 1000
# faz com que o próximo cliente tenha ID único incrementado

        self.__id = Cliente.ultimo_id 
        Cliente.ultimo_id += 1        

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone
    
    def get_email(self):
        return self.__email
    
    def get_id(self):
        return self.__id
    #sem setter para id; fixo 
    def set_nome(self, novo_nome:str):
        self.__nome = novo_nome

    def set_telefone(self,novo_telefone:str):
        self.__telefone = novo_telefone

    def set_email(self, novo_email:str):
        self.__email = novo_email

class Quarto():
    def __init__(self, numero:int, tipo:str, diaria:float, status:str):
        self.__numero = numero
        self.__tipo = tipo
        self.__diaria = diaria
        self.__status = status

    def get_numero(self):
        return self.__numero
    def get_tipo(self):
        return self.__tipo
    def get_diaria(self):
        return self.__diaria
    def get_status(self):
        return self.__status

# sem setter pra número; fixo 
    def set_tipo(self, novo_tipo):
        self.__tipo = novo_tipo
    def set_diaria(self, nova_diaria):
        self.__diaria = nova_diaria
    def set_status(self, novo_status):
        status_validos = ["disponível", "ocupado"]
        if novo_status in status_validos:
            self.__status = novo_status
        else:
            print(f"\nStatus inválido! Use: {status_validos}")

class Reserva:
    ultimo_id = 1
    
    def __init__(self, cliente: Cliente, quarto: Quarto, checkin: str, checkout: str, status:str):
        self.__cliente = cliente
        self.__quarto = quarto
        self.__checkin = checkin
        self.__checkout = checkout
        self.__status = status
        self.__id = Reserva.ultimo_id
        Reserva.ultimo_id += 1

    def get_cliente(self):
        return self.__cliente
    def get_quarto(self):
        return self.__quarto
    def get_checkin(self):
        return self.__checkin
    def get_checkout(self):
        return self.__checkout
    def get_status(self):
        return self.__status
    def get_id(self):
        return self.__id
# sem setter pra mudar id; fixo
    def set_cliente(self, novo_cliente):
        self.__cliente = novo_cliente
    def set_quarto(self, novo_quarto):
        self.__quarto = novo_quarto
    def set_checkin(self, novo_checkin):
        self.__checkin = novo_checkin
    def set_checkout(self, novo_checkout):
        self.__checkout = novo_checkout
    def set_status(self, novo_status):
        self.__status = novo_status

class Hotel():
    def __init__(self, nome: str, logradouro: str, numero: int, rede: str):
        self.__nome = nome
        self.__logradouro = logradouro
        self.__numero = numero
        self.__rede = rede
        self.__lista_de_quartos = []
        self.__lista_de_clientes = []

    def get_nome(self):
        return self.__nome
    
    def get_logradouro(self):
        return self.__logradouro
    
    def get_numero(self):
        return self.__numero
    
    def get_rede(self):
        return self.__rede
    
    def get_lista_de_quartos(self):
        return self.__lista_de_quartos
    
    def get_lista_de_clientes(self):
        return self.__lista_de_clientes

    def set_nome(self, novo_nome):
        self.__nome = novo_nome
    
    def set_rede(self, nova_rede):
        self.__rede = nova_rede

    def cadastrar_cliente(self):
        nome = input("Digite o nome do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        email = input("Digite o e-mail do cliente: ")
        cliente = Cliente(nome=nome, telefone=telefone, email=email)
        self.__lista_de_clientes.append(cliente)
        return f"Cliente {nome}.title() cadastrado"

    def listar_clientes(self):
        if not self.__lista_de_clientes:
            return "\nNenhum cliente cadastrado"

        for cliente in self.__lista_de_clientes:
            print(f"""
                    ===INFORMAÇÕES====================
                    ID: {cliente.get_id()}
                    Nome: {cliente.get_nome().title()}
                    Telefone: {cliente.get_telefone()}
                    E-mail: {cliente.get_email()}
                    ==================================
                    """)
            return "Fim da lista de clientes"

    def editar_cliente(self):
        cliente_modificado = input("Digite o nome do cliente a modificar: ")
        for cliente in self.__lista_de_clientes:
            if cliente.get_nome().lower() == cliente_modificado.lower():
                while True:
                    modificar = input("""Modificar:
                                        1 - Nome
                                        2 - Telefone
                                        3 - E-mail
                                        """)
                    match modificar:
                        case "1":
                            novo_nome = input("Digite o novo nome: ")
                            cliente.set_nome(novo_nome)
                            return "\nNome modificado"
                        case "2":
                            novo_telefone = input("Digite o novo telefone: ")
                            cliente.set_telefone(novo_telefone)
                            return "\nTelefone modificado"
                        case "3":
                            novo_email = input("Digite o novo e-mail: ")
                            cliente.set_email(novo_email)
                            return "\nE-mail modificado"

    def excluir_cliente(self):
        cliente_excluido = input("Digite o nome do cliente a excluir: ")
        for cliente in self.__lista_de_clientes:
            if cliente.get_nome() == cliente_excluido:
                self.__lista_de_clientes.remove(cliente)
                return f"Cliente {cliente.get_nome()} excluído"


    def cadastrar_quarto(self):
        numero = int(input("Digite o número do quarto: "))
        tipo = input("Digite o tipo de quarto: ")
        diaria = input("Digite o valor da diária: ")
        status = "Disponível"
        quarto = Quarto(numero=numero, tipo=tipo, diaria=diaria, status=status)
        self.__lista_de_quartos.append(quarto)
        return f"\nQuarto {numero} cadastrado com sucesso!"

    def editar_quarto(self):
        if not self.__lista_de_quartos: 
            return "\nNenhum quarto cadastrado"
        quarto_modificado = int(input("Digite o número do quarto a modificar: "))
        for quarto in self.__lista_de_quartos:
            if quarto.get_numero() == quarto_modificado:
                while True:
                    submenu = input("""
1 - Diaria
2 - Status
3 - Voltar
""")
                    match submenu:
                        case "1":
                            nova_diaria = float(input("Digite o voo valor da diária: "))
                            quarto.set_diaria(nova_diaria)
                            return "Valor da diária atualizado"
                        case "2":
                            novo_status = input("Digite o novo status: ")
                            quarto.set_status(novo_status)
                            return f"Status do quarto atualizado. Novo status: {novo_status}"
                        case "3":
                            break
                        case _:
                            return "Opção inválida"
        
            
                    
    def excluir_quarto(self):
        if not self.__lista_de_quartos:
            return "\nNenhum quarto cadastrado."
        quarto_excluido = int(input("Digite o número do quarto a excluir: "))
        for quarto in self.__lista_de_quartos:
            if quarto.get_numero() == quarto_excluido:
                self.__lista_de_quartos.remove(quarto)
                return f"\nQuarto {quarto_excluido} excluído com sucesso!"
        return f"\nQuarto {quarto_excluido} não encontrado."
        
        
    def listar_quartos(self):
        if not self.__lista_de_quartos:
            return "\nNão há quartos cadastrados."
    
        print("\nQuartos disponíveis:")
        for quarto in self.__lista_de_quartos:
            if quarto.get_status() == "disponível":
                print(f"Quarto {quarto.get_numero()} - {quarto.get_tipo().title()} - R${quarto.get_diaria()}")
    
        print("\nQuartos indisponíveis:")
        for quarto in self.__lista_de_quartos:
            if quarto.get_status() != "disponível":
                print(f"Quarto {quarto.get_numero()} - {quarto.get_tipo().title()} - R${quarto.get_diaria()}")
        
class Gerenciador():
    def __init__(self, hotel:Hotel):
        self.__hotel = hotel
        self.__lista_de_reservas = []

    def get_hotel(self):
        return self.__hotel
    
    def get_lista_de_reservas(self):
        return self.__lista_de_reservas
    
    def verificar_disponibilidade(self):
        return self.__hotel.listar_quartos()

    def criar_reserva(self):
        cliente = input("Digite o nome do cliente: ")
        numero_quarto = input("Digite o numero do quarto alocado: ")
        checkin = input("Digite a data do check-in: ")
        checkout = input("Digite a data do check-out: ")
        status = "Indisponível"
        reserva = Reserva(cliente=cliente, quarto=numero_quarto, checkin=checkin, checkout=checkout, status=status)
        self.__lista_de_reservas.append(reserva)
        return "Reserva criada com sucesso"

    def listar_reservas(self):
        if not self.__lista_de_reservas:
            return "Não há reservas cadastradas"
        for reserva in self.__lista_de_reservas:
            cliente = reserva.get_cliente()
            quarto = reserva.get_quarto()
            print(f"""
                    ===INFORMAÇÕES DA RESERVA====================
                    ID da Reserva: {reserva.get_id()}
                    Cliente: {cliente.get_nome().title()}
                    Quarto: {quarto.get_numero()}
                    Check-in: {reserva.get_checkin()}
                    Check-out: {reserva.get_checkout()}
                    Status: {reserva.get_status().title()}
                    ============================================
                    """)
        return "Fim da lista de reservas"


    def modificar_reserva(self):
        reserva_modificada = input("Digite o ID da reserva a modificar: ")
        for reserva in self.__lista_de_reservas:
            if reserva.get_id() == reserva_modificada:
                while True:
                    modificar = input("""Modificar:
                                        1 - Cliente
                                        2 - Quarto
                                        3 - Check-in
                                        4 - Check-out
                                        5 - Status
                                        """)
                    match modificar:
                        case "1":
                            novo_cliente = input("Digite o novo cliente: ")
                            reserva.set_cliente(novo_cliente)
                            return "\nCliente modificado"
                        case "2":
                            novo_quarto = input("Digite o novo quarto: ")
                            reserva.set_quarto(novo_quarto)
                            return "\nQuarto modificado"
                        case "3":
                            novo_checkin = input("Digite o novo check-in: ")
                            reserva.set_checkin(novo_checkin)
                            return "\nCheck-in modificado"
                        case "4":
                            novo_checkout = input("Digite o novo check-out: ")
                            reserva.set_checkout(novo_checkout)
                            return "\nCheck-out modificado"
                        case "5":
                            novo_status = input("Digite o novo status: ")
                            reserva.set_status(novo_status)
                            return "\nStatus modificado"
            

    def cancelar_reserva(self):
        reserva_cancelada = input("Digite o nome do cliente para cancelar a reserva: ")
        for reserva in self.__lista_de_reservas:
            if reserva.get_cliente().get_id() == id_cliente:
                self.__lista_de_reservas.remove(reserva)
                reserva.get_quarto().set_status("disponível")
        return "Reserva cancelada"
            
    def listar_informacoes(self):
        for reserva in self.__lista_de_reservas:
            cliente = reserva.get_cliente()
            print(f"Nome: {cliente.get_nome()} | Telefone: {cliente.get_telefone()} | E-mail: {cliente.get_email()}")


