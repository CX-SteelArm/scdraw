import numpy as np
import sys
import os.path
import matplotlib.pyplot as plt
from conf import *

fig, ax = plt.subplots();

def sta(data, start, step, segments):
	d = np.zeros(segments);
	for i in data:
		c = int((i-start) / step);
		if c < segments-1:
			d[c] += 1;
		else:
			d[-1] += 1;
			
	e = [' ']* segments;
	for i in range(0, segments-1):
		e[i] = str(start+step*i) + '-' + str(start+step*(i+1));
	e[-1] = ">" + str(start+step*(segments-1))
	return d*100/1.0/len(data), e;

fileNum = len(IFNAME);
for i in range(fileNum):	
	dlist = np.genfromtxt(os.path.join(sys.path[0], IFNAME[i]));
	nd, nt = sta(dlist, START, STEP, SEGMENTS);
	index = np.arange(SEGMENTS);
	rect = plt.bar(index+i*BAR_WIDTH, nd, BAR_WIDTH, alpha=OPACITY, color=COLOR_BOX[i], label=LABELS[i]);

plt.xlabel(XLABEL, fontsize=18);
plt.ylabel(YLABEL, fontsize=18);
plt.xticks(index + BAR_WIDTH*fileNum/2.0, nt);
plt.ylim(*YLIM);
plt.legend();
plt.tight_layout();


S = raw_input("Save or not ?(y/n):");
if S == "y":
	plt.savefig(os.path.join(sys.path[0], "output.jpg"), doi=300);
else:
	plt.show();