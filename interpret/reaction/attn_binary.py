from remove_arrary_outerside import remove_outer_layer
from tokenizer import tokenize_smiles
import matplotlib.pyplot as plt
import os
from binarize_by_ratio import binarize_by_ratio
import numpy as np

def attn_64_img(attn,folder_name_img,mol_name,ratio,saving_img_flag):
    # input one mol 8*8 attn,
    # output img of the mol attn,jpg is attn ,png is binarize
    for i in range(8):
        for j in range(8):
            attn_single=attn[i][j]
            attn_del2=remove_outer_layer(attn_single)
            mol_name_suf=f"{mol_name}_{ratio}"
            folder_name_mol=os.path.join(folder_name_img,mol_name_suf)

            if not os.path.exists(folder_name_mol):
                os.makedirs(folder_name_mol)

            ## decrease ratio for  one mol no highlight atoms
            ratio_decrease_one=ratio-0.01
            path_decrease_one_suf=f"{ratio_decrease_one}"
            folder_decrease_one=os.path.join(folder_name_mol,path_decrease_one_suf)
            if not os.path.exists(folder_decrease_one):
                os.makedirs(folder_decrease_one)

            ## decrease ratio for  one mol no highlight atoms
            ratio_decrease_two=ratio_decrease_one-0.01
            path_decrease_two_suf=f"{ratio_decrease_two}"
            folder_decrease_two=os.path.join(folder_name_mol,path_decrease_two_suf)
            if not os.path.exists(folder_decrease_two):
                os.makedirs(folder_decrease_two)

            if saving_img_flag:
                single_name_greys = f'{i}_{j}.jpg'
                file_path_greys =os.path.join(folder_name_mol, single_name_greys)
                plt.savefig(file_path_greys)
                plt.close()

            ## binarize attn array
            #ratio=0.95 # set front ratio to  0
            attn_del2_bin = binarize_by_ratio(attn_del2,ratio)
            attn_del2_bin_decrease_one = binarize_by_ratio(attn_del2, ratio_decrease_one)
            attn_del2_bin_decrease_two = binarize_by_ratio(attn_del2, ratio_decrease_two)
            #attn_del2_bin = find_and_keep_largest_block(attn_del2_bin) #find max bolk


            single_name_npy=f'{i}_{j}.npy'
            file_path_single_npy = os.path.join(folder_name_mol,single_name_npy)
            np.save(file_path_single_npy, attn_del2_bin)

            single_name_npy=f'{i}_{j}.npy'
            file_path_decrease_one_npy = os.path.join(folder_decrease_one,single_name_npy)
            np.save(file_path_decrease_one_npy,attn_del2_bin_decrease_one)

            single_name_npy=f'{i}_{j}.npy'
            file_path_decrease_two_npy = os.path.join(folder_decrease_two,single_name_npy)
            np.save(file_path_decrease_two_npy , attn_del2_bin_decrease_two)

    return folder_name_mol,folder_decrease_one,folder_decrease_two

if __name__ == "__main__":
   print()
