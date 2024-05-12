import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

ChestPainType = {"ASY":496,"ATA":173,"NAP":203,"TA":46}
RestingECG = {"Normal":552,"LVH":188,"ST":178}
age = [40,49,37,48,54,39,45,54,37,48,37,58,39,49,42,54,38,43,60,36,43,44,49,44,40]
cholesterolLevel=[289,180,283,214,195,339,237,208,207,284,211,164,204,234,211,273,196,201,248,267,223,184,201,288,215]
restingHeartRate = [140,160,130,138,150,120,130,110,140,120,130,136,120,140,115,120,110,120,100,120,100,120,124,150,130]

#title
root = tk.Tk()
root.title("Health Dashboard")

#side frame
sideFrame = tk.Frame(root, bg="purple")
sideFrame.pack(side=tk.LEFT, fill=tk.Y)

label = tk.Label(sideFrame, text="Health Dashboard", font=("Times", 16), fg="white", bg="purple")
label.pack()

#chart frame
chartFrame = tk.Frame(root)
chartFrame.pack(side=tk.LEFT)

#upper chart frame
upperChartFrame = tk.Frame(chartFrame)
upperChartFrame.pack()

#bar
plt.figure(figsize=(6,4))
plt.bar(ChestPainType.keys(), ChestPainType.values())
plt.title("Chest Paint Type Frequency")
plt.xlabel("Chest Paint Type")
plt.ylabel("Frequency")
barCanvas = FigureCanvasTkAgg(plt.gcf(), master=upperChartFrame)
barCanvas.draw()
barCanvas.get_tk_widget().pack(side=tk.LEFT)

#scatter
plt.figure(figsize=(6,4))
plt.scatter(age, cholesterolLevel)
plt.title("Relation between Age and Cholesterol Level")
plt.xlabel("Age")
plt.ylabel("Cholesterol Level")
scatterCanvas = FigureCanvasTkAgg(plt.gcf(), master=upperChartFrame)
scatterCanvas.draw()
scatterCanvas.get_tk_widget().pack(side=tk.LEFT)

#lower chart frame
lowerChartFrame = tk.Frame(chartFrame)
lowerChartFrame.pack()

#pie
plt.figure(figsize=(6,4))
plt.pie(RestingECG.values(), labels=RestingECG.keys(), autopct='%1.1f%%')
plt.title("Resting ECG")
pieCanvas = FigureCanvasTkAgg(plt.gcf(), master=lowerChartFrame)
pieCanvas.draw()
pieCanvas.get_tk_widget().pack(side=tk.LEFT)

#box
plt.figure(figsize=(6,4))
plt.boxplot(restingHeartRate)
plt.title("Resting Heart Rate")
boxCanvas = FigureCanvasTkAgg(plt.gcf(), master=lowerChartFrame)
boxCanvas.draw()
boxCanvas.get_tk_widget().pack(side=tk.LEFT)

#main loop
root.mainloop()