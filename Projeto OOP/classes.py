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
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_telefone(self,novo_telefone):
        self.__telefone = novo_telefone

    def set_email(self, novo_email):
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

    def set_numero(self, novo_numero):
        self.__numero = novo_numero
    def set_tipo(self, novo_tipo):
        self.__tipo = novo_tipo
    def set_diaria(self, nova_diaria):
        self.__diaria = nova_diaria
    def set_status(self, novo_status):
        self.__status = novo_status

class Reserva:
    def __init__(self, cliente: Cliente, quarto: Quarto, checkin: str, checkout: str, status:str):
        self.__cliente = cliente
        self.__quarto = quarto
        self.__checkin = checkin
        self.__checkout = checkout
        self.__status = status

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
    def __init__(self, nome:str, logradouro:str, numero:int, rede:str):
        self.nome = nome
        self.logradouro = logradouro
        self.numero = numero
        self.rede = rede
        self.lista_de_quartos = []

    def cadastrar_quarto(self, numero:int, tipo:str, diaria:float, status:str):
        quarto = Quarto(numero, tipo, diaria, status)
        if status == "s":
            quarto.status = "Disponível"
        if status == "n":
            quarto.status = "Indisponível"
        self.lista_de_quartos.append(quarto)

    def editar_quarto(self, numero, nova_diaria: float, novo_status: str):
        if not self.lista_de_quartos:
            return "\nNenhum quarto cadastrado."
        for quarto in self.lista_de_quartos:
            if quarto.numero == numero:
                quarto.diaria = nova_diaria
                quarto.status = novo_status
            
                    
    def excluir_quarto(self, numero):
        if not self.lista_de_quartos:
            return "\nNenhum quarto cadastrado."
        for quarto in self.lista_de_quartos:
            if quarto.numero == numero:
                self.lista_de_quartos.remove(quarto)
        
        
    def listar_quartos(self):
        if not self.lista_de_quartos:
            return {"disponíveis": [], "indisponíveis": []}
        
        disponiveis = []
        indisponiveis = []

        for quarto in self.lista_de_quartos:
            info = {
                "numero": quarto.numero,
                "tipo": quarto.tipo,
                "diaria": quarto.diaria,
                "status": quarto.status,
            }

            if quarto.status == "Disponível":
                disponiveis.append(info)
            else:
                indisponiveis.append(info)
            
        return {
                "disponiveis": disponiveis,
                "indisponiveis": indisponiveis
            }
        
class Gerenciador():
    def __init__(self, hotel:str):
        self.hotel = hotel
        self.lista_de_reservas = []
    
    def verificar_disponibilidade(self):
        return self.hotel.listar_quartos()

    def criar_reserva(self, cliente: Cliente, numero_quarto: int, checkin: str, checkout: str, status: str):
        quarto_encontrado = None
        for quarto in self.hotel.lista_de_quartos:
            if quarto.numero == numero_quarto:
                quarto_encontrado = quarto
                break
        if not quarto_encontrado:
            return "Quarto não encontrado"
        
        if quarto_encontrado.status != "Disponível":
            return "Quarto não está disponível"
        
        reserva = Reserva(
            cliente=cliente,
            quarto=quarto_encontrado,
            checkin=checkin,
            checkout=checkout,
            status=status
        )

        quarto_encontrado.status = "Indisponível"

        self.lista_de_reservas.append(reserva)

        return f"Reserva criada para {cliente.get_nome()} (ID: {cliente.get_id()})"

    def listar_reservas(self):
        if not self.lista_de_reservas:
            return "Não há reservas cadastradas"
        for reserva in self.lista_de_reservas:
            print(f"Nome: {reserva.cliente.get_nome()} | ID: {reserva.cliente.get_id()} | Quarto: {reserva.quarto} | Check-in: {reserva.checkin} | Check-out: {reserva.checkout} | Status: {reserva.status}")

    def modificar_reserva(self, id_cliente: int, novo_quarto: Quarto, novo_checkin:str, novo_checkout:str, novo_status:str):
        for reserva in self.lista_de_reservas:
            if reserva.cliente.get_id() == id_cliente:
                reserva.quarto = novo_quarto
                reserva.checkin = novo_checkin
                reserva.checkout = novo_checkout
                reserva.status = novo_status
        return "Reserva atualizada"

    def cancelar_reserva(self, id_cliente: int):
        for reserva in self.lista_de_reservas:
            if reserva.cliente.get_id() == id_cliente:
                self.lista_de_reservas.remove(reserva)
                reserva.quarto.status = "Disponível"
        return "Reserva cancelada"
            
    def listar_informacoes(self):
        for reserva in self.lista_de_reservas:
            print(f"Nome: {reserva.nome} | Telefone: {reserva.telefone} | E-mail: {reserva.email}")
