#	Insights into rotaxane formation enables cyclase engineering for lasso peptide diversification

This repository contains Molecular Dynamics (MD) data and the python code used to generate calculations and figures in the manuscript.

##	MD Simulations Data
All the MD trajectory files conducted by Folding@home can be downloaded from https://uofi.box.com/s/uqhedj758tfa4dvjrmfp1d66jr25phsq, including five systems: FusA:FusC(RUN0), FusA I11R:FusC(RUN1), FusA I11R:FusC R321G(RUN2), FusA V13R:FusC(RUN3), FusA V13R:FusC R321G(RUN4).

##	Peptide-Enzyme Pairwise Residue Distances
Pairwise_residue_distances.py: Python script to calculate pairwise residue distances between peptide FusA and enzyme FusC.

##	Peptide Native Contacts
Native_Contacts.py: Python script to calculate the fraction of native contacts of peptide FusA and variants.

##	Peptide-Enzyme Contact Probability Heatmap
Contact_probability_heatmap.py: Python script to calculate contact probability between peptide FusA and enzyme FusC, and plot as heatmap. (Figure 2, Figure S22)

##	Peptide Residue Contributions to Contact Probability
Contact_probability_contribution.py: Python script to calculate FusA residue contributions to contact probability. (Figure S23)

##	Petide Native Contacts Probability Density 
Native_Contacts_histogram.py: Python script to calculate the probability density distribution of FusA native contacts. (Figure 3, Figure S34)

