import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Arial'
import os
import pickle
import tol_colors as tc
tol_cmap = tc.tol_cmap('rainbow_PuBr')

file_dir = ' '

FusA_I11R_FusC_list = []
for k in [0,1,2]:
    with open(file_dir + 'native_contact/RUN'+str(k)+'/RUN'+str(k)+'_native_contacts_list.pkl','rb') as f:
        native_contacts = pickle.load(f)
    native_contacts_connected = np.concatenate(native_contacts,axis=0)
    native_contacts_connected = native_contacts_connected.reshape((len(native_contacts_connected),))
    FusA_I11R_FusC_list.append(native_contacts_connected)

FusA_V13R_FusC_list = []
for k in [0,3,4]:
    with open(file_dir + 'native_contact/RUN'+str(k)+'/RUN'+str(k)+'_native_contacts_list.pkl','rb') as f:
        native_contacts = pickle.load(f)
    native_contacts_connected = np.concatenate(native_contacts,axis=0)
    native_contacts_connected = native_contacts_connected.reshape((len(native_contacts_connected),))
    FusA_V13R_FusC_list.append(native_contacts_connected)

def plot_hist_1(data, figname, num_iterations, color_index, bins_):
    colors = [['r', 'c', 'm'], ['orange', 'purple', 'blue']]  
    fig, axs = plt.subplots(1,1,figsize=(10,7))
    for i in range(len(data)):
        bootstrap_results = np.zeros((num_iterations, bins_))
        for j in range(num_iterations):
            bootstrap_sample = np.random.choice(data[i], size=int(0.8*len(data[i])), replace=True)
            nSD, binsSD = np.histogram(bootstrap_sample, bins=bins_, density=True)
            bootstrap_results[j, :] = nSD
        maxy = np.max(bootstrap_results,axis=0)
        miny = np.min(bootstrap_results,axis=0)
        meany = np.mean(bootstrap_results,axis=0)
        axs.plot(binsSD[0:-1], meany, linewidth=3, c=colors[color_index][i])
        axs.fill_between(binsSD[0:-1], miny, maxy, alpha=0.3, color=colors[color_index][i])
    axs.set_xlim([0, 1])
    axs.set_ylim([0, 4])
    axs.set_xticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    axs.set_xticklabels([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    axs.set_yticks([0, 1, 2, 3, 4])
    axs.set_yticklabels([0, 1, 2, 3, 4])
    axs.tick_params(width=3,length=5, labelsize=22)
    axs.spines['top'].set_visible(False)
    axs.spines['right'].set_visible(False)
    plt.xlabel('The fraction of native contacts', fontsize=24)
    plt.ylabel('Probability density', fontsize=24)
    plt.rc('xtick', labelsize=24)
    plt.rc('ytick', labelsize=24)
    plt.tight_layout()
    plt.savefig(figname,dpi=500)

def plot_hist_2(data, figname, num_iterations, color_index, bins_):
    colors = [['r', 'c', 'm'], ['orange', 'purple', 'blue']]  
    fig, axs = plt.subplots(1,1,figsize=(10,7))
    for i in range(len(data)):
        bootstrap_results = np.zeros((num_iterations, bins_))
        for j in range(num_iterations):
            bootstrap_sample = np.random.choice(data[i], size=int(0.8*len(data[i])), replace=True)
            nSD, binsSD = np.histogram(bootstrap_sample, bins=bins_, density=True)
            bootstrap_results[j, :] = nSD
        maxy = np.max(bootstrap_results,axis=0)
        miny = np.min(bootstrap_results,axis=0)
        meany = np.mean(bootstrap_results,axis=0)
        axs.plot(binsSD[0:-1], meany, linewidth=3, c=colors[color_index][i])
        axs.fill_between(binsSD[0:-1], miny, maxy, alpha=0.3, color=colors[color_index][i])
    axs.set_xlim([0, 1])
    axs.set_ylim([0, 5])
    axs.set_xticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    axs.set_xticklabels([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    axs.set_yticks([0, 1, 2, 3, 4, 5])
    axs.set_yticklabels([0, 1, 2, 3, 4, 5])
    axs.tick_params(width=3,length=5, labelsize=22)
    axs.spines['top'].set_visible(False)
    axs.spines['right'].set_visible(False)
    plt.xlabel('The fraction of native contacts', fontsize=24)
    plt.ylabel('Probability density', fontsize=24)
    plt.rc('xtick', labelsize=24)
    plt.rc('ytick', labelsize=24)
    plt.tight_layout()
    plt.savefig(figname,dpi=500)

os.chdir(file_dir)
plot_hist_1(FusA_I11R_FusC_list, 'FusA_I11R_FusC_native_contact_hist.png', 200, 0, 100)
plot_hist_2(FusA_V13R_FusC_list, 'FusA_V13R_FusC_native_contact_hist.png', 200, 1, 100)