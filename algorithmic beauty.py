
# Run from terminal in virtual environment for best results:
# source Users/katherinajesek/Documents/GitHub/Modern-Art-Study/.venv/bin/activate
# python -m idlelib.idle

#pure plastic art
#by Katherina "Kate the Cursed" Jesek

import drawsvg as draw
import math
import random
import json
import numpy as np
from scipy.spatial.distance import pdist

def title_block(): #Cute ASCII title card
    print('\n')
    print('   __  ___   __ _   ___  __      __    ')
    print('  /__\/ __\ / /(_) / _ \/ _\ ___/ _\   ')
    print(' /_\ / /   / / | |/ /_)/\ \ / _ \ \    ')
    print('//__/ /___/ /__| / ___/ _\ \  __/\ \   ')
    print('\__/\____/\____/_\/     \__/\___\__/   ')
    print(' ~ ~ ~ a generative art piece ~ ~ ~    ')
    print('by Katherina "Kate the Cursed" Jesek   ')
    print('AlphaV0.02                    © 2026   ')
    print('\n\n')
def import_table(filename): #Handles loading the JSON file with the odds
    with open(filename, 'r') as odds_file:
        odds_data = json.load(odds_file)
        return odds_data

def get_odds(num_id,odds_data): #Retrieves a percentage from the loaded odds table
    for odds_dict in odds_data:
        if odds_dict["oid"] == num_id:
            return int(odds_dict["odds"])

def get_setting(name,dataset): #Retrieves a percentage from the loaded odds table
    for set_dict in dataset:
        if set_dict["name"] == name:
            return set_dict["value"]
    

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

def fibonacci_list(user_input): #Creates a list of Fibonacci sequence and
                            #returns the list itself
    fib_list = [0, 1, 1]
    for iterator in range(user_input+2):
        if iterator > 1:
            new_entry = fib_list[iterator]+fib_list[iterator-1]
            fib_list.append(new_entry)
    #print(fib_list) #debug print
    del fib_list[0],fib_list[1]
    return fib_list

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

def fibonacci_lines_hor(x1,x2,y1,y2,n,m,cnv): #
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
    render.append(draw.Use(cnv,0,0,transform='rotate(45),scale(1.75),translate('+str(0)+','+str(-d_height/2)+')')) #Print the secondary canvas to the main canvas

def mondrian_straight(x1,x2,y1,y2,n,cnv,posX,posY,fill_pattern):
    mondrian_lines(x1,x2,y1,y2,n,cnv,fill_pattern)
    render.append(draw.Use(cnv,0,0,transform='rotate(0),scale(1),translate('+str(posX)+','+str(posY)+')'))

