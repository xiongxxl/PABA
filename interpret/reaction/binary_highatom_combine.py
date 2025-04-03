import os
import numpy as np
import pandas as pd
from tokenizer import tokenize_smiles
from highlight_num_atoms import highlight_num_atoms
from remove_letter_number import find_and_remove_non_letters
from exact_smile_fragment import extract_specified_atoms
from find_functional_group import identify_functional_groups
from restrain_functional_reactive import restrain_functional_axis
from annotate_num_chemical import annotate_atoms


def remove_rows_and_columns(matrix, rows_to_remove, cols_to_remove):
    # Convert the input list to a NumPy array.
    matrix_np = np.array(matrix)
    # Delete the specified row.
    matrix_np = np.delete(matrix_np, rows_to_remove, axis=0)
    # Delete the specified column.
    matrix_np = np.delete(matrix_np, cols_to_remove, axis=1)
    return matrix_np

def highlight_chemical_atoms_single(folder_path,filename_without_extension,saving_img_flag,ratio,smiles_address):
    if 'H' in filename_without_extension:
        pass
    else:
        df_frag_smile_single_4_5=pd.DataFrame()
        df_frag_smile_single_7_7 = pd.DataFrame()

        for file_name in os.listdir(folder_path):
            if file_name.endswith('.npy'):
                file_path = os.path.join(folder_path, file_name)
                #file_path='/mnt/work/code/tian/smiles/data/result/img_reactive/old/double_0911mark/CCC(=O)CC(=O)C(F)(F)F.Nc1ccccc1Br_0.96/5_4.npy'

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
                #print('attn_binary_del:', np.shape(attn_binary_letter))

                # find no_zero_element
                non_zero_positions = np.nonzero(attn_binary_letter)
                non_zero_col=np.unique(non_zero_positions[0]).tolist()
                ##concatatenate nadarry  and del copy
                # non_zero_positions_combined = np.concatenate(non_zero_positions[0], non_zero_positions[1])
                # non_zero_positions_combined_unique = np.unique(non_zero_positions_combined)
                smiles = filename_without_extension
                atom_indices = non_zero_col
                # atom_indices_restrain=non_zero_col
                results,reactive_atoms_restrain_last,less_dot, greater_equal_dot= restrain_functional_axis(smiles, atom_indices)
                atom_indices_restrain=list(set(reactive_atoms_restrain_last))
                #non_zero_row=np.unique(non_zero_positions[1]).tolist()

                if saving_img_flag:
                    img_data = highlight_num_atoms(smiles, atom_indices_restrain)
                    file_name_no_suffix=os.path.splitext(file_name)[0]
                    img_filename=f'{file_name_no_suffix}.jpeg'
                    img_path=os.path.join(folder_path,img_filename)
                    #img = Image.open(io.BytesIO(img_data))
                    #img.show()
                    with open(img_path, "wb") as f:
                        f.write(img_data)

                   ###deal (4_5) head ###
                file_name_no_suffix = os.path.splitext(file_name)[0]
                if file_name_no_suffix == '4_5':
                    combine_file = 'combine'
                    parent_folder_path = os.path.dirname(os.path.dirname(folder_path))
                    predict_folder = os.path.join(parent_folder_path, combine_file)
                    if not os.path.exists(predict_folder):
                        os.makedirs(predict_folder)
                    atom_indices_adaptive = atom_indices_restrain
                    keep_single_elements, del_single_elements, frag_smiles = extract_specified_atoms(smiles, atom_indices_adaptive)
                    functional_groups_state, functional_groups_detail= identify_functional_groups(frag_smiles, smiles)

                    file_name_nosuffix = os.path.splitext(file_name)[0]
                    frag_smiles_dict= {
                                          'smiles' :[filename_without_extension],
                                     'frag_smiles' :[frag_smiles],
                                'functional_group' :[functional_groups_detail],
                                  'reactive_atoms' :[str(atom_indices_adaptive)],
                                       'head_axis' :[file_name_nosuffix],
                                       }

                    df_frag_smile_attention_4_5=pd.DataFrame(frag_smiles_dict)
                    df_frag_smile_single_4_5=pd.DataFrame(pd.concat([df_frag_smile_single_4_5,df_frag_smile_attention_4_5],ignore_index=True))

                    img_data = highlight_num_atoms(smiles, atom_indices_adaptive)
                    file_name_no_suffix = os.path.splitext(file_name)[0]
                    img_filename = f'{smiles_address}_{file_name_no_suffix}_{ratio}.jpeg'
                    img_path = os.path.join(predict_folder, img_filename)
                    with open(img_path, "wb") as f:
                        f.write(img_data)

                      ### deal (7_7) head ###
                file_name_no_suffix = os.path.splitext(file_name)[0]
                if file_name_no_suffix == '7_7':
                    predict_file = 'combine'
                    parent_folder_path = os.path.dirname(os.path.dirname(folder_path))
                    predict_folder = os.path.join(parent_folder_path, predict_file)
                    if not os.path.exists(predict_folder):
                        os.makedirs(predict_folder)
                    atom_indices_adaptive = atom_indices_restrain

                    keep_single_elements, del_single_elements, frag_smiles = extract_specified_atoms(smiles, atom_indices_adaptive)
                    functional_groups_state, functional_groups_detail = identify_functional_groups(frag_smiles, smiles)
                    file_name_nosuffix = os.path.splitext(file_name)[0]
                    frag_smiles_dict = {
                        'smiles': [filename_without_extension],
                        'frag_smiles': [frag_smiles],
                        'functional_group': [functional_groups_detail],
                        'reactive_atoms': [str(atom_indices_adaptive)],
                        'head_axis': [file_name_nosuffix],
                    }

                    df_frag_smile_attention_7_7 = pd.DataFrame(frag_smiles_dict)
                    df_frag_smile_single_7_7 = pd.DataFrame(pd.concat([df_frag_smile_single_7_7,df_frag_smile_attention_7_7], ignore_index=True))

                    img_data = highlight_num_atoms(smiles, atom_indices_adaptive)
                    file_name_no_suffix = os.path.splitext(file_name)[0]
                    img_filename = f'{smiles_address}_{file_name_no_suffix}_{ratio}.jpeg'
                    img_path = os.path.join(predict_folder, img_filename)
                    with open(img_path, "wb") as f:
                        f.write(img_data)

        return df_frag_smile_single_4_5, df_frag_smile_single_7_7

if __name__ == "__main__":
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    data_files_npy_simple ='data/result/img_reactive/old/double_0911mark/CCC(=O)CC(=O)C(F)(F)F.Nc1ccccc1Br_0.96'
    folder_path =os.path.join(parent_dir, data_files_npy_simple)
    filename_without_extension='CCC(=O)CC(=O)C(F)(F)F.Nc1ccccc1Br'
    saving_img_flag=1
    file_path_decrease_one_npy=''
    file_path_decrease_two_npy=''
    ratio=0.98
    saving_img_flag=1
    smiles_address='CCC(=O)CC(=O)C(F)(F)F.Nc1ccccc1Br'
    #statistics_fragment_path= 'data/result/statistics_reactive/double_1028mark/frag_smiles_main_0.98.csv'
    #df_frag_smile_single=highlight_chemical_atoms(folder_path,filename_without_extension,saving_img_flag)
    df_frag_smile_single=highlight_chemical_atoms_single(folder_path, file_path_decrease_one_npy, file_path_decrease_two_npy,
                             filename_without_extension, saving_img_flag, ratio,smiles_address)
    print(df_frag_smile_single)

