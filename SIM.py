import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("berlin52.csv")

X = df.iloc[:,0:1].values
Y = df.iloc[:,1:2].values

class Coordinate:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    @staticmethod
    def get_distance(a,b):
        return np.sqrt(np.abs(a.x-b.x)+np.abs(a.y-b.y))

    @staticmethod
    def get_total_distance(coords):
        dist=0
        for first,second in zip(coords[:-1],coords[1:]):
            dist+=Coordinate.get_distance(first,second)
        dist+=Coordinate.get_distance(coords[0],coords[-1])
        return dist*12

if __name__ == '__main__':
    coords=[]
    costs=[]
    t=[]
    start_pos = []
    for i in range(len(X)):
        coords.append(Coordinate(int(X[i]),int(Y[i])))
        start_pos.append(Coordinate(int(X[i]),int(Y[i])))

    fig=plt.figure(figsize=(7,5))

    for first,second in zip(coords[:-1],coords[1:]):
        plt.plot([first.x,second.x],[first.y,second.y],"grey")
    plt.plot([coords[0].x,coords[-1].x],[coords[0].y,coords[-1].y],"black")

    for c in coords:
        plt.plot(c.x,c.y,"r.")
    plt.show()

    T=10000
    factor=0.98
    cost0=Coordinate.get_total_distance(coords)
    print(cost0)
    for i in range(450): #ITERATION
        print ("Iter:",i,"Cost:", cost0)
        costs.append(cost0)
        t.append(T)
        T=T*factor

        for j in range(150):
            r1,r2=np.random.randint(0,52,size=2)
            temp=coords[r1]
            coords[r1]=coords[r2]
            coords[r2]=temp
            cost1=Coordinate.get_total_distance(coords)
            if cost1<cost0:
                cost0=cost1
            else:
                r=np.random.uniform()
                if r<np.exp((cost0-cost1)/T):
                    cost0=cost1
                else:
                    temp=coords[r1]
                    coords[r1]=coords[r2]
                    coords[r2]=temp

    print("Final Cost: ",Coordinate.get_total_distance(coords))

    for first,second in zip(start_pos[:-1],start_pos[1:]):
        plt.plot([first.x,second.x],[first.y,second.y],"grey")
    plt.plot([start_pos[0].x,start_pos[-1].x],[start_pos[0].y,start_pos[-1].y],"grey")

    for first,second in zip(coords[:-1],coords[1:]):
        plt.plot([first.x,second.x],[first.y,second.y],"red")
    plt.plot([coords[0].x,coords[-1].x],[coords[0].y,coords[-1].y],"red")

    for c in coords:
        plt.plot(c.x,c.y,".", c="black")
    plt.show()

    for first,second in zip(coords[:-1],coords[1:]):
        plt.plot([first.x,second.x],[first.y,second.y],"purple")
    plt.plot([coords[0].x,coords[-1].x],[coords[0].y,coords[-1].y],"black")

    for c in coords:
        plt.plot(c.x,c.y,".", c="orange")
    plt.show()

    plt.plot(costs,"black")
    plt.show()