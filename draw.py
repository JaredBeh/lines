from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    
    #check that line goes left to right
    if(x0>x1):
        x0,x1 = x1,x0
        y0,y1 = y1,y0

    m = (y1-y0)/(x1-x0)

    #octant 2
    if (m > 1):
        x0,y0,x1,y1 = y0,x0,y1,x1
        x, y = x0, y0
        A = 2*(y1 - y0)
        B = -(x1 - x0)
        d = A + B
        B *= 2
        while (x <= x1):
            plot(screen,color,y,x)
            if (d > 0):
                y+=1
                d+=B
            x+=1
            d+=A
        
        
    #octant 1
    elif(m >= 0):
        x, y = x0, y0
        A = 2*(y1 - y0)
        B = -(x1 - x0)
        d = A + B
        B *= 2
        while (x <= x1):
            plot(screen,color,x,y)
            if (d > 0):
                y+=1
                d+=B
            x+=1
            d+=A

    
