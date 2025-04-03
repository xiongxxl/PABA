import math
import matplotlib.pyplot as plt
import numpy as np
import os



##single location

current_dir = os.getcwd()
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
data_files_smiles='data/result/statistic_function/statistics_functional_10000/deal_smiles_frag_1111/histogram'
foldername=os.path.join(parent_dir, data_files_smiles)

## functional group and fragments
## 1
data={
'[nH3]' :3,
'[O+]'  :3,
'[Ti]' : 3,
'[As]' : 5,
'[Cu]':	5,
'[Cr]' : 6,
'[OH-]' : 7,
'[Al]' : 7,
'[Se]' :  8,
'[Mn]':	8,
'[Zn]' : 8,
'[C-]':	11,
'[n+]' :16,
'[Si]' :18,
's'    :28,
'[N-]' :31,
'o' 	:41,
'R3P'	:46,
'[N+]' :53,
'[O-]' :136,
'S' :	386,
'n' :	404,
'N' :	1699,
'X-(F,Br,Cl,I)':2231,
'c':	2405,
'O':	3241,
'C-H':9424,
        }

data = {key: math.log(value) for key, value in data.items()}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)
fig, ax = plt.subplots(figsize=(8,8))
ax.barh(group_names,group_data,color='#b4e0f6')
ax.set_xlabel('Log(Number)', fontsize=16, fontweight='bold')
ax.set_ylabel('Functional group and fragments', fontsize=16, fontweight='bold')
ax.set_title('The top abundant 1-atom fragments', fontsize=16, fontweight='bold')
ax.tick_params(axis='both', which='major', labelsize=10)
ax.set(xlim=[0, 10])
ax.tick_params(axis='both', which='major', labelsize=12)  # 设置刻度标签字体大小
for tick in ax.get_xticklabels() + ax.get_yticklabels():
    tick.set_fontweight('bold')  # 设置数字加粗
plt.ylim(-1, len(group_names) )  # 调整 y 轴范围
plt.margins(y=0)  # 移除多余边距
plt.tight_layout()
fragment_img=f'The top abundant 1-atom fragments'  #save functional group path
statistics_fragment_path= os.path.join(foldername, fragment_img)
plt.savefig(statistics_fragment_path)
plt.show()
plt.close()

##2
data={
'C≡C' :1,
'O=S'	:55,
'cCl'	: 76,
'C#N'	: 82,
'O.[O-]': 84,
'NN'	:85,
'[N+]=O':88,
'cO'	:89,
'cN'	:92,
'N=O'	:98,
'R-S-R' :104,
'c.n'	:124,
'R-SH'	:133,
'Cl.c'	:143,
'n.n'	:168,
'N.c'	:192,
'cn'	:197,
'N.N'	:198,
'Cc'	:217,
'N.O'	:366,
'C=C'	:383,
'O.c'	:412,
'C.c'	:486,
'O.O'	:780,
'R-NH2'	:859,
'C=O'	:903,
'R-OH'	:1002,
'c.c'	:1548,
'cc'	:2917,

       }

data = {key: math.log(value) for key, value in data.items()}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)
fig, ax = plt.subplots(figsize=(8,8))
ax.barh(group_names,group_data,color='#b4e0f6')
ax.set_xlabel('Log(Number)', fontsize=16, fontweight='bold')
ax.set_ylabel('Functional group and fragments', fontsize=16, fontweight='bold')
ax.set_title('The top abundant 2-atom fragments', fontsize=16, fontweight='bold')
ax.tick_params(axis='both', which='major', labelsize=10)
ax.set(xlim=[0, 9])
ax.tick_params(axis='both', which='major', labelsize=12)  # 设置刻度标签字体大小
for tick in ax.get_xticklabels() + ax.get_yticklabels():
    tick.set_fontweight('bold')  # 设置数字加粗
plt.ylim(-1, len(group_names) )  # 调整 y 轴范围
plt.margins(y=0)  # 移除多余边距
plt.tight_layout()
fragment_img=f'The top abundant 2-atom fragments'  #save functional group path
statistics_fragment_path= os.path.join(foldername, fragment_img)
plt.savefig(statistics_fragment_path)
plt.show()


