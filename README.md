
 Reaction Center Prediction by Analyzing Attention Matrices of a Chemical Language Model.
 
  1. inputing the trained network to obtain the attention matrix. The pre-trained parameters can be accessed at the following URL:https://github.com/WeilabMSU/PretrainModels/blob/main/README.md
     After downroading "pretrainModels-main" ,put 'attention' file.
  2. We have modified the original model's literature code to extract the attention matrix. It is essential to use the modified code provided in this paper entirely, avoiding updates to
     file packages such as function libraries, which could lead to failure in extracting the attention.
  3. Converting the samples into SMILES expressions without "H" and create a .smi file. The extracted attention files will be saved to the data/middle_attention/npy folder.
  4. Inputing reactants to 'data/inputs_smiles/sample', and  result of predicting  reaction center is in 'result/statistics_reactive'.
  

