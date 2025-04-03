
import numpy as np
import os
import pandas as pd
from tokenizer import tokenize_smiles
import sys
from binary_highatom_function import highlight_chemical_atoms
from syn_1_img import syn_1_jpg
from syn_1_img import syn_1_jpeg
from syn_1_img import syn_1_png
from attn_binary_function import attn_64_img
import sys
import os
import time
import multiprocessing as mp


ratio=0.95
# for ratio in np.arange(0.96, 0.99, 0.05):
current_dir = os.getcwd()
parent_dir = os.path.dirname(os.path.dirname(current_dir))
data_files_npy='data/middle_attention/npy_function/npy_12105'
folder_name_npy=os.path.join(parent_dir, data_files_npy)
data_files_img='data/result/img_function/img_10000'
folder_name_img=os.path.join(parent_dir, data_files_img)

statistics_path='data/result/statistic_function/statistics_functional_10000'
fragment_excel=f'frag_smiles_main_{ratio}.csv'  #save functional group path
statistics_fragment_path= os.path.join(statistics_path, fragment_excel)
folder_name_statistics=os.path.join(parent_dir, statistics_fragment_path)

j=0
df_frag_smiles_multi=pd.DataFrame()
save_img_flag=0 # 1 saving img and 0 not saving img

for filename in os.listdir(folder_name_npy):
    if filename.endswith('.npy'):
        filepath = os.path.join(folder_name_npy, filename)
        attn = np.load(filepath)
        filename_without_extension = os.path.splitext(filename)[0]
        if 'H' in filename_without_extension:
            #j=j+1
            pass
        else:
            # data_files_npy_simple='data/middle_attention/npy_reactive/double_molecule_0911mark/C[Si](C)(C)C#CCO.N#Cc1ccccc1.npy'
            # attn=np.load(os.path.join(parent_dir, data_files_npy_simple))
            # filename_without_extension='C[Si](C)(C)C#CCO.N#Cc1ccccc1'
            filename_without_extension = filename_without_extension.replace("x", "/")
            filename_without_extension_re= tokenize_smiles(filename_without_extension)  #re syn like cl to one element
            filename_without_extension_forsaving=filename_without_extension.replace("/", "x") #this filename for saving address
            j=j+1
            print(f'Filename: {filename_without_extension}')
            print(j)

            start_time1=time.time()
            img_64_filename=attn_64_img(attn, folder_name_img, filename_without_extension,ratio,save_img_flag)
            if save_img_flag:
                syn_name_attn=f'{filename_without_extension_forsaving}_{ratio}.jpg'
                output_image_attn=os.path.join(folder_name_img, syn_name_attn)
                attn_syn_img=syn_1_jpg(img_64_filename, output_image_attn) #syn 64 attention to 1 image
                print(img_64_filename)
            end_time1=time.time()
            print(f"code 1 time：{end_time1-start_time1}s")

            if save_img_flag:
                suffix_b = '_binarize'
                syn_name_binarize=f'{filename_without_extension_forsaving}{suffix_b}_{ratio}.jpg'
                output_image_binarize=os.path.join(folder_name_img, syn_name_binarize)
                attn_syn_binarize=syn_1_png(img_64_filename, output_image_binarize)

            ##syn 64 highatom images
            start_time2 = time.time()
            df_frag_smile_single=highlight_chemical_atoms(img_64_filename,filename_without_extension,save_img_flag)  #produce high atom imagge
            df_frag_smiles_multi = pd.DataFrame(pd.concat([df_frag_smiles_multi, df_frag_smile_single], ignore_index=True))
            end_time2 = time.time()
            print(f"code 2 time：{end_time2 - start_time2}s")
            if save_img_flag:
                suffix_c = '_lightatom'
                syn_name_atom=f'{filename_without_extension_forsaving}{suffix_c}_{ratio}.jpg'
                output_image_atom=os.path.join(folder_name_img, syn_name_atom)
                attn_syn_atom=syn_1_jpeg(img_64_filename, output_image_atom)

            if j>9999:
                df_frag_smiles_multi.to_csv(folder_name_statistics)
            sys.exit()


# def job(x):
#     return x*x
#
# def multicore():
#     pool = mp.Pool()
#     res = pool.map(job, range(10000))
#     # print(res)
#     # res = pool.apply_async(job, (2,))
#     # print(res.get())
#     # multi_res =[pool.apply_async(job, (i,)) for i in range(10)]
#     # print([res.get() for res in multi_res])
#
# if __name__ == '__main__':
#     multicore()