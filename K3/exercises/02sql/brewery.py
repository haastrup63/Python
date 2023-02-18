class Brewery:
    def __init__(self, id, name, adress, country):
        self.id = id
        self.name = name
        self.adress = adress
        self.country = country

    def __str__(self):
        return f'{self.id} {self.name} {self.adress} {self.country}'