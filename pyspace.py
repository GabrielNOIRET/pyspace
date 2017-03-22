import tkinter
from random import randint

class Canvas3d(tkinter.Canvas):
    def __init__(self, master, persX, persY, width = None, height = None):
        tkinter.Canvas.__init__(self, master, width = width, height = height)
        self.master = master
        self.persX = persX
        self.persY = persY
        if width != None:
            self.width = width
        else:
            self.width = self.winfo_screenwidth()
        if height != None:
            self.height = height
        else:
            self.height = self.winfo_screenheight()
        self.children3d = []
    
    def update_all(self):
        """recreate all children widgets"""
        for i in range(len(self.children3d)):
            self.children3d[i].update()

class Terrain:
    def __init__(self, canvas3d, x, y, z, lenX, lenY, lenZ, pointRatio = 50, maxHeight = 200, minHeight = -200, color = "black"):
        self.parent3d = canvas3d
        self.x = x
        self.y = y
        self.z = z
        self.lenX = lenX
        self.lenY = lenY
        self.lenZ = lenZ
        self.maxHeight = min(self.lenY, maxHeight)
        self.minHeight = minHeight
        self.pointRatio = pointRatio
        self.color = color
        self.parent3d.children3d.append(self)
        self.id = []
        self.points = []
        
    def generate(self):
        if len(self.points) == 0:
            for x in range(0, self.lenX, self.pointRatio):
                for z in range(0, self.lenZ, self.pointRatio):
                    newHeight = randint(self.minHeight, self.maxHeight)
                    self.points.append([self.x + x + ((self.parent3d.persX - self.x - x) * (self.z + z) / self.parent3d.width), self.y + ((self.parent3d.persY - self.y - newHeight) * (self.z + z) / self.parent3d.height), newHeight])
      
    def create(self):
        if len(self.points) > 0:
            i = 0
            for x in range(0, self.lenX, self.pointRatio):
                for z in range(0, self.lenZ, self.pointRatio):
                    if z > 0:
                        self.id.append(self.parent3d.create_line(self.points[i][0], self.points[i][1], self.points[i - 1][0], self.points[i - 1][1], fill = self.color))
                    if x > 0:
                        self.id.append(self.parent3d.create_line(self.points[i][0], self.points[i][1], self.points[i - int(self.lenZ / self.pointRatio)][0], self.points[i - int(self.lenZ / self.pointRatio)][1], fill = self.color))
                    i += 1

       
root = tkinter.Tk()
canvas = Canvas3d(root, 400, 250, width = root.winfo_screenwidth(), height = root.winfo_screenheight())
canvas.pack()
terrain = Terrain(canvas, -canvas.width / 2, 790, 0, canvas.width * 2, canvas.height, 800, maxHeight=100, minHeight=0)
terrain.generate()
terrain.create()
