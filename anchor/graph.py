import csv
import matplotlib.pyplot as plt
import numpy as np

epoch = []

for i in range(30):
    epoch.append(i)

brainstem = []
eyeL = []
eyeR = []
mandible = []
spine = []
tmjl = []
tmjr = []
trachea = []

anchor = [
    "Brain Stem.nrrd",  # 2
    "Eye-L.nrrd",  # 6
    "Eye-R.nrrd",  # 7
    "Mandible.nrrd",  # 12
    "Spinal Cord.nrrd",  # 21
    "TMJL.nrrd",  # 26
    "TMJR.nrrd",  # 27
    "Trachea.nrrd",  # 28
]
# opening the CSV file
with open("csvs/50 epoch/new_data_anchor.csv", mode="r") as file:

    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        # print(lines)
        brainstem.append(lines[1])
        eyeL.append(lines[2])
        eyeR.append(lines[3])
        mandible.append(lines[4])
        spine.append(lines[5])
        tmjl.append(lines[6])
        tmjr.append(lines[7])
        trachea.append(lines[8])

brainstem_f = [float(i) for i in brainstem]
eyeL_f = [float(i) for i in eyeL]
eyeR_f = [float(i) for i in eyeR]
mandible_f = [float(i) for i in mandible]
spine_f = [float(i) for i in spine]
tmjl_f = [float(i) for i in tmjl]
tmjr_f = [float(i) for i in tmjr]
trachea_f = [float(i) for i in trachea]

plt.plot(brainstem_f, label="brainstem_f")
plt.plot(eyeL_f, label="eyeL_f")
plt.plot(eyeR_f, label="eyeR_f")  # Plot the chart
plt.plot(mandible_f, label="mandible_f")  # Plot the chart
plt.plot(spine_f, label="spine_f")
plt.plot(tmjl_f, label="tmjl_f")
plt.plot(tmjr_f, label="tmjr_f")
plt.plot(trachea_f, label="trachea_f")

leg = plt.legend(loc="upper left")

plt.show()
