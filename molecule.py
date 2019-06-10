from element import element

class molecule:
    def __init__(self,formula=None,name=None,coeff=1):
        if name:
            self.name = formula
        if formula:
            self.formula = name
        self.coeff = coeff
    def __add__(self,ele,eman=None):
        return molecule(eman,self.formula+ele.formula)
    def components(self):
        elements = []
        new_ele = 0
        ele = ""
        for part in self.formula:
            try:
                part = int(part)
            except:
                pass
            if type(part) == str:
                if new_ele == 0 or part == part.lower():
                    new_ele = 1
                    ele += part
                else:
                    elements.append(element(ele, 1))
                    ele = part
                    new_ele = 1
            elif type(part) == int:
                elements.append(element(ele, part))
                ele = ""
                new_ele = 0
        if ele != "":
            elements.append(element(ele, 1))
        return elements

print(molecule("water","H2O",1).components())
