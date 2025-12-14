class Cliente():
    ultimo_id = 1000

    def __init__(self, nome: str, telefone: str, email:str):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        
# cria primeiro cliente com ID único = 1000
# faz com que o próximo cliente tenha ID único incremental

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