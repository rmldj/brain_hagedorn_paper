# Downloading and preprocessing information

Here we provide scripts equivalent to the ones we used for downloading and preprocessing data resulting in the binarized data used in the paper. The scripts need to be modified with login credentials and possible path information. Note that the download script `download_hcp100.py` converts the `*.dtseries.nii` files into numpy `*.npz` arrays and erases the original. Comment out the relevant lines if you want to keep the `*.dtseries.nii` files.

The script `prepare_binarized_yeo_parcellations.py` uses the downloaded data in the form of `*.npz` arrays to create the binarized files for the Yeo-7 and Yeo-17 RSN parcellations.

These scripts require `nilbabel` (https://nipy.org/nibabel/gettingstarted.html), `nilearn` (https://nilearn.github.io/stable/index.html) and `hcp-utils` (https://rmldj.github.io/hcp-utils/) packages.


