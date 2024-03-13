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

##### Calculate Native Contact #####
                  
parm_list = ['Fus_WT_FusC_WT.parm7','Fus_I11R_FusC_WT.parm7','Fus_I11R_FusC_R321G.parm7','Fus_V13R_FusC_WT.parm7','Fus_V13R_FusC_R321G.parm7']

def q_func(traj, native):
    BETA_CONST = 50  # 1/nm
    LAMBDA_CONST = 1.8
    NATIVE_CUTOFF = 0.45  # nanometers
    # get the indices of all of the heavy atoms
    heavy = native.topology.select_atom_indices('heavy')
    # get the pairs of heavy atoms which are farther than 3
    # residues apart
    heavy_pairs = np.array(
        [(i,j) for (i,j) in combinations(heavy, 2)
            if abs(native.topology.atom(i).residue.index - \
                   native.topology.atom(j).residue.index) > 3])
    
    # compute the distances between these pairs in the native state
    heavy_pairs_distances = md.compute_distances(native[0], heavy_pairs)[0]
    # and get the pairs s.t. the distance is less than NATIVE_CUTOFF
    native_contacts = heavy_pairs[heavy_pairs_distances < NATIVE_CUTOFF]
    # now compute these distances for the whole trajectory
    r = md.compute_distances(traj, native_contacts)
    # and recompute them for just the native state
    r0 = md.compute_distances(native[0], native_contacts)
    q = np.mean(1.0 / (1 + np.exp(BETA_CONST * (r - LAMBDA_CONST * r0))), axis=1)
    return q

def cal_native_contact(traj_dir,native_heavy):      
      i = int(traj_dir.split('/')[-1].rstrip('.xtc').split('_')[0].replace('RUN',''))
      traj = md.load(traj_dir, top = file_dir + parm_list[i])
      traj_peptide=traj.atom_slice(traj.topology.select("resid 610 to 627 and not element H"))
      q = q_func(traj_peptide, native_heavy)
      np.save(file_dir + 'native_contact/RUN'+str(i)+'/'+ traj_dir.split('/')[-1].rstrip('.xtc')+'_native_contact.npy',q)
      del traj
      del q

def run_cal_native_contact(r):
      j = int(traj_dir[r].split('/')[-1].rstrip('.xtc').split('_')[0].replace('RUN',''))
      native = md.load_pdb(file_dir + '/native_contact/RUN'+str(j)+'_Fus_initial_structure.pdb')
      native_heavy = native.atom_slice(native.topology.select("not element H")[:-1])
      os.makedirs(file_dir + 'native_contact/RUN'+str(j), exist_ok = True)
      cal_native_contact(traj_dir[r], native_heavy)

p = Pool(16)
p.map(run_cal_native_contact, range(len(traj_dir)))
p.close()
p.join()

##### Combine the features #####

os.chdir(file_dir + 'native_contact/')
native_contact_list = []
for i in range(5):
      for j in range(100):
            run_clone_features=np.load('RUN'+str(i)+'/RUN'+str(i)+'_CLONE'+str(j)+'_traj_native_contact.npy')
            run_clone_features=run_clone_features.reshape((run_clone_features.shape[0],1))
            native_contact_list.append(run_clone_features)
      with open('RUN'+str(i)+'_native_contact_list.pkl','wb') as f:
            pickle.dump(native_contact_list,f)