
class Element:
    def __init__(self,formula,coeff=1):
        self.formula = formula
        self.coeff = int(coeff)
        if formula.isalpha() == False:
            self.diatomic = True
        else:
            self.diatomic = False
    def __add__(self,add):
        return Element(self.formula,self.coeff+add.coeff)
    def __str__(self):
        if self.coeff == 1:
            coeff = ""
        else: coeff = self.coeff
        return "{}{}".format(self.formula,coeff)

