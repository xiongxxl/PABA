import sys

import numpy as np
import os
from tokenizer import tokenize_smiles
from highlight_num_atoms import highlight_num_atoms
from remove_no_alpha import find_and_remove_non_letters
from remove_no_alpha import find_non_alphanumeric_positions_and_remove
from exact_smile_fragment import extract_specified_atoms
from find_functional_group import identify_functional_groups
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import io

def remove_rows_and_columns(matrix, rows_to_remove, cols_to_remove):

    matrix_np = np.array(matrix)
    # Delete the specified rows.
    matrix_np = np.delete(matrix_np, rows_to_remove, axis=0)
    # Delete the specified columns.
    matrix_np = np.delete(matrix_np, cols_to_remove, axis=1)
    return matrix_np


all_frag_smiles = []
all_frag_functional=[]
def highlight_chemical_atoms(folder_path,filename_without_extension,save_img_flag):
    if 'H' in filename_without_extension:
        pass
    else:
        df_frag_smile_single = pd.DataFrame()
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.npy'):
                file_path = os.path.join(folder_path, file_name)
                # file_path='/mnt/work/code/tian/smiles/data/result/img_function/img_300/Nc1cc(Cl)cc(Cl)c1_0.95/4_7.npy'
                attn_binary = np.load(file_path)
                #np.fill_diagonal(attn_binary,0) #set diagonal element to 0
                attn_binary_del=attn_binary

                # del non-character
                filename_without_extension_re = tokenize_smiles(filename_without_extension)
                ## delete alpha
                #positions, cleaned_string = find_non_alphanumeric_positions_and_remove(filename_without_extension_re)
                positions, cleaned_string = find_and_remove_non_letters(filename_without_extension_re)
                # np.save(f'{filename_without_extension}.npy',attn_binary_del)
                # print('cleaned_string is:',cleaned_string)
                # print('positions is:', positions)
                # print('attn_binary :', np.shape(attn_binary))
                # print(attn_binary_del)

                # del Delete the corresponding rows and columns
                attn_binary_letter = remove_rows_and_columns(attn_binary_del, positions, positions)
                # print('attn_binary_del:', np.shape(attn_binary_letter))


                # find no_zero_element
                non_zero_positions = np.nonzero(attn_binary_letter)
                non_zero_col=np.unique(non_zero_positions[0]).tolist()
                # non_zero_row=np.unique(non_zero_positions[1]).tolist()

                ## find functonal group
                smiles = filename_without_extension
                atom_indices = non_zero_col
                keep_single_elements,del_single_elements,frag_smiles = extract_specified_atoms(smiles, atom_indices)
                functional_groups_state, functional_groups_detail = identify_functional_groups(frag_smiles, smiles)

                ## save all_frag_smiles
                file_name_nosuffix = os.path.splitext(file_name)[0]

                frag_smiles_dict= {
                                      'smiles' :[filename_without_extension],
                                 'frag_smiles' :[frag_smiles],
                            'functional_group' :[functional_groups_detail],
                                   'location'  :[str(non_zero_col)],
                              'attention_axis' :[file_name_nosuffix],
                                    }

                df_frag_smile_attention=pd.DataFrame(frag_smiles_dict)
                df_frag_smile_single=pd.DataFrame(pd.concat([df_frag_smile_single,df_frag_smile_attention],ignore_index=True))

                ##highlight atoms
                atom_indices=non_zero_col
                #atom_indices = non_zero_row
                if save_img_flag:
                    img_data = highlight_num_atoms(smiles, atom_indices)
                    file_name_no_suffix=os.path.splitext(file_name)[0]
                    img_filename=f'{file_name_no_suffix}.jpeg'
                    img_path=os.path.join(folder_path,img_filename)
                    with open(img_path, "wb") as f:
                        f.write(img_data)
                    #img = Image.open(io.BytesIO(img_data))
                    #img.show()
                # sys.exit()

        return df_frag_smile_single

if __name__ == "__main__":
    save_img_flag = 0
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(os.path.dirname(current_dir))
    data_files_npy_simple ='data/result/img_function/img_300/Nc1cc(Cl)cc(Cl)c1_0.97.npy'
    folder_path =os.path.join(parent_dir, data_files_npy_simple)
    filename_without_extension='Nc1cc(Cl)cc(Cl)c1'
    df_frag_smile_single=highlight_chemical_atoms(folder_path,filename_without_extension,save_img_flag)
    path=f'frag_smiles_main_frag_0.98.csv'
    df_frag_smile_single.to_csv(path)

