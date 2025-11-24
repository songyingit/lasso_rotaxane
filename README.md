# Substrate Interactions Guide Cyclase Engineering and Lasso Peptide Diversification

<p align="center">
  <img src="./MD_graphical_abstract.png" alt="Graphical Abstract" width="600"/>
</p>

**Paper:** [Nature Chemical Biology (2024)](https://www.nature.com/articles/s41589-024-01727-w)  
**Data Repository:** [Zenodo/Figshare Link](https://doi.org/10.5061/dryad.fttdz092h)  
**Code Repository:** [https://github.com/ShuklaGroup/lasso_rotaxane/](https://github.com/ShuklaGroup/lasso_rotaxane/)

---

## Table of Contents

- [Abstract](#abstract)
- [System Nomenclature](#system-nomenclature)
- [MD Simulation Data](#md-simulation-data)
  - [Trajectory Files](#1-md-simulation-trajectories)
  - [Pairwise Residue Distances](#2-pairwise-residue-side-chain-heavy-distances)
  - [Fraction of Native Contacts (Q)](#3-fraction-of-native-contacts-q)
  - [Contact Probability](#4-contact-probability)
  - [Q Probability Density](#5-fraction-of-native-contacts-q-probability-density)
  - [Peptide Residue Contributions](#6-peptide-residue-contributions-to-contact-probability)
- [Analysis Code](#analysis-code)
- [Citation](#citation)

---

## Abstract

This repository contains molecular dynamics (MD) simulation data and analysis code for the manuscript *"Substrate interactions guide cyclase engineering and lasso peptide diversification"* published in Nature Chemical Biology. We performed extensive MD simulations (50 μs per system) on five different FusA (Fusilassin peptide) : FusC (Fusilassin cyclase) complex systems to investigate substrate-enzyme interactions that guide cyclase engineering and enable lasso peptide diversification.

The simulations were performed using OpenMM 7.6.0 on the Folding@home distributed computing platform with the CHARMM36m force field. Analysis was conducted using MDTraj 1.9.9 to extract key structural and interaction features.

---

## System Nomenclature

Five systems were simulated, each representing different peptide-enzyme variant combinations:

| System Name | Description | Run Index |
|-------------|-------------|-----------|
| **FusA_FusC** | FusA wildtype : FusC wildtype | RUN0 |
| **FusA_I11R_FusC** | FusA I11R : FusC wildtype | RUN1 |
| **FusA_I11R_FusC_R321G** | FusA I11R : FusC R321G | RUN2 |
| **FusA_V13R_FusC** | FusA V13R : FusC wildtype | RUN3 |
| **FusA_V13R_FusC_R321G** | FusA V13R : FusC R321G | RUN4 |

*Note: Mutation notation indicates position and amino acid change (e.g., I11R = Isoleucine at position 11 mutated to Arginine)*

---

## MD Simulation Data

### 1. MD Simulation Trajectories

**Simulation Details:**
- **Software:** OpenMM 7.6.0
- **Platform:** Folding@home
- **Force Field:** CHARMM36m
- **Total Time per System:** 50 μs
- **Trajectories per System:** 100 (500 ns each)
- **Frames per Trajectory:** 5,000

**Data Files:**

| File | Size | Description |
|------|------|-------------|
| `FusA_FusC.tar.gz` | 19.1 GB | RUN0: Wildtype system |
| `FusA_I11R_FusC.tar.gz` | 19.1 GB | RUN1: I11R peptide mutant |
| `FusA_I11R_FusC_R321G.tar.gz` | 19.1 GB | RUN2: I11R peptide + R321G cyclase |
| `FusA_V13R_FusC.tar.gz` | 19.1 GB | RUN3: V13R peptide mutant |
| `FusA_V13R_FusC_R321G.tar.gz` | 19.0 GB | RUN4: V13R peptide + R321G cyclase |

**Archive Contents:**
- 1 topology file (`.parm7`) - CHARMM36m force field parameters
- 100 trajectory files (`.xtc`) - Named as `RUN[index]_CLONE[index]_traj.xtc`

---

### 2. Pairwise Residue Side Chain Heavy Distances

Pairwise side chain heavy atom distances between FusA and FusC were calculated to characterize substrate-enzyme interactions.

**Selection Criteria:**
- **FusC:** 112 residues within 8 Å of FusA in the active site
- **FusA:** All 18 residues

**Data Files:**

| File | Size | Description |
|------|------|-------------|
| `FusA_FusC_res_dist.tar.gz` | 17.7 GB | Distance matrices for all 5 systems |

**Archive Contents:**
- `FusA_FusC_res_dist.pkl`
- `FusA_I11R_FusC_res_dist.pkl`
- `FusA_I11R_FusC_R321G_res_dist.pkl`
- `FusA_V13R_FusC_res_dist.pkl`
- `FusA_V13R_FusC_R321G_res_dist.pkl`

**Analysis Code:** [`Pairwise_residue_distances.py`](https://github.com/ShuklaGroup/lasso_rotaxane/blob/main/Pairwise_residue_distances.py)

---

### 3. Fraction of Native Contacts (Q)

The fraction of native contacts quantifies peptide pre-folding and structural stability.

**Data Files:**

| File | Size | Description |
|------|------|-------------|
| `FusA_FusC_Q.tar.gz` | 8.4 MB | Q values for all systems and frames |

**Archive Contents:**
- `FusA_FusC_Q.pkl`
- `FusA_I11R_FusC_Q.pkl`
- `FusA_I11R_FusC_R321G_Q.pkl`
- `FusA_V13R_FusC_Q.pkl`
- `FusA_V13R_FusC_R321G_Q.pkl`

**Analysis Code:** [`Native_Contacts.py`](https://github.com/ShuklaGroup/lasso_rotaxane/blob/main/Native_Contacts.py)

---

### 4. Contact Probability

Contact probability represents the likelihood of residue pairs exhibiting side chain heavy atom distances < 5 Å in frames where peptide Q > 0.8.

**Manuscript Figures:**
- **Fig. 2c, d, e:** FusA_FusC system
- **Extended Data Fig. 5a:** FusA_FusC system
- **Extended Data Fig. 5b:** FusA_I11R_FusC system
- **Extended Data Fig. 5c:** FusA_I11R_FusC_R321G system
- **Extended Data Fig. 5d:** FusA_V13R_FusC system
- **Extended Data Fig. 5e:** FusA_V13R_FusC_R321G system

**Data Files:**

| File | Size | Description |
|------|------|-------------|
| `FusA_FusC_contact_prob.tar.gz` | 18.8 kB | Contact probability matrices for all systems |

**Archive Contents:**
- `FusA_FusC_contact_prob.npy`
- `FusA_I11R_FusC_contact_prob.npy`
- `FusA_I11R_FusC_R321G_contact_prob.npy`
- `FusA_V13R_FusC_contact_prob.npy`
- `FusA_V13R_FusC_R321G_contact_prob.npy`

**Analysis Code:** [`Contact_probability_heatmap.py`](https://github.com/ShuklaGroup/lasso_rotaxane/blob/main/Contact_probability_heatmap.py)

---

### 5. Fraction of Native Contacts (Q) Probability Density

Q probability density distributions characterize the conformational landscape of the peptide substrate.

**Manuscript Figures:**
- **Fig. 3c:** FusA_I11R_FusC_R321G system
- **Extended Data Fig. 6d:** FusA_V13R_FusC_R321G system

**Data Files:**

| File | Size | Description |
|------|------|-------------|
| `FusA_FusC_Q_prob_density.tar.gz` | 13.9 kB | Probability density data (bins, mean, SD) |

**Archive Contents:**
- `FusA_FusC_Q_prob_density.pkl`
- `FusA_I11R_FusC_Q_prob_density.pkl`
- `FusA_I11R_FusC_R321G_Q_prob_density.pkl`
- `FusA_V13R_FusC_Q_prob_density.pkl`
- `FusA_V13R_FusC_R321G_Q_prob_density.pkl`

**Analysis Code:** [`Native_Contacts_prob_density.py`](https://github.com/ShuklaGroup/lasso_rotaxane/blob/main/Native_Contacts_prob_density.py)

---

### 6. Peptide Residue Contributions to Contact Probability

Individual FusA residue contributions were calculated by summing contact probabilities with all selected FusC residues and normalizing.

**Manuscript Figures:**
- **Supplementary Fig. 10:** All systems

**Data Files:**

| File | Size | Description |
|------|------|-------------|
| `FusA_FusC_pep_res_contributions.tar.gz` | 1.0 kB | Contribution values for all systems |

**Archive Contents:**
- `FusA_FusC_pep_res_contr.npy`
- `FusA_I11R_FusC_pep_res_contr.npy`
- `FusA_I11R_FusC_R321G_pep_res_contr.npy`
- `FusA_V13R_FusC_pep_res_contr.npy`
- `FusA_V13R_FusC_R321G_pep_res_contr.npy`

**Analysis Code:** [`Contact_probability_contribution.py`](https://github.com/ShuklaGroup/lasso_rotaxane/blob/main/Contact_probability_contribution.py)

---

## Analysis Code

All analysis scripts are available in the main repository: [https://github.com/ShuklaGroup/lasso_rotaxane/](https://github.com/ShuklaGroup/lasso_rotaxane/)

### Available Scripts

| Script | Purpose | Input | Output |
|--------|---------|-------|--------|
| `Pairwise_residue_distances.py` | Calculate side chain heavy atom distances | Trajectories (.xtc, .parm7) | Distance matrices (.pkl) |
| `Native_Contacts.py` | Compute fraction of native contacts | Trajectories (.xtc, .parm7) | Q values (.pkl) |
| `Contact_probability_heatmap.py` | Calculate contact probabilities | Distance matrices + Q values | Contact prob. matrices (.npy) |
| `Native_Contacts_prob_density.py` | Generate Q probability distributions | Q values (.pkl) | Density data (.pkl) |
| `Contact_probability_contribution.py` | Compute residue contributions | Contact prob. matrices | Contribution values (.npy) |

### Software Requirements

- **Python:** 3.7+
- **OpenMM:** 7.6.0
- **MDTraj:** 1.9.9
- **NumPy:** Latest stable version
- **Matplotlib:** For visualization (optional)

---

## Citation

If you use this data or code in your research, please cite:

```bibtex
@article{substrate_cyclase_2024,
  title={Substrate interactions guide cyclase engineering and lasso peptide diversification},
  journal={Nature Chemical Biology},
  year={2024},
  doi={10.1038/s41589-024-01727-w},
  url={https://www.nature.com/articles/s41589-024-01727-w}
}
```

---

## License

*Add your license information here (e.g., MIT, GPL, CC-BY)*

---