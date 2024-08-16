import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data= pd.read_excel("F:\Progress\Progress - 2\Climate Maps\SSP5.xlsx")

Cl = data["Classification"].tolist()
TN = data["TN"].tolist()
TL = data["TL"].tolist()

barWidth = 0.3
fig = plt.subplots(figsize =(10, 4))

br1 = np.arange(len(Cl))
br2 = [x + barWidth for x in br1]

plt.bar(br1, TN, color ='navy', width = barWidth,
		edgecolor ='grey', label ='TB/TN')
plt.bar(br2, TL, color ='dodgerblue', width = barWidth,
		edgecolor ='grey', label ='TB/TL')

plt.ylabel('Percentage Area Change(%)', fontsize = 18)
plt.xlabel('Classification', fontsize = 18)
plt.xticks([r + barWidth for r in range(len(Cl))],
		Cl, fontsize = 18)

plt.legend(fontsize = 20)
plt.title("SSP5-8.5",fontsize = 20, fontweight="bold")
plt.grid(True)
plt.savefig("F:\Progress\Progress - 2\Climate Maps\Bar chart\SSP585.png", dpi=500, bbox_inches='tight')
plt.show()
