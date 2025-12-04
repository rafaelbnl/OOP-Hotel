class Cliente():
    ultimo_id = 1000
    
    def __init__(self, nome: str, telefone: str, email:str):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        
        self.__id = Cliente.ultimo_id # cria primeiro cliente com ID único = 1000
        Cliente.ultimo_id += 1        # faz com que o próximo cliente tenha ID único incrementado

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

    def set_nome(self, novo_nome):
        self.__nome = novo_nome
    
    def set_rede(self, nova_rede):
        self.__rede = nova_rede

    def cadastrar_quarto(self, numero: int, tipo: str, diaria: float, status: str):
        if status.lower() == "s":
            status_completo = "disponível"  
        elif status.lower() == "n":
            status_completo = "ocupado"
        else:
            print("\nStatus inválido! Use 's' ou 'n'.")
            return
        
        quarto = Quarto(numero, tipo, diaria, status_completo)
        self.__lista_de_quartos.append(quarto)
        print(f"\nQuarto {numero} cadastrado com sucesso!")

    def editar_quarto(self, numero: int, nova_diaria: float, novo_status: str):
        if not self.__lista_de_quartos: 
            return "\nNenhum quarto cadastrado."
        
        for quarto in self.__lista_de_quartos:
            if quarto.get_numero() == numero:  
                quarto.set_diaria(nova_diaria) 
                quarto.set_status(novo_status)  
                return f"\nQuarto {numero} editado com sucesso!"
        
        return f"\nQuarto {numero} não encontrado."
            
                    
    def excluir_quarto(self, numero):
        if not self.__lista_de_quartos:
            return "\nNenhum quarto cadastrado."
        for quarto in self.__lista_de_quartos:
            if quarto.get_numero() == numero:
                self.__lista_de_quartos.remove(quarto)
                return f"\nQuarto {numero} excluído com sucesso!"
        return f"\nQuarto {numero} não encontrado."
        
        
    def listar_quartos(self):
        if not self.__lista_de_quartos:
            return "\nNão há quartos cadastrados."
    
        print("\nQuartos disponíveis:")
        for quarto in self.__lista_de_quartos:
            if quarto.get_status() == "disponível":
                print(f"Quarto {quarto.get_numero()} - {quarto.get_tipo()} - R${quarto.get_diaria()}")
    
        print("\nQuartos indisponíveis:")
        for quarto in self.__lista_de_quartos:
            if quarto.get_status() != "disponível":
                print(f"Quarto {quarto.get_numero()} - {quarto.get_tipo()} - R${quarto.get_diaria()} - {quarto.get_status()}")
        
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

    def criar_reserva(self, cliente: Cliente, numero_quarto: int, checkin: str, checkout: str, status: str):
        quarto_encontrado = None
        for quarto in self.__hotel.get_lista_de_quartos():
            if quarto.get_numero() == numero_quarto:
                quarto_encontrado = quarto
                break
        if not quarto_encontrado:
            return "Quarto não encontrado"
        
        if quarto_encontrado.get_status() != "disponível":
            return "Quarto não está disponível"
        
        reserva = Reserva(
            cliente=cliente,
            quarto=quarto_encontrado,
            checkin=checkin,
            checkout=checkout,
            status=status
        )

        quarto_encontrado.set_status("ocupado")

        self.__lista_de_reservas.append(reserva)

        return f"Reserva criada para {cliente.get_nome()} (ID: {cliente.get_id()})"

    def listar_reservas(self):
        if not self.__lista_de_reservas:
            return "Não há reservas cadastradas"
        for reserva in self.__lista_de_reservas:
            print(f"Nome: {reserva.get_cliente().get_nome()} | ID: {reserva.get_cliente().get_id()} | Quarto: {reserva.get_quarto().get_numero()} | Check-in: {reserva.get_checkin()} | Check-out: {reserva.get_checkout()} | Status: {reserva.get_status()}")

    def modificar_reserva(self, id_cliente: int, novo_quarto: Quarto, novo_checkin:str, novo_checkout:str, novo_status:str):
        for reserva in self.__lista_de_reservas:
            if reserva.get_cliente().get_id() == id_cliente:
                reserva.set_quarto(novo_quarto)
                reserva.set_checkin(novo_checkin)
                reserva.set_checkout(novo_checkout)
                reserva.set_status(novo_status)
        return "Reserva atualizada"

    def cancelar_reserva(self, id_cliente: int):
        for reserva in self.__lista_de_reservas:
            if reserva.get_cliente().get_id() == id_cliente:
                self.__lista_de_reservas.remove(reserva)
                reserva.get_quarto().set_status("disponível")
        return "Reserva cancelada"
            
    def listar_informacoes(self):
        for reserva in self.__lista_de_reservas:
            cliente = reserva.get_cliente()
            print(f"Nome: {cliente.get_nome()} | Telefone: {cliente.get_telefone()} | E-mail: {cliente.get_email()}")
