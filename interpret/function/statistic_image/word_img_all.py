
import pandas as pd
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
parent_dir_dir = os.path.dirname(parent_dir)

##1
data_files_smiles = 'data/result/statistic_function/statistics_functional_10000/deal_smiles_frag_1111'
file_name = os.path.join(parent_dir_dir, data_files_smiles)
excel_path = f'frag_smiles_main_frag_0.96_split_frequency.xlsx'
excel_path_detail = os.path.join(file_name, excel_path)
df_element = pd.read_excel(excel_path_detail)

word_freq = dict(zip(df_element['fragments'], df_element['Frequency']))
wordcloud = WordCloud(width=1600, height=1000, background_color='white').generate_from_frequencies(word_freq)
plt.figure(figsize=(20, 16))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title("Word_image of all atoms",fontsize=16, fontweight='bold')
plt.axis('off')

file_word=f'word_img'
word_img_folder = os.path.join(file_name,file_word)
img_name = f'Word_image of all atoms.jpeg'
img_name_detail=os.path.join(word_img_folder,img_name)
plt.savefig(img_name_detail, bbox_inches='tight')
plt.show()
#wordcloud.to_file('wordcloud_from_frequencies.png')
#wordcloud.to_file(path)




