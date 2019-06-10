class Element:
    def __init__(self,formula,coeff=1):
        self.formula = formula
        self.coeff = coeff
    def __str__(self):
        if self.coeff == 1:
            coeff = ""
        else: coeff = self.coeff
        return "{}{}".format(self.formula,coeff)
    def __add__(self,ele,eman=None):
        return molecule(eman,self.formula+ele.formula)
