import matplotlib.pyplot as plt
%matplotlib inline
import os

def plot(x, y, legend, fig = 1):
    plt.figure(num = fig)
    plt.plot(x,y)
    plt.title('performance')
    plt.legend(legend)
    plt.xlabel("episodes")
    plt.ylabel("total rewards")
    plt.show()
    
def readResult(filename):
    x = []
    y = []
    dir = os.path.join(os.getcwd(), "results", filename)
    f = open(dir, 'r')
    lines = f.readlines()
    episode_size = int(lines[0])
    for i,l in enumerate(lines[1:]):
        y.append(float(l[0:-1]))
        x.append((i + 1) * episode_size)
    return x,y

def mean(y):
    meany = []
    sum = 0
    for i, v in enumerate(y):
        sum += v
        meany.append(sum / (i + 1))
    return meany
x, y = readResult("")
my = mean(y)
plot(x, y,["withOnehotAndNormalize"], fig = 2)
plot(x,my, ["withOnehotAndNormalize","mean"], fig = 3)
