from tkinter import *
from tkinter import messagebox



##lst = ['X' , 'O']


root = Tk()
root.geometry('400x400')
##root.minsize(433 , 333)
##root.maxsize(433 , 333)
root.config(bg = "#BEBEBE")
root.title('TIC-TAC-TOE')

class Player():
    def __init__(self ,colour , value, name):
        self.colour = colour
        self.value = value
        self.name = name
        
P1 = Player('red' , 'O' , 'Player-1')
P2 = Player('blue' , 'X' , 'Player-2')
CurrentPlayer=P1

def SwitchPlayer():
    global CurrentPlayer
    if CurrentPlayer == P2:
        CurrentPlayer = P1
    else:
        CurrentPlayer = P2



label_move = Label(root , text = 'Next Move : Player-1 [O]' , bg = '#BEBEBE' , fg= 'black' ,font = ('comic sans ms' , '12' , 'bold'))
label_move.place(x = 120 , y = 50 )


w = 185
h = 185
cx = 125
cy = 125


cvs = Canvas(root , width = w , height = h , highlightthickness = 0 ,  bg = '#BEBEBE')
cvs.place(x = cx , y = cy)

cvs.create_line(w/3,0, w/3 , h , fill = 'black')
cvs.create_line(2*w/3,0, 2*w/3 , h , fill = 'black')

cvs.create_line(0,h/3, w , h/3 , fill = 'black')
cvs.create_line(0,2*h/3, w , 2*h/3 , fill = 'black')



class Buttons():

    def __init__(self , master , text , i, j,x , y , command = None , cursor = 'plus' , state = 'normal' , activebackground = None):
        self.master = master
        self.text = text
        self.command = command
        self.i = i
        self.j = j
        self.x = x
        self.y = y
        self.cursor = cursor
        self.state = state
        self.activebackground = activebackground

        self.btn = Button(self.master , text = self.text , cursor = self.cursor , state = self.state, activebackground = self.activebackground)
        self.btn.place(x = self.x , y = self.y)
        self.btn.bind('<Enter>' , self.bind_state)
        self.btn['command'] = lambda i=self.i , j =self.j : click(i,j)


    def destroy(self):
        self.btn.destroy()

    def bind_state(self , event):
        self.btn['activebackground'] = CurrentPlayer.colour
        self.btn['state'] = 'active'

        
won=False
def check_winner():
    global won
                    
    if var_lst[0][0]==var_lst[1][1]==var_lst[2][2]:
        cvs.create_line(w/12, h/12 , 11*w/12 , 11*h/12 , fill='black', width=2)
        won=True

    elif var_lst[2][0]==var_lst[1][1]==var_lst[0][2]:
        cvs.create_line(11*w/12 , h/12 , w/12 , 11*h/12 , fill='black' , width=2)
        won=True

    else:
        for k in range(2):
            for i in range(0,3):
                if k ==0:
                    if var_lst[i][0]==var_lst[i][1]==var_lst[i][2]:
                        cvs.create_line((2*i +1)*w/6 , 10 , (2*i +1)*w/6 , h-10 , fill = 'black' , width=2)
                        won=True
                else:
                    if var_lst[0][i]==var_lst[1][i]==var_lst[2][i]:
                        cvs.create_line(10, (2*i +1)*h/6 , w-10 , (2*i +1)*h/6, fill = 'black' , width=2)
                        won=True

    
    if won:
        SwitchPlayer()
        messagebox.showinfo(title = 'Result' , message = f'{CurrentPlayer.name} [ {CurrentPlayer.value} ] won this match !'.upper())
        root.destroy()
        return

    #CHECK IF DRAW
    for i in range(0,3):
        for j in range(0,3):
            if var_lst[i][j]!= P1.value and var_lst[i][j] != P2.value:
                return
    else:
        messagebox.showinfo(title = 'Result' , message = '\t It\'s a draw \t\t'.upper())
        root.destroy()
        

                        
##    if (var_lst[0][0] in lst) and (var_lst[0][1] in lst) and (var_lst[0][2] in lst) and (var_lst[1][0] in lst) and (var_lst[1][1] in lst) and (var_lst[1][2] in lst) and (var_lst[2][0] in lst) and (var_lst[2][1] in lst) and (var_lst[2][2] in lst):
##        messagebox.showinfo(title = 'Match' , message = '                It\'s a draw                     '.upper())
##        root.destroy()

              


def click(i,j):
    grid[i][j].destroy()

    cvs.create_text((2*i + 1)*w/6 , (2*j + 1)*h/6 , fill = CurrentPlayer.colour , font = 'Verdana 17 bold' ,text = CurrentPlayer.value)
    var_lst[i][j]=CurrentPlayer.value
    print(CurrentPlayer.value)

    SwitchPlayer()

    label_move.config(text = f'Next Move : {CurrentPlayer.name} [{CurrentPlayer.value}]')

    check_winner()
    
        
    

grid=[[],[],[]]
for i in range(0,3):
    for j in range(0,3):
##        grid[i][j] = Buttons(root ,'         ', i, j,cx + (2*i + 1)*w/6 -w/11 , cy + (2*j + 1)*h/6 -h/14, click)
        grid[i].append( Buttons(root ,'         ', i, j,cx + (2*i + 1)*w/6 -w/11 , cy + (2*j + 1)*h/6 -h/14, click) )




var_lst = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
          ]


root.mainloop()
