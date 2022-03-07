# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

from chemistry import make_periodic_table, \
    parse_formula, compute_molar_mass, FormulaError
from pytest import approx
import pytest


# These are the indexes of the
# elements in the periodic table.
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1


def test_make_periodic_table():
    """Verify that the make_periodic_table function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the make_periodic_table function and store the returned
    # dictionary in a variable named periodic_table_dict.
    periodic_table_dict = make_periodic_table()

    # Verify that the make_periodic_table function returns a dictionary.
    assert isinstance(periodic_table_dict, dict), \
        "make_periodic_table function must return a dictionary: " \
        f" expected a dictionary but found a {type(periodic_table_dict)}"

    # Check each item in the periodic table dictionary.
    check_element(periodic_table_dict, "Ac", [ "Actinium",	227, 89])
    check_element(periodic_table_dict, "Ag", [ "Silver",	107.8682, 47])
    check_element(periodic_table_dict, "Al", [ "Aluminum",	26.9815386, 13])
    check_element(periodic_table_dict, "Ar", [ "Argon",	39.948, 18])
    check_element(periodic_table_dict, "As", [ "Arsenic",	74.9216, 33])
    check_element(periodic_table_dict, "At", [ "Astatine",	210, 85])
    check_element(periodic_table_dict, "Au", [ "Gold",	196.966569, 79])
    check_element(periodic_table_dict, "B", [ "Boron",	10.811, 5])
    check_element(periodic_table_dict, "Ba", [ "Barium",	137.327, 56])
    check_element(periodic_table_dict, "Be", ["Beryllium",	9.012182, 4])
    check_element(periodic_table_dict, "Bi", ["Bismuth",	208.9804, 83])
    check_element(periodic_table_dict, "Br", [ "Bromine",	79.904, 35])
    check_element(periodic_table_dict, "C", [ "Carbon",	12.0107, 6])
    check_element(periodic_table_dict, "Ca", [ "Calcium",	40.078, 20])
    check_element(periodic_table_dict, "Cd", [ "Cadmium",	112.411, 48])
    check_element(periodic_table_dict, "Ce", [ "Cerium",	140.116, 58])
    check_element(periodic_table_dict, "Cl", [ "Chlorine",	35.453, 17])
    check_element(periodic_table_dict, "Co", [ "Cobalt",	58.933195, 27])
    check_element(periodic_table_dict, "Cr", [ "Chromium",	51.9961, 24])
    check_element(periodic_table_dict, "Cs", [ "Cesium",	132.9054519, 55])
    check_element(periodic_table_dict, "Cu", [ "Copper",	63.546, 29])
    check_element(periodic_table_dict, "Dy", [ "Dysprosium",	162.5, 66])
    check_element(periodic_table_dict, "Er", [ "Erbium",	167.259, 68])
    check_element(periodic_table_dict, "Eu", [ "Europium",	151.964, 63])
    check_element(periodic_table_dict, "F", [ "Fluorine",	18.9984032, 9])
    check_element(periodic_table_dict, "Fe", [ "Iron",	55.845, 26])
    check_element(periodic_table_dict, "Fr", [ "Francium",	223, 87])
    check_element(periodic_table_dict, "Ga", [ "Gallium",	69.723, 31])
    check_element(periodic_table_dict, "Gd", [ "Gadolinium",	157.25, 64])
    check_element(periodic_table_dict, "Ge", ["Germanium",	72.64, 32])
    check_element(periodic_table_dict, "H",  [ "Hydrogen",	1.00794, 1])
    check_element(periodic_table_dict, "He", [ "Helium",	4.002602, 2])
    check_element(periodic_table_dict, "Hf", [ "Hafnium",	178.49, 72])
    check_element(periodic_table_dict, "Hg", [ "Mercury",	200.59, 80])
    check_element(periodic_table_dict, "Ho", [ "Holmium",	164.93032, 67])
    check_element(periodic_table_dict, "I",  [ "Iodine",	126.90447, 53])
    check_element(periodic_table_dict, "In", [ "Indium",	114.818, 49])
    check_element(periodic_table_dict, "Ir", [ "Iridium",	192.217, 77])
    check_element(periodic_table_dict, "K",  [ "Potassium",	39.0983, 19])
    check_element(periodic_table_dict, "Kr", [ "Krypton",	83.798, 36])
    check_element(periodic_table_dict, "La", ["Lanthanum", 138.90547, 57])
    check_element(periodic_table_dict, "Li", ["Lithium", 6.941, 3])
    check_element(periodic_table_dict, "Lu", ["Lutetium", 174.9668, 71])
    check_element(periodic_table_dict, "Mg", ["Magnesium", 24.305, 12])
    check_element(periodic_table_dict, "Mn", ["Manganese", 54.938045, 25])
    check_element(periodic_table_dict, "Mo", ["Molybdenum", 95.96, 42])
    check_element(periodic_table_dict, "N",  ["Nitrogen", 14.0067, 7])
    check_element(periodic_table_dict, "Na", ["Sodium", 22.98976928, 11])
    check_element(periodic_table_dict, "Nb", ["Niobium", 92.90638, 41])
    check_element(periodic_table_dict, "Nd", ["Neodymium", 144.242, 60])
    check_element(periodic_table_dict, "Ne", ["Neon", 20.1797, 10])
    check_element(periodic_table_dict, "Ni", ["Nickel", 58.6934, 28])
    check_element(periodic_table_dict, "Np", ["Neptunium", 237, 93])
    check_element(periodic_table_dict, "O", ["Oxygen", 15.9994, 8])
    check_element(periodic_table_dict, "Os", ["Osmium", 190.23, 76])
    check_element(periodic_table_dict, "P",  ["Phosphorus", 30.973762, 15])
    check_element(periodic_table_dict, "Pa", ["Protactinium", 231.03588, 91])
    check_element(periodic_table_dict, "Pb", ["Lead", 207.2, 82])
    check_element(periodic_table_dict, "Pd", ["Palladium", 106.42, 46])
    check_element(periodic_table_dict, "Pm", ["Promethium", 145, 61])
    check_element(periodic_table_dict, "Po", ["Polonium", 209, 84])
    check_element(periodic_table_dict, "Pr", ["Praseodymium", 140.90765, 59])
    check_element(periodic_table_dict, "Pt", ["Platinum", 195.084, 78])
    check_element(periodic_table_dict, "Pu", ["Plutonium", 244, 94])
    check_element(periodic_table_dict, "Ra", ["Radium", 226, 88])
    check_element(periodic_table_dict, "Rb", ["Rubidium", 85.4678, 37])
    check_element(periodic_table_dict, "Re", ["Rhenium", 186.207, 75])
    check_element(periodic_table_dict, "Rh", ["Rhodium", 102.9055, 45])
    check_element(periodic_table_dict, "Rn", ["Radon", 222, 86])
    check_element(periodic_table_dict, "Ru", ["Ruthenium", 101.07, 44])
    check_element(periodic_table_dict, "S", ["Sulfur", 32.065, 16])
    check_element(periodic_table_dict, "Sb", ["Antimony", 121.76, 51])
    check_element(periodic_table_dict, "Sc", ["Scandium", 44.955912, 21])
    check_element(periodic_table_dict, "Se", ["Selenium", 78.96, 34])
    check_element(periodic_table_dict, "Si", ["Silicon", 28.0855,14])
    check_element(periodic_table_dict, "Sm", ["Samarium", 150.36, 62])
    check_element(periodic_table_dict, "Sn", ["Tin", 118.71, 50])
    check_element(periodic_table_dict, "Sr", ["Strontium", 87.62, 38])
    check_element(periodic_table_dict, "Ta", ["Tantalum", 180.94788, 73])
    check_element(periodic_table_dict, "Tb", ["Terbium", 158.92535, 65])
    check_element(periodic_table_dict, "Tc", ["Technetium", 98, 43])
    check_element(periodic_table_dict, "Te", ["Tellurium", 127.6, 52])
    check_element(periodic_table_dict, "Th", ["Thorium", 232.03806, 90])
    check_element(periodic_table_dict, "Ti", ["Titanium", 47.867, 22])
    check_element(periodic_table_dict, "Tl", ["Thallium", 204.3833, 81])
    check_element(periodic_table_dict, "Tm", ["Thulium", 168.93421, 69])
    check_element(periodic_table_dict, "U", ["Uranium", 238.02891, 92])
    check_element(periodic_table_dict, "V", ["Vanadium", 50.9415, 23])
    check_element(periodic_table_dict, "W", ["Tungsten", 183.84, 74])
    check_element(periodic_table_dict, "Xe", ["Xenon", 131.293, 54])
    check_element(periodic_table_dict, "Y", ["Yttrium", 88.90585, 39])
    check_element(periodic_table_dict, "Yb", ["Ytterbium", 173.054, 70])
    check_element(periodic_table_dict, "Zn", ["Zinc", 65.38, 30])
    check_element(periodic_table_dict, "Zr", ["Zirconium", 91.224, 40])


def check_element(periodic_table_dict, symbol, expected):
    """Verify that the actual element that came from the
    periodic_table_dict contains the same values as the
    expected element.

    Parameters
        symbol: a symbol for a chemical element
        expected: a list that contains the expected values for symbol
    Return: nothing
    """
    # Verify that symbol is in the periodic table dictionary.
    assert symbol in periodic_table_dict, \
        f'"{symbol}" is missing from the periodic table dictionary.'
    actual = periodic_table_dict[symbol]

    # Verify that the element's name is correct.
    act_name = actual[NAME_INDEX]
    exp_name = expected[NAME_INDEX]
    assert act_name == exp_name, \
            f'wrong name for "{symbol}": ' \
            f'expected {exp_name} but found {act_name}'

    # Verify that the element's atomic mass is correct.
    act_mass = actual[ATOMIC_MASS_INDEX]
    exp_mass = expected[ATOMIC_MASS_INDEX]
    assert act_mass == approx(exp_mass), \
            f"wrong atomic mass for {exp_name}: " \
            f"expected {exp_mass} but found {act_mass}"


def test_parse_formula():
    """Verify that the parse_formula function works correctly.

    Parameters: none
    Return: nothing
    """
    periodic_table_dict = make_periodic_table()
    assert isinstance(periodic_table_dict, dict), \
        "make_periodic_table function must return a dictionary: " \
        f" expected a dictionary but found a {type(periodic_table_dict)}"

    sym_quant_list = parse_formula("H2O", periodic_table_dict)
    assert isinstance(sym_quant_list, list), \
        "parse_formula function must return a list: " \
        f" expected a list but found a {type(sym_quant_list)}"

    assert parse_formula("H2O", periodic_table_dict) \
            == [("H",2), ("O",1)]
    assert parse_formula("C6H6", periodic_table_dict) \
            == [("C",6), ("H",6)]
    assert parse_formula("(C2(NaCl)4H2)2C4Na", periodic_table_dict) \
            == [("C",8), ("Na",9), ("Cl",8), ("H",4)]
    with pytest.raises(FormulaError):
        parse_formula("L", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("4H", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("H2L4", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("-H", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("(H2O", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("H2)O3", periodic_table_dict)


def test_compute_molar_mass():
    """Verify that the compute_molar_mass function works correctly.

    Parameters: none
    Return: nothing
    """
    periodic_table_dict = make_periodic_table()
    assert isinstance(periodic_table_dict, dict), \
        "make_periodic_table function must return a dictionary: " \
        f" expected a dictionary but found a {type(periodic_table_dict)}"

    molar_mass = compute_molar_mass([["O",2]], periodic_table_dict)
    assert isinstance(molar_mass, int) or isinstance(molar_mass, float), \
        "compute_molar_mass function must return a number: " \
        f" expected a number but found a {type(molar_mass)}"

    assert compute_molar_mass([], periodic_table_dict) == 0
    assert compute_molar_mass([["O",2]], periodic_table_dict) \
            == approx(31.9988)
    assert compute_molar_mass([["C",6],["H",6]], periodic_table_dict) \
            == approx(78.11184)
    assert compute_molar_mass([["C",13],["H",16],["N",2],["O",2]],
            periodic_table_dict) == approx(232.27834)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
