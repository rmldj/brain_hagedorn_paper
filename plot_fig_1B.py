import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':18})
plt.rcParams.update({'legend.fontsize':14})
plt.rcParams['figure.constrained_layout.use'] = True

states7 = np.load('yeo7_stateids.npz')['arr_0'].reshape(-1)
states17 = np.load('yeo17_stateids.npz')['arr_0'].reshape(-1)


states7rnd = np.load('yeo7rnd_stateids.npz')['arr_0'].reshape(-1)
states17rnd = np.load('yeo17rnd_stateids.npz')['arr_0'].reshape(-1)



def analyze(states, N):

    _, cnts = np.unique(states, return_counts=True)

    p = cnts/np.sum(cnts)

    ind = np.argsort(p)[::-1]

    p = p[ind]

    en = -np.log(p)
    en = en - en[0]
    en = en/N

    ns = np.arange(1, len(p)+1)
    logns = np.log(ns)

    scumulative = logns/N

    return en, scumulative

en7, scum7 = analyze(states7, 7)
en17, scum17 = analyze(states17, 17)

en7rnd, scum7rnd = analyze(states7rnd, 7)
en17rnd, scum17rnd = analyze(states17rnd, 17)

lo = 0.23
hi = 0.4

i0 = np.where(en17>lo)[0][0]
i1 = np.where(en17>hi)[0][0]
print('fit range', i0, en17[i0], i1, en17[i1])
print()

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(en17[i0:i1].reshape(-1, 1), scum17[i0:i1])
a = lr.coef_[0]
b = lr.intercept_
print('a', a)
print('b', b)
print('1/a', 1/a)

xsfit = np.linspace(0.0, 0.6, 100)
ysfit = lr.predict(xsfit.reshape(-1, 1))



xs = np.linspace(0, 0.6, 100)

plt.figure(figsize=(6,6))
plt.plot(en7, scum7, marker='o', alpha=1.0, markerfacecolor='white', label='Yeo 7')
plt.plot(en17, scum17, marker='s',alpha=1.0, markerfacecolor='white', label='Yeo 17')
plt.plot(xsfit, ysfit, color='k', alpha=1, linestyle='dashed', label='T={:.1f}'.format(1/a))

plt.plot(en7rnd, scum7rnd, linestyle='dashed', color='tab:blue', alpha=1.0, label='Yeo 7 shuffled')
plt.plot(en17rnd, scum17rnd, linestyle='dashed', color='tab:orange', alpha=1.0, label='Yeo 17 shuffled')


plt.xlabel('E/N')
plt.ylabel('S/N')
plt.xlim(0, 0.7)
plt.ylim(0, 0.7)
plt.xticks(np.arange(8)/10)
plt.legend()

plt.gca().set_box_aspect(1)

plt.show()

