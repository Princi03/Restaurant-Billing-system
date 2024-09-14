from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox

root =Tk()

root.geometry('500x650')
root.maxsize(500,650)
root.minsize(500,650)

def submit():
    if (e1.get()=='' or e2.get()=='' or e3.get()=='' or e4.get()=='' or listcity.get()==''):
        messagebox.showerror('Error','All Fields Are Require')
    else:
        messagebox.showinfo('Welcome',f'Welcome {e1.get()}')
    
        name = e1.get()
        email=e2.get()
        phone=e3.get()
        city=listcity.get()
        add=e4.get()
        gen=gender.get()
    
        print('Name - ',name)
        print('Email - ',email)
        print('Mob No - ',phone)
        print('City - ',city)
        print('Address - ',add)
        print('Gender - ',gen)
    
img=Image.open("C:\\Users\\Neha\\Downloads\\user.png")
img = img.resize((90,90))
my = ImageTk.PhotoImage(img)
label = Label(root, image = my)
label.place(x=220,y=10)

l1=Label(root, text='Zaayka Registration Panel',font=('algerian',20,'bold'),fg='firebrick4')
l1.place(x = 50, y = 120)

l2=Label(root, text='Enter Name',font=('times new roman',15,'bold'))
l2.place(x=30,y=190)

e1= Entry(root,width=30,bd=3)
e1.place(x=260 , y=190)

l3=Label(root, text='Enter Email',font=('times new roman',15,'bold'))
l3.place(x=30,y=230)

e2= Entry(root,width=30,bd=3)
e2.place(x=260 , y=230)

l4=Label(root, text='Enter Mobile No',font=('times new roman',15,'bold'))
l4.place(x=30,y=270)

e3= Entry(root,width=30,bd=3)
e3.place(x=260 , y=270)

l5 = Label(root, text = 'Select City',font=('times new roman',15,'bold'))
l5.place(x = 30, y =310)

lists = ['Kanpur','Prayag Raj','Varanasi','Patna','Agra','Mirzapur','Jhansi','Lucknow','Mathura','Noida','Meerut']
listcity = StringVar(root)
listcity.set('Select Your City')
menu= OptionMenu(root, listcity, *lists)
menu.place(x=260, y=310, width = 190)

l6=Label(root, text='Enter Address',font=('times new roman',15,'bold'))
l6.place(x=30,y=350)
e4= Entry(root,width=30,bd=3)
e4.place(x=260 , y=350)

l7 = Label(root, text ='Select Gender',font=('times new roman',15,'bold'))
l7.place(x = 30, y =390)
gender=StringVar()
g1 =  Radiobutton(root, text='Male',variable=gender,value='Male',font=('times new roman',15,'bold'))
g1.select()
g1.place(x=260, y= 390)

g2 =  Radiobutton(root, text='Female',variable=gender,value='Female',font=('times new roman',15,'bold'))
g2.deselect()
g2.place(x=360, y= 390)

l8 = Label(root, text = 'Select Service Type',font=('times new roman',15,'bold'))
l8.place(x = 30, y =430)

var1 = StringVar()
var2 = StringVar()

l9 = Checkbutton(root, text = 'Pick- up',font=('times new roman',15,'bold'))
l9.deselect()
l9.place(x = 260, y =430)

l10 = Checkbutton(root, text = 'Packing',font=('times new roman',15,'bold'))
l10.select()
l10.place(x = 360, y =430)

button = Button(root, text = 'Submit',font=('times new roman',15,'bold'),fg='white',cursor='hand2',bg='blue',width=34,command=submit)
button.place(x = 32, y =520)

#button2 = Button(root, text = 'Exit',font=('times new roman',15,'bold'),cursor='hand2',fg='white',bg='firebrick4',width=34, command =quit)
#button2.place(x = 32, y =570)

root.mainloop()
