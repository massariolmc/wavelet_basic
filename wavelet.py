import pywt
import pandas as pd
import os
import matplotlib.pyplot as plt

# (cA, cD) = pywt.dwt([1,2,3,4,5,6], 'db1')
# print (cA)
# print (cD)

print("\n")
arq = os.path.join(os.getcwd(),'ETo_Ventura_.xlsx')
df = pd.read_excel(arq, sheet_name='Plan1')

col = df['Eto – mm/d'].values.tolist()
#print(col[:20])
#print("tipo: ",type(col))

cA, cD = pywt.dwt(col, 'db1')
y = pywt.idwt(cA,cD,'db1')

coeffs = pywt.wavedec(col, 'db1', level=2)
cA2, cD2, cD1 = coeffs

fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, figsize=(20,10))

ax1.set(title="Dados Originais", xlabel="Amostras", ylabel="Eto - mm/d")
ax1.plot(col,color='r')

ax2.set(title="Coeficientes de aproximação", xlabel="Amostras", ylabel="cA")
ax2.plot(cA,color='g')

ax3.set(title="Detalhes dos coeficientes", xlabel="Amostras", ylabel="cD")
ax3.plot(cD,color='g')

ax4.set(title="Reconstrução das Amostras", xlabel="Amostras", ylabel="Eto - mm/d")
ax4.plot(y,color='r')

plt.tight_layout()
plt.show()




# plt.figure(figsize=(30,20))

# plt.subplot(4,1,1)
# plt.plot(col,color='r')
# plt.title('Dados Originais')#Titulod o gráfico
# plt.xlabel('Amostras')#Nome do eixo X
# plt.ylabel('Eto - mm/d')# nome do eixo y

# plt.subplot(4,1,2)
# plt.plot(cA,color='g')
# plt.title('Coeficientes de aproximação')#Titulod o gráfico
# plt.xlabel('Amostras')#Nome do eixo X
# plt.ylabel('cA')# nome do eixo y

# plt.subplot(4,1,3)
# plt.plot(cA,color='b')
# plt.title('Detalhes dos coeficientes')#Titulod o gráfico
# plt.xlabel('Amostras')#Nome do eixo X
# plt.ylabel('cD')# nome do eixo y

# plt.subplot(4,1,4)
# plt.plot(y,color='r')
# plt.title('Reconstrução das Amostras')#Titulod o gráfico
# plt.xlabel('Amostras')#Nome do eixo X
# plt.ylabel('Eto - mm/d')# nome do eixo y

# #plt.tight_layout()
# plt.show()