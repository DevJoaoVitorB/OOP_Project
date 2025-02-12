# class Usuario
class Usuario:

    def __init__(self, id, nome, email, senha, endereco, cep, cpf, admin):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.endereco = endereco
        self.cep = cep
        self.cpf= cpf
        self.admin = admin

        
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, novo_id):
        self._id = novo_id
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, novo_email):
        self._email = novo_email
    
    
    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, novo_senha):
        self._senha = novo_senha
    
    
    @property
    def endereco(self):
        return self._endereco
    @endereco.setter
    def endereco(self, novo_endereco):
        self._endereco = novo_endereco
    
    
    @property
    def cep(self):
        return self._cep
    @cep.setter
    def cep(self, novo_cep):
        self._cep = novo_cep
    
    
    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf
    
    
    
    @property
    def admin(self):
        return self._admin
    @admin.setter
    def admin(self, novo_admin):
        self._admin = novo_admin
    
    def __str__(self):
        if admin == true:
            f"{id} - {nome} \n\tEmail: {email} \n\tSenha: {senha} \n";
        else:
            return f"{id} - {nome} \n\tEmail: {email} \n\tSenha: {senha} \n\tEndereço: {endereco} \n\tCEP: {CEP} \n\tCPF: {CPF} \n";
    
