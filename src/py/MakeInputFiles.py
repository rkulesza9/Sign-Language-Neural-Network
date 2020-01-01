### IMPORTS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv

### PARAMATERS
INPUT_FILE = "../input/sign-mnist/sign_mnist_test.csv"
DF = None
X = None
LABELS = None
OUTPUT_DIR = '../input/images/'
N = 100

### LOAD INPUT DATA
DF = pd.read_csv(INPUT_FILE)
LABELS = DF.drop("label",1).columns
X = np.array(DF.drop("label",1))
X = X.reshape(len(X),28,28)

### SHOW IMAGE
for x in range(0,N):
    img = X[x]
    img.reshape(28,28,1)
    img_file = OUTPUT_DIR+'img_'+str(x)+'.jpg'
    csv_file = OUTPUT_DIR+'csv_'+str(x)+'.csv'
    plt.imsave(img_file, img, cmap='gray')
    with open(csv_file, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(LABELS)
        wr.writerow(img.reshape(28*28))
    print(img_file," was created successfully!")
    print(csv_file," was created successfully!")
