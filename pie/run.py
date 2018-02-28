import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({'font.size': 14});

fig, ax = plt.subplots(figsize=(10,10));

data = [7.54, 4.54, 24.59, 34.47, 5.91, 22.36, 0.59];

labels = ['Ti', 'Nb', 'Cr', 'Mo', 'Co', 'Ni', 'Al'];

colors  = ["#66cc78","red","coral","green","yellow","orange","#cccccc"]

ax.pie(data, labels=labels, colors=colors, autopct='%1.2f%%');

plt.show();