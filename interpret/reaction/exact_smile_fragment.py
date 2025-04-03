from rdkit import Chem
from rdkit.Chem import rdmolops

def split_and_remove_single_elements(input_string):
    # Use the split method to split the string by '.'
    elements = input_string.split('.')
    # Filter out elements that are single characters.

    filtered_elements = [element for element in elements if len(element) > 1]
    return filtered_elements

def split_string_by_dot(input_string):
    # Use the split method to split the string by '.'
    elements = input_string.split('.')
    return elements

def extract_specified_atoms(smiles, atom_indices):
    # Use RDKit to parse the SMILES string.

    mol = Chem.MolFromSmiles(smiles)

    # Create a new molecule editor object.
    rw_mol = Chem.RWMol(mol)

    #
    # Mark the atoms that need to be deleted.
    atoms_to_remove = [atom.GetIdx() for atom in rw_mol.GetAtoms() if atom.GetIdx() not in atom_indices]

    #
    # Delete atoms in reverse order to prevent index changes.
    for atom_idx in sorted(atoms_to_remove, reverse=True):
        rw_mol.RemoveAtom(atom_idx)

    # Convert the molecule back to a regular molecule object
    frag_mol = rw_mol.GetMol()

    # Obtain the SMILES representation of a fragment
    frag_smiles = Chem.MolToSmiles(frag_mol)
    keep_single_elements = split_string_by_dot(frag_smiles)
    del_single_elements = split_and_remove_single_elements(frag_smiles)
    return  del_single_elements,keep_single_elements,frag_smiles




if __name__ == "__main__":
    # Example input: SMILES string and atom position.
    # smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"  #
    # atom_indices = [0,1,3]  # Specify the atom positions to be retained.

    smiles = "C=CC1=CC=CC=C1.O=CCC"
    atom_indices = [0,5,8,9]  # Specify the positions of the atoms to be retained.

    # 提取片段并输出结果
    keep_single_elements,del_single_elements,frag_smiles = extract_specified_atoms(smiles, atom_indices)
    print("Extracted Fragment SMILES:", keep_single_elements,del_single_elements,frag_smiles)