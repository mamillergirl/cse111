import random
from textwrap import fill
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)
    
    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.



def draw_sky(canvas, width, height):
    horizon = 150
    draw_rectangle(canvas, 0, horizon, width, height, fill = "SteelBlue2"  )
    draw_oval(canvas, 50, 380, 150, 480, width = 1, outline = "", fill = "gold")
  
    draw_clouds(canvas, 200, width, 350, height)
    draw_bird(canvas, 80, 350)
    draw_bird(canvas, 25, 320)
    draw_bird(canvas, 120, 300)

def draw_ground(canvas, width):
    
    draw_grass(canvas, width)
    draw_fence(canvas, width, 150, 25)
    draw_tree(canvas, 200, 150, 250)
    draw_tree(canvas, 675, 150, 200)
    draw_fence(canvas, width, 0, 35)
    draw_gate(canvas)
    draw_house(canvas)
    draw_path(canvas)
    draw_bush(canvas, 0, 405)
    draw_bush(canvas, 470, 800)
    draw_flower(canvas, 0, 405)
    draw_flower(canvas, 470, 800)

def draw_house(canvas):
    #draw main house
    draw_rectangle(canvas, 320, 150, 560, 285, fill = "burlywood3")
    #draw roof
    draw_polygon(canvas, 317, 285, 440, 350, 563, 285, fill = "saddleBrown")
    #draw door
    draw_rectangle(canvas, 420, 150, 460, 220, fill= "saddleBrown" )
    draw_oval(canvas, 453, 185, 458, 190, fill = "gray64")
    #draw windows
    draw_rectangle(canvas, 355, 210, 395, 250, fill = 'gray75')
    draw_rectangle(canvas, 485, 210, 525, 250, fill = "gray75")

def draw_cloud(canvas, x_min, x_max, y_min, y_max):
    color_number = random.randint(0,2)
    color = "white"
    if color_number == 0:
        color = "grey89"
    elif color_number == 1:
        color = "grey98"
   
    for i in range(0, 4, 1):
        x1 = random.randrange(x_min, x_max)
        y1 = random.randrange(y_min, y_max)
        x2 = x1 + 150
        y2 = y1 + 35
        draw_oval(canvas, x1, y1, x2, y2, width = 1, outline = "", fill = color)
    
def draw_clouds(canvas, x_min, x_max, y_min, y_max):
    for i in range(x_min, x_max, 150):
        draw_cloud(canvas, x_min, x_max, y_min, y_max)

def draw_fence(canvas, width, starting_point, fence_height):
    for x in range(0, width, 13):
        x1 = x
        x2 = x + 10
        y1 = starting_point
        y2 = y1 + fence_height
        draw_rectangle(canvas, x1, y1, x2, y2, outline = "black", fill = "white"  )

def draw_flower(canvas, x_min, x_max):
    for i in range(0, 7, 1):
        x1 = random.randrange(x_min, x_max)
        y1 = random.randrange(35, 130)
        x2 = x1 + 2
        y2 = y1 + 15
        draw_rectangle(canvas, x1, y1, x2, y2, outline = "", fill = "green1")
        y3 = y2 + 10
        x3 = x1 - 5
        x4 = x2 + 5
        draw_oval(canvas, x3,y2, x4, y3, fill = "orchid1")


def draw_gate(canvas):
    draw_rectangle(canvas, 405, 0, 475, 40, outline = "black", fill = "white" )
    draw_oval(canvas, 463, 16, 470, 23, fill = "gray64")

def draw_path(canvas):
    draw_rectangle(canvas, 415, 40, 465, 150, fill = "gray35" )
    
def draw_bush(canvas, start_bush, end_bush):
    for x in range(start_bush, end_bush, 60):
        x1 = x
        x2 = x + 53
        y1 = 135
        y2 = 160
        draw_oval(canvas, x1, y1, x2, y2, width = 1, outline = "black", fill = "darkGreen" )

def draw_grass(canvas, width):    
    for x in range (0, width, 2):
        x1 = x
        x2 = x + 2
        y1 = 0
        y2 = 150
        draw_rectangle(canvas, x1, y1, x2, y2, outline = "black", fill = "forestGreen")




def draw_bird(canvas, center_x, center_y):
    left = center_x - 20
    right = center_x + 20
    top = center_y + 15
    draw_line(canvas, center_x, center_y, right, top, width = 2, fill = "black")
    draw_line(canvas,left, top, center_x, center_y, width = 2, fill = "black")


def draw_tree(canvas, center_x, bottom, height):
    #draw trunk
    trunk_width = height / 10
    trunk_height = height / 6
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom 
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill = "tan4")
    #draw skirt
    skirt_width = height / 2
    
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill = "darkGreen")

# Call the main function so that
# this program will start executing.
main()