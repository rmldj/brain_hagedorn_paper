import os
import numpy as np
from nilearn.signal import clean
import hcp_utils as hcp
from time import time


def binarize(Xorg):
    # binarizes between 0 and 1 using uint8 in order to save space
    medians = np.median(Xorg, axis=0)
    X = np.zeros_like(Xorg, dtype=np.uint8)
    X[:, :] = 0
    for c in range(len(medians)):
        X[Xorg[:,c]>medians[c], c] = 1
    return X


print()


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

variants = ['REST1_LR', 'REST1_RL', 'REST2_LR', 'REST2_RL']

# RSN parcellations

nsubjects = len(subjects)   # 100

nums = [7, 17]

parcellations = dict()
alldata = dict()
name = dict()

parcellations[7] = hcp.yeo7
name[7] = 'yeo7'
alldata[7] = np.zeros((nsubjects, 4, 1140, 7), dtype=np.uint8)

parcellations[17] = hcp.yeo17
name[17] = 'yeo17'
alldata[17] = np.zeros((nsubjects, 4, 1140, 17), dtype=np.uint8)



for i, sub in enumerate(subjects):
    t0 = time()
    for j, variant in enumerate(variants):
        X = np.load('data/{}_{}.npz'.format(sub, variant))['arr_0']
        X = clean(X, t_r=0.72, high_pass=0.01, low_pass=0.25)

        # eliminate first 30 and last 30 TRs
        X = X[30:-30]

        # parcellate and normalize

        for num in nums:
            parcellation = schaefer[num]
            data = alldata[num]
            Xp = hcp.normalize(hcp.parcellate(X, parcellation))
            data[i, j, :, :] = binarize(Xp)

    print('{}/100 subject {} finished in {:.1f}s'.format(i+1, sub, time()-t0))

print()
for num in nums:
    data_fname = '{}_binarized.npz'.format(name[num])
    print('saving binarized data to', data_fname)
    np.savez_compressed(data_fname, alldata[num])



