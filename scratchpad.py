import numpy as np

a = np.array([2,100,1])
b = np.array([3,100,1])



max = 0
choice = 0
for i in range(a.size) :
    draw = np.random.beta(a[i], b[i], 1)
    print(draw)
    if draw > max:
        max = draw
        choice = i
print(choice)



me = 123

data = np.empty([0,6], dtype=int)
newrow = np.array([1, 123, 2, 0, 124, 2], dtype=int)
data = np.vstack([data, newrow])
newrow = np.array([1, 124, 2, 0, 124, 2], dtype=int)
data = np.vstack([data, newrow])
newrow = np.array([1, 123, 3, 1, 124, 2], dtype=int)
data = np.vstack([data, newrow])
newrow = np.array([1, 123, 3, 1, 124, 2], dtype=int)
data = np.vstack([data, newrow])
newrow = np.array([1, 123, 2, 1, 124, 2], dtype=int)
data = np.vstack([data, newrow])


sub = data[data[:,1] == me]     # select my rows
sub = sub[sub[:,3] == 1]        # select successes

a = np.zeros(11)
for i in range(a.size):
    a[i] = np.sum(sub[sub[:,2] == i][:,3])
    
    
            
        # 0: Round
        # 1: Agent ID
        # 2: Who offered?
        # 3: The offer 0-10
        # 4: The response 0-1
        # 5: The partner
        # 6: The profit (= #3*#4)