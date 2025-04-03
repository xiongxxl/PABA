from highlight_num_atoms import highlight_num_atoms
import os
import pandas as pd

from rdkit import Chem
from rdkit.Chem import Draw

from rdkit import Chem
from rdkit.Chem import Draw


# def highlight_num_atoms(smiles, atom_indices):

#     # Use RDKit to create a molecule object from a SMILES string.
#     mols = Chem.MolFromSmiles(smiles)
#     if not mols:
#         raise ValueError("Invalid SMILES string")
#
#     # If the input SMILES represents multiple molecules, split it into multiple molecules.
#     if isinstance(mols, tuple):
#         mols = [m for m in mols if m is not None]
#     else:
#         mols = [mols]
#
#     # Set all highlighted atoms to blue (RGB: (0, 0, 255)).
#     blue_color = (0,1,1)
#     highlight_colors = {idx: blue_color for idx in atom_indices}
#
#     # Create a molecule drawing object.
#     drawer = Draw.MolDraw2DCairo(600, 300)
#     opts = drawer.drawOptions()
#
#     # Draw each molecule and highlight the specified atoms.
#     for mol in mols:
#         drawer.DrawMolecule(mol, highlightAtoms=atom_indices, highlightAtomColors=highlight_colors)
#
#     # End the drawing and obtain the image.
#     drawer.FinishDrawing()
#     img = drawer.GetDrawingText()
#
#     return img
#
#
# # Test input.
# smiles = "C1=CC=CC=C1.CC(NC2=CC=C(C)C=C2)=O"
# atom_indices = [0, 1, 2, 7,8]  # Indices of atoms to be highlighted.
# img_data= highlight_num_atoms(smiles, atom_indices)

# from PIL import Image
# import io
# img = Image.open(io.BytesIO(img_data))
# img.show()




# produce label image
current_dir = os.getcwd()
parent_dir = os.path.dirname(os.path.dirname(current_dir))
folder_label=os.path.join(parent_dir,'data/result/img_reactive/double_para/combine/combine_label_100/label')
folder_result=os.path.join(parent_dir,'data/result/img_reactive/double_para/combine/combine_label_100/product')
input_files_smiles = os.path.join(parent_dir, 'data/result/statistics_reactive/double_para/combine')
df_criterion = pd.read_excel(os.path.join(input_files_smiles, 'double_criterion_100.xlsx'))

df_product = pd.read_excel(os.path.join(input_files_smiles, 'product_smiles_100.xlsx'))
smiles=df_criterion['smiles']
#
# current_dir = os.getcwd()
# parent_dir = os.path.dirname(os.path.dirname(current_dir))
# folder_label=os.path.join(parent_dir,'data/result/img_reactive/single_8/predict/label')
# folder_result=os.path.join(parent_dir,'data/result/img_reactive/single_8/predict/label')
# input_files_smiles = os.path.join(parent_dir, 'data/result/statistics_reactive/single_8')
# df_criterion = pd.read_excel(os.path.join(input_files_smiles, 'single_criterion_8.xlsx'))
#
# # df_product = pd.read_excel(os.path.join(input_files_smiles, 'product_smiles_100.xlsx'))
# smiles=df_criterion['smiles']



##produce img of label

for index_criterion, row_criterion in df_criterion.iterrows():
    smile = row_criterion['smiles']
    gold_criterion = row_criterion['gold_criterion']
    atom_indices=eval(gold_criterion)
    atom_indices = [int(i) for i in atom_indices]
    img_data = highlight_num_atoms(smile, atom_indices)
    # smile_drr=smile.replace("/", "x")
    img_file=f'{smile}_label.png'
    folder_path=os.path.join(folder_label,img_file)
    with open(folder_path, "wb") as f:
      f.write(img_data)

    # #
    # from PIL import Image
    # import io
    # img = Image.open(io.BytesIO(img_data))
    # img.show()


# #
# ## produce img of  product
# for index_criterion, row_criterion in df_product.iterrows():
#     smile = row_criterion['smiles']
#     atom_indices=[]
#     print(smile)
#     img_data = highlight_num_atoms(smile, atom_indices)
#
#     smile_addr = smile.replace("/", "x")
#     img_file=f'{smile_addr}_product.png'
#     folder_path=os.path.join(folder_result,img_file)
#     with open(folder_path, "wb") as f:
#       f.write(img_data)

    # #
    # from PIL import Image
    # import io
    # img = Image.open(io.BytesIO(img_data))
    # img.show()