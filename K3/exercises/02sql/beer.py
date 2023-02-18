class Beer:
    def __init__(self, id, name, alc, kind, brewery_id):
        self.id = id
        self.name = name
        self.alc = alc
        self.kind = kind
        self.brewery_id = brewery_id
    
    def __str__(self):
        return f'{self.id} {self.name} {self.alc} {self.kind} {self.brewery_id}'