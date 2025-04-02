from sklearn import neighbors
import time

X = [ [2.0,1.5,1.0], [1.0,1.0,0.5], [1.0,3.0,1.5], [0.8,2.2,0.7], [3.0,1.0,0.2], [0.4,2.0,1.7], [1.2,1.2,1.5]  ]

Y = [ 1, 0, 1, 0, 1, 1, 1 ]


clf = neighbors.KNeighborsClassifier(n_neighbors=5) #k =1, 3, 5, 7
clf.fit(X, Y)


# wall time   = time.time()
# CPU time = time.process_time()

initial_wall_time = time.time()
initial_cpu_time = time.process_time()

for i in range(0,10):
    y_ind = clf.predict([[0.9, 1.1, 0.5]])

final_cpu_time = time.process_time()
final_wall_time = time.time()

total_cpu_time = final_cpu_time - initial_cpu_time
total_wall_time = final_wall_time - initial_wall_time

print("Total CPU time = %f miliseconds" %(total_cpu_time*1000))
print("Total Wall time = %f miliseconds" %(total_wall_time*1000))

#print(clf.predict([[0.9, 1.1, 0.5]]))
#print(clf.predict_proba([[0.9, 1.1, 0.5]]))
