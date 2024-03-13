import numpy as np
import mdtraj as md
import os
import itertools
import pickle
from multiprocessing import Pool
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Arial'
from matplotlib import rc

##### Define the files path #####

file_dir = ' '
traj_dir = []
for i in range(5):
      for j in range(100):
            os.chdir(file_dir + 'RUN' + str(i) + '/CLONE'+ str(j) + '/')
            if os.path.isfile('RUN' + str(i) + '_CLONE'+ str(j)+ '_traj.xtc'):
                  traj_dir.append(file_dir + 'RUN' + str(i) + '/CLONE'+ str(j) + '/RUN' + str(i) + '_CLONE'+ str(j)+ '_traj.xtc')

##### Calculate Pairwise Distances #####

os.makedirs(file_dir + 'pairwise_distances/', exist_ok = True)
parm_list = ['Fus_WT_FusC_WT.parm7','Fus_I11R_FusC_WT.parm7','Fus_I11R_FusC_R321G.parm7','Fus_V13R_FusC_WT.parm7','Fus_V13R_FusC_R321G.parm7']
pep = list(np.arange(610,628))
enz = [153, 156, 211, 215, 231, 232, 233, 234, 236, 237, 238, 239, 240, 241, 242, 243, 256, 257, 258, 286, 288, 290, 291, 292, 293, 294, 295, 296, 302, 303, 304, 305, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 324, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 371, 373, 410, 415, 418, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 476, 479, 480, 481, 482, 483, 484, 488, 506, 507, 510, 511, 514, 530, 532, 533, 534, 535, 536, 537, 538, 539, 540, 576, 577, 578, 579, 581, 583, 584, 585, 588]
enz = np.array(enz) - 1
pep_enz_all_pairs = list(itertools.product(pep,enz))

def dis_Fus_FusC(traj_dir):
      i = int(traj_dir.split('/')[-1].rstrip('.xtc').split('_')[0].replace('RUN',''))
      traj = md.load(traj_dir, top = file_dir + parm_list[i])
      Fus_Fusc_sidechain_distance = md.compute_contacts(traj,pep_enz_all_pairs,scheme='sidechain-heavy',ignore_nonprotein=True, periodic=True)
      np.save((file_dir + 'pairwise_distances/RUN'+str(i)+'/'+ traj_dir.split('/')[-1]).rstrip('.xtc')+'_pairwise_distance.npy',Fus_Fusc_sidechain_distance[0])

def cal_dis_Fus_FusC(r):
    j = int(traj_dir[r].split('/')[-1].rstrip('.xtc').split('_')[0].replace('RUN',''))
    os.makedirs(file_dir + 'pairwise_distances/RUN'+str(j), exist_ok = True)
    dis_Fus_FusC(traj_dir[r])

os.chdir(file_dir + 'pairwise_distances/')
p = Pool(16)
p.map(cal_dis_Fus_FusC, range(len(traj_dir)))
p.close()
p.join()

##### Combine the features #####

for i in range(5):
      os.chdir(file_dir + 'pairwise_distances/')
      peptide_enzyme_features_list = []
      for j in range(100):
            run_clone_features=np.load('RUN'+str(i)+'/RUN'+str(i)+'_CLONE'+str(j)+'_traj_pairwise_distance.npy')
            peptide_enzyme_features_list.append(run_clone_features)
      with open('RUN'+str(i)+'_pairwise_distance_list.pkl','wb') as f:
            pickle.dump(peptide_enzyme_features_list,f)
      del peptide_enzyme_features_list