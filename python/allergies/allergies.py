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

    def __init__(self, number):
        self.number = number
        self.list = []

    def is_allergic_to(self, list):
        for thing in list:
            if self.number & allergens[thing] != 0:
                self.list.append(thing)
        return self.list
