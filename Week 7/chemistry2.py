
def main():
    # Get a chemical formula for a molecule from the user.
    formula = input('Enter the molecular formula of the sample:  ')
    # Get the mass of a chemical sample in grams from the user.
    sample_mass = input('Enter the mass in grams of the sample:  ')
    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    periodic_table_dict = make_periodic_table()
    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    symbol_quantity_list = parse_formula(formula, periodic_table_dict)
    print(symbol_quantity_list)
    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)
    # Compute the number of moles in the sample.
    
    # Print the molar mass.
    print(f'{molar_mass: .4f} grams/mole')
    # Print the number of moles.


def make_periodic_table():
    periodic_table_dict = [
        {'symbol' : "Ac" , 	'name': "Actinium", 'atomic_mass':	227    },    
        {'symbol' : "Ag" , 	'name': "Silver", 'atomic_mass':	107.8682},
        {'symbol' : "Al" , 	'name': "Aluminum", 'atomic_mass':	26.9815386},
        {'symbol' : "Ar" , 	'name': "Argon", 'atomic_mass':	39.948     },
        {'symbol' : "As" , 	'name': "Arsenic", 'atomic_mass':	74.9216},
        {'symbol' : "At" , 	'name': "Astatine", 'atomic_mass':	210},
        {'symbol' : "Au" , 	'name': "Gold", 'atomic_mass':	196.966569},
        {'symbol' : "B"  , 	'name': "Boron", 'atomic_mass':	10.811},
        {'symbol' : "Ba" , 	'name': "Barium", 'atomic_mass':	137.327},
        {'symbol' : "Be" , 	'name': "Beryllium", 'atomic_mass':	9.012182},
        {'symbol' : "Bi" , 	'name': "Bismuth", 'atomic_mass':	208.9804},
        {'symbol' : "Br" , 	'name': "Bromine", 'atomic_mass':	79.904},
        {'symbol' : "C"  , 	'name': "Carbon", 'atomic_mass':	12.0107},
        {'symbol' : "Ca" , 	'name': "Calcium", 'atomic_mass':	40.078},
        {'symbol' : "Cd" , 	'name': "Cadmium", 'atomic_mass':	112.411},
        {'symbol' : "Ce" , 	'name': "Cerium", 'atomic_mass':	140.116},
        {'symbol' : "Cl" , 	'name': "Chlorine", 'atomic_mass':	35.453},
        {'symbol' : "Co" , 	'name': "Cobalt", 'atomic_mass':	58.933195},
        {'symbol' : "Cr" , 	'name': "Chromium", 'atomic_mass':	51.9961},
        {'symbol' : "Cs" , 	'name': "Cesium", 'atomic_mass':	132.9054519},
        {'symbol' : "Cu" , 	'name': "Copper", 'atomic_mass':	63.546},
        {'symbol' : "Dy" , 	'name': "Dysprosium", 'atomic_mass':	162.5},
        {'symbol' : "Er" , 	'name': "Erbium", 'atomic_mass':	167.259},
        {'symbol' : "Eu" , 	'name': "Europium", 'atomic_mass':	151.964},
        {'symbol' : "F"  , 	'name': "Fluorine", 'atomic_mass':	18.9984032},
        {'symbol' : "Fe" , 	'name': "Iron", 'atomic_mass':	55.845},
        {'symbol' : "Fr" , 	'name': "Francium", 'atomic_mass':	223},
        {'symbol' : "Ga" , 	'name': "Gallium", 'atomic_mass':	69.723},
        {'symbol' : "Gd" , 	'name': "Gadolinium", 'atomic_mass':	157.25},
        {'symbol' : "Ge" , 	'name': "Germanium", 'atomic_mass':	72.64},
        {'symbol' : "H"  , 	'name': "Hydrogen", 'atomic_mass':	1.00794},
        {'symbol' : "He" , 	'name': "Helium", 'atomic_mass':	4.002602},
        {'symbol' : "Hf" , 	'name': "Hafnium", 'atomic_mass':	178.49},
        {'symbol' : "Hg" , 	'name': "Mercury", 'atomic_mass':	200.59},
        {'symbol' : "Ho" , 	'name': "Holmium", 'atomic_mass':	164.93032},
        {'symbol' : "I"  , 	'name': "Iodine", 'atomic_mass':	126.90447},
        {'symbol' : "In" , 	'name': "Indium", 'atomic_mass':	114.818},
        {'symbol' : "Ir" , 	'name': "Iridium", 'atomic_mass':	192.217},
        {'symbol' : "K"  , 	'name': "Potassium", 'atomic_mass':	39.0983},
        {'symbol' : "Kr" , 	'name': "Krypton", 'atomic_mass':	83.798},
        {'symbol' : "La" , 	'name': "Lanthanum", 'atomic_mass':	138.90547},
        {'symbol' : "Li" , 	'name': "Lithium", 'atomic_mass':	6.941},
        {'symbol' : "Lu" , 	'name': "Lutetium", 'atomic_mass':	174.9668},
        {'symbol' : "Mg" , 	'name': "Magnesium", 'atomic_mass':	24.305},
        {'symbol' : "Mn" , 	'name': "Manganese", 'atomic_mass':	54.938045},
        {'symbol' : "Mo" , 	'name': "Molybdenum", 'atomic_mass':	95.96},
        {'symbol' : "N"  , 	'name': "Nitrogen", 'atomic_mass':	14.0067},
        {'symbol' : "Na" , 	'name': "Sodium", 'atomic_mass':	22.98976928},
        {'symbol' : "Nb" , 	'name': "Niobium", 'atomic_mass':	92.90638},
        {'symbol' : "Nd" , 	'name': "Neodymium", 'atomic_mass':	144.242},
        {'symbol' : "Ne" , 	'name': "Neon", 'atomic_mass':	20.1797},
        {'symbol' : "Ni" , 	'name': "Nickel", 'atomic_mass':	58.6934},
        {'symbol' : "Np" , 	'name': "Neptunium", 'atomic_mass':	237},
        {'symbol' : "O"  , 	'name': "Oxygen", 'atomic_mass':	15.9994},
        {'symbol' : "Os" , 	'name': "Osmium", 'atomic_mass':	190.23},
        {'symbol' : "P"  , 	'name': "Phosphorus", 'atomic_mass':	30.973762},
        {'symbol' : "Pa" , 	'name': "Protactinium", 'atomic_mass':	231.03588},
        {'symbol' : "Pb" , 	'name': "Lead", 'atomic_mass':	207.2},
        {'symbol' : "Pd" , 	'name': "Palladium", 'atomic_mass':	106.42},
        {'symbol' : "Pm" , 	'name': "Promethium", 'atomic_mass':	145},
        {'symbol' : "Po" , 	'name': "Polonium", 'atomic_mass':	209},
        {'symbol' : "Pr" , 	'name': "Praseodymium", 'atomic_mass':	140.90765},
        {'symbol' : "Pt" , 	'name': "Platinum", 'atomic_mass':	195.084},
        {'symbol' : "Pu" , 	'name': "Plutonium", 'atomic_mass':	244},
        {'symbol' : "Ra" , 	'name': "Radium", 'atomic_mass':	226},
        {'symbol' : "Rb" , 	'name': "Rubidium", 'atomic_mass':	85.4678},
        {'symbol' : "Re" , 	'name': "Rhenium", 'atomic_mass':	186.207},
        {'symbol' : "Rh" , 	'name': "Rhodium", 'atomic_mass':	102.9055},
        {'symbol' : "Rn" , 	'name': "Radon", 'atomic_mass':	222},
        {'symbol' : "Ru" , 	'name': "Ruthenium", 'atomic_mass':	101.07},
        {'symbol' : "S"  , 	'name': "Sulfur", 'atomic_mass':	32.065},
        {'symbol' : "Sb" , 	'name': "Antimony", 'atomic_mass':	121.76},
        {'symbol' : "Sc" , 	'name': "Scandium", 'atomic_mass':	44.955912},
        {'symbol' : "Se" , 	'name': "Selenium", 'atomic_mass':	78.96},
        {'symbol' : "Si" , 	'name': "Silicon", 'atomic_mass':	28.0855},
        {'symbol' : "Sm" , 	'name': "Samarium", 'atomic_mass':	150.36},
        {'symbol' : "Sn" , 	'name': "Tin", 'atomic_mass':	118.71},
        {'symbol' : "Sr" , 	'name': "Strontium", 'atomic_mass':	87.62},
        {'symbol' : "Ta" , 	'name': "Tantalum", 'atomic_mass':	180.94788},
        {'symbol' : "Tb" , 	'name': "Terbium", 'atomic_mass':	158.92535},
        {'symbol' : "Tc" , 	'name': "Technetium", 'atomic_mass':	98},
        {'symbol' : "Te" , 	'name': "Tellurium", 'atomic_mass':	127.6},
        {'symbol' : "Th" , 	'name': "Thorium", 'atomic_mass':	232.03806},
        {'symbol' : "Ti" , 	'name': "Titanium", 'atomic_mass':	47.867},
        {'symbol' : "Tl" , 	'name': "Thallium", 'atomic_mass':	204.3833},
        {'symbol' : "Tm" , 	'name': "Thulium", 'atomic_mass':	168.93421},
        {'symbol' : "U"  , 	'name': "Uranium", 'atomic_mass':	238.02891},
        {'symbol' : "V"  , 	'name': "Vanadium", 'atomic_mass':	50.9415},
        {'symbol' : "W"  , 	'name': "Tungsten", 'atomic_mass':	183.84},
        {'symbol' : "Xe" , 	'name': "Xenon", 'atomic_mass':	131.293},
        {'symbol' : "Y"  , 	'name': "Yttrium", 'atomic_mass':	88.90585},
        {'symbol' : "Yb" , 	'name': "Ytterbium", 'atomic_mass':	173.054},
        {'symbol' : "Zn" , 	'name': "Zinc", 'atomic_mass':	65.38         },
        {'symbol' : "Zr" , 	'name': "Zirconium", 'atomic_mass':	91.224}          
        ]
    return periodic_table_dict


