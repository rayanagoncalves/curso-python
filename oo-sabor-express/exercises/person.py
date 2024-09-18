class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def __str__(self):
        return f'{self.name} | {self.age} | {self.profession}'
    
    def birthday(self):
        self.age += 1

    @property
    def greeting(self):
        if(self.profession):
            return f'Olá, sou {self.name}! Trabalho como {self.profession}.'
        else:
            return f'Olá, sou {self.name}!'
        
person = Person(name='Rayana', age=25, profession='Desenvolvedora')
print(person)
person.birthday()
print(person)
print(person.greeting)