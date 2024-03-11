import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':18})
plt.rcParams.update({'legend.fontsize':14})
plt.rcParams['figure.constrained_layout.use'] = True

dim = 7

states = np.load('yeo7_stateids.npz')['arr_0']

ids, counts = np.unique(states, return_counts=True)

ind = np.argsort(counts)[::-1]

ids = ids[ind]
counts = counts[ind]

maxn = 30
ids = ids[:maxn]
counts = counts[:maxn]

raster = np.zeros((maxn, dim), dtype=int)

for i in range(maxn):
    raster[i, :] = [int(s) for s in np.binary_repr(ids[i], dim)]


plt.figure(figsize=(6,4))
plt.imshow(raster.T, aspect='auto', cmap='gray')
plt.xlabel('LOWEST energy states')
plt.ylabel('RSN')

plt.xticks(ticks=np.arange(maxn), labels=ids, rotation=90, fontsize=13)

rsns = ['Visual', 'SomMot', 'DorsAtt', 'VenAtt', 'Limbic', 'FrontPar', 'Default']

plt.yticks(ticks=np.arange(dim), labels=rsns, fontsize=13)



plt.show()




