from tkinter import *
from tkinter import messagebox
from socket import *
from threading import Thread

player = 1
turn = 0
finish = False

def win(player):
    messagebox.showinfo(title = "Congratulation",message = 'winner is ' + player )

def tie():
    messagebox.showinfo(title = "Game Over",message = 'Try again')

def resetGame():
    bt1["text"]=" "
    bt2["text"]=" "
    bt3["text"]=" "
    bt4["text"]=" "
    bt5["text"]=" "
    bt6["text"]=" "
    bt7["text"]=" "
    bt8["text"]=" "
    bt9["text"]=" "
    s.close()
    handle_client()   

def quit():
    s.close()
    wind.destroy()

def check():
    global turn
    turn +=1
        
    b1=bt1['text']
    b2=bt2['text']
    b3=bt3['text']
    b4=bt4['text']    
    b5=bt5['text']    
    b6=bt6['text']
    b7=bt7['text']
    b8=bt8['text']
    b9=bt9['text']
    
    if (b1==b2 and b2==b3 and b1 =='O') or (b1==b2 and b2==b3 and b1 =='X'):
        finish = True
        win(b1)
    if (b4==b5 and b5==b6 and b4 =='O') or (b4==b5 and b5==b6 and b4 =='X'):
        finish = True
        win(b4)
    if (b7==b8 and b8==b9 and b7 =='O') or (b7==b8 and b8==b9 and b7 =='X'):
        finish = True
        win(b7)
    if (b1==b4 and b4==b7 and b1 =='O') or (b1==b4 and b4==b7 and b1 =='X'):
        finish = True
        win(b1)
    if (b2==b5 and b5==b8 and b2 =='O') or (b2==b5 and b5==b8 and b2 =='X'):
        finish = True
        win(b2)
    if (b3==b6 and b6==b9 and b3 =='O') or (b3==b6 and b6==b9 and b3 =='X'):
        finish = True
        win(b3)
    if (b1==b5 and b5==b9 and b1 =='O') or (b1==b5 and b5==b9 and b1 =='X'):
        finish = True
        win(b1)
    if (b3==b5 and b5==b7 and b3 =='O') or (b3==b5 and b5==b7 and b3 =='X'):
        finish = True
        win(b3)

    if (turn == 9):
        turn = 0
        if (finish is False):
            tie()
        
def clicked1():
    global player
    if (bt1['text']==" "):
        if (player == 1):
            player=2
            bt1['text']='O'
            send_play(1)
        check()

def clicked2():
    global player
    if (bt2['text']==" "):
        if (player == 1):
            player=2
            bt2['text']='O'
            send_play(2)
        check()
        
def clicked3():
    global player
    if (bt3['text']==" "):
        if (player == 1):
            player=2
            bt3['text']='O'
            send_play(3)
        check()
        
def clicked4():
    global player
    if (bt4['text']==" "):
        if (player == 1):
            player=2
            bt4['text']='O'
            send_play(4)
        check()
        
def clicked5():
    global player
    if (bt5['text']==" "):
        if player == 1:
            player=2
            bt5['text']='O'
            send_play(5)
        check()
        
def clicked6():
    global player
    if (bt6['text']==" "):
        if( player == 1):
            player=2
            bt6['text']='O'
            send_play(6)
        check()
        
def clicked7():
    global player
    if (bt7['text']==" "):
        if (player == 1):
            player=2
            bt7['text']='O'
            send_play(7)
        check()
        
def clicked8():
    global player
    if (bt8['text']==" "):
        if (player == 1):
            player=2
            bt8['text']='O'
            send_play(8)
        check()
        
def clicked9():
    global player
    if (bt9['text']==" "):
        if (player == 1):
            player=2
            bt9['text']='O'
            send_play(9)
        check()

def send_play(n):
    n = str(n)
    n = n.encode() 
    c.send(n)
    
def handle_play(n):
    global player
    n = n-1
    button_list [n]["text"] = "X"
    player = 1

