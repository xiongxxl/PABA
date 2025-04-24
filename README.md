
 Reaction Center Prediction by Analyzing Attention Matrices of a Chemical Language Model.
 
  1. Inputing the trained network to obtain the attention matrix. The pre-trained parameters can be accessed at the following URL:https://github.com/WeilabMSU/PretrainModels/blob/main/README.md
     After downroading "pretrainModels-main" ,put 'attention' file.
  2. We have modified the original model's literature code to extract the attention matrix. It is essential to use the modified code provided in this paper entirely, avoiding updates to
     file packages such as function libraries, which could lead to failure in extracting the attention.
  3. Converting the samples into SMILES expressions without "H" and create a .smi file. The extracted attention files will be saved to the data/middle_attention/npy folder.
  4. Code of extracting molecular fragments  is in   "interpret/function" file. Inputing 10000 smaple,method will produces functional group dict.
  5. Code of predicting reaction centers is in "interpret/reaction" ."mian_find_heads" method ensure heads axis as 4_5 and 7_7, "main_find_apha” method ensure alpha.
      

