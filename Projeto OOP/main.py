from classes import *

hotel1 = Hotel(nome="Refúgio dos Sonhos", logradouro="Rua da Paz", numero=123, rede="Accor")

hotel1.cadastrar_quarto(numero=1, tipo="single", diaria=1000, status="Disponível")
hotel1.cadastrar_quarto(numero=2, tipo="single", diaria=1000, status="Disponível")
hotel1.cadastrar_quarto(numero=3, tipo="double", diaria=1000, status="Disponível")
hotel1.cadastrar_quarto(numero=4, tipo="suite", diaria=1000, status="Indisponível")

refugio = Gerenciador(hotel1)

cliente1 = Cliente(nome="João da Silva", telefone= 85974562153, email="joaozins@gmail.com", id=id)
cliente2 = Cliente(nome="Maria de Sousa", telefone= 85979865153, email="mariazinhas@hotmail.com", id=id)
cliente3 = Cliente(nome="Matusalém dos Santos", telefone= 85884561278, email="oveimatusa@uol.com.br", id=id)

refugio.criar_reserva(cliente1, numero_quarto=1, checkin="01/12/2025", checkout="06/12/2025", status="Paga")
refugio.criar_reserva(cliente2, numero_quarto=2, checkin="03/12/2025", checkout="19/12/2025", status="Pendente")
refugio.criar_reserva(cliente3, numero_quarto=3, checkin="05/12/2025", checkout="10/12/2025", status="Em análise")

refugio.listar_informacoes()


# refugio.listar_reservas()

# print(refugio.modificar_reserva())
# print(refugio.cancelar_reserva())

# # refugio.verificar_disponibilidade()

# # hotel1.editar_quarto()
# # hotel1.editar_quarto()
# # hotel1.excluir_quarto()

