from tkinter import *

contadorx = 0  
contadory = 0

ventana =Tk()
ventana.title("Animación")
ventana.geometry("800x400")

canvas = Canvas(ventana,width=800,height=800)
canvas.pack()

canvas2 = Canvas(ventana,width=150,height=100)
canvas2.pack()

imagen = PhotoImage(file="balon.png")
imagen2 = PhotoImage(file="arcofut.png")

canvas.create_image(0,0,anchor=NW,image=imagen)
canvas2.create_image(0,0,anchor=NW,image=imagen2)

def coordenadas(x,y):
    Label(ventana,text=str(x),bg ="black",fg="white",font =("Ravie",15)).place(x=0,y=350)
    Label(ventana,text=str(y),bg="skyblue",fg="white",font =("Ravie",15)).place(x=50,y=350)

def mover_imagen(event):
    global contadorx  
    global contadory 
    if event.keysym == 'Up':
        canvas.move(1,0,-3)
        contadory = contadory+1
        coordenadas(contadorx,contadory)
        gol(contadorx,contadory)
    elif event.keysym=='Down':
        canvas.move(1,0,3)
        contadory = contadory-1
        coordenadas(contadorx,contadory-1)
        gol(contadorx,contadory)
    elif event.keysym =='Left':
        canvas.move(1,-3,0)
        contadorx = contadorx-1
        coordenadas(contadorx-1,contadory)
        gol(contadorx,contadory)
    else:
        canvas.move(1,3,0)
        contadorx = contadorx+1
        coordenadas(contadorx+1,contadory)
        gol(contadorx,contadory)
        
def gol(x,y):
    if(x>180 & x<210 and y >-18 & y<-50):
        ventana1 = Tk()
        ventana1.title("GOL")
        ventana1.geometry("100x100")
        ventana1.configure(background="black")
        mensaje = "Gol..!!!!!"
        msg = Message(ventana1, text = mensaje)
        msg.config(bg='black',fg ="white",font=('times', 20, 'italic'))
        msg.pack( )
        
canvas.place(x=0,y=0)
canvas2.place(x=650,y=150)

canvas.bind_all('<KeyPress-Up>',mover_imagen)
canvas.bind_all('<KeyPress-Down>',mover_imagen)
canvas.bind_all('<KeyPress-Left>',mover_imagen)
canvas.bind_all('<KeyPress-Right>',mover_imagen)
ventana.mainloop()
