
import os

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



categories = ['Condensation', 'Addition', 'Substitution', 'Others']
# function =[3,20,27]
# combine  =[4,30,48]
# predict  =[4,26,40]
values1 = [27.03,43.75,50.00,40.00]
values2 = [35.13,27.50,25.00,33.33]
values3 = [51.35,50.00,59.38,53.33]

# total1 = sum(values1)
# total2 = sum(values2)
# total3 = sum(values3)
total1 = 100
total2 = 100
total3 = 100


percentages1 = [v / total1 * 100 for v in values1]
percentages2 = [v / total2 * 100 for v in values2]
percentages3 = [v / total3 * 100 for v in values3]

# Draw a bar chart.
width = 0.2  # Draw a bar chart.
x = np.arange(len(categories))  # X-axis position.

fig, ax = plt.subplots(figsize=(10,8))

ax.bar(x - width, percentages1, width, label='4_5',color='#32CD32')
ax.bar(x, percentages2, width, label='7_7',color='#800080')
ax.bar(x + width, percentages3, width, label='Combine',color='#FF6347')
#32CD32','#800080','#FF6347'
ax.set_xticks(x)
ax.set_xticklabels(categories)


for i in range(len(categories)):
    ax.text(x[i] - width, percentages1[i] +0.35, f'{percentages1[i]:.2f}%', ha='center', va='bottom',fontsize=14,fontweight='bold')
    ax.text(x[i], percentages2[i] + 0.35, f'{percentages2[i]:.2f}%', ha='center', va='bottom',fontsize=14,fontweight='bold')
    ax.text(x[i] + width, percentages3[i] + 0.35, f'{percentages3[i]:.2f}%', ha='center', va='bottom',fontsize=14,fontweight='bold')


plt.legend(loc='upper left')
plt.legend(fontsize=12,)
plt.gca().spines['top'].set_linewidth(1)
plt.gca().spines['right'].set_linewidth(1)
plt.gca().spines['left'].set_linewidth(1)
plt.gca().spines['bottom'].set_linewidth(1)
# 设置标签
ax.set_ylabel('Percentage (%)')
ax.set_title('The accuracy of different reactive types')
plt.xlabel('Reactive types',fontsize=18, fontweight='bold')
plt.ylabel('Atoms_error',fontsize=18, fontweight='bold')
plt.title('The accuracy of different reactive types',fontsize=20, fontweight='bold')
plt.xticks(fontsize=16, fontweight='bold')
plt.yticks(fontsize=16, fontweight='bold')
plt.tight_layout()
plt.subplots_adjust()

current_dir = os.getcwd()
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
file_name='data/result/statistics_reactive/double_para/reactive_type'
input_files_smiles = os.path.join(parent_dir, file_name)
jpg_accuracy_path=f'The accuracy of different reactive types.jpeg'
reactive_path=os.path.join(input_files_smiles ,jpg_accuracy_path)
plt.savefig(reactive_path,dpi=300)
plt.show()


## 4_5


categories = ['Condensation', 'Addition', 'Substitution', 'Others']
data = {
    'Condensation': [2,2,1,1,1,4,1,0,3,4],
    'Addition': [3,0,1,4,3,0,0],
    'Substitution': [1,2,2,3,2,2,2,1,2,0,2,1,4,2,2,0],
    'Others': [3,1,2,0,3,4]
}
# Convert data format.
df = pd.DataFrame([(cat, val) for cat, values in data.items() for val in values],
                  columns=['Category', 'Value'])

plt.figure(figsize=(8, 6))
# Draw a violin plot.
sns.violinplot(x="Category", y="Value", data=df, inner="quartile", cut=0,palette=['#32CD32','#800080','#FF6347','#9DD79D'])
# sns.violinplot(x="Category", y="Value", data=df, inner="quartile", cut=0,palette=['#32CD32','#800080','#FF6347','#9DD79D'])

sns.pointplot(x="Category", y="Value", data=df, estimator=np.mean, color="black",
              errorbar=("pi", 100), join=False, capsize=0.2, markers="o")

