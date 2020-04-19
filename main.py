import random
import time
import matplotlib.pyplot as plt

def evolve(world, h, w):
    new_world = [[0 for i in range(w)] for j in range(h)]
    #loop through all pxiels
    for i in range(0,h):
        for j in range(0,w):
            alive=0
            #check pixel's neighbours for alive pixels
            for yd in range(i-1,i+2):
                for xd in range(j-1,j+2):
                    if yd<0 : yd=0
                    if yd>=h : yd=h-1
                    if xd<0 : xd=0
                    if xd>=w : xd=w-1
                    if(yd==i and xd==j):continue
                    if world[yd][xd]:alive+=1
            if world[i][j]:
                if alive<2 or alive>3 :new_world[i][j]=0
                else:new_world[i][j]=1
            else:
                if alive==3: new_world[i][j]=1
    for i in range(0,h):
        for j in range(0,w):
            world[i][j]=new_world[i][j]

def draw(world,im):
    im.set_data(world)
    plt.pause(0.01)

def main():
    
    #Define world dimensions
    w=50
    h=50
    
    #initiate world
    world = [[0 for i in range(w)] for j in range(h)]

    #randomize world initiate state 
    random.seed(time.time())
    for i in range(h):
        for j in range(w):
            world[i][j]= 0 if random.random()>0.1 else 1 

    #initiate plotter
    im=plt.imshow(world,cmap='gray')

    #evolution and draw loop
    while(True):
        draw(world,im)
        evolve(world,h,w)
        time.sleep(0.1)

if __name__=="__main__":
    main()
