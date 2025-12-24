from cliente import Cliente
from quarto import Quarto

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
        try:
            nome = input("Digite o nome do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            email = input("Digite o e-mail do cliente: ")
            cliente = Cliente(nome=nome, telefone=telefone, email=email)
            self.__lista_de_clientes.append(cliente)
            return f"Cliente {nome.title()} cadastrado"
        except Exception as e:
            return f"Erro ao cadastrar cliente: {e}"

    def listar_clientes(self):
        if not self.__lista_de_clientes:
            return "\nNenhum cliente cadastrado"

        for cliente in self.__lista_de_clientes:
            print(f"""
                    ===INFORMAÇÕES====================
                    ID: {cliente.id}
                    Nome: {cliente.nome.title()}
                    Telefone: {cliente.telefone}
                    E-mail: {cliente.email}
                    ==================================
                    """)
            return "Fim da lista de clientes"

    def editar_cliente(self):
        cliente_modificado = int(input("Digite o ID do cliente a modificar: "))
        for cliente in self.__lista_de_clientes:
            if cliente.id == cliente_modificado:
                try:
                    while True:
                        modificar = input("""Modificar:
                                            1 - Nome
                                            2 - Telefone
                                            3 - E-mail
                                            4 - Voltar
                                            """)
                        match modificar:
                            case "1":
                                novo_nome = input("Digite o novo nome: ")
                                cliente.nome = novo_nome
                                return "\nNome modificado"
                            case "2":
                                novo_telefone = input("Digite o novo telefone: ")
                                cliente.telefone = novo_telefone
                                return "\nTelefone modificado"
                            case "3":
                                novo_email = input("Digite o novo e-mail: ")
                                cliente.email = novo_email
                                return "\nE-mail modificado"
                            case "4":
                                return "\nOperação cancelada"
                            case _:
                                print("\nOpção inválida")
                except:
                    return "\nErro ao modificar cliente"
        return f"\nCliente '{cliente_modificado}' não encontrado"

    def excluir_cliente(self):
        cliente_excluido = int(input("Digite o ID do cliente a excluir: "))
        for cliente in self.__lista_de_clientes:
            if cliente.id == cliente_excluido:
                self.__lista_de_clientes.remove(cliente)
                return f"Cliente {cliente.nome} excluído"


    def cadastrar_quarto(self):
        try:
            numero = int(input("Digite o número do quarto: "))
            tipo = input("Digite o tipo de quarto: ")
            diaria = float(input("Digite o valor da diária: "))
            status = "Disponível"
            quarto = Quarto(numero=numero, tipo=tipo, diaria=diaria, status=status)
            self.__lista_de_quartos.append(quarto)
            return f"\nQuarto {numero} cadastrado com sucesso!"
        except Exception as e:
            return f"\nErro ao cadastrar quarto: {e}"

    def editar_quarto(self):
        if not self.__lista_de_quartos: 
            return "\nNenhum quarto cadastrado"
        quarto_modificado = int(input("Digite o número do quarto a modificar: "))
        for quarto in self.__lista_de_quartos:
            if quarto.numero == quarto_modificado:
                try:
                    while True:
                        submenu = input("""
                            1 - Diaria
                            2 - Status
                            3 - Voltar
                            """)
                        match submenu:
                            case "1":
                                nova_diaria = float(input("Digite o voo valor da diária: "))
                                quarto.diaria = nova_diaria
                                return "Valor da diária atualizado"
                            case "2":
                                novo_status = input("Digite o novo status: ")
                                quarto.status = novo_status
                                return f"Status do quarto atualizado. Novo status: {novo_status}"
                            case "3":
                                break
                            case _:
                                return "Opção inválida"
                except Exception as e:
                    return f"Erro ao modificar quarto: {e}"
        
            
                    
    def excluir_quarto(self):
        if not self.__lista_de_quartos:
            return "\nNenhum quarto cadastrado."
        try:
            quarto_excluido = int(input("Digite o número do quarto a excluir: "))
            for quarto in self.__lista_de_quartos:
                if quarto.numero == quarto_excluido:
                    self.__lista_de_quartos.remove(quarto)
                    return f"\nQuarto {quarto_excluido} excluído com sucesso!"
        except Exception as e:
            return f"\nErro ao excluir quarto: {e}"
        return f"\nQuarto {quarto_excluido} não encontrado."
        
        
    def listar_quartos(self):
        if not self.__lista_de_quartos:
            return "\nNão há quartos cadastrados."
    
        print("\nQuartos disponíveis:")
        for quarto in self.__lista_de_quartos:
            if quarto.status == "disponível":
                print(f"Quarto {quarto.numero} - {quarto.tipo.title()} - R${quarto.diaria}")
    
        print("\nQuartos indisponíveis:")
        for quarto in self.__lista_de_quartos:
            if quarto.status != "disponível":
                print(f"Quarto {quarto.numero} - {quarto.tipo.title()} - R${quarto.diaria}")
        