from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit import Chem
from rdkit.Chem import Draw

def highlight_num_atoms(smiles, atom_indices):

    #
    # Create a molecule object from SMILES using RDKit.
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        raise ValueError("Invalid SMILES string")

    # highlight_colors={0:(0,0,255),1:(0,0,255)}

    # Create a molecular drawing object and highlight the specified atoms.
    drawer = Draw.MolDraw2DCairo(300, 300)
    opts = drawer.drawOptions()
    drawer.DrawMolecule(mol, highlightAtoms=atom_indices)
    # drawer.DrawMolecule(mol, highlightAtoms=atom_indices)
    drawer.FinishDrawing()
    img = drawer.GetDrawingText()
    return img

if __name__ == "__main__":
    # highlight atom
    #smiles="ClC1=CC=CC=C1I.C1(NC2=CC=CC=C2)=CC=CC=C1"
    #smiles="ClC1=CC=CC=C1I.C2(NC9=CC=CC=C9)=CC=CC=C2"
    #smiles="CC(C)C(=O)CC(=O)C(F)(F)F.Nc1ccccc1N"
    smiles="CCCCCCC[C@@H]1NN1CC2=CC=CC=C2"
    location=[0,1]

    atom_indices=location
    # smiles="CCC(=O)CC(=O)C(F)(F)F.Nc1cccc

    # atom_indices=[0,3,6,16,17,18,11]
    img_data=highlight_num_atoms(smiles, atom_indices)
    #Save the image as a file.
    # with open("highlighted_molecule.png", "wb") as f:
    #   f.write(img_data)
    # #Display the image.
    from PIL import Image
    import io
    img = Image.open(io.BytesIO(img_data))
    img.show()