from rdkit import Chem
import pandas as pd
# Define the SMARTS patterns and chemical formulas for common functional groups.
functional_groups = {
    "Alkane": {"smarts": "[CX4]", "formula": "C-H"},
    "Alkene": {"smarts": "[CX3]=[CX3]", "formula": "C=C"},
    "Alkyne": {"smarts": "[CX2]#[CX2]", "formula": "C≡C"},
    "Aromatic": {"smarts": "c1ccccc1", "formula": "C6H5"},
    "Halide": {"smarts": "[F,Cl,Br,I]", "formula": "X (F, Cl, Br, I)"},
    "Alcohol": {"smarts": "[OX2H]", "formula": "R-OH"},
    "Phenol": {"smarts": "c1ccc(O)cc1", "formula": "C6H5OH"},
    "Ether": {"smarts": "[OD2]([#6])[#6]", "formula": "R-O-R"},
    "Aldehyde": {"smarts": "[CX3H1](=O)[#6]", "formula": "R-CHO"},
    "Ketone": {"smarts": "[CX3](=O)[#6]", "formula": "R-CO-R"},
    "Carboxylic Acid": {"smarts": "[CX3](=O)[OX2H1]", "formula": "R-COOH"},
    "Ester": {"smarts": "[CX3](=O)[OX2][#6]", "formula": "R-COO-R"},
    "Amide": {"smarts": "[NX3][CX3](=[OX1])[#6]", "formula": "R-CONH2"},
    "Amine": {"smarts": "[NX3][#6]", "formula": "R-NH2"},
    "Nitrate": {"smarts": "[NX3](=O)([OX1-])[OX1-]", "formula": "R-NO3"},
    "Nitro": {"smarts": "[NX3](=O)[OX1-]", "formula": "R-NO2"},
    "Sulfonic Acid": {"smarts": "S(=O)(=O)[O-]", "formula": "R-SO3H"},
    "Thiol": {"smarts": "[SX2H]", "formula": "R-SH"},
    "Thioether": {"smarts": "[SX2][#6]", "formula": "R-S-R"},
    "Disulfide": {"smarts": "[SX2][SX2]", "formula": "R-S-S-R"},
    "Sulfoxide": {"smarts": "[SX3](=O)[#6]", "formula": "R-S(=O)-R"},
    "Sulfone": {"smarts": "[SX4](=O)(=O)[#6]", "formula": "R-SO2-R"},
    "Phosphine": {"smarts": "[PX3]", "formula": "R3P"},
    "Phosphate": {"smarts": "P(=O)(O)(O)O", "formula": "R-O-PO3H2"},
    "Isocyanate": {"smarts": "N=C=O", "formula": "R-N=C=O"},
    "Isothiocyanate": {"smarts": "N=C=S", "formula": "R-N=C=S"},
    "Cyano":{"smarts": "[NX1]#[CX2]", "formula":"R-C≡N" },
     "hydrazine":{"smarts":"[NH2]-[NH]" ,"formula":"R-NH-NH2"},

}

def identify_functional_groups(frag_smiles,smiles):

        # Use RDKit to parse the SMILES string.
        mol = Chem.MolFromSmiles(frag_smiles)
        functional_groups_state = []
        functional_groups_axis=[]
        mol_data = {'smiles': smiles}
        for group_name, properties in functional_groups.items():
            pattern = Chem.MolFromSmarts(properties["smarts"])
            if mol is not None and hasattr(mol, 'HasSubstructMatch'):
                #if mol.HasSubstructMatch(pattern):
                mol_data[properties["formula"]] = mol.HasSubstructMatch(pattern)
        functional_groups_state.append(mol_data)

        true_keys = [k for item in functional_groups_state for k, v in item.items() if v is True]
        if not true_keys:
            functional_groups_detail =frag_smiles
        else:
            ture_keys_str =','.join(true_keys)
            functional_groups_detail = ture_keys_str

        return functional_groups_state, functional_groups_detail



if __name__ == "__main__":

    #smiles = "CC(=O)O"
    frag_smiles='Cc1c(N=C=O)cccc1N=C=O'
    smiles='Cc1c(N=C=O)cccc1N=C=O'

    # Identify and output functional groups.
    functional_groups_state, functional_groups_detail = identify_functional_groups(frag_smiles,smiles)
    print(functional_groups_state)
    print(functional_groups_detail)
    # for group_name, formula in detected_groups:
    #     print(f"Detected functional group: {group_name}, Chemical formula: {formula}")



