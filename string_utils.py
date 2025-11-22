def split_before_uppercases(formula):
    if formula == "":
        return []
    current = 0
    end = 1
    new_list = []

    for char in formula[1:]:
        if char.isupper():
            new_list.append(formula[current:end])
            current = end
        end += 1

    new_list.append(formula[current:end])
    return new_list


def split_at_digit(formula):
    for i in range(len(formula)):
        if formula[i].isdigit():
            prefix = formula[:i]
            number = int(formula[i:])
            return prefix, number
    return formula, 1


def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""
    
    my_dict = {}

    for piece in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(piece)
        my_dict[atom_name] = my_dict.get(atom_name, 0) + atom_count

    return my_dict


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""

    reaction_equation = reaction_equation.replace(" ", "")  
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")


def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""

    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
