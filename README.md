#	Substrate interactions guide cyclase engineering and lasso peptide diversification

This repository contains code to analyze Molecular Dynamics (MD) simulations data in the manuscript [Substrate interactions guide cyclase engineering and lasso peptide diversification](https://www.nature.com/articles/s41589-024-01727-w). In this paper, we conducted Molecular Dynamics (MD) simulations for five different FusA (Fusilassin, peptide) : FusC (Fusilassin cyclase, enzyme) complex systems. The system names and their explanations are as follows:

* **FusA_FusC** represents FusA wildtype : FusC wildtype
* **FusA_I11R_FusC** represents FusA I11R : FusC wildtype (I11R indicates that residue 11 I was mutated to R, same for below)
* **FusA_I11R_FusC_R321G** represents FusA I11R : FusC R321G
* **FusA_V13R_FusC** represents FusA V13R : FusC wildtype
* **FusA_V13R_FusC_R321G** represents FusA V13R : FusC R321G

These system names are used as prefixes for all the data files mentioned below.

### 1. MD Simulations Trajectories

MD simulations were performed using OpenMM 7.6.0 on the distributed computing platform Folding@home. All the topology and trajectory files for each system are saved in `system name.tar.gz` files.
**Files:**

* **FusA_FusC.tar.gz (19.1 GB)**  (RUN0)
* **FusA_I11R_FusC.tar.gz (19.1 GB)**  (RUN1)
* **FusA_I11R_FusC_R321G.tar.gz (19.1 GB)**  (RUN2)
* **FusA_V13R_FusC.tar.gz (19.1 GB)**  (RUN3)
* **FusA_V13R_FusC_R321G.tar.gz (19.0 GB)**  (RUN4)

  Each `.tar.gz` file contains:

- 1 topology file (`.parm7`). The topology file was generated using the CHARMM36m force field and shared among all the trajectories for each system.
- 100 simulation trajectory (`.xtc`) files. Each trajectory file is named by `RUN[index]_CLONE[index]_traj.xtc`, where `RUN Index` specifies the corresponding simulation system as shown above (0-4) and `CLONE Index` is the index for trajectory (0-99). Each trajectory represents 500 ns simulations divided into 5000 frames, resulting in a total of 50 μs data per system.

### 2. Pairwise Residue Side Chain Heavy Distances

Pairwise residue side chain heavy distances between the peptide and cyclase were calculated using MDTraj 1.9.9. We selected 112 FusC residues within 8 Å of FusA in the active site and all 18 FusA residues to study their interactions. These pairwise distances were calculated for each frame in every trajectory for each system and then saved in `system name_res_dist.pkl` files.
**Files:**

* **FusA_FusC_res_dist.tar.gz (17.7 GB)** - Including FusA_FusC_res_dist.pkl, FusA_I11R_FusC_res_dist.pkl, FusA_I11R_FusC_R321G_res_dist.pkl, FusA_V13R_FusC_res_dist.pkl, and FusA_V13R_FusC_R321G_res_dist.pkl.

**Code:** [Pairwise_residue_distances.py](https://github.com/ShuklaGroup/lasso_rotaxane/blob/main/Pairwise_residue_distances.py)

### 3. Fraction of Native Contacts (Q)

The fraction of native contacts (Q) of the peptide was computed using MDTraj 1.9.9 to demonstrate the formation of the pre-folded state of peptide. The Q values of FusA were calculated for each frame in every trajectory for each system and then saved in `system name_Q.pkl` files.
**Files:**

* **FusA_FusC_Q.tar.gz (8.4 MB)** - Including FusA_FusC_Q.pkl, FusA_I11R_FusC_Q.pkl, FusA_I11R_FusC_R321G_Q.pkl, FusA_V13R_FusC_Q.pkl, and FusA_V13R_FusC_R321G_Q.pkl.

**Code:** [Native_Contacts.py](https://github.com/ShuklaGroup/lasso_rotaxane/blob/main/Native_Contacts.py)

### 4. Contact Probability

Contact probability refers to the likelihood of exhibiting residue side chain heavy distances less than 5 Å within the subset of frames characterized by the peptide Q value exceeding 0.8. Contact probabilities calculated for each system were saved in `system name_contact_prob.npy` files and used to plot Fig. 2c, d, e, and Extended Data Fig. 5a, b, c, d, and e in the manuscript.
**Files:**

* **FusA_FusC_contact_prob.tar.gz (18.8 kB)** - Including FusA_FusC_contact_prob.npy (Fig. 2c, d, e, and Extended Data Fig. 5a), FusA_I11R_FusC_contact_prob.npy (Extended Data Fig. 5b), FusA_I11R_FusC_R321G_contact_prob.npy (Extended Data Fig. 5c), FusA_V13R_FusC_contact_prob.npy (Extended Data Fig. 5d), and FusA_V13R_FusC_R321G_contact_prob.npy (Extended Data Fig. 5e).

**Code:** [Contact_probability_heatmap.py](https://github.com/ShuklaGroup/lasso_rotaxane/blob/main/Contact_probability_heatmap.py)

### 5. Fraction of Native Contacts (Q) Probability Density

The fraction of native contacts (Q) probability density was calculated based on previous Q data and used to plot Fig. 3c and Extended Data Fig. 6d in the manuscript. The bins, mean, and standard deviation (SD) values of probability density for plotting were saved in `system name_Q_prob_density.pkl` files.

**Files:**

* **FusA_FusC_Q_prob_density.tar.gz (13.9 kB)** - Including FusA_FusC_Q_prob_density.pkl, FusA_I11R_FusC_Q_prob_density.pkl, FusA_I11R_FusC_R321G_Q_prob_density.pkl (Fig. 3c), FusA_V13R_FusC_Q_prob_density.pkl, and FusA_V13R_FusC_R321G_Q_prob_density.pkl (Extended Data Fig. 6d).

**Code:** [Native_Contacts_prob_density.py](https://github.com/ShuklaGroup/lasso_rotaxane/blob/main/Native_Contacts_prob_density.py)

### 6. Peptide Residue Contributions to Contact Probability

The contact probabilities between each peptide FusA residue and all selected FusC residues were summed. The proportion of each FusA residue's contact probability to the total was then calculated to evaluate the contribution. The calculated contribution values were saved in `system name_pep_res_contr.npy` files and used to plot Supplementary Fig. 10 in the manuscript.
**Files:**

* **FusA_FusC_pep_res_contributions.tar.gz (1.0 kB)** - Including FusA_FusC_pep_res_contr.npy, FusA_I11R_FusC_pep_res_contr.npy, FusA_I11R_FusC_R321G_pep_res_contr.npy, FusA_V13R_FusC_pep_res_contr.npy, and FusA_V13R_FusC_R321G_pep_res_contr.npy (Supplementary Fig. 10).

**Code:** [Contact_probability_contribution.py](https://github.com/ShuklaGroup/lasso_rotaxane/blob/main/Contact_probability_contribution.py)

## Code/Software

All the code used in this work is openly available at [https://github.com/ShuklaGroup/lasso_rotaxane/](https://github.com/ShuklaGroup/lasso_rotaxane/)
