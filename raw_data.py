import pyabf  # abf file reading
import pandas as pd
import matplotlib.pyplot as plt

file_names = {'WTM3':'2024_11_12_0003.abf',
              'Bckdk':'2024_11_27_0017.abf',
              'USP7': '2024_12_02_0009.abf'}
sheet_names = {'WTM3': 'WT M3 C3 003.abf',
               'Bckdk': 'Bckdk KO M11 C3 017.abf ',
               'USP7': 'Usp7 Het M13 009.abf'}

consider = 'WTM3'
data = pd.read_excel('AP_traces.xlsx', sheet_name=sheet_names[consider],
                     usecols='B:O',  header=0, skiprows=[1])
plt.plot(data['Time (ms)'], data['15 pA'])
plt.plot(data['Time (ms)'], data['25 pA'])
plt.plot(data['Time (ms)'], data['35 pA'])
plt.plot(data['Time (ms)'], data['45 pA'])

plt.show()


# data1 = pyabf.ABF('2024_11_12_0003.abf')
# data1.setSweep(3)
# plt.plot(data1.sweepX, data1.sweepC); plt.show()  # time vs protocol
