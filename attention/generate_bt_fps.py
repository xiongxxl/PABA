from fairseq.models.roberta import RobertaModel
import argparse
import sys
import numpy as np
import torch
import matplotlib.pyplot as plt
import os
# global j
# j=0
# global t
# t=0

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
data_files_smiles='data/input_smiles/supevision/example_mulit_1000_double_20_atoms.smi'
#data_files_smiles='data/input_smiles/examples/disconnect_USPTO50K.smi'
folder_name_smiles=os.path.join(parent_dir, data_files_smiles)


def load_pretrain_model(model_name_or_path, checkpoint_file, data_name_or_path, bpe='smi'):
    '''Currently only load to cpu()'''

    # load model
    pretrain_model = RobertaModel.from_pretrained(
        model_name_or_path,
        checkpoint_file,
        data_name_or_path,  # dict_dir,
        bpe=bpe,
    )
    pretrain_model.eval()
    return pretrain_model


def extract_hidden(pretrain_model, target_file):

    sample_num = 0
    for i, line in enumerate(open(target_file)):
        if len(line.strip()) == 0:
            continue
        sample_num += 1
    hidden_features = {i: None for i in range(sample_num)}

    for i, line in enumerate(open(target_file)):
        if len(line.strip()) == 0:
            continue

        tokens = pretrain_model.encode(line.strip())
        if len(tokens) > pretrain_model.args.max_positions:
            tokens = torch.cat(
                (tokens[:pretrain_model.args.max_positions - 1], tokens[-1].unsqueeze(0)))

        _, all_layer_hiddens,attn, attn_8head = pretrain_model.model(
            tokens.unsqueeze(0), features_only=True, return_all_hiddens=True)


        hidden_info = all_layer_hiddens['inner_states'][-1]
        # last_hidden shape [tokens_num, sample_num(default=1), hidden_dim]

        # hidden_features.append(hidden_info.squeeze(1).cpu().detach().numpy())
        hidden_features[i] = hidden_info.squeeze(1).cpu().detach().numpy()
        line_dit=line.strip()
        line_dit=line_dit.replace("/", "x")# use q replace '/' for save npy,x is not in dict

        #data_files_npy = f'data/middle_attention/npy_property/double_molecule_0911mark/{line_dit}.npy'
        data_files_npy = f'data/middle_attention/npy_supervision/multi_1000_double_20_atoms/{line_dit}.npy'
        folder_name_attention = os.path.join(parent_dir, data_files_npy)
        attn_8head = np.array(attn_8head)
        np.save(folder_name_attention,attn_8head)
    # hidden_features type: dict, length: samples_num
    return hidden_features ,attn, attn_8head



def extract_features_from_hidden(hidden_info):

    samples_num = len(hidden_info)
    hidden_dim = np.shape(hidden_info[0])[-1]
    samples_features = np.zeros([samples_num, hidden_dim])
    for n_sample, hidden in hidden_info.items():
        # hidden shape [tokens, embed_dim]
        samples_features[n_sample, :] = hidden[0, :]

    return samples_features


def main(args):
    pretrain_model = load_pretrain_model(
        args.model_name_or_path, args.checkpoint_file, args.data_name_or_path, args.bpe)

    hidden_info,attn, attn_8head = extract_hidden(pretrain_model, args.target_file)
    attn_8head = np.array(attn_8head)

    #np.save('result/8_npy/Oc1ccc(OCc2ccccc2)cc1.npy', attn_twodim_array)
    # plt.figure(figsize=(8,8))
    # plt.imshow(attn_twodim,cmap='Greys')
    # plt.suptitle("GridSpec Inside GridSpec")
    # plt.imshow(attn_twodim)
    # plt.show()

    print('Generate features from hidden information')
    samples_features = extract_features_from_hidden(hidden_info)
    print(f'Features shape: {np.shape(samples_features)}')
    np.save(args.save_feature_path, samples_features)
    return(attn_8head)

def parse_args(args):
    parser = argparse.ArgumentParser(description="Tools kit for downstream jobs")

    parser.add_argument('--model_name_or_path', default="./chembl_pubchem_zinc_models/chembl27_512/", type=str,
                        help='Pretrained model folder')
    parser.add_argument('--checkpoint_file', default='checkpoint_best.pt', type=str,
                        help='Pretrained model name')
    parser.add_argument('--data_name_or_path', default="./chembl_pubchem_zinc_models/chembl27_512/", type=str,
                        help="Pre-training dataset folder")
    parser.add_argument('--dict_file', default='dict.txt', type=str,
                        help="Pre-training dict filename(full path)")
    parser.add_argument('--bpe', default='smi', type=str)
 #  parser.add_argument('--target_file', default='./examples/data/example_single.smi', type=str,
 #                           help="Target file for feature extraction, default format is .smi")
    parser.add_argument('--target_file', default=folder_name_smiles, type=str,
                        help="Target file for feature extraction, default format is .smi")
    parser.add_argument('--save_feature_path', default='extract_f1.npy', type=str,
                        help="Saving feature filename(path)")
    args = parser.parse_args()
    return args


def cli_main():
    args = parse_args(sys.argv[1:])
    print(args)
    attn_twodim_array=main(args)
    return(attn_twodim_array)


if __name__ == '__main__':
    attn=cli_main()

    # for i in range(8):
    #     for j in range(8):
    #         attn_single=attn[i][j]
    #         filename = f'./result/attention/first/npy/first_{i}_{j}.npy'
    #         np.save(filename,attn_single)
    #         plt.imshow(attn_single, cmap='Greys')
    #         plt.savefig(f'./result/attention/first/img/first_{i}_{j}.jpg')
    # import os
    # from PIL import Image
    # import matplotlib.pyplot as plt
    #
    # # 定义图像文件夹路径
    # image_folder = './result/attention/first/img/'
    # # 获取所有图像文件的路径列表
    # image_paths = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if
    #                f.endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
    # # 确保图像数量至少为64
    # if len(image_paths) < 64:
    #     print("图像数量不足64")
    # else:
    #     # 读取前64副图像
    #     images = [Image.open(image_paths[i]) for i in range(64)]
    #     # 创建一个 8x8 的网格显示图像
    #     fig, axes = plt.subplots(8, 8, figsize=(20, 20), dpi=200)  # 调整 figsize 和 dpi 参数
    #     for i, ax in enumerate(axes.flat):
    #         ax.imshow(images[i])
    #         ax.axis('off')  # 关闭坐标轴
    #     plt.tight_layout()  # 调整子图之间的间距
    #     plt.show()  # 显示图像
    #     plt.savefig(f'./result/attention/first/img/64_img.jpg')