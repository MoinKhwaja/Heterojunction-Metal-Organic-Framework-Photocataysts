from padelpy import from_sdf

# calculate molecular descriptors for molecules in `mols.sdf`
descriptors = from_sdf('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/fingerprints/mof1.sdf')

# in addition to descriptors, calculate PubChem fingerprints
desc_fp = from_sdf('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/fingerprints/mof1.sdf', fingerprints=True)

# only calculate fingerprints
fingerprints = from_sdf('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/fingerprints/mof1.sdf', fingerprints=True, descriptors=False)

# setting the number of threads, this uses one cpu thread to compute descriptors
desc_fp = from_sdf('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/fingerprints/mof1.sdf', threads=1)

# save descriptors to a CSV file
_ = from_sdf('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/fingerprints/mof1.sdf', output_csv='descriptors.csv')