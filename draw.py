from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    
    dy = y1 - y0
    dx = x1 - x0
    rotated = False
    flipped = False
    #rotate line so the slope is between -1 and 1
    if( abs(dy) > abs(dx) ):
        x0,y0 = y0,x0
        x1,y1 = y1,x1
        dx,dy = dy,dx
        rotated = True

    #check that line goes left to right
    if(dx < 0):
        x0,x1 = x1,x0
        y0,y1 = y1,y0
        dx = -1 * dx
        dy = -1 * dy

    #flip line so the slope is between 0 and 1
    if(dy < 0):
        y0,y1 = -1 * y0,-1 * y1
        dy = -1 * dy
        flipped = True
        

    x,y = x0,y0
    A = 2 * dy
    B = -1 * dx
    d = A + B
    B *= 2
    while(x <= x1):
        if(rotated and flipped):
            plot(screen,color,-1 * y,x)
        elif(rotated):
            plot(screen,color,y,x)
        elif(flipped):
            plot(screen,color,x,-1 * y)
        else:
            plot(screen,color,x,y)
        if(d>0):
            y+=1
            d+=B
        x+=1
        d+=A
