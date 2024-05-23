class ContaBancaria:
    def __init__(self, titular='', saldo=0):
        self._ativo = False
        self.titular = titular
        self.saldo = saldo
    
    def __str__(self):
        return f'Titular {self.titular} tem saldo de R${self.saldo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

conta1 = ContaBancaria("Vincius", 2500)
conta2 = ContaBancaria("Maria", 450)
conta3 = ContaBancaria("Carlos", 200)

print(conta1)
print(conta2)

print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")
