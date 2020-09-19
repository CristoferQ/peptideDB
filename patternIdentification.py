import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ruta = "../peptideDB/peptide_sequences/embedding_encoding/"
archivo = "AntiHIV.npz"

data = np.load(ruta+archivo, allow_pickle=True)
lst = data.files
a = []
ite = 0
for item in lst:
    #print(item)
    #print(data[item])
    a.append(data[item].tolist())
    #print (a['avg']) #(a['pooled']) no se ocupara aun

distances = []

for i in a:
    for j in a:        
        distances.append(np.sum(np.abs(i['avg']-j['avg'])))
    

df = pd.DataFrame(distances)
print(df)



x = df
hist, bins = np.histogram(x, bins=50)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)

print(Q1)
print(Q3)