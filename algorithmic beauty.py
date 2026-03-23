#pure plastic art
#by Katherina "Kate the Cursed" Jesek

#DEV BRANCH

import drawsvg as draw
import math
import random

def RGB(r,g,b): #DrawSVG library likes strings for some reason, so here's a
                #compatibility function that lets us do color math
    red_ch = r
    green_ch = g
    blue_ch = b
    color1 = ('rgb('+str(red_ch)+','+str(green_ch)+','+str(blue_ch)+')')
    return color1

def fibonacci(user_input): #Creates a list of Fibonacci sequence and
                            #returns the nth entry in the list
    fib_list = [0, 1, 1]
    for iterator in range(user_input):
        if iterator > 1:
            new_entry = fib_list[iterator]+fib_list[iterator-1]
            fib_list.append(new_entry)
    #print(fib_list) #debug print
    return fib_list[user_input]

def fibonacci_ratio(user_input): #Creates a list of Fibonacci sequence and
                                    #returns the entries for n-2, n-1, n
    fib_list = [0, 1, 1]
    for iterator in range(user_input):
        if iterator > 1:
            new_entry = fib_list[iterator]+fib_list[iterator-1]
            fib_list.append(new_entry)
    #print(fib_list) #debug print
    return fib_list[user_input-2], fib_list[user_input-1], fib_list[user_input]
        
def fibonacci_lines_vert(x1,x2,y1,y2,n,m,cnv): #left bound, right bound,
            #top bound, bottom bound, fibonacci number, mode (0 or 1), canvas
    acc_next_line = 0
    for i in range(n):
        if i >= 2:
            x,y,z = fibonacci_ratio(i)
            if m == 1: #quick flip to change the mode
                x=y
            path_1 = draw.Lines((x2-x1)/z*x, y1, (x2-x1)/z*x, y2,
                               stroke=color[1], stroke_width=stroke_large)
                                                        #Major dividing line
                                                            #in golden ratio
            cnv.append(path_1)
           
            if (x2-x1)/z*x > x1 and (x2-x1)/z*x < x2:
                #Determines the appropriate jumping off point for the next set
                acc_next_line_t = (x2-x1)/z*x
                if acc_next_line_t > acc_next_line:
                    acc_next_line = acc_next_line_t
    return acc_next_line

def fibonacci_lines_hor(x1,x2,y1,y2,n,m,cnv):
    acc_next_line = 0
    for i in range(n):
        if i >= 2:
            x,y,z = fibonacci_ratio(i)
            if m == 1:
                x=y
            path_1 = draw.Line(x1, (y2-y1)/z*x, x2, (y2-y1)/z*x,
                               stroke=color[1], stroke_width=stroke_large)
                                #Major dividing line in golden ratio
            cnv.append(path_1)
            
            if (y2-y1)/z*x > y1 and (y2-y1)/z*x < y2:
                #Determines the appropriate jumping off point for the next set
                acc_next_line_t = (y2-y1)/z*x
                if acc_next_line_t > acc_next_line:
                    acc_next_line = acc_next_line_t
    return acc_next_line

def mondrian_lines(x1,x2,y1,y2,recursions,cnv,fill_pattern): #Call vertical
                                #then horizontal twice for each recursion
    previousX = x1
    previousY = y1
    previousX2 = x2
    previousY2 = y2

    for i in range(recursions): #I popped off here this code is disgusting
        if i > 1:
            rect_2 = draw.Rectangle(previousX,previousY,abs(
                previousX2-previousX),abs(previousY2-previousY),
                fill=fill_pattern,stroke_width=stroke_large,
                stroke = 'white')
            cnv.append(rect_2)
        previousX = fibonacci_lines_vert(previousX,
                                         d_width*random.randint(0,1),
                                         previousY,
                                         d_height*random.randint(0,1),
                                         random.randint(4,7),
                                         random.randint(0,1),
                                         cnv)
        previousY = fibonacci_lines_hor(previousX2,
                                        d_width*random.randint(0,1),
                                        previousY,
                                        d_height*random.randint(0,1),
                                        random.randint(4,7),
                                        random.randint(0,1),
                                        cnv)
        previousX2 = fibonacci_lines_vert(previousX,
                                          d_width*random.randint(0,1),
                                          previousY,
                                          d_height*random.randint(0,1),
                                          random.randint(4,7),
                                          random.randint(0,1),
                                          cnv)
        previousY2 = fibonacci_lines_hor(previousX2,
                                         d_width*random.randint(0,1),
                                         previousY,
                                         d_height*random.randint(0,1),
                                         random.randint(4,7),
                                         random.randint(0,1),
                                         cnv)
        
