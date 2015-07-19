class Allergies(object):

    allergens = {'eggs': 1,
                 'peanuts': 2,
                 'shellfish': 4,
                 'strawberries': 8,
                 'tomatoes': 16,
                 'chocolate': 32,
                 'pollen': 64,
                 'cats': 128
    }
    al = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']
    def __init__(self, number):
        self.number = number
        self.list = [item for item in self.al if self.number&self.allergens[item]!=0]
    def is_allergic_to(self, item):
        return self.number & self.allergens[item] != 0