plt.xlabel('Reactive type',fontsize=14, fontweight='bold')
plt.ylabel('Atoms_error',fontsize=14, fontweight='bold')
plt.title('The distribution of accurate reactive types(4_5)',fontsize=16, fontweight='bold')
plt.xticks(fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')

current_dir = os.getcwd()
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
file_name='data/result/statistics_reactive/double_para/reactive_type'
input_files_smiles = os.path.join(parent_dir, file_name)
jpg_method_path=f'The distribution of accurate reactive types_4_5.jpeg'
reactive_path=os.path.join(input_files_smiles ,jpg_method_path)
plt.savefig(reactive_path)
plt.show()

##7_7
categories = ['Condensation', 'Addition', 'Substitution', 'Others']
data = {
    'Condensation': [3,2,4,3,3,3,2,4,2,2,4,4,4],
    'Addition': [1,1,3,2,1,2],
    'Substitution': [1,4,3,2,4,3,2,4],
    'Others': [2,2,3,1,4]
}

df = pd.DataFrame([(cat, val) for cat, values in data.items() for val in values],
                  columns=['Category', 'Value'])

plt.figure(figsize=(8, 6))
# 绘制小提琴图
sns.violinplot(x="Category", y="Value", data=df, inner="quartile", cut=0,palette=['#32CD32','#800080','#FF6347','#9DD79D'])

sns.pointplot(x="Category", y="Value", data=df, estimator=np.mean, color="black",
              errorbar=("pi", 100), join=False, capsize=0.2, markers="o")

plt.xlabel('Reactive type',fontsize=14, fontweight='bold')
plt.ylabel('Atoms_error',fontsize=14, fontweight='bold')
plt.title('The distribution of accurate reactive types(7_7)',fontsize=16, fontweight='bold')
plt.xticks(fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')

current_dir = os.getcwd()
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
file_name='data/result/statistics_reactive/double_para/reactive_type'
input_files_smiles = os.path.join(parent_dir, file_name)
jpg_method_path=f'The distribution of accurate reactive types_7_7.jpeg'
reactive_path=os.path.join(input_files_smiles ,jpg_method_path)
plt.savefig(reactive_path)
plt.show()

## combine

categories = ['Condensation', 'Addition', 'Substitution', 'Others']
data = {
    'Condensation': [2,2,2,1,1,3,1,4,1,3,3,2,4,2,0,2,4,3,4],
    'Addition': [3,0,1,3,2,1,0,0],
    'Substitution': [1,2,2,3,2,4,2,2,2,1,2,0,2,1,4,2,3,2,0],
    'Others': [2,3,1,3,1,0,3,4]
}

df = pd.DataFrame([(cat, val) for cat, values in data.items() for val in values],
                  columns=['Category', 'Value'])

plt.figure(figsize=(8, 6))

sns.violinplot(x="Category", y="Value", data=df, inner="quartile", cut=0,palette=['#32CD32','#800080','#FF6347','#9DD79D'])

sns.pointplot(x="Category", y="Value", data=df, estimator=np.mean, color="black",
              errorbar=("pi", 100), join=False, capsize=0.2, markers="o")

plt.xlabel('Reactive type',fontsize=14, fontweight='bold')
plt.ylabel('Atoms_error',fontsize=14, fontweight='bold')
plt.title('The distribution of accurate reactive types(combine)',fontsize=16, fontweight='bold')
plt.xticks(fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')

current_dir = os.getcwd()
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
file_name='data/result/statistics_reactive/double_para/reactive_type'
input_files_smiles = os.path.join(parent_dir, file_name)
jpg_method_path=f'The distribution of accurate reactive types_combine.jpeg'
reactive_path=os.path.join(input_files_smiles ,jpg_method_path)
plt.savefig(reactive_path)
plt.show()



#
# # 生成示例数据
# categories = ['Condensation', 'Addition', 'Substitution', 'Others']
# data = {
#     # 'A': np.random.normal(10, 2, 20),
#     # 'B': np.random.normal(15, 3, 20),
#     # 'C': np.random.normal(7, 2, 20),
#     # 'D': np.random.normal(20, 4, 20),
#     'Condensation': [2,2,2,1,1,3,1,4,1,3,3,2,4,2,0,2,4,3,4],
#     'Addition': [3,0,1,3,2,1,0,0],
#     'Substitution': [1,2,2,3,2,4,2,2,2,1,2,0,2,1,4,2,3,2,0],
#     'Others': [2,3,1,3,1,0,3,4],
#       }
# means = [np.mean(data[cat]) for cat in categories]
# stds = [np.std(data[cat]) for cat in categories]
#
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.bar(categories, means, yerr=stds, capsize=5, color='#b4e0f6', label='Mean ± Std Dev')
#
# ax.set_title('The distribution of accurate reactive types')
# plt.xlabel('Reactive type',fontsize=14, fontweight='bold')
# plt.ylabel('Atoms_error',fontsize=14, fontweight='bold')
# plt.title('The distribution of accurate reactive types',fontsize=16, fontweight='bold')
# plt.xticks(fontsize=12, fontweight='bold')
# plt.yticks(fontsize=12, fontweight='bold')
#
# current_dir = os.getcwd()
# parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
# file_name='data/result/statistics_reactive/double_para/reactive_type'
# input_files_smiles = os.path.join(parent_dir, file_name)
# jpg_method_path=f'The distribution of accurate reactive types.jpeg'
# reactive_path=os.path.join(input_files_smiles ,jpg_method_path)
# plt.savefig(reactive_path)
# plt.show()
#
#