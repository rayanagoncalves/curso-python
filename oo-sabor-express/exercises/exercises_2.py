# Exercício 1
class BankAccount:
    def __init__(self, holder, balance):
        self._holder = holder
        self._balance = balance
        self._active = False

    def __str__(self):
        return f'{self._holder} - {self._balance}'
    
    @property
    def holder(self):
        return self._holder
    
    @property
    def balance(self): 
        return self._balance
    
    @property
    def active(self): 
        return self._active
    
    @classmethod
    def active_account(cls, account):
        account._active = True
    
first_bank_account = BankAccount('Rayana', 1000)
second_bank_account = BankAccount('Jonathann', 1100)

print(first_bank_account)
print(second_bank_account)

third_bank_account = BankAccount('João', 500)
print(third_bank_account)
BankAccount.active_account(third_bank_account)
print(third_bank_account)
print(third_bank_account.holder)

class BankClient:
    def __init__(self, name, age, address, document, profession):
        self.name = name
        self.age = age
        self.address = address
        self.document = document
        self.profession = profession

    @classmethod
    def create_account(cls, name, age, address, document, profession):
        account = BankClient(name, age, address, document, profession)
        return account

cliente2 = BankClient("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = BankClient("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")

account = BankClient.create_account("Ana", 30, "Rua A", "123.456.789-01", "Backend")
print(f"Conta de {account.name} criada com sucesso.")


