import matplotlib.pyplot as plt
import numpy as np
import os
current_dir = os.getcwd()
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
filename_predict=os.path.join(parent_dir,'data/result/statistics_reactive/double_para/predict')

### result of  three methods ###
categories = ['4_5', '7_7', 'Combine']
# function =[3,20,27]
# combine  =[4,30,48]
# predict  =[4,26,40]
values1 = [48.75,36.25,60]
values2 = [15,15,30]


# Calculate the sum of each group.
# total1 = sum(values1)
# total2 = sum(values2)
# total3 = sum(values3)
total1 = 100
total2 = 100


# Calculate the percentage.
percentages1 = [v / total1 * 100 for v in values1]
percentages2 = [v / total2 * 100 for v in values2]


# Draw a bar chart.
width = 0.2  # Width of each group's bar chart.
x = np.arange(len(categories))  # X-axis position.

fig, ax = plt.subplots()

ax.bar(x - width, percentages1, width, label='<20',color='#800080')
ax.bar(x, percentages2, width, label='20<=number<40',color='#FF6347')


ax.set_xticks(x)
ax.set_xticklabels(categories)

# Add percentage labels.
for i in range(len(categories)):
    ax.text(x[i] - width, percentages1[i] +0.35, f'{percentages1[i]:.2f}%', ha='center', va='bottom',fontweight='bold')
    ax.text(x[i], percentages2[i] + 0.35, f'{percentages2[i]:.2f}%', ha='center', va='bottom',fontweight='bold')


ax.legend(loc='upper left')

# Bolden the axis numbers.
# ax.tick_params(axis='both', which='major', labelsize=14, width=4)
# ax.tick_params(axis='both', which='minor', labelsize=10, width=2)
plt.xlabel('Heads',fontsize=14, fontweight='bold')
plt.ylabel('Percentage (%)',fontsize=14, fontweight='bold')
plt.title('Atoms number of reactants',fontsize=16, fontweight='bold')
plt.xticks(fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')

jpg_method_path=f'Atoms number of reactants.jpeg'
three_method_path=os.path.join(filename_predict,jpg_method_path)
plt.savefig(three_method_path)
plt.show()
