import math
import matplotlib.pyplot as plt
import numpy as np
import os



##single location

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
parent_dir_dir=os.path.dirname(parent_dir)
data_files_smiles='data/result/statistic_function/statistics_functional_10000/deal_smiles_frag_1111/histogram'
foldername=os.path.join(parent_dir_dir, data_files_smiles)

## functional group and fragments
## 1
data={
'R-S-S-R'	:304,
'O.c.cc'	:305,
'ccc.cccc'	:305,
'cccC'	    :305,
'O.ccc'	    :337,
'c.c.cc'	:357,
'N.O'	    :366,
'C.c.c'	    :369,
'C.cccc'	:376,
'S'	        :386,
'c.cccc'	:390,
'n'	        :404,
'O.c'	    :412,
'C.ccc'	    :414,
'O.cc'	    :436,
'C.c.cc'	:446,
'R-S(=O)-R'	:453,
'ccC'	:467,
'C.cc'	:473,
'C.c'	:486,
'cc.cc'	:525,
'C≡C'	:527,
'O.O'	:780,
'C=O'	:903,
'R3P'	:908,
'c.ccc'	:1003,
'ccccc'	:1175,
'c.c'	:1548,
'R-SO2-R'	:1687,
'N'	        :1699,
'R-NO2'	    :1769,
'cccc'	    :1873,
'ccc'	    :1898,
'c.cc'	    :2051,
'c'	        :2405,
'R-SH'	    :2512,
'cc'	    :2917,
'O'	        :3241,
'R-S-R'	    :5007,
'R-CONH2'	:6297,
'R-COOH'	:6829,
'R-COO-R'	:7811,
'C6H5OH'	:8552,
'R-CHO'	    :8964,
'C=C'	    :15032,
'R-O-R'	    :17280,
'X-(F,Br,Cl,I)'	 : 21826,
'R-CO-R'    :25877,
'C6H5'	    :26028,
'R-OH'	    :31783,
'R-NH2'	    :33827,
'C-H'	    :108813,

        }

data = {key: math.log(value) for key, value in data.items()}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)
fig, ax = plt.subplots(figsize=(16,10))
ax.barh(group_names,group_data,color='#b4e0f6')
ax.set_xlabel('Log(Number)', fontsize=16, fontweight='bold')
ax.set_ylabel('Functional group and fragments', fontsize=16, fontweight='bold')
ax.set_title('The top abundant all fragments', fontsize=16, fontweight='bold')
ax.tick_params(axis='both', which='major', labelsize=10)
ax.set(xlim=[0, 12])
ax.tick_params(axis='both', which='major', labelsize=12)  # 设置刻度标签字体大小
for tick in ax.get_xticklabels() + ax.get_yticklabels():
    tick.set_fontweight('bold')  # 设置数字加粗
plt.ylim(-1, len(group_names) )  # 调整 y 轴范围
plt.margins(y=0)  # 移除多余边距
plt.tight_layout()
fragment_img=f'The top abundant all fragments'  #save functional group path
statistics_fragment_path= os.path.join(foldername, fragment_img)
plt.savefig(statistics_fragment_path)
plt.show()


