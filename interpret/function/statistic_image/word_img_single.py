
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
excel_path = f'statistic_function_element_1_split_frequency_ascend_del.xlsx'
excel_path_detail = os.path.join(file_name, excel_path)
df_element = pd.read_excel(excel_path_detail)


word_freq = dict(zip(df_element['fragments'], df_element['Frequency']))
wordcloud = WordCloud(width=800, height=600, background_color='white').generate_from_frequencies(word_freq)
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title("Word_image of 1 atoms",fontsize=16, fontweight='bold')
plt.axis('off')

file_word=f'word_img'
word_img_folder = os.path.join(file_name,file_word)
img_name = f'word_image of 1 atom.jpeg'
img_name_detail=os.path.join(word_img_folder,img_name)
plt.savefig(img_name_detail, bbox_inches='tight')
plt.show()

#wordcloud.to_file('wordcloud_from_frequencies.png')
#wordcloud.to_file(path)

##2
data_files_smiles = 'data/result/statistic_function/statistics_functional_10000/deal_smiles_frag_1111'
file_name = os.path.join(parent_dir_dir, data_files_smiles)
excel_path = f'statistic_function_element_2_split_frequency_ascend_del.xlsx'
excel_path_detail = os.path.join(file_name, excel_path)
df_element = pd.read_excel(excel_path_detail)

word_freq = dict(zip(df_element['fragments'], df_element['Frequency']))
wordcloud = WordCloud(width=800, height=600, background_color='white').generate_from_frequencies(word_freq)
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title("Word_image of 2 atoms",fontsize=16, fontweight='bold')
plt.axis('off')

file_word=f'word_img'
word_img_folder = os.path.join(file_name,file_word)
img_name = f'word_image of 2 atom.jpeg'
img_name_detail=os.path.join(word_img_folder,img_name)
plt.savefig(img_name_detail, bbox_inches='tight')
plt.show()
#wordcloud.to_file('wordcloud_from_frequencies.png')
#wordcloud.to_file(path)

##3
data_files_smiles = 'data/result/statistic_function/statistics_functional_10000/deal_smiles_frag_1111'
file_name = os.path.join(parent_dir_dir, data_files_smiles)
excel_path = f'statistic_function_element_3_split_frequency_ascend_del.xlsx'
excel_path_detail = os.path.join(file_name, excel_path)
df_element = pd.read_excel(excel_path_detail)

word_freq = dict(zip(df_element['fragments'], df_element['Frequency']))
wordcloud = WordCloud(width=800, height=600, background_color='white').generate_from_frequencies(word_freq)
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title("Word_image of 3 atoms",fontsize=16, fontweight='bold')
plt.axis('off')

file_word=f'word_img'
word_img_folder = os.path.join(file_name,file_word)
img_name = f'word_image of 3 atom.jpeg'
img_name_detail=os.path.join(word_img_folder,img_name)
plt.savefig(img_name_detail, bbox_inches='tight')
plt.show()
#wordcloud.to_file('wordcloud_from_frequencies.png')
#wordcloud.to_file(path)

##4
data_files_smiles = 'data/result/statistic_function/statistics_functional_10000/deal_smiles_frag_1111'
file_name = os.path.join(parent_dir_dir, data_files_smiles)
excel_path = f'statistic_function_element_4_split_frequency_ascend_del.xlsx'
excel_path_detail = os.path.join(file_name, excel_path)
df_element = pd.read_excel(excel_path_detail)

word_freq = dict(zip(df_element['fragments'], df_element['Frequency']))
wordcloud = WordCloud(width=800, height=600, background_color='white').generate_from_frequencies(word_freq)
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title("Word_image of 4 atoms",fontsize=16, fontweight='bold')
plt.axis('off')

file_word=f'word_img'
word_img_folder = os.path.join(file_name,file_word)
img_name = f'word_image of 4 atom.jpeg'
img_name_detail=os.path.join(word_img_folder,img_name)
plt.savefig(img_name_detail, bbox_inches='tight')
plt.show()
#wordcloud.to_file('wordcloud_from_frequencies.png')
#wordcloud.to_file(path)

##5
data_files_smiles = 'data/result/statistic_function/statistics_functional_10000/deal_smiles_frag_1111'
file_name = os.path.join(parent_dir_dir, data_files_smiles)
excel_path = f'statistic_function_element_5_split_frequency_ascend_del.xlsx'
excel_path_detail = os.path.join(file_name, excel_path)
df_element = pd.read_excel(excel_path_detail)

word_freq = dict(zip(df_element['fragments'], df_element['Frequency']))
wordcloud = WordCloud(width=800, height=600, background_color='white').generate_from_frequencies(word_freq)
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title("Word_image of 5 atoms",fontsize=16, fontweight='bold')
plt.axis('off')

file_word=f'word_img'
word_img_folder = os.path.join(file_name,file_word)
img_name = f'word_image of 5 atom.jpeg'
img_name_detail=os.path.join(word_img_folder,img_name)
plt.savefig(img_name_detail, bbox_inches='tight')
plt.show()
#wordcloud.to_file('wordcloud_from_frequencies.png')
#wordcloud.to_file(path)

##6
data_files_smiles = 'data/result/statistic_function/statistics_functional_10000/deal_smiles_frag_1111'
file_name = os.path.join(parent_dir_dir, data_files_smiles)
excel_path = f'statistic_function_element_6_split_frequency_ascend_del.xlsx'
excel_path_detail = os.path.join(file_name, excel_path)
df_element = pd.read_excel(excel_path_detail)

word_freq = dict(zip(df_element['fragments'], df_element['Frequency']))
wordcloud = WordCloud(width=800, height=600, background_color='white').generate_from_frequencies(word_freq)
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title("Word_image of 6 atoms",fontsize=16, fontweight='bold')
plt.axis('off')

file_word=f'word_img'
word_img_folder = os.path.join(file_name,file_word)
img_name = f'word_image of 6 atom.jpeg'
img_name_detail=os.path.join(word_img_folder,img_name)
plt.savefig(img_name_detail, bbox_inches='tight')
plt.show()
#wordcloud.to_file('wordcloud_from_frequencies.png')
#wordcloud.to_file(path)



