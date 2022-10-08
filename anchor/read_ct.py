import numpy as np
import nrrd

# Some sample numpy data
# data = np.zeros((5,4,3,2))
filename = "data/raw/0522c0012/img.nrrd"

# Read the data back from file
readdata, header = nrrd.read(filename)
print(readdata.shape)
print(header)
