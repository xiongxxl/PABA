import numpy as np
import os
import pandas as pd
from tokenizer import tokenize_smiles
import sys
from binary_highatom_function import highlight_chemical_atoms
from annotate_num_chemical import annotate_atoms
from syn_1_img import syn_1_jpg
from syn_1_img import syn_1_jpeg
from syn_1_img import syn_1_png
from adaptive_weight import find_and_keep_largest_block
from attn_binary_function import attn_64_img
import sys
import os
import time

ratio=0.999
current_dir = os.getcwd()
parent_dir = os.path.dirname(os.path.dirname(current_dir))
data_files_npy='data/middle_attention/npy_function/attn_npy_300'
folder_name_npy=os.path.join(parent_dir, data_files_npy)
data_files_img='data/result/img_function/img_300'
folder_name_img=os.path.join(parent_dir, data_files_img)

statistics_path='data/result/statistic_function/statistics_functional_300'
fragment_excel=f'frag_smiles_main_frag_{ratio}.xlsx'  #save functional group path
statistics_fragment_path= os.path.join(statistics_path, fragment_excel)
folder_name_statistics=os.path.join(parent_dir, statistics_fragment_path)

save_img_flag=1
j=0

df_frag_smiles_multi=pd.DataFrame()
for filename in os.listdir(folder_name_npy):
    if filename.endswith('.npy'):
        filepath = os.path.join(folder_name_npy, filename)
        attn = np.load(filepath)
        filename_without_extension = os.path.splitext(filename)[0]
        if 'H' in filename_without_extension:
            #j=j+1
            pass
        else:
            data_files_npy_simple='data/middle_attention/npy_function/attn_npy_300/Nc1cc(Cl)cc(Cl)c1.npy'
            attn=np.load(os.path.join(parent_dir, data_files_npy_simple))
            filename_without_extension='Nc1cc(Cl)cc(Cl)c1'
            filename_without_extension = filename_without_extension.replace("x", "/")
            filename_without_extension_re= tokenize_smiles(filename_without_extension)  #re syn like cl to one element
            filename_without_extension_forsaving=filename_without_extension.replace("/", "x") #this filename for saving address
            j=j+1
            print(f'Filename: {filename_without_extension}')
            print(j)

            start_time1=time.time()
            img_64_filename=attn_64_img(attn, folder_name_img, filename_without_extension,ratio,save_img_flag)#produce 64 attn image
            syn_name_attn=f'{filename_without_extension_forsaving}_{ratio}.jpg'
            output_image_attn=os.path.join(folder_name_img, syn_name_attn)
            attn_syn_img=syn_1_jpg(img_64_filename, output_image_attn) #syn 64 attention to 1 image
            print(img_64_filename)
            end_time1=time.time()
            print(f"代码1运行时间：{end_time1-start_time1}秒")

            # syn 64 binary attention to  1 image
            suffix_b = '_binarize'
            syn_name_binarize=f'{filename_without_extension_forsaving}{suffix_b}_{ratio}.jpg'
            output_image_binarize=os.path.join(folder_name_img, syn_name_binarize)
            attn_syn_binarize=syn_1_png(img_64_filename, output_image_binarize)

            ##syn 64 highatom images
            start_time2 = time.time()
            df_frag_smile_single=highlight_chemical_atoms(img_64_filename,filename_without_extension,save_img_flag)  #produce high atom imagge
            df_frag_smile_single.to_excel(folder_name_statistics)
            df_frag_smiles_multi = pd.DataFrame(pd.concat([df_frag_smiles_multi, df_frag_smile_single], ignore_index=True))
            end_time2 = time.time()
            print(f"代码2运行时间：{end_time2 - start_time2}秒")

            suffix_c = '_lightatom'
            syn_name_atom=f'{filename_without_extension_forsaving}{suffix_c}_{ratio}.jpg'
            output_image_atom=os.path.join(folder_name_img, syn_name_atom)
            attn_syn_atom=syn_1_jpeg(img_64_filename, output_image_atom)
            sys.exit()

df_frag_smiles_multi.to_excel(folder_name_statistics)

