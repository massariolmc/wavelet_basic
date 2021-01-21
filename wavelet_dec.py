#python -m pip install --upgrade pip
#pip install pandas
#pip install xlrd -> é uma extensão do pandas para ler xlsx
#pip install openpyxl
#pip install matplotlib
#pip install PyWavelets
#apt-get install liblzma-dev


import pywt
import pandas as pd
import os
import matplotlib.pyplot as plt


print("\n")
arq = os.path.join(os.getcwd(),'ETo_Ventura_.xls')
df = pd.read_excel(arq, sheet_name='Plan1')

col = df['Eto – mm/d'].values.tolist()

coeffs = pywt.wavedec(col, 'db1', level=5)
cA5, cD5, cD4,cD3, cD2,cD1 = coeffs
y = pywt.waverec(coeffs,'db1')

#--------------------------------
fig, original = plt.subplots(nrows=1, ncols=1, figsize=(20,10))

original.set(title="Dados Originais", xlabel="Amostras", ylabel="Eto - mm/d")
original.plot(col,color='r')

plt.tight_layout()
plt.savefig('original.png',dpi=100)
#plt.show()
#--------------------------------

#--------------------------------
fig, (dec1, dec2, dec3, dec4, dec5) = plt.subplots(nrows=5, ncols=1, figsize=(20,10))

dec1.set(title="1º Decomposição", xlabel="Amostras", ylabel="cD1")
dec1.plot(cD1,color='b')

dec2.set(title="2º Decomposição", xlabel="Amostras", ylabel="cD2")
dec2.plot(cD2,color='g')

dec3.set(title="3º Decomposição", xlabel="Amostras", ylabel="cD3")
dec3.plot(cD3,color='y')

dec4.set(title="4º Decomposição", xlabel="Amostras", ylabel="cD4")
dec4.plot(cD4,color='c')

dec5.set(title="5º Decomposição", xlabel="Amostras", ylabel="cD5")
dec5.plot(cD5,color='m')

plt.tight_layout()
plt.savefig('decomposições.png',dpi=100)
#plt.show()
#--------------------------------

#--------------------------------
fig, cA5_af = plt.subplots(nrows=1, ncols=1, figsize=(20,10))

cA5_af.set(title="Sinal após 5 decomposições", xlabel="Amostras", ylabel="cA5")
cA5_af.plot(cA5,color='m')
plt.tight_layout()
plt.savefig('Sinal_apos_5_dec.png',dpi=100)
#plt.show()

#--------------------------------
fig, rec = plt.subplots(nrows=1, ncols=1, figsize=(20,10))

rec.set(title="Sinal reconstruído", xlabel="Amostras", ylabel="Eto - mm/d")
rec.plot(y,color='r')

plt.tight_layout()
plt.savefig('Wavelet_Inversa.png',dpi=100)
#plt.show()
#--------------------------------
