import numpy as np
import sys
import os.path
import matplotlib.pyplot as plt
from conf import *
	
dlist = np.genfromtxt(os.path.join(sys.path[0], "data.lua"));

r, c = dlist.shape;

fig, ax = plt.subplots();

for index in range(c):
	plt.bar(np.arange(r)+BAR_WIDTH*index, dlist[:,index], BAR_WIDTH, alpha=OPACITY, color=COLOR_BOX[index], label=LABELS[index]);

plt.xlabel(XLABEL, fontsize=20);
plt.ylabel(YLABEL, fontsize=20);
plt.xticks(np.arange(r) + BAR_WIDTH*c/2.0, XTICKS, fontsize=16);
plt.ylim(*YLIM);
plt.legend();
plt.tight_layout();

S = raw_input("Save or not ?(y/n):");
if S == "y":
	plt.savefig(os.path.join(sys.path[0], "output.jpg"), dpi=300);
else:
	plt.show();