##3
data={
'R-N=C=O' : 1,
'R-S-S-R'  :4,
'R-S(=O)-R' :30,
'R-O-R' :112,
'Cl.cc'	:116,
'Cc.c'	:120,
'Cl.c.c':124,
'N.c.c'	:131,
'C=O.O'	:135,
'ccn'	:137,
'c.cn'	:145,
'ccO'   : 174,
'ccCl'	: 174,
'N.cc'	: 175,
'ccN'	:177,
'O.O.O'	:179,
'c[N+]=O':238,
'O.c.c'	:264,
'R-COOH' :271,
'c.c.c'	:284,
'C.c.c'	:369,
'O.cc'	:436,
'R-CHO'	:459,
'R-CO-R' :459,
'ccC'	:467,
'C.cc'	:473,
'c.cc'	:2051,

       }

data = {key: math.log(value) for key, value in data.items()}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)
fig, ax = plt.subplots(figsize=(8,8))
ax.barh(group_names,group_data,color='#b4e0f6')
ax.set_xlabel('Log(Number)', fontsize=16, fontweight='bold')
ax.set_ylabel('Functional group and fragments', fontsize=16, fontweight='bold')
ax.set_title('The top abundant 3-atom fragments', fontsize=16, fontweight='bold')
ax.tick_params(axis='both', which='major', labelsize=10)
ax.set(xlim=[0, 8])
ax.tick_params(axis='both', which='major', labelsize=12)  # 设置刻度标签字体大小
for tick in ax.get_xticklabels() + ax.get_yticklabels():
    tick.set_fontweight('bold')  # 设置数字加粗

plt.ylim(-1, len(group_names) )  # 调整 y 轴范围
plt.margins(y=0)  # 移除多余边距
plt.tight_layout()
fragment_img=f'The top abundant 3-atom fragments'  #save functional group path
statistics_fragment_path= os.path.join(foldername, fragment_img)
plt.savefig(statistics_fragment_path)
plt.show()

##4
data={
'R-NO3':3,
'R-SO3H':4,
'R-SO2-R':12,
'R-CONH2':23,
'C.O.cc':	87,
'cccn':	90,
'ccC=O':95,
'CC.cc':96,
'cc(c)C':104,
'R-COO-R':111,
'ccnc' :118,
'cccN'	:120,
'cccCl'	:134,
'N.ccc'	:143,
'N.c.cc':150,
'cccO'	:174,
'c.ccC'	:184,
'O.c.cc':305,
'cccC'	:305,
'O.ccc'	:337,
'c.c.cc':357,
'C.ccc'	:414,
'C.c.cc':446,
'cc.cc'	:525,
'c.ccc'	:1003,
'cccc'	:1873,
       }

data = {key: math.log(value) for key, value in data.items()}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)
fig, ax = plt.subplots(figsize=(8,8))
ax.barh(group_names,group_data,color='#b4e0f6')
ax.set_xlabel('Log(Number)', fontsize=16, fontweight='bold')
ax.set_ylabel('Functional group and fragments', fontsize=16, fontweight='bold')
ax.set_title('The top abundant 4-atom fragments', fontsize=16, fontweight='bold')
ax.tick_params(axis='both', which='major', labelsize=10)
ax.set(xlim=[0, 8.5])
ax.tick_params(axis='both', which='major', labelsize=12)  # 设置刻度标签字体大小
for tick in ax.get_xticklabels() + ax.get_yticklabels():
    tick.set_fontweight('bold')  # 设置数字加粗

plt.ylim(-1, len(group_names) )  # 调整 y 轴范围
plt.margins(y=0)  # 移除多余边距
plt.tight_layout()
fragment_img=f'The top abundant 4-atom fragments'  #save functional group path
statistics_fragment_path= os.path.join(foldername, fragment_img)
plt.savefig(statistics_fragment_path)
plt.show()

