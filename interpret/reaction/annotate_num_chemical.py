from rdkit import Chem
from rdkit.Chem import Draw
import re
import os
def annotate_atoms(smiles):
    numbers_after_dot=[]
    numbers_before_dot=[]
    # Parse SMILES
    mol = Chem.MolFromSmiles(smiles)
    for atom in mol.GetAtoms():
        atom.SetAtomMapNum(atom.GetIdx()+1)
        #atom.SetAtomMapNum(atom.GetIdx())
    # Generate SMILES with atomic numbers.
    annotated_smiles = Chem.MolToSmiles(mol)
    # Generate chemical formula image.
    img = Draw.MolToImage(mol, legend=annotated_smiles)

    # Enter SMILES expression.
    #smiles = '[CH2:1]=[CH:2][CH2:3][NH:4][CH3:5].[CH3:6][N:7]=[C:8]=[O:9]'
    # Use regular expressions to extract numbers.
    str_before_dot = re.findall(r'\[.*?:(\d+)\]', annotated_smiles.split('.')[0])
    numbers_before_dot = [int(num_str) for num_str in str_before_dot]
    numbers_before_dot = list(map(lambda x: x - 1, numbers_before_dot))
    str_after_dot = re.findall(r'\[.*?:(\d+)\]', annotated_smiles.split('.')[1])
    numbers_after_dot = [int(num_str) for num_str in str_after_dot]
    numbers_after_dot = list(map(lambda x: x - 1, numbers_after_dot))

    return annotated_smiles,img,numbers_before_dot,numbers_after_dot

if __name__ == "__main__":
    smiles="O/N=C/C1=CC=CC=C1"
    annotated_smiles, img,numbers_before_dot,numbers_after_dot = annotate_atoms(smiles)
    print("Before dot:", numbers_before_dot)
    print("After dot:", numbers_after_dot)

    img.show()