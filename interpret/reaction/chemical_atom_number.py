from rdkit import Chem


# 查找并返回指定元素的原子编号
def get_atom_indices_by_symbol(molecule_smiles, element_symbol):
    # Convert the SMILES string to a molecular object.
    mol = Chem.MolFromSmiles(molecule_smiles)
    if not mol:
        return "Invalid SMILES"
    # Find all atoms of the specified element.
    atom_indices = []
    # Iterate through all atoms to find those that match the specified element symbol.
    for atom in mol.GetAtoms():
        if atom.GetSymbol() == element_symbol:  # Check if it is the specified element.
            atom_indices.append(atom.GetIdx())  # Get the index of the atom.

    return atom_indices

if __name__ == "__main__":
    # Example molecule
    molecule_smiles = "CC1=CC=C(C=O)C=C1.C2CCCCN2"
    # Avatar
    # Enter the element symbol you want to find.
    element_symbol = 'N'  # It can be replaced with 'C', 'N', 'H', and so on.
    atom_indices = get_atom_indices_by_symbol(molecule_smiles, element_symbol)
    #
    # Output the atom numbers of the specified element.
    if atom_indices:
        print(f"The indices of {element_symbol} atoms in the molecule are: {atom_indices}")
    else:
        print(f"No {element_symbol} atoms found.")