import pandas as pd
from calculate_str_number import calulate_eval
statistic_function_10000 = pd.read_csv('/mnt/work/code/tian/smiles/data/result/statistic_function/statistics_functional_10000/deal_smiles_frag_1111/frag_smiles_main_frag_0.96.csv',sep=',')
statistic_function_element_1=statistic_function_10000[statistic_function_10000['location'].apply(lambda x: calulate_eval(x)==1)]
statistic_function_element_2=statistic_function_10000[statistic_function_10000['location'].apply(lambda x: calulate_eval(x)==2)]
statistic_function_element_3=statistic_function_10000[statistic_function_10000['location'].apply(lambda x: calulate_eval(x)==3)]
statistic_function_element_4=statistic_function_10000[statistic_function_10000['location'].apply(lambda x: calulate_eval(x)==4)]
statistic_function_element_5=statistic_function_10000[statistic_function_10000['location'].apply(lambda x: calulate_eval(x)==5)]
statistic_function_element_6=statistic_function_10000[statistic_function_10000['location'].apply(lambda x: calulate_eval(x)==6)]

statistic_function_element_1.to_csv('/mnt/work/code/tian/smiles/data/result/statistic_function/statistics_functional_10000/deal_smiles_frag_1111/statistic_function_element_1.csv')
statistic_function_element_2.to_csv('/mnt/work/code/tian/smiles/data/result/statistic_function/statistics_functional_10000/deal_smiles_frag_1111/statistic_function_element_2.csv')
statistic_function_element_3.to_csv('/mnt/work/code/tian/smiles/data/result/statistic_function/statistics_functional_10000/deal_smiles_frag_1111/statistic_function_element_3.csv')
statistic_function_element_4.to_csv('/mnt/work/code/tian/smiles/data/result/statistic_function/statistics_functional_10000/deal_smiles_frag_1111/statistic_function_element_4.csv')
statistic_function_element_5.to_csv('/mnt/work/code/tian/smiles/data/result/statistic_function/statistics_functional_10000/deal_smiles_frag_1111/statistic_function_element_5.csv')
statistic_function_element_6.to_csv('/mnt/work/code/tian/smiles/data/result/statistic_function/statistics_functional_10000/deal_smiles_frag_1111/statistic_function_element_6.csv')