
ehealth = 100
edamage = 10

class Enemy:
    def __init__(self, ehealth, edamage):
        self.ehealth = ehealth
        self.edamage = edamage

    def Eonhit(self, pdamage):
        self.ehealth -= pdamage



