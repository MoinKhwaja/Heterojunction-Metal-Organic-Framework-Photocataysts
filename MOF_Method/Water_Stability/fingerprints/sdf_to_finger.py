from padelpy import from_sdf, from_mdl


fingerprints = from_sdf('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/fingerprints/mof2.sdf', fingerprints=True, descriptors=False)
desc_fp = from_sdf('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/fingerprints/mof2.sdf', threads=1)

_ = from_sdf('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/fingerprints/mof2.sdf', output_csv='descriptors.csv')