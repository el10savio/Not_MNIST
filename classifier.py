from PIL import Image
import numpy, os
from sklearn.neighbors import KNeighborsClassifier

path="Dataset Path"
Xlist=[]
Ylist=[]

for directory in os.listdir(path):
	for file in os.listdir(path+"/"+directory):
		img=Image.open(path+"/"+directory+"/"+file)
		featurevector=numpy.array(img).flatten()
		Xlist.append(featurevector)
		Ylist.append(directory)

Xtest=Xlist[:20]
Ytest=Ylist[:20]

knn = KNeighborsClassifier(n_neighbors=1)
print('KNN score: %f' % (knn.fit(Xlist, Ylist).score(Xtest, Ytest)))

path_test=raw_input("Image Path:")

print knn.predict(numpy.array(Image.open(path_test)).flatten())

