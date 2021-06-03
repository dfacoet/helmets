import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.txt', index_col=0, comment='#')

fig, ax = plt.subplots()
df.plot.scatter(x=1, y=2, ax=ax, s=40)
nox = 1
oxs = [-2]+[nox]*7
noy = 0.5
oys = [-2.5]+[noy]*7
for i in range(len(df)):
    ax.annotate(df.iloc[i,0],(df.iloc[i,1]+oxs[i],df.iloc[i,2]+oys[i]))

ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
ax.set_xlabel('Helmet wearing rate, %')

fig.savefig('scatter.pdf')

dpi = 1024/fig.get_size_inches()[0]
fig.savefig('scatter.png',dpi=dpi)
