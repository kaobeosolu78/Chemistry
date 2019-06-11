from element import Element
from molecule import Molecule
from operator import itemgetter
from itertools import product

class Equation:
    def __init__(self,reactants,products,balanced=True):
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
        if sorted(check[0],key=itemgetter(0)) == sorted(check[1],key=itemgetter(0)):
            return True
        else:
            return False

    def balance(self):
        coeffs = [cor.coeff for cor in self.reactants]+[cop.coeff for cop in self.products]
        els = [cor.formula for cor in self.reactants]+[cop.formula for cop in self.products]
        p = [prod.components(prod.coeff) for prod in self.products]
        r = [reac.components(reac.coeff) for reac in self.reactants]

        loops = [l for l in product((i for i in range(1,21)), repeat=len(coeffs))]
        working_coeffs = []
        for loop in range(len(loops)):
            new_reacts,new_prods = [],[]
            count = -1
            for reacts in self.reactants:
                count += 1
                new_reacts.append(Molecule(formula=reacts.formula,coeff=loops[loop][count]))
            for prods in self.products:
                count += 1
                new_prods.append(Molecule(formula=prods.formula,coeff=loops[loop][count]))
            check = Equation(new_reacts,new_prods).check_balance()
            if check == True:
                working_coeffs.append(loops[loop])
        return els,working_coeffs

water = (Equation([Molecule("hydrogen","H2",2),Molecule("oxygen","O2")],[Molecule("water","H2O",2)]))
print(water.balance())
