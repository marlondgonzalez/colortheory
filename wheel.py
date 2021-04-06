import math
import matplotlib.colors as libcolors

class Color():
    allColors = libcolors.cnames
    def __init__(self, color):
        self.color = color.lower()
        self.checkColor()
        self.hex = Color.allColors[self.color]
        self.rgb = libcolors.to_rgb(self.hex)

    def checkColor(self):
        if self.color not in Color.allColors:
            raise ValueError("Color Not Recognized, please check spelling")
        else:
            return 0

class Wheel():
    def __init__(self):
        self.MinRange = 0
        self.MaxRange = 360
        self.IntervalValue = 60
        self.HalfValue = 180
        self.Radius = 1

    def setDirection(self, angle):
        if self.MinRange <= angle and angle < self.MaxRange:
            self.Angle = angle
        elif angle == self.MaxRange:
            self.Angle = self.MinRange
        else:
            raise ValueError("Angle Incorrect")

    def setRadius(self, distance):
        self.Radius = distance

    def getComplement(self):
        if self.Angle <= self.HalfValue:
            return self.Angle + self.HalfValue
        else:
            return self.Angle - self.HalfValue

    def colorMap(self):
        position = self.Angle / self.IntervalValue
        intervalIndex = self.Angle // self.IntervalValue
        if intervalIndex % 2 == 0:
            delta = position - intervalIndex
        else:
            delta = 1 - (position - intervalIndex)
        if intervalIndex == 0:
            rgbTuple = (1, 0, delta)
        elif intervalIndex == 1:
            rgbTuple = (delta, 0, 1)
        elif intervalIndex == 2:
            rgbTuple = (0, delta, 1)
        elif intervalIndex == 3:
            rgbTuple = (0, 1, delta)
        elif intervalIndex == 4:
            rgbTuple = (delta, 1, 0)
        elif intervalIndex == 5:
            rgbTuple = (1, delta, 0)
        return libcolors.rgb2hex(rgbTuple)

w = Wheel()
w.setDirection(88)
print(w.colorMap())
cw = Wheel()
cw.setDirection(w.getComplement())
print(cw.colorMap())
