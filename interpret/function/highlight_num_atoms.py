from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit import Chem
from rdkit.Chem import Draw

def highlight_num_atoms(smiles, atom_indices):

    # Create a molecule object from SMILES using RDKit.
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        raise ValueError("Invalid SMILES string")

    # 创建分子绘图对象，并高亮指定的原子
    drawer = Draw.MolDraw2DCairo(300, 300)
    opts = drawer.drawOptions()
    drawer.DrawMolecule(mol, highlightAtoms=atom_indices)
    drawer.FinishDrawing()
    img = drawer.GetDrawingText()
    return img

if __name__ == "__main__":
    # highlight atom
    #smiles="ClC1=CC=CC=C1I.C1(NC2=CC=CC=C2)=CC=CC=C1"
    #smiles="ClC1=CC=CC=C1I.C2(NC9=CC=CC=C9)=CC=CC=C2"
    #smiles="CC(C)C(=O)CC(=O)C(F)(F)F.Nc1ccccc1N"
    smiles="C=CC1=CC=CC=C1.O=CCC"
    location=[0,1]

    atom_indices=location
    # smiles="CCC(=O)CC(=O)C(F)(F)F.Nc1cccc

    # atom_indices=[0,3,6,16,17,18,11]
    img_data=highlight_num_atoms(smiles, atom_indices)
    #Save image as file
    # with open("highlighted_molecule.png", "wb") as f:
    #   f.write(img_data)
    # #Display image
    from PIL import Image
    import io
    img = Image.open(io.BytesIO(img_data))
    img.show()