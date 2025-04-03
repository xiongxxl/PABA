import pandas as pd
import numpy as np
import os
import re

def get_diff(A, B):
    A = sorted(A)
    B = sorted(B)
    diff = -1
    for b in B:
        if b in A:
            pass
        else:
            return diff
    diff = len(A) - len(B)
    return diff





def calculate_reactive_percentage(df_criterion, df_sample):
    df_error_atoms = pd.DataFrame()
    df_criterion_axis = df_criterion[['smiles', 'gold_criterion']]

    tmp_location = {}
    tmp_attention_axis = {}
    tmp_flag={}
    for atom_num in range(6):
        atom_num = str(atom_num)

        for index_criterion, row_criterion in df_criterion_axis.iterrows():
            tmp_location[index_criterion] = []
            tmp_attention_axis[index_criterion] = []
            tmp_flag[index_criterion] = []

            value_smiles_criterion = row_criterion['smiles']
            value_location_criterion = row_criterion['gold_criterion']
            # Here you can perform operations on value1 and value2
            # print(value_smiles_criterion, value_location_criterion)
            filtered_df = df_sample[df_sample['smiles'] == value_smiles_criterion]
            filtered_df_64 = filtered_df.reset_index(drop=True)
            attention_axis_multi=[]
            # # Iterate through each row of the DataFrame and compare it with the array.
            for index_sample, row_sample in filtered_df_64.iterrows():
                # if set(value_location_criterion).issubset(set(row_sample['location'])):
                # if contains(value_location_criterion,row_sample['location']):
                row_sample_location = row_sample['reactive_atoms']
                #A=row_sample['location']
                row_sample_location = eval(row_sample_location)
                value_location_criterion = eval(str(value_location_criterion))
                erro = get_diff(row_sample_location, value_location_criterion)
                if erro == eval(atom_num):
                    tmp_flag[index_criterion]=1
                    # df_criterion.at[index_criterion, column_name_location] = row_sample['location']
                    tmp_location[index_criterion].append(row_sample['reactive_atoms'])
                    # df_criterion.at[index_criterion, column_name_attention_axis] = row_sample['attention_axis']
                    tmp_attention_axis[index_criterion].append(row_sample['head_axis'])

        column_name_flag = f'flag_{atom_num}'
        column_name_location = f'reactive_atoms_{atom_num}'
        column_name_attention_axis = f'head_axis_{atom_num}'
        df_flag_tmp= pd.DataFrame(list(tmp_flag.items()), columns=['index', 'flag'])
        df_criterion[column_name_flag]=df_flag_tmp['flag']
        df_location_tmp= pd.DataFrame(list(tmp_location.items()), columns=['index', 'reactive_atoms'])
        df_criterion[column_name_location]=df_location_tmp['reactive_atoms']
        df_attention_axis_tmp = pd.DataFrame(list(tmp_attention_axis.items()), columns=['index', 'head_axis'])
        df_criterion[column_name_attention_axis] = df_attention_axis_tmp['head_axis']

    return df_criterion

if __name__ == "__main__":
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    statistics_detail = 'data/result/statistics_reactive/double_100'
    statistics_folder=os.path.join(parent_dir,statistics_detail)
    df_criterion = pd.read_excel(os.path.join(statistics_folder, 'double_criterion_100.xlsx'))
    df_sample= pd.read_csv(os.path.join(statistics_folder, 'frag_smiles_main_0.96.csv'))
    results = calculate_reactive_percentage(df_criterion, df_sample)
    results_df=pd.DataFrame(results)
    atoms_number_excel = f'frag_atoms_error_main_0.96.xlsx'  # save functional group path
    statistics_atoms_number_path = os.path.join(statistics_folder, atoms_number_excel)
    results_df.to_csv(statistics_atoms_number_path, index=False)