def draw_circles(cx,cy,r,cnv,scale_fac):
    circ_1_ol = draw.Circle(cx,cy,r+(d_avg/34),fill='black',stroke='none',stroke_width=stroke_large)
    circ_1 = draw.Circle(cx,cy,r,fill='black',stroke=color[1],stroke_width=stroke_large)
    cnv.append(circ_1)
    circ_2 = draw.Circle(cx,cy,int(r*scale_fac//1),fill='none',stroke=color[1],stroke_width=stroke_large,transform='rotate('+str(random.randint(1,360))+'),translate('+str(cx//random.randint(8,12))+','+str(0)+')')
    cnv.append(circ_2)

def draw_equi_tri(centerX,centerY,sideLength,color,rot,canvas):
    triangle_group = draw.Group(transform='rotate('+str(rot)+')')
    height = ((-(sideLength/2)**2+sideLength**2))**0.5
    if rot >= 45:
        centerY-=(d_avg)
    elif rot <= -45:
        centerY+=(d_avg)
    triangle = draw.Lines(
        centerX-int(sideLength//2),centerY+int(height//2),
        centerX+int(sideLength//2),centerY+int(height//2),
        centerX,centerY-int(height//2),
        stroke=color,stroke_width=stroke_large,close='true'
        )
    triangle_group.append(triangle)
    canvas.append(triangle_group)

def draw_arrow(centerX,centerY,sideLength,tailLength,color,rot,canvas):
    triangle_group = draw.Group(transform='rotate('+str(rot)+')')
    height = ((-(sideLength/2)**2+sideLength**2))**0.5
    if rot >= 45:
        centerY-=(d_avg)
    elif rot <= -45:
        centerY+=(d_avg)
    triangle = draw.Lines(
        centerX-int(sideLength//2),centerY+int(height//2),
        centerX,centerY+int(height//2),
        centerX,centerY+int(tailLength),
        centerX,centerY+int(height//2),
        centerX+int(sideLength//2),centerY+int(height//2),
        centerX,centerY-int(height//2),
        stroke=color,stroke_width=stroke_large,close='true'
        )
    triangle_group.append(triangle)
    canvas.append(triangle_group)
    
    

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

def chordal_lines(): #Lines with gaps based on chords
    chord = [0,3,7,10,12]
    chord_mod_list = [0,random.randint(-1,1),random.randint(-1,1),random.randint(-2,1),random.randint(0,3)]
    new_chord = []
    chord_chance = get_odds(1,odds_data)
    chord_roll = random.randint(0,100)
    chord_angle = random.randint(-1,1)*45
    if chord_roll <= chord_chance:
        for octaves in range(1,5): 
            steps = 0 #Reset for each octave
            y_value = d_avg/13*random.randint(3,8)
            x_value = d_avg/21*random.randint(5,13)
            for i in chord:
                j = i + chord_mod_list[steps] 
                if steps >= 1:
                    while j == new_chord[steps-1]: #Makes sure we don't overlap
                        j += 2
                new_chord.append(j)
                chord_line = draw.Line((
                    x_value+d_avg/fibonacci(10)*j)+(d_avg/fibonacci(10)*(octaves*12)),
                    y_value,x_value+(d_avg/fibonacci(10)*j)+(d_avg/fibonacci(10)*
                                                        (octaves*12)),
                                       y_value+(d_avg/13),stroke_width=stroke_large,
                                       stroke=color[1],
                                       transform='rotate('+str(chord_angle)+')')
                steps+=1
                render.append(chord_line)

def fibonacci_segments(u): #Lines with gaps based on fib sequence (like chordal lines)
    chord = [*fibonacci_list(u)]
    chord_chance = get_odds(2,odds_data)
    chord_roll = random.randint(0,100)
    chord_angle = random.randint(-1,1)*45
    if chord_roll <= chord_chance:
        steps = 0
        y_value = d_avg/13*random.randint(3,8)
        x_value = d_avg/21*random.randint(5,13)
        for i in chord:
            
            chord_line = draw.Line(
                x_value+((d_avg/fibonacci(16)*i)+(d_avg/fibonacci(16))),
                y_value,x_value+((d_avg/fibonacci(16)*i)+(d_avg/fibonacci(16))),
                                       y_value+d_avg/13,stroke_width=stroke_large,
                                       stroke=color[1],
                                       transform='rotate('+str(chord_angle)+')')
            steps+=1
            render.append(chord_line)

def chord_seq():
    chord = [0,3,7,10,12]
    chord_mod_list = [0,random.randint(-1,1),random.randint(-1,1),random.randint(-2,1),random.randint(0,3)]
    new_chord = []
    c = 0
    for note in chord:
        new_note = note + chord_mod_list[c]
        c+=1
        new_chord.append(new_note)
    #print(new_chord)
    return new_chord

def tri_wave(startX,startY,iterations,period,color,rot,duplicates,offset):
    tri_drawing = draw.Group(id='tri_wave')

    if iterations % 2 == 0:
        iterations+=1
    if iterations == 2:
        iterations += 2

    for v in range(duplicates):        
        amp = int(period//2)
        x = [startX+x*period for x in range(int(iterations))]
        y = [v*offset+startY-amp,v*offset+startY+amp]*int(iterations//2)
        xy_flat = []
        if rot == 90:
            for x2,y2 in zip(y,x):
                xy_flat.extend([x2,y2])
        else:
            for x2,y2 in zip(x,y):
                xy_flat.extend([x2,y2])
        new_line = draw.Lines(*xy_flat,stroke=color,stroke_width=stroke_small,fill='none')
        
        tri_drawing.append(new_line)
    render.append(tri_drawing)

def tri_wave_chordal(startX,startY,iterations,period,color,rot,duplicates,offset):
    if iterations % 2 == 0:
        iterations+=1
    if iterations == 2:
        iterations += 2

    tri_drawing = draw.Group(id='tri_wave')
    c_ticker = 0
    c_oct = 1
    chordal_seq = [*chord_seq()]
    for v in range(duplicates):

        c_offset = (offset/4)*((c_oct*12)+chordal_seq[c_ticker])
        
        amp = int(period//2)
        x = [startX+x*period for x in range(int(iterations))]
        y = [c_offset+startY-amp,c_offset+startY+amp]*int(iterations//2)
        xy_flat = []
        
        if rot == 90:
            for x2,y2 in zip(y,x):
                xy_flat.extend([x2,y2])
        else:
            for x2,y2 in zip(x,y):
                xy_flat.extend([x2,y2])
        new_line = draw.Lines(*xy_flat,stroke=color,stroke_width=stroke_small,fill='none')
        
        tri_drawing.append(new_line)
        if c_ticker >= 4:
            c_ticker = 0
            c_oct += 1
        else:
            c_ticker+=1
    render.append(tri_drawing)

def tri_wave_fib(startX,startY,iterations,period,color,rot,duplicates,offset):
    if iterations % 2 == 0:
        iterations+=1
    if iterations == 2:
        iterations += 2

    tri_drawing = draw.Group(id='tri_wave')
    f_ticker = 0
    fib_seq = [*fibonacci_list(duplicates)]
    for v in range(duplicates):

        f_offset = ((offset//2)*(fib_seq[f_ticker]))
        
        amp = int(period//2)
        x = [startX+x*period for x in range(int(iterations))]
        y = [f_offset+startY-amp,f_offset+startY+amp]*int(iterations//2)
        xy_flat = []
        
        if rot == 90:
            for x2,y2 in zip(y,x):
                xy_flat.extend([x2,y2])
        else:
            for x2,y2 in zip(x,y):
                xy_flat.extend([x2,y2])
        new_line = draw.Lines(*xy_flat,stroke=color,stroke_width=stroke_small,fill='none')
        f_ticker+=1
        tri_drawing.append(new_line)
    render.append(tri_drawing)


def save_input_preset(filename,overwrite,output_mode,seed,seq_min,seq_max,seq_step):
    global stop_asking
    while True:
        try:
            if stop_asking != 'y' and stop_asking != 'Y':
                save_mode = str(input('Save these settings as quick preset? y/n '))
                if save_mode == 'y' or save_mode == 'Y':
                    preset_list = [
                        {"name":"filename", "value":filename},
                        {"name":"overwrite", "value":overwrite},
                        {"name":"output_mode", "value":output_mode},
                        {"name":"seed", "value":seed},
                        {"name":"seq_min", "value":seq_min},
                        {"name":"seq_max", "value":seq_max-seq_step},
                        {"name":"seq_step", "value":seq_step}
                    ]

                    with open("preset_table.json", "w") as file:
                        json.dump(preset_list, file, indent=4)
                else:
                    stop_asking = str(input('Should I stop asking? y/n'))
            break
        except NameError:
            stop_asking = 'n'
def is_in_mandelbrot_set(x,y,z_axis,w_axis,zoom):
    c = complex(x/zoom, y/zoom)
    color_ticker=0
    z=complex(z_axis+w_axis)
    #print(x,y)
            
    magnitude_z = (z.real**2+z.imag**2)**0.5
    while abs(magnitude_z) < 2:
                
        color_ticker+=1
        z = z**2+c
        magnitude_z = (z.real**2+z.imag**2)**0.5
        if color_ticker > 24:
            return False
            break
    return True

def connect_dots_inner(array_data,super_list):
    
    last_point = array_data[0] 
    
    
    array_data_upd = np.delete(array_data, 0, axis=0)
    distances = np.linalg.norm(array_data_upd - last_point, axis=1)
    sorted_indices = np.argsort(distances)

    
    sorted_points = array_data_upd[sorted_indices]
    
    sorted_distances = distances[sorted_indices]

    for dist in range(0,len(sorted_distances),1):
        if sorted_distances[dist] < sorted_distances[dist-1] and dist!= 0:
            

            break
    
    return sorted_points,array_data[0]

def connect_dots(array_data):
    sorted_points = []
    while len(array_data) > 1:
        array_data,super_data = connect_dots_inner(array_data,sorted_points)
        #print(array_data)
        sorted_points.append(tuple(super_data))
        
    #print('super list'+str(sorted_points))
    converted = [(int(a), int(b)) for a, b in sorted_points]
    flattened=[]
    for a, b in converted:
        flattened.extend([a,b])
    #print(converted)
    #print(flattened)
    return flattened



def mandelbrot_set(xpos,ypos,width,height,viewX,viewY,scale,z_axis,w_axis,zoom,canvas):
    frac_canv = draw.Group(id='fractal')
    frac_canv2 = draw.Group(id='fractal2')
    frac_canv3 = draw.Group(id='fractal3')
    frac_tracer_list = []
    
    for x in range(viewX-width//2,viewX+width//2,2):
        for y in range(viewY-height//2,viewY+height//2,2):
            c = complex(x/zoom, y/zoom)
            color_ticker=0
            z=complex(z_axis+w_axis)

            #print(x,y) #Sanity check
            
            magnitude_z = (z.real**2+z.imag**2)**0.5
            while abs(magnitude_z) < 2:
                
                color_ticker+=1
                z = z**2+c
                magnitude_z = (z.real**2+z.imag**2)**0.5
                if color_ticker > 24:
                    fill_color = 'white'


                    #print(x,y) #Sanity check

                    
                    #Check all surrounding pixels to see if it's on the border
                    buffer_check = []
                    buffer_AND = True

                    for x2 in range(-1,2):
                        for y2 in range(-1,2):
                            if is_in_mandelbrot_set(x+x2,y+y2,z_axis,w_axis,zoom):
                                buffer_check.append(True)
                            else:
                                buffer_check.append(False)
                    for buffer in buffer_check:
                        if buffer == False:
                            buffer_AND = False
                    if buffer_AND == False:
                        #print(x,y) #Sanity check
                        frac_tracer_list.append(x)
                        frac_tracer_list.append(y)
                        
                        
                    
                    #print('nope')
                    break
                fill_color = RGB(color_ticker*40,0,0)
            
            
            #m_path = draw.Rectangle(x*scale+xpos+width//2,y*scale+ypos+height//2,2*scale,2*scale,fill=fill_color,stroke=fill_color,stroke_width=stroke_large)
            #frac_canv.append(m_path)
            #canvas.append(frac_canv)
    
    #frac_tracer = draw.Lines(frac_tracer_list[0]*scale+xpos+width//2, frac_tracer_list[1]*scale+ypos+height//2,stroke='yellow',stroke_width=1,fill='none',closed='true')
    point_list_x = []
    point_list_y = []
    projected_point_list = []
    for i in range(0,(len(frac_tracer_list)//2)+2,2):
        #frac_canv2.append(draw.Circle(frac_tracer_list[i]*scale+xpos+width//2, frac_tracer_list[i+1]*scale+ypos+height//2, 0.5, fill='yellow',stroke='yellow',stroke_width=stroke_large))
        #frac_canv2.append(frac_tracer.T(frac_tracer_list[i]*scale+xpos+width//2, frac_tracer_list[i+1]*scale+ypos+height//2))
        #print(frac_tracer_list[i]*scale+xpos+width//2, frac_tracer_list[i+1]*scale+ypos+height//2)
        point_list_x.append(frac_tracer_list[i]*scale+xpos+width//2)
        point_list_y.append(frac_tracer_list[i+1]*scale+ypos+height//2)
        current_point = (frac_tracer_list[i]*scale+xpos+width//2,frac_tracer_list[i+1]*scale+ypos+height//2)
        projected_point_list.append(current_point)
    array_data = np.array(projected_point_list)

    #print(len(array_data))
    last_point = array_data[-1] 
    
    #print(array_data)
    canvas.append(frac_canv2)

    list_data_new = connect_dots(array_data)
    frac_tracer_new = draw.Lines(list_data_new[0],list_data_new[1],stroke='blue',stroke_width=1,fill='none',closed='true')
    for i in range(0,(len(list_data_new)//2)+2,2):
        frac_canv3.append(frac_tracer_new.L(list_data_new[i],list_data_new[i+1]))
    canvas.append(frac_canv3)
# ------------------

d_width = 320 #Drawing space dimensions
d_height = d_width/2*3 

#Establish some standard line widths
d_avg = (d_height+d_width)/2 #average of height and width
stroke_small = d_avg / 192
stroke_large = d_avg / 128



seq_min=0
seq_max=0
seq_step=0


while True:


    title_block()
    
    quick_mode=False
    preset_data = import_table('preset_table.json')
    while True: #Take your anti-crash-out pills, Python
        try:
            print('Tip: Enter Q as file name to run quick preset mode')

            filename = str(input('Enter a file name: (do not add extension) '))

            if filename == 'q' or filename == 'Q': #Quick preset mode

                #Adjust the parameters
                filename = get_setting("filename",preset_data)
                overwrite = get_setting("overwrite",preset_data)
                output_mode = int(get_setting("output_mode",preset_data))
                seed = int(get_setting("seed",preset_data))
                seq_min = int(get_setting("seq_min",preset_data))
                seq_max = int(get_setting("seq_max",preset_data))
                seq_step = int(get_setting("seq_step",preset_data))

                seq_max += seq_step
                quick_mode = True

                input('Quick mode selected: hit enter to run')
                break

            overwrite = str(input('Overwrite? y/n (y = overwrite, n = append) '))
            output_mode = int(
                input('Output mode? (0 is a single svg, 1 is a range of seeds) '))


            if output_mode == 1:
                seq_min = int(input('Sequence minimum '))
                seq_max = int(input('Sequence maximum '))
                seq_step = int(input('Increment size '))
                
                seq_max += seq_step #Makes the range inclusive
                seed = seq_min
                
                save_input_preset(filename,overwrite,output_mode,seed,seq_min,seq_max,seq_step)
                break
            elif output_mode == 0:
                
                break
        except ValueError:
            print('wtf')


    seq_iterator = seq_min

    odds_data = import_table('odds_table.json')

    while True: #Second loop to actually execute
        try:
            
            #Original mode, entering seeds one at a time
            if output_mode == 0: 
                seed = int(
                        input('Enter the random seed (must be an integer):'))
                if quick_mode == True:
                    save_input_preset(filename,overwrite,output_mode,seed,seq_min,seq_max,seq_step)

            #Secondary mode, entering a range and getting a series
            elif output_mode == 1: 
                seed = seq_iterator
                seq_iterator += seq_step

                if seq_iterator > seq_max or seq_step == 0:
                    break
            random.seed(seed)
            print('Drawing SVG',end=' ')    
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


            print('.',end=' ')


            frac_ex = int(input('Enter fractal zoom level'))
            
            mandelbrot_set(0,0,256,256,0,0,1,0,1,frac_ex,render)
            #For reference:
            #mandelbrot_set(xpos,ypos,width,height,viewX,viewY,scale,z_axis,w_axis,zoom,canvas)
            
            print('.')

            #White border
            render.append(rect_2)
            
            #Save the final canvas as an SVG file        
            print('Saving SVG . . .')
            if overwrite == 'y':
                render.save_svg(filename+'.svg')
                print('Saved '+filename+'.svg')
            elif overwrite == 'n':
                render.save_svg(filename+'_'+str(seed)+'.svg')
                print('Saved '+filename+'_'+str(seed)+'.svg')
            #print('Generated image #'+str(seed))
        
        except ValueError:
            print('Back to main menu ->')
            break

    print('Check the folder of the .py module~!')
    print('Restarting . . .')
