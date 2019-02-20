import urllib
from urllib import request
import numpy as np

fname = 'https://stepic.org/media/attachments/lesson/16462/boston_houses.csv'  # read file name from stdin
f = urllib.request.urlopen(fname)  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with
y = data[:,0].reshape((data.shape[0], 1))
x = np.hstack((np.ones((data.shape[0], 1)), data[:,1:]))
bhat = (np.linalg.inv(x.T.dot(x))).dot(x.T.dot(y)).flatten()
print(" ".join(map(str, bhat)))