#za huai functional group

    # "Furan": {"smarts": "[#6]1=[#6][#6]=[#6][O]1", "formula": "R-C4H-O-R"},
    # "Pyrrole": {"smarts": "[#6]1=[#6][#6]=[#6][N]1", "formula": "R-C4H-N-R"},
    # "Thiophene": {"smarts": "[#6]1=[#6][#6]=[#6][S]1", "formula": "R-C4H-S-R"},
    # "Oxazole": {"smarts": "[#6]1=[N][#6]=[#6][O]1", "formula": "R-C3H-N-O-R"},
    # "Imidazole": {"smarts": "[#6]1=[N][#6]=[#6][N]1", "formula": "R-C3H-N2-R"},
    # "Thiazole": {"smarts": "[#6]1=[N][#6]=[#6][S]1", "formula": "R-C3H-N-S-R"},
    # "Isoxazole": {"smarts": "[N]1=[#6][#6]=[#6][O]1", "formula": "R-C3H-N-O-R"},
    # "Pyrazole": {"smarts": "[N]1=[#6][#6]=[#6][N]1", "formula": "R-C3H-N2-R"},
    # "Isothiazole": {"smarts": "[N]1=[#6][#6]=[#6][S]1", "formula": "R-C3H-N-S-R"},
    # "Pyridine": {"smarts": "[#6]1=[N][#6]=[#6][#6]=[#6]1", "formula": "R-C5H-N-R"},
    # "Pyran": {"smarts": "[#6]1=[#6][O][#6]=[#6][#6]1", "formula": "R-C5H-O-R"},
    # "Pyridazine": {"smarts": "[#6]1=[N][#6]=[N][#6]=[#6]1", "formula": "R-C4H-N2-R"},
    # "Pyrimidine": {"smarts": "[#6]1=[N][#6]=[#6][N]=[#6]1", "formula": "R-C4H-N2-R"},
    # "Pyrazine": {"smarts": "[#6]1=[N][#6]=[#6][#6]=[N]1", "formula": "R-C4H-N2-R"},
    # "γ-pyrone": {"smarts": "[O]=[#6]1[#6]=[#6][O][#6]=[#6]1", "formula": "R-C5H-O2-R"},
    # "α-pyrone": {"smarts": "[O]=[#6]1[O][#6]=[#6][#6]=[#6]1", "formula": "R-C5H-O2-R"},
    # "1H-1,2-diazepine": {"smarts": "[#6]1=[N][N][#6]=[#6][#6]=[#6]1", "formula": "R-C5H-N2-R"},
    # "1H-azepine": {"smarts": "[#6]1=[#6][N][#6]=[#6][#6]=[#6]1", "formula": "R-C6H-N-R"},
    # "2H-azepin-2-one": {"smarts": "[O]=[#6]1[#6]=[#6][#6]=[#6][N]=[#6]1", "formula": "R-C6H-N-O-R"},
    # "1,2-thiazepine": {"smarts": "[#6]1=[N][S][#6]=[#6][#6]=[#6]1", "formula": "R-C5H-N-S-R"},
    # "1,2-diazepane": {"smarts": "[#6]1[N][N][#6][#6][#6][#6]1", "formula": "R-C5H-N2-R"},
    # "Azocane": {"smarts": "[#6]1[#6][#6][#6][#6][N][#6][#6]1", "formula": "R-C7H-N-R"},
    # "azocan-2-one": {"smarts": "[O]=[#6]1[#6][#6][#6][#6][#6][N]1", "formula": "R-C7H-N-O-R"},
    # "1,5-diazocan-2-one": {"smarts": "[O]=[#6]1[#6][N][#6][#6][N][#6]1", "formula": "R-C6H-N2-O-R"},
    # "(Z)-1,2,3,4,7,8-hexahydroazocine": {"smarts": "[#6]1=[#6]\\[#6][#6][N][#6][#6]\\1", "formula": "R-C8H-N-R"},
    # "Indole": {"smarts": "[#6]1([N][#6]=[#6]2)=[#6]2[#6]=[#6][#6]=[#6]1", "formula": "R-C8H-N-R"},
    # "Purine": {"smarts": "[#6]1([N][#6]=[N]2)=[#6]2[#6]=[N][#6]=[#6]1", "formula": "R-C5H-N4-R"},
    # "Benzothiophene": {"smarts": "[#6]1([S][#6]=[#6]2)=[#6]2[#6]=[#6][#6]=[#6]1", "formula": "R-C8H-S-R"},
    # "Benzofuran": {"smarts": "[#6]1([O][#6]=[#6]2)=[#6]2[#6]=[#6][#6]=[#6]1", "formula": "R-C8H-O-R"},
    # "Benzopyran": {"smarts": "[#6]1([O][#6]=[#6]2)=[#6]2[#6]=[#6][#6]=[#6]1", "formula": "R-C9H-O-R"},
    # "Benzo-γ-pyrone": {"smarts": "[O]=[#6]1[#6]=[#6][O][#6]=[#6]2=[#6]1[#6]=[#6]=[#6]2", "formula": "R-C9H-O2-R"},
    # "Quinoline": {"smarts": "[#6]1([#6]=[#6][#6]=[#6]2)=[#6]2[N]=[#6]=[#6]1", "formula": "R-C9H-N-R"},
    # "Isoquinoline": {"smarts": "[#6]1([#6]=[#6][#6]=[#6]2)=[#6]2[#6]=[N]=[#6]1", "formula": "R-C9H-N-R"},
    # "2,3,4,5-tetrahydro-1H-benzo[b]azepine": {"smarts": "[#6]12=[#6][#6]=[#6][#6]=[#6]1[N][#6][#6][#6][#6]2", "formula": "R-C11H-N-R"},
    # "1H-benzo[b]azepine": {"smarts": "[#6]12=[#6][#6]=[#6][#6]=[#6]1[N]=[#6][#6]=[#6]2", "formula": "R-C11H-N-R"},
    # "benzo[f][1,2]thiazepine": {"smarts": "[#6]12=[#6][#6]=[#6][#6]=[#6]1[S][N]=[#6]=[#6]2", "formula": "R-C10H-N-S-R"},
    # "(1Z,5Z)-4,6a-dihydro-3H-pyrido[1,2-d][1,4]diazocine": {"smarts": "[#6]12[#6]=[#6][#6]=[#6][N]1/\\[#6]=[N]/[#6]=[N]/[#6]=[#6]2", "formula": "R-C9H-N3-R"},
    # "Carbazole": {"smarts": "[#6]1([N]2)=[#6]([#6]3=[#6]2[#6]=[#6][#6]=[#6]3)[#6]=[#6]=[#6]1", "formula": "R-C12H-N-R"},
    # "Acridine": {"smarts": "[#6]12=[#6][#6]=[#6][#6]=[#6]1[#6]=[#6]3([#6][#6]=[#6][#6]=[#6]3)=N2", "formula": "R-C13H-N-R"}