def apply_play(p):
    p = p.decode()
    p = int(p)
    handle_play(p)

wind = Tk()

wind.title('Server: Tic Tac Toe')
wind.geometry('280x440')
wind.resizable(width=False, height=False)
wind.configure(background = 'white')

tops = Frame(wind, bg ='black', pady=2, width=500, height=200)
tops.grid(row=0, column=0)

lblTitle = Label(tops, font=('arial', 30,'bold'),text="Tic Tac Toe", bd=21, fg='black', justify = CENTER)
lblTitle.grid(row=0, column=0)

mainFrame = Frame(wind, bg='grey', bd=10, width=500, height=200) 
mainFrame.grid(row=1, column=0)

# lb1 = Label(wind, text='player1: O', font=('Helvetica','15'))
# lb1.grid(row=0, column=0)    

button_list = list()

bt1=Button(mainFrame, text=" ",bg="black",fg="white",width = 5, height = 2,font=('Helvetica','15'),command = clicked1)
bt1.grid(row = 0, column=1)

bt2=Button(mainFrame, text=" ",bg="black",fg="white",width = 5, height = 2,font=('Helvetica','15'),command = clicked2)
bt2.grid(row = 0, column=2)

bt3=Button(mainFrame, text=" ",bg="black",fg="white",width = 5, height = 2,font=('Helvetica','15'),command = clicked3)
bt3.grid(row = 0, column=3)

bt4=Button(mainFrame, text=" ",bg="black",fg="white",width = 5, height = 2,font=('Helvetica','15'),command = clicked4)
bt4.grid(row = 1, column=1)

bt5=Button(mainFrame, text=" ",bg="black",fg="white",width = 5, height = 2,font=('Helvetica','15'),command = clicked5)
bt5.grid(row = 1, column=2)

bt6=Button(mainFrame, text=" ",bg="black",fg="white",width = 5, height = 2,font=('Helvetica','15'),command = clicked6)
bt6.grid(row = 1, column=3)

bt7=Button(mainFrame, text=" ",bg="black",fg="white",width = 5, height = 2,font=('Helvetica','15'),command = clicked7)
bt7.grid(row = 2, column=1)

bt8=Button(mainFrame, text=" ",bg="black",fg="white",width = 5, height = 2,font=('Helvetica','15'),command = clicked8)
bt8.grid(row = 2, column=2)

bt9=Button(mainFrame, text=" ",bg="black",fg="white",width = 5, height = 2,font=('Helvetica','15'),command = clicked9)
bt9.grid(row = 2, column=3)

button_list.append(bt1)
button_list.append(bt2)
button_list.append(bt3)
button_list.append(bt4)
button_list.append(bt5)
button_list.append(bt6)
button_list.append(bt7)
button_list.append(bt8)
button_list.append(bt9)

btnRestart = Button(text="Restart", font=('arial', 16, 'bold'), height=1, width=20, command=resetGame) 
btnRestart.grid(row=8, column=0 ,padx=6, pady=10)

btnQuit = Button(text="Quit", font=('arial', 16, 'bold'), height=1, width=20, command = quit) 
btnQuit.grid(row=10, column=0 ,padx=6, pady=10)


s = socket(AF_INET,SOCK_STREAM)


s.bind(('127.0.0.1', 7676)) #การกำหนดค่าต่างๆที่จำเป้นให้กับ socket object
s.listen(5) #จำนวนงานที่เข้ามาได้ จะทำงานโดยรอรับคำขอเชื่อมต่อจาก client 
c=None

def handle_client():
    global player
    global c
    player = 1
    c, ad = s.accept()
    receive = Thread(target = receive_message, args = [c,])
    receive.start()
    
def receive_message(c):
    while True:
        p = c.recv(10) #ขนาดข้อมูล 10
        apply_play(p)

acc = Thread(target=handle_client)
acc.start()
    
wind.mainloop()
