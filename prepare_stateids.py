import numpy as np

# copy state ids and randomization code


variants = ['yeo7', 'yeo17']


for variant in variants:

    # convert binary data into unique identifiers (integers 0..2^N)

    Xall = np.load('{}_binarized.npz'.format(variant))['arr_0']
    Xall = Xall.astype(int)
    N = Xall.shape[-1]

    pow2 = 2**np.arange(N)[::-1]
    ids = np.dot(Xall, pow2) 

    print(variant, len(np.unique(ids)), 'unique states', ids.shape)

    np.savez_compressed('{}_stateids.npz'.format(variant), ids)

    # repeat the same after decorrelating each channel

    U, S, T, N = Xall.shape

    Xall = Xall.reshape(-1, N)
    maxt = len(Xall)
    Xrnd = np.zeros_like(Xall)
    rnd = np.random.default_rng(555)
    for c in range(N):
        dt = rnd.integers(maxt)
        Xrnd[:, c] = np.roll(Xall[:, c], dt)

    Xrnd = Xrnd.reshape(U, S, T, N)

    pow2 = 2**np.arange(N)[::-1]
    ids = np.dot(Xrnd, pow2) 

    print(variant,'randomized', len(np.unique(ids)), 'unique states', ids.shape)

    np.savez_compressed('{}rnd_stateids.npz'.format(variant), ids)