class FormulaError(ValueError):
    """FormulaError is the type of error that
    parse_formula will raise if a formula is invalid.
    """

def parse_formula(formula, periodic_table_dict):
    """Convert a chemical formula for a molecule into a compound list
    that stores the quantity of atoms of each element in the molecule.
    For example, this function will convert "H2O" to [["H", 2], ["O", 1]]
    and "PO4H2(CH2)12CH3" to [["P", 1], ["O", 4], ["H", 29], ["C", 13]]

    Parameters
        formula: a string that contains a chemical formula
        periodic_table_dict: the compound dictionary returned
            from make_periodic_table
    Return: a compound list that contains chemical symbols and
        quantities like this [["Fe", 2], ["O", 3]]
    """
    assert isinstance(formula, str), \
        "wrong data type for parameter formula; " \
        f"formula is a {type(formula)} but must be a string"
    assert isinstance(periodic_table_dict, dict), \
        "wrong data type for parameter periodic_table_dict; " \
        f"periodic_table_dict is a {type(periodic_table_dict)} " \
        "but must be a dictionary"

    def parse_quant(formula, index):
        quant = 1
        if index < len(formula) and formula[index].isdecimal():
            start = index
            index += 1
            while index < len(formula) and formula[index].isdecimal():
                index += 1
            quant = int(formula[start:index])
        return quant, index

    def get_quant(elems, symbol):
        return 0 if symbol not in elems else elems[symbol]

    def parse_r(formula, index, level):
        start_index = index
        start_level = level
        elem_dict = {}
        while index < len(formula):
            ch = formula[index]
            if ch == "(":
                group_dict, index = parse_r(formula, index+1, level+1)
                quant, index = parse_quant(formula, index)
                for symbol in group_dict:
                    prev = get_quant(elem_dict, symbol)
                    elem_dict[symbol] = prev + group_dict[symbol] * quant
            elif ch.isalpha():
                symbol = formula[index:index+2]
                if symbol in periodic_table_dict:
                    index += 2
                else:
                    symbol = formula[index:index+1]
                    if symbol in periodic_table_dict:
                        index += 1
                    else:
                        raise FormulaError(
                            "invalid formula, unknown element symbol:",
                            formula, index)
                quant, index = parse_quant(formula, index)
                prev = get_quant(elem_dict, symbol)
                elem_dict[symbol] = prev + quant
            elif ch == ")":
                if level == 0:
                    raise FormulaError(
                        "invalid formula, unmatched close parenthesis:",
                        formula, index)
                level -= 1
                index += 1
                break
            else:
                if ch.isdecimal():
                    # Decimal digit not preceded by an
                    # element symbol or close parenthesis
                    message = "invalid formula:"
                else:
                    # Illegal character: [^()0-9a-zA-Z]
                    message = "invalid formula, illegal character:"
                raise FormulaError(message, formula, index)
        if level > 0 and level >= start_level:
            raise FormulaError(
                "invalid formula, unmatched open parenthesis:",
                formula, start_index - 1)
        return elem_dict, index

    # Return the compound list of element symbols and
    # quantities. Each element in the compound list
    # will be a list in this form: ["symbol", quantity]
    elem_dict, _ = parse_r(formula, 0, 0)
    return list(elem_dict.items())


# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary returned
            from make_periodic_table.
        Return: the total molar mass of all the elements in
            symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # For each list in the compound symbol_quantity_list:
        # Separate the list into symbol and quantity.
        # Get the atomic mass for the symbol from the dictionary.
        # Multiply the atomic mass by the quantity.
        # Add the product into the total mass.

    total_mass = 0
    for i in symbol_quantity_list:
        small_symbol_quantity = i
        element = small_symbol_quantity[0]
        quantity = small_symbol_quantity[1]
        element_list = periodic_table_dict[element]
        atomic_mass = element_list[ATOMIC_MASS_INDEX]
        mass_element = atomic_mass * quantity
        total_mass += mass_element


        
    # Return the total mass.
    return total_mass

if __name__ == "__main__":
    main()



