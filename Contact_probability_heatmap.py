import numpy as np
import matplotlib.pyplot as plt
import os
import pickle
from matplotlib import rc
import itertools
import pickle
import tol_colors as tc
tol_cmap = tc.tol_cmap('rainbow_PuBr')

##### Define the files path #####

file_dir = ' '
sys_list = ['FusA:FusC','FusA I11R:FusC','FusA I11R:FusC R321G','FusA V13R:FusC','FusA V13R:FusC R321G']
FusC_seq = 'MVGCISPYFAVFPDKDVLGQATDRLPAAQTLASHPSGRPWLVGALPADQLLLVEAGERRLAVIGHCSAEPERLRAELAQIDDVAQFDRLARTLDGSFHLVVVVGDQMRIQGSVSGLRRVFHAHVGTARIAADRSDVLAAVLGVSPDPDVLALRMFNGLPYPLSELPPWPGVEHVPAWHYLSLGLHDGRHRVVQWWHPPEAELDVTAAAPLLRTALAGAVDTRTRGGGVVSADLSGGLDSTPLCALAARGPAKVVALTFSSGLDTDDDLRWAKIAHQSFPSVEHVVLSPEDIPGFYAGLDGEFPLLDEPSVAMLSTPRILSRLHTARAHGSRLHMDGLGGDQLLTGSLSLYHDLLWQRPWTALPLIRGHRLLAGLSLSETFASLADRRDLRAWLADIRHSIATGEPPRRSLFGWDVLPKCGPWLTAEARERVLARFDAVLESLEPLAPTRGRHADLAAIRAAGRDLRLLHQLGSSDLPRMESPFLDDRVVEACLQVRHEGRMNPFEFKSLMKTAMASLLPAEFLTRQSKTDGTPLAAEGFTEQRDRIIQIWRESRLAELGLIHPDVLVERVKQPYSFRGPDWGMELTLTVELWLRSRERVLQGANGGDNRS'
Fus_seq = ['WYTAEWGLELIFVFPRFI', 'WYTAEWGLELRFVFPRFI', 'WYTAEWGLELRFVFPRFI', 'WYTAEWGLELIFRFPRFI', 'WYTAEWGLELIFRFPRFI']

##### Colormap Label #####

FusC_index = [153, 156, 211, 215, 231, 232, 233, 234, 236, 237, 238, 239, 240, 241, 242, 243, 256, 257, 258, 286, 288, 290, 291, 292, 293, 294, 295, 296, 302, 303, 304, 305, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 324, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 371, 373, 410, 415, 418, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 476, 479, 480, 481, 482, 483, 484, 488, 506, 507, 510, 511, 514, 530, 532, 533, 534, 535, 536, 537, 538, 539, 540, 576, 577, 578, 579, 581, 583, 584, 585, 588]
FusC_index = np.array(FusC_index) - 1
FusC_label = []
for run_id in range(5):
    FusC_label_run = []
    for fusc_index in FusC_index:
        if fusc_index == 320 and (run_id == 2 or run_id == 4):
            FusC_label_run.append('G321')
        else:
            FusC_label_run.append(FusC_seq[fusc_index]+str(fusc_index+1))
    FusC_label.append(FusC_label_run)

pep=list(np.arange(610,628))
pep_enz_all_pairs = list(itertools.product(pep,FusC_index))

##### Calculate Contact Probability #####

for k in range(5):
    with open(file_dir + 'native_contact/RUN'+str(k)+'_native_contacts_list.pkl','rb') as f:
        native_contacts = pickle.load(f)
    native_contacts_connected = np.concatenate(native_contacts,axis=0)
    native_contacts_connected = native_contacts_connected.reshape((len(native_contacts_connected),))
    native_contacts_filter_list = []
    for  nc_id, nc in enumerate(native_contacts_connected):
        if nc >= 0.8:
            native_contacts_filter_list.append(nc_id)
    nonc = len(native_contacts_filter_list)
    # del native_contacts

    with open(file_dir + '/pairwise_distances/RUN'+str(k)+'_pairwise_distance_list.pkl', 'rb') as f:
        all_features = pickle.load(f)
    all_features_connected=np.concatenate(all_features,axis=0)

    fraction_array = np.zeros((len(pep),len(FusC_index)))
    for pep_res_id, pep_res in enumerate(pep):
        for enz_res_id, enz_res in enumerate(FusC_index):
            feature_index = pep_enz_all_pairs.index((int(pep_res), int(enz_res)))
            x_feature = all_features_connected[:,feature_index]
            x_feature = x_feature[np.array(native_contacts_filter_list)]
            x_feature = x_feature[x_feature <= 0.50]
            frac = len(x_feature) / nonc
            fraction_array[pep_res_id][enz_res_id] = frac
    np.save(file_dir + "/Run_"+str(k)+"_fraction_array.npy",fraction_array)
    # del all_features

    ## Plot the colormap
    fig, axs = plt.subplots(1, 2, figsize=(20, 5), gridspec_kw={'width_ratios': [1, 0.010]})
    im = axs[0].pcolor(fraction_array, cmap='ocean_r',ec='k',lw=0.3)
    cbar = fig.colorbar(im, cax=axs[1], ticks=[0, 0.2, 0.4, 0.6, 0.8, np.max(fraction_array)])
    cbar.set_label('Contact probability',size=18)
    cbar.ax.set_yticklabels(['0', '0.2', '0.4', '0.6', '0.8', '1.0'])
    cbar.ax.tick_params(labelsize=10)
    axs[0].set_yticks(np.arange(0.5,18,1))
    ytick = [Fus_seq[k][i] for i in range(18)]
    axs[0].set_yticklabels(ytick,fontname='Courier New', fontsize=12)
    if k == 1 or k == 2:
        plt.setp(axs[0].get_yticklabels()[10], color='red', weight = 'bold')
    elif k == 3 or k == 4:
        plt.setp(axs[0].get_yticklabels()[12], color='red', weight = 'bold')
    axs[0].set_xticks(np.arange(0.5,112,1))
    xtick = FusC_label[k]
    if k == 2 or k == 4:
        plt.setp(axs[0].get_xticklabels()[46], color='red', weight = 'bold')
    axs[0].set_xticklabels(xtick,fontname='Courier New',fontsize=12, rotation=270)
    axs[0].set_ylabel('FusA core', fontname='Arial', fontsize=18)
    axs[0].set_xlabel('FusC',fontname='Arial', fontsize=18)
    fig.suptitle(sys_list[k], fontsize=18, y=0.95)
    fig.tight_layout()
    fig.savefig(file_dir + '/RUN_'+str(k)+'_colormap.png',dpi=600)



    

    