##5
data={
'R-O-PO3H2' :1,
'O.O.ccc':	70,
'c.cccC'	:77,
'C.O.c.cc':78,
'O.cc.cc'	:79,
'ccc(c)C'	:80,
'CC.ccc'	:84,
'ccccCl'	:85,
'O.O.c.cc'	:85,
'C.cc.cc'	:87,
'ccccO'	:89,
'CC.c.cc'	:90,
'O.c.ccc'	:113,
'cc.ccC'	:117,
'ccccN'	:130,
'C.c.ccc'	:167,
'c.c.ccc'	:171,
'c.cc.cc'	:207,
'ccccC'	:222,
'cc.ccc'	:260,
'O.cccc'	:273,
'C.cccc'	:376,
'c.cccc'	:390,
'ccccc'	:1175,
  }

data = {key: math.log(value) for key, value in data.items()}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)
fig, ax = plt.subplots(figsize=(8,8))
ax.barh(group_names,group_data,color='#b4e0f6')
ax.set_xlabel('Log(Number)', fontsize=16, fontweight='bold')
ax.set_ylabel('Functional group and fragments', fontsize=16, fontweight='bold')
ax.set_title('The top abundant 5-atom fragments', fontsize=16, fontweight='bold')
ax.tick_params(axis='both', which='major', labelsize=10)
ax.set(xlim=[0, 8])
ax.tick_params(axis='both', which='major', labelsize=12)  # 设置刻度标签字体大小
for tick in ax.get_xticklabels() + ax.get_yticklabels():
    tick.set_fontweight('bold')  # 设置数字加粗

plt.ylim(-1, len(group_names) )  # 调整 y 轴范围
plt.margins(y=0)  # 移除多余边距
plt.tight_layout()
fragment_img=f'The top abundant 5-atom fragments'  #save functional group path
statistics_fragment_path= os.path.join(foldername, fragment_img)
plt.savefig(statistics_fragment_path)
plt.show()

##6
data={
'cccccn'	:48,
'C.ccccC'	:49,
'c.c.cc.cc'	:49,
'C.c.cccc'	:49,
'ccccC=O'	:52,
'ccc(c)cc'	:54,
'cc.cc.cc'	:55,
'cccc(c)N'	:56,
'cccc(c)O'	:56,
'C=O.cccc'	:57,
'O.O.cccc'	:61,
'N.ccccc'	:66,
'C.C.cccc'	:69,
'C.O.cccc'	:69,
'cccccO'	:77,
'cccc[N+]=O'	:84,
'cccccN'	:88,
'c.c.cccc'	:92,
'CC.cccc'	:94,
'cccc(c)C'  :100,
'ccccOC'	:121,
'cccccc'	:147,
'cccccC'	:157,
'ccc.ccc'	:184,
'c.cc.ccc'	:216,
'O.ccccc'	:241,
'C.ccccc'	:245,
'c.ccccc'	:251,
'cc.cccc'	:291,
'C6H5'	:372,
       }

data = {key: math.log(value) for key, value in data.items()}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)
fig, ax = plt.subplots(figsize=(8,8))
ax.barh(group_names,group_data,color='#b4e0f6')
ax.set_xlabel('Log(Number)', fontsize=16, fontweight='bold')
ax.set_ylabel('Functional group and fragments', fontsize=16, fontweight='bold')
ax.set_title('The top abundant 6-atom fragments', fontsize=16, fontweight='bold')
ax.tick_params(axis='both', which='major', labelsize=10)
ax.set(xlim=[0, 6])
ax.tick_params(axis='both', which='major', labelsize=12)  # 设置刻度标签字体大小
for tick in ax.get_xticklabels() + ax.get_yticklabels():
    tick.set_fontweight('bold')  # 设置数字加粗

plt.ylim(-1, len(group_names) )  # 调整 y 轴范围
plt.margins(y=0)  # 移除多余边距
plt.tight_layout()
fragment_img=f'The top abundant 6-atom fragments'  #save functional group path
statistics_fragment_path= os.path.join(foldername, fragment_img)
plt.savefig(statistics_fragment_path)
plt.show()


