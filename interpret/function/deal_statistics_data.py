import pandas as pd
import os
from find_functional_group import identify_functional_groups
import numpy as np


current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
parent_dir_dir=os.path.dirname(parent_dir)
data_files_smiles='data/result/statistic_function/statistics_functional_10000/deal_smiles_frag_1111'
foldername=os.path.join(parent_dir_dir, data_files_smiles)

#del o row

#df = pd.read_excel((os.path.join(foldername, 'frag_smiles_main_frag_0.96.xlsx')),header=0,index_col=0)
#df = np.where(df.drop(columns = ['rna_plate']).duplicated(keep = 'first')==False)[0]
# df = df.loc[~(df == 0).all(axis=1)]
# df = df.dropna(how='all')
# df=df.reset_index(drop=False)
# df.to_excel((os.path.join(foldername, 'frag_smiles_main_deal_0.95.xlsx')), index=True)
#df.to_excel((os.path.join(foldername, 'frag_smiles_main_deal_0.95.xlsx')), index=True)

# # find functional group
# file_path = os.path.join(foldername, 'frag_smiles_main_deal_0.95.xlsx') #
# #df.set_index('smiles',inplace=True)
#
# for i in range(len(df)):
#     smiles=str(df.at[i,'smiles'])
#     frag=str(df.at[i,'frag'])
#     detected_groups = identify_functional_groups(frag,smiles)
#
#     true_keys = [k for item in detected_groups for k, v in item.items() if v is True]
#     if not true_keys:
#         df.at[i, 'functional_group'] = df.at[i, 'frag']
#     else:
#         ture_keys_str =','.join(true_keys)
#         df.at[i, 'functional_group'] = ture_keys_str
#
# output_file =os.path.join(foldername, 'frag_smiles_main_deal_functional_0.95.xlsx')
# df.to_excel(output_file, index=False)

#devide multiple functional to single functional group

df = pd.read_csv(os.path.join(foldername, 'frag_smiles_main_frag_0.96.csv'))


split_df = df['functional_group'].str.split(',', expand=True).stack()
split_df = split_df.reset_index(level=1, drop=True).reset_index(name='fragments')
# Save the result as a new Excel file.
split_df.to_excel(os.path.join(foldername, 'frag_smiles_main_frag_0.96_split.xlsx'),index=False)


#find frequeny
file_path = os.path.join(foldername, 'frag_smiles_main_frag_0.96_split.xlsx')
df = pd.read_excel(file_path)

column_name = 'fragments'
frequency = df[column_name].value_counts()

frequency_df = frequency.reset_index()
frequency_df.columns = [column_name, 'Frequency']
output_file =os.path.join(foldername, 'frag_smiles_main_frag_0.96_split_frequency.xlsx')
frequency_df.to_excel(output_file, index=False)

# #produce frequency image
# file_path = os.path.join(foldername, 'frag_smiles_main_deal_functional_split_frequency.xlsx') # 替换为你的文件路径
# df = pd.read_excel(file_path)
# produce_word_image(df)

