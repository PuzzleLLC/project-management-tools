import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse
from typing import *


def lrs(f: str) -> (float, float):
    if len(f.split("-")) == 2:
        l, r = [int(v) for v in f.split("-")]
        w = r - l
        x = l + w / 2.
    else:
        w = 1
        x = float(f)

    return x, w / 2.


# Name, Difficulty/Cost, Benefit
features = """
Defect Calculators on Handheld,30-55,3
Louder Sound on Handheld Interaction,15-30,1
Human-Based Scale Integration,25-60,9-11
Force a Sync After Printing,5-10,4
Email Reminders for Unfinished FEMT Forms,35-50,7
Price Entry/Management (UI and Security),90-170,11
Deck Field for Loads (e.g. G3),5-15,2
"""

f1 = features.split("\n")
f2 = [f.split(",") for f in f1 if len(f.split(",")) == 3]

f3 = []
xscale = 0
yscale = 0
for f in f2:

    name = f[0]
    cost = f[1]
    benefit = f[2]

    xw = lrs(cost)
    yh = lrs(benefit)

    if np.sum(xw) > xscale:
        xscale = np.sum(xw)
    if np.sum(yh) > yscale:
        yscale = np.sum(yh)

    f3.append([name, xw, yh])

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

ells = []
for f in f3:  # type: Tuple[str, Tuple[float, float], Tuple[float, float]]
    w = (f[1][1]/xscale)*2. if f[1][1] != 1 else .1
    h = (f[2][1]/yscale)*2. if f[2][1] != 1 else .1
    ells.append(Ellipse(
        xy=(1. - f[1][0]/xscale, f[2][0]/yscale),
        width=w,
        height=h,
        facecolor=(.0, .5, .5, .5),
    ))

    plt.text(ells[-1].center[0] - w/2., ells[-1].center[1], f[0])

for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)

ax.set_ylabel('Benefit')
ax.set_xlabel('Ease of Development (Inverse Cost)')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.xticks([])
plt.yticks([])

ax.set_ylim(-.05, 1)
ax.set_xlim(-.05, 1.75)

plt.show()
