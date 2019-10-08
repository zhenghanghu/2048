import simplegui
import random
import math
import codeskulptor

board=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]

vis_board=[[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
merge_num=1

# Tile Images
IMAGENAME = "assets_2048.png"
TILE_SIZE = 100
HALF_TILE_SIZE = TILE_SIZE / 2
BORDER_SIZE = 45
change=0          
            
    
def merge(key):
    global board,vis_board,change    
    if key == simplegui.KEY_MAP['up']:
        rotate_up()
        limitless_merge()
        rotate_up()
        rotate_up()
        rotate_up()

    elif key == simplegui.KEY_MAP['down']:
        rotate_up()
        rotate_up()
        rotate_up()
        limitless_merge()
        rotate_up()

    elif key == simplegui.KEY_MAP['left']:
        limitless_merge()

    elif key == simplegui.KEY_MAP['right']:
        rotate_right()
        limitless_merge()
        rotate_right()
     

    if( change ):
        change=0
        add()
        print_result()
    
def rotate_right():
    for i in range (4):
        temp=board[i][0]
        board[i][0]=board[i][3]
        board[i][3]=temp
        temp=board[i][1]
        board[i][1]=board[i][2]
        board[i][2]=temp 
def rotate_up():
    global board
    temp=[[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
    for i in range (4):
        m=3
        for j in range(4):
            temp[m][i]=board[i][j]
            m=m-1
    board=temp
    
def limitless_merge():
    global board,vis_board,change,merge_num
    for i in range(4):
            for j in range(1,4):
                m=j
                if (board[i][j]==0):
                    continue
                j=j-1
                while(board[i][j]==0):
                    if(j<0):
                        break
                    j=j-1        
                #if j=-1, [i][j]前面全是0
                if (j==-1):#前面全是0
                    board[i][0]=board[i][m]
                    board[i][m]=0
                    change=1
                else :
                    if(board[i][j]==board[i][m]):
                        if (vis_board[i][j]==0):
                            board[i][j]*=2
                            board[i][m]=0
                            vis_board[i][j]=1
                            change=1
                            merge_num = merge_num + 1
                        else:
                            board[i][j+1]=board[i][m]
                            if(j+1==m):
                                continue
                            else:
                                board[i][m]=0
                    else:#和前面数值不等
                        board[i][j+1]=board[i][m]
                        if(j+1==m):
                            continue
                        else:
                            board[i][m]=0
                            change=1
    vis_board=[[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]
    
def print_result():
    for i in range (4):
        print board[i]
    print
    
def add():
    for i in range(10000):
            location_i=random.randrange(0,3)
            location_j=random.randrange(0,3)
            if(board[location_i][location_j]==0):
                board[location_i][location_j]=random.choice( [2,4,2,2,2] )
                break
def new_game():
    global board,merge_num
    board=[[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
    add()
    add()
    merge_num=0
    l2.set_text('Merge number '+str(merge_num))
    
def draw(canvas):
    global merge_num
    for row in range(4):
        for col in range(4):
                tile = board[row][col]
                if tile == 0:
                    val = 0
                else:
                    val = int(math.log(tile, 2))
                canvas.draw_image(simplegui.load_image(codeskulptor.file2url(IMAGENAME)),
                    [HALF_TILE_SIZE + val * TILE_SIZE, HALF_TILE_SIZE],
                    [TILE_SIZE, TILE_SIZE],
                    [col * TILE_SIZE + HALF_TILE_SIZE + BORDER_SIZE,
                     row * TILE_SIZE + HALF_TILE_SIZE + BORDER_SIZE],
                    [TILE_SIZE, TILE_SIZE])   
    l2.set_text('Merge number '+str(merge_num))
                
print_result()
frame = simplegui.create_frame("2048", 500, 500)
frame.set_keydown_handler(merge)
frame.set_draw_handler(draw)
frame.set_canvas_background("#BCADA1")
frame.add_button('New Game', new_game)
l2=frame.add_label('')
frame.add_label('')
frame.add_label('The limit is 8196')


frame.start()
new_game()
