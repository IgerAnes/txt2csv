from cProfile import label
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# it will read excel file as a dataframe format
excelData = pd.read_excel(r"C:\Users\z5259\OneDrive\2022_論文撰寫檔案夾\network-test-v2\total_avg_latency.xlsx",
                          usecols=["5G SA", "5G NSA"])

latencyArray = excelData.to_numpy()

# ----------------------------------------- plot 5G SA latency CDF -----------------------------------------------
latency5GSA = latencyArray[:,0]
max5GSA = np.max(latency5GSA)

# plot cdf as continuous distrubute
x = latency5GSA
hist, bin_edge = np.histogram(x, bins=20)
cdf = np.cumsum(hist/sum(hist))

cdf = np.insert(cdf, 0, 0)

print("[--------------5G SA-----------------]")
cdfDataArray = np.stack((cdf, bin_edge), axis=1)
print(cdfDataArray)

plt.grid(color='#E3E8E5')
barWidth = (bin_edge[1] - bin_edge[0])*0.8
plt.bar(bin_edge[1:], hist/sum(hist), width=barWidth, color='#D9D7D4', label="PDF")

# plt.plot(bin_edge[0:], cdf, color='#FFBD2E', label="cdf")
plt.plot(bin_edge[0:], cdf, label="CDF")

# dx = 1
# xrange = np.arange(bin_edge[0], max5GSA, dx)

plt.xlabel("Latency (ms)")
plt.ylabel("Probability")
plt.xlim([bin_edge[0], max5GSA])
# plt.xticks(xrange)
plt.ylim([0.9, 1])
plt.title("CDF of 5G SA Latency")
# plt.show()
plt.savefig("5gsa-cdf-plot-09-10.png")


# ----------------------------------------- plot 5G NSA latency CDF -----------------------------------------------
latency5GNSA = latencyArray[:,1]
latency5GNSA = latency5GNSA[~np.isnan(latency5GNSA)]
max5GNSA = np.max(latency5GNSA)

# plot cdf as continuous distrubute
x = latency5GNSA
hist, bin_edge = np.histogram(x, bins=50)
cdf = np.cumsum(hist/sum(hist))

cdf = np.insert(cdf, 0, 0)
print("[--------------5G NSA-----------------]")
cdfDataArray = np.stack((cdf, bin_edge), axis=1)
print(cdfDataArray)

plt.grid(color='#E3E8E5')
barWidth = (bin_edge[1] - bin_edge[0])*0.8
plt.bar(bin_edge[1:], hist/sum(hist), width=barWidth, color='#D9D7D4', label="PDF")

plt.plot(bin_edge[0:], cdf, label="CDF")

plt.xlabel("Latency (ms)")
plt.ylabel("Probability")
plt.xlim([bin_edge[0], 100])
plt.ylim([0.9, 1])
plt.title("CDF of 5G NSA Latency")
# plt.show()
plt.savefig("5gnsa-cdf-plot-09-10.png")