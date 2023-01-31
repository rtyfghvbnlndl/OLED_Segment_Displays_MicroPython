from machine import Pin, I2C
import ssd1306
import time


class num(object):
    def __init__(self,display):
        self.display=display
        self.px=0
        self.pp=1

    def rect(self,x0,y0,x1,y1,col):
        for x in range(x0-1,x1):
            for y in range (y0-1,y1):
                self.display.pixel(x,y,col)

    def num(self,lis):
        for item in lis:
            if item==1:
                self.rect(16, 1, 22, 32, 1)
            if item==2:
                self.rect(16, 1, 64, 6, 1)
            if item==3:
                self.rect(16, 26, 64, 32, 1)
            if item==4:
                self.rect(61, 1, 67, 32, 1)
            if item==5:
                self.rect(64, 1, 112, 6, 1)
            if item==6:
                self.rect(64, 26, 112, 64, 1)
            if item==7:
                self.rect(106, 1, 112, 64, 1)
            if item==8:
                self.rect(16, 13, 64, 19, 1)
            if item==9:
                self.rect(64, 13, 112, 19, 1)
    
    def move(self):
        #防止烧屏
        if self.px==14:
            self.pp=-1
        elif self.px==-14:
            self.pp=1
        self.px+=self.pp
        self.display.scroll(self.px,0)

    def show(self,num):
        #清空
        self.display.fill(0)
        #模拟数码管大数字
        a=[[1,2,3,5,6,7],[8,9],[1,2,4,6,7],[1,2,4,5,7],[3,4,2,5],[1,3,4,5,7],[1,3,4,5,6,7],[1,2,5],[1,2,3,4,5,6,7],[1,2,3,4,5,7]]
        self.num(a[num])
        self.move()
        self.display.show()


i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)

display.text('MicroPython', 25, 13, 1)
display.show()
time.sleep(0.3)

p1=num(display)
px,pp=0,1
while True:
    for i in range(10):
        p1.show(i)
        time.sleep(0.2)