from element import Element

class Molecule:
    def __init__(self,name=None,formula=None,coeff=1):
        if name:
            self.name = name
        if formula:
            self.formula = formula
        self.coeff = int(coeff)

    def components(self,coeff=1):
        elements = []
        for k in range(len(self.formula) + 1):
            if self.formula[-k].upper() == self.formula[-k] and k != 0 and self.formula[-k].isalpha() != False:
                try:
                    g
                except:
                    g = -len(self.formula)
                new = self.formula[-k:-g]
                g = k
                if new.isalpha() == True:
                    elements.append(Element(new,1*coeff))
                else:
                    try:
                        int(new[-2:])
                        elements.append(Element(new[:-2],int(new[-2:])*coeff))
                    except:
                        elements.append(Element(new[:-1],int(new[-1:])*coeff))
        return elements