def mondrian_angled(x1,x2,y1,y2,n,cnv,fill_pattern):
            
    mondrian_lines(x1,x2,y1,y2,n,cnv,fill_pattern)
    render.append(draw.Use(cnv,0,0,transform='rotate(42.5),scale(1.75),translate('+str(0)+','+str(-d_height/2)+')')) #Print the secondary canvas to the main canvas

def mondrian_straight(x1,x2,y1,y2,n,cnv,posX,posY,fill_pattern):
    mondrian_lines(x1,x2,y1,y2,n,cnv,fill_pattern)
    render.append(draw.Use(cnv,0,0,transform='rotate(0),scale(1),translate('+str(posX)+','+str(posY)+')'))

def draw_circles(cx,cy,r,cnv,scale_fac):
    circ_1_ol = draw.Circle(cx,cy,r+(d_avg/34),fill='black',stroke='none',stroke_width=stroke_large)
    circ_1 = draw.Circle(cx,cy,r,fill='black',stroke=color[1],stroke_width=stroke_large)
    cnv.append(circ_1)
    circ_2 = draw.Circle(cx,cy,int(r*scale_fac//1),fill='none',stroke=color[1],stroke_width=stroke_large,transform='rotate('+str(random.randint(1,360))+'),translate('+str(cx//random.randint(8,12))+','+str(0)+')')
    cnv.append(circ_2)

def draw_rect(x,y,sizeX,sizeY,cnv,fill_pattern):
    rect = draw.Rectangle(x,y,sizeX,sizeY,fill=fill_pattern,stroke=color[1],stroke_width=stroke_small)
    cnv.append(rect)

def rect_seq(x,y,sizeX,sizeY,cnv,n,dx,dy):
    for i in range(n):
        l_color = i*(255/n)
        draw_rect(x+(dx*i),y+(dy*i),sizeX,sizeY,cnv,RGB(l_color,l_color,l_color))

def rect_sequence_vert(n,f): #Sequence out some squares. This can probably be made more efficient
    a,b,c = fibonacci_ratio(f)
    rect_flag = random.randint(0,3)
    if rect_flag == 0:
        rect_seq(d_width/b,
                     d_height/b,
                     d_avg/c,
                     d_avg/c,
                     render,n,
                     0,
                     d_avg/b)
    elif rect_flag == 1:
        rect_seq(d_width/b,
                     d_height-(d_height/b)-d_avg/c,
                     d_avg/c,
                     d_avg/c,
                     render,n,
                     0,
                     -d_avg/b)
    elif rect_flag == 2:
        rect_seq(d_width-(d_width/b)-d_avg/c,
                     d_height-(d_height/b)-d_avg/c,
                     d_avg/c,
                     d_avg/c,
                     render,n,
                     0,
                     -d_avg/b)
    elif rect_flag == 3:
        rect_seq(d_width-(d_width/b)-d_avg/c,
                     d_height/b,
                     d_avg/c,
                     d_avg/c,
                     render,n,
                     0,
                     d_avg/b)

def rect_sequence_hor(n,f):
    a,b,c = fibonacci_ratio(f)
    rect_flag = random.randint(0,3)
    if rect_flag == 0:
        rect_seq(d_width/b,
                     d_height/b,
                     d_avg/c,
                     d_avg/c,
                     render,n,
                     d_avg/b,
                     0)
    elif rect_flag == 1:
        rect_seq(d_width/b,
                     d_height-(d_height/b)-d_avg/c,
                     d_avg/c,
                     d_avg/c,
                     render,n,
                     d_avg/b,
                     0)
    elif rect_flag == 2:
        rect_seq(d_width-(d_width/b)-d_avg/c,
                     d_height-(d_height/b)-d_avg/c,
                     d_avg/c,
                     d_avg/c,
                     render,n,
                     -d_avg/b,
                     0)
    elif rect_flag == 3:
        rect_seq(d_width-(d_width/b)-d_avg/c,
                     d_height/b,
                     d_avg/c,
                     d_avg/c,
                     render,n,
                     -d_avg/b,
                     0)

def chordal_lines():
    chord = [0,3,7,10,12]
    chord_mod_list = [0,random.randint(-1,1),random.randint(-1,1),random.randint(-2,1),random.randint(0,3)]
    new_chord = []
    chord_chance = 32
    chord_roll = random.randint(0,100)
    chord_angle = random.randint(0,1)*42.5
    if chord_roll <= chord_chance:
        for octaves in range(1,5):
            steps = 0
            
            for i in chord:
                j = i + chord_mod_list[steps]
                if steps >= 1:
                    while j == new_chord[steps-1]:
                        j += 2
                new_chord.append(i)
                chord_line = draw.Line((
                    d_avg/fibonacci(10)*j)+(d_avg/fibonacci(10)*(octaves*12)),
                    d_avg/13*5,(d_avg/fibonacci(10)*j)+(d_avg/fibonacci(10)*
                                                        (octaves*12)),
                                       d_avg/13*3,stroke_width=stroke_large,
                                       stroke=color[1],
                                       transform='rotate('+str(chord_angle)+')')
                steps+=1
                render.append(chord_line)


d_width = 640 #Drawing space dimensions
d_height = d_width/2*3 

#Establish some standard line widths
d_avg = (d_height+d_width)/2 #average of height and width
stroke_small = d_avg / 192
stroke_large = d_avg / 128

seq_min=0
seq_max=0
seq_step=0

quick_mode=False

while True: #Take your anti-crash-out pills, Python
    try:
        print('Tip: Enter Q as file name for quick preset mode')

        filename = str(input('Enter a file name: (do not add extension) '))

        if filename == 'q' or filename == 'Q': #Quick preset mode

            #Adjust the parameters
            filename = 'n'
            overwrite = 'n'
            output_mode = 1
            seed = 1
            seq_min = 0
            seq_max = 250
            seq_step = 10
            seq_max += seq_step

            quick_mode = True
            break

        overwrite = str(input('Overwrite? y/n (y = overwrite, n = append) '))
        output_mode = int(
            input('Output mode? (0 is a single svg, 1 is a range of seeds) '))

        if output_mode == 1:
            seq_min = int(input('Sequence minimum '))
            seq_max = int(input('Sequence maximum '))
            seq_step = int(input('Increment size '))
            
            seq_max += seq_step #Makes the range inclusive

            break
        elif output_mode == 0:
            break
    except ValueError:
        print('wtf')


seq_iterator = seq_min

while True: #Second loop to actually execute
    try:
        
        #Original mode, entering seeds one at a time
        if output_mode == 0: 
            if quick_mode == False:
                seed = int(
                    input('Enter the random seed (must be an integer):'))
            else:
                input('Quick mode: hit enter to run')

        #Secondary mode, entering a range and getting a series
        elif output_mode == 1: 
            seed = seq_iterator
            seq_iterator += seq_step

            if seq_iterator > seq_max or seq_step == 0:
                break
        random.seed(seed)
            
        #Init a main "canvas"
        render = draw.Drawing(d_width, d_height) 
        #We're drawing to a secondary canvas or three so we can apply
        #transformations before printing to the main canvas
        drawing1 = draw.Group(id='canvas1')

        mask1 = draw.Mask(maskContentUnits='objectBoundingBox')
        
        drawing2 = draw.Group(id='canvas2',mask=mask1)
        drawing3 = draw.Group(id='canvas3')
        drawing4 = draw.Group(id='canvas4')
        color = ['black',RGB(255,255,255),
                 RGB(0,0,0),RGB(200,25,25),
                 RGB(100,100,100)]
        rect_1 = draw.Rectangle(0,0,d_width,d_height,
                                fill='black',stroke=color[1],
                                stroke_width=stroke_large) #Black background
        rect_2 = draw.Rectangle(0,0,d_width,d_height,
                                stroke=color[1],
                                stroke_width=stroke_large*2,
                                fill='none') #White outline

        



        drawing1.append(rect_1)#Background square
        render.append(rect_1)
        
                        
        
        #Drawing section
        mondrian_angled(0,d_width,0,d_height,4,drawing1,color[3])
        mask1.append(drawing1)
        chordal_lines()
        mondrian_straight(0,d_width,0,d_height,5,drawing2,d_width/8*random.randint(3,5),d_height/8*random.randint(3,5),color[2])
        mondrian_angled(0,d_width,0,d_height,4,drawing3,color[2])
        mondrian_straight(0,d_width,0,d_height,6,drawing4,0,d_height/5*random.randint(0,5),color[4])
        
        
        
        
        
        rect_percent_chance = 32
        rect_roll = random.randint(0,100)
        rect_coin_flip = random.randint(0,1)
        rect_fib = random.randint(3,6)
        if rect_roll <= rect_percent_chance:
            if rect_coin_flip == 0:
                rect_sequence_vert(fibonacci(rect_fib),8)
            else:
                rect_sequence_hor(fibonacci(rect_fib),8)

        draw_circles(d_width/8*random.randint(3,5),d_height/13*random.randint(5,8),d_avg/8,render,0.618)

        
        
        #White border
        render.append(rect_2)
        
        #Save the final canvas as an SVG file        
        if overwrite == 'y':
            render.save_svg(filename+'.svg')
        elif overwrite == 'n':
            render.save_svg(filename+'_'+str(seed)+'.svg')
        
    
    except ValueError:
        print('girlie please i cannot paint with that')

print('Sequence finished, check the folder of the .py module~!')
