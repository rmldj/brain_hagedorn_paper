import os
import nibabel as nib
import numpy as np

# erase these lines after you inserted correct information later in the script
print('update USER and PASSWORD for HCP before running this script')
quit()


os.makedirs('data', exist_ok=True)

# subject list extracted from the csv files for 100 unrelated subjects

subjects = [100307, 100408, 101107, 101309, 101915, 103111, 103414, 103818,
       105014, 105115, 106016, 108828, 110411, 111312, 111716, 113619,
       113922, 114419, 115320, 116524, 117122, 118528, 118730, 118932,
       120111, 122317, 122620, 123117, 123925, 124422, 125525, 126325,
       127630, 127933, 128127, 128632, 129028, 130013, 130316, 131217,
       131722, 133019, 133928, 135225, 135932, 136833, 138534, 139637,
       140925, 144832, 146432, 147737, 148335, 148840, 149337, 149539,
       149741, 151223, 151526, 151627, 153025, 154734, 156637, 159340,
       160123, 161731, 162733, 163129, 176542, 178950, 188347, 189450,
       190031, 192540, 196750, 198451, 199655, 201111, 208226, 211417,
       211720, 212318, 214423, 221319, 239944, 245333, 280739, 298051,
       366446, 397760, 414229, 499566, 654754, 672756, 751348, 756055,
       792564, 856766, 857263, 899885]


rooturl = 'https://db.humanconnectome.org/data/archive/projects/HCP_1200/subjects/{0}/experiments/{0}_CREST/resources/{0}_CREST/files'

variants = ['REST1_LR', 'REST1_RL', 'REST2_LR', 'REST2_RL']



for sub in subjects[1:]:
    for variant in variants:
        fpath = 'MNINonLinear/Results/rfMRI_{0}'.format(variant)
        fname = 'rfMRI_{}_Atlas_MSMAll_hp2000_clean.dtseries.nii'.format(variant)
        output = ''
        cmd = 'curl -u USER:PASSWORD -O {}/{}/{}'.format(rooturl.format(sub), fpath, fname)
        print(cmd)
        os.system(cmd)
        X = nib.load(fname)
        arr = X.get_fdata().astype(np.float32)
        outfile = 'data/{}_{}.npz'.format(sub, variant)
        print('saving to', outfile)
        os.system('rm {}'.format(fname))    # COMMENT OUT IF YOU WANT TO KEEP THE dtseries.nii FILE
        print('removing', fname)
        np.savez_compressed(outfile, arr)




