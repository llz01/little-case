#coding=utf8
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt

class Drawing():
    def __init__(self,array1,array2,array3):
        self.array1 = array1;
        self.array2 = array2;
        self.array3 = array3;
        
    def draw(self):
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        fig = plt.figure(u'三维井眼轨迹展示')
        fig.suptitle(u'三维井眼轨迹展示')
        drawing = fig.add_subplot(111, projection='3d')
        x = self.array1
        y = self.array2
        z = self.array3
        drawing.plot(x, y, z, label=u'井眼轨迹曲线')
        drawing.set_xlabel(u'X轴')
        drawing.set_ylabel(u'Y轴')
        drawing.set_zlabel(u'Z轴')
        drawing.legend()
        plt.show()
      
def readFile():
    f = open('data.txt','rb')
    data = f.readlines()
    f.close()
    for line in data:
        list = line.split()
    x = [float(x) for x in list[::3] ]
    y = [float(y) for y in list[1::3]]
    z = [float(z) for z in list[2::3]]
    return x,y,z

x,y,z = readFile()
Drawing(x,y,z).draw()
