
from rdkit import Chem
from rdkit.Chem import Draw


def annotate_atoms(smiles):
    mol = Chem.MolFromSmiles(smiles)
    max_atom_idx = 0

    for atom in mol.GetAtoms():
        atom_idx = atom.GetIdx()
        atom.SetAtomMapNum(atom_idx)
        if atom_idx > max_atom_idx:
            max_atom_idx = atom_idx

    annotated_smiles = Chem.MolToSmiles(mol)
    img = Draw.MolToImage(mol, legend=annotated_smiles)

    print("Annotated SMILES:", annotated_smiles)
    print("Max Atom Index:", max_atom_idx)
    atoms_num=max_atom_idx+1
    return img ,atoms_num


if __name__ == "__main__":
    smiles = "NC1CCCCC1.O=CC2=CC=CC=C2"
    img = annotate_atoms(smiles)
    img.show()