import math as m
import random as r
import pyautogui
g = pyautogui

def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

def intersect(points):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def draw_circle(rx, ry):

    a = 0

    cx, cy = g.position()
    g.move(rx, 0)
    pyautogui.mouseDown()

    while a < m.pi * 2.1:
    
    
        x = cx + m.cos(a) * rx;
        y = cy + m.sin(a) * ry;

        g.moveTo(x, y)

        a += 0.15

    pyautogui.mouseUp()

def draw_rect(x, y):
    g.drag(x, 0, x/300)
    g.drag(0, y, y/300)
    g.drag(-x, 0, x/300)
    g.drag(0, -y, y/300)
    

def draw_shape(points):
    g.moveTo(points[0][0], points[0][1])

    for i in range(1, len(points)):
        g.dragTo(points[i][0], points[i][1], 0.1)
    
    g.dragTo(points[0][0], points[0][1], 0.1)

x0,y0 = g.position()


draw_circle(150,150)

