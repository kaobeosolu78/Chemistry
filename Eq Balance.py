from element import element
from molecule import molecule
from operator import itemgetter

class equation:
    def __init__(self,products,reactants,balanced):
        self.reactants = reactants
        self.products = products

    def __str__(self):
        eq = ""
        for k in range(len(self.products)):
            if k != len(self.products)-1:
                eq += "{}{}+".format(self.products[k].coeff,self.products[k].formula)
            else:
                eq += "{}{}->".format(self.products[k].coeff,self.products[k].formula)
        for i in range(len(self.reactants)):
            if i != len(self.reactants)-1:
                eq += "{}{}+".format(self.reactants[i].coeff,self.reactants[i].formula)
            else:
                eq += "{}{}".format(self.reactants[i].coeff,self.reactants[i].formula)
        return eq

    def check_balance(self):
        check = [[],[]]
        for k in range(2):
            for p_mol in [self.products,self.reactants][k]:
                for p_ele in p_mol.components():
                        check[k].append([p_ele.formula,p_mol.coeff*p_ele.coeff])
        check = sorted(check,key=itemgetter(1))
        if check[0] == check[1]:
            return True
        else:
            return False

    


water = (equation([molecule("hydrogen","H2",2),molecule("oxygen","O2")],[molecule("water","H2O",2)],True)).check_balance()
