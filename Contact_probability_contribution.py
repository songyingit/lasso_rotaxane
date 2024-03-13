import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Arial'
import os
from matplotlib import rc
import tol_colors as tc
tol_cmap = tc.tol_cmap('rainbow_PuBr')
from matplotlib.colors import LinearSegmentedColormap

file_dir = ' '

sys_list = ['FusA:FusC','FusA I11R:FusC','FusA I11R:FusC R321G','FusA V13R:FusC','FusA V13R:FusC R321G']
Fus_seq = ['WYTAEWGLELIFVFPRFI', 'WYTAEWGLELRFVFPRFI', 'WYTAEWGLELRFVFPRFI', 'WYTAEWGLELIFRFPRFI', 'WYTAEWGLELIFRFPRFI']

results = {}
for k in range(5):
      os.chdir(file_dir)
      fraction_array = np.load(file_dir + "/Run_"+str(k)+"_fraction_array.npy")
      sum_cp = np.sum(fraction_array, axis=1)
      results[sys_list[k]] = sum_cp/np.sum(sum_cp)

category_names = [i for i in range(1,19)]

def cp_bar(results, category_names, show_labels):
      labels = list(results.keys())
      data = np.array(list(results.values()))
      data_cum = data.cumsum(axis=1)
      cmap = LinearSegmentedColormap.from_list('custom_colormap', plt.cm.Blues(np.linspace(0, 1, 256)))

      fig, ax = plt.subplots(1, 2, figsize=(8, 3), gridspec_kw={'width_ratios': [1, 0.02]})
      ax[0].invert_yaxis()
      ax[0].xaxis.set_visible(True)
      ax[0].set_xlim(0, np.sum(data, axis=1).max())

      for i, (colname, color) in enumerate(zip(category_names, np.arange(len(category_names)) / len(category_names))):
            widths = data[:, i]
            starts = data_cum[:, i] - widths
            colors = cmap(widths / np.max(data))
            rects = ax[0].barh(labels, widths, left=starts, height=0.5, label=colname, color=colors)
            for j in range(len(labels)):
                  ax[0].plot([starts[j] + widths[j], starts[j] + widths[j]], [j - 0.25, j + 0.25], color='grey', lw=0.1)

            if show_labels is None or colname in show_labels:
                  for rect in rects:
                        width = rect.get_width()
                        label_color = 'white' if colname == 1 or colname == 18 else 'black'
                        ax[0].text(width / 2 + rect.get_x(), rect.get_y() + rect.get_height() / 2,
                              f'{colname}', 
                              ha='center', va='center', color=label_color, weight='bold')                  

      im = ax[1].pcolor(data, cmap='Blues',ec='k',lw=0.3)
      cbar = fig.colorbar(im, cax=ax[1], ticks=[0, 0.2])
      cbar.set_label('Contribution',size=12)
      cbar.ax.text(2.2, 0.15, 'High', ha='center', va='center', fontsize=8)
      cbar.ax.text(2.2, 0.005, 'Low', ha='center', va='center', fontsize=8)
      cbar.ax.tick_params(labelsize=10)

      ax[0].set_xlabel('FusA residue contributions to contact probability', fontsize=12)
      fig.tight_layout()
      fig.savefig(file_dir + "/Contact_probability_contribution.png", dpi = 600)

show_labels = [1, 9, 11, 13, 15, 18]
cp_bar(results, category_names, show_labels)

    

    





