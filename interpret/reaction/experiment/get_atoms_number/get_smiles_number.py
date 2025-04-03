import numpy as np
import pandas as pd
import os
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
    return atoms_num


current_dir = os.getcwd()
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))
file_name='data/result/statistics_reactive/double_para/double_criterion_100.xlsx'
input_files_smiles = os.path.join(parent_dir, file_name)
df_ratio=pd.read_excel(input_files_smiles)

# top one
# df_head_first['ratio']=df_ratio['smiles']
df_ratio['atoms_number'] = df_ratio['smiles'].apply(annotate_atoms)
file_name_out='data/result/statistics_reactive/double_para/double_criterion_100_atoms_number.xlsx'
out_files_smiles = os.path.join(parent_dir, file_name_out)
df_ratio.to_excel(out_files_smiles)