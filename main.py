from tkinter import *

window = Tk()       # creating a new window

window.geometry('650x400')
window.minsize(650, 400)
window.maxsize(650, 40)
window.title("Website Blocker")

heading = Label(window, text="Website Blocker", font="arial")
heading.pack()

# we will be using the host file for this
# if the website is not already in the
# host file we should add it there
# reverse for the unblock

host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

def Blocker():
    website_lists = enter_website.get(1.0, END)
    website = list(website_lists.split(","))

    with open(host_path, "r+") as host_file:
        file_content = host_file.read()
        for web in website:
            if web in file_content:
                display = Label(window, text="Already blocked", font="arial")
                display.place(x=200, y=200)
                pass
            else:
                host_file.write(ip_address + " " + web + "\n")
                Label(window, text="Blocked", font="arial").place(x=200, y=200)

def Unblock():
    website_lists = enter_website.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.readlines()
        for web in Website:
            if web in website_lists:
                with open (host_path , 'r+') as f:
                    for line in file_content:
                        if line.strip(',') != website_lists:
                            f.write(line)
                            Label(window, text = "UnBlocked", font = 'arial').place(x=350,y =200)
                            pass
            else:
                display=Label(window, text = 'Already UnBlocked' , font = 'arial')
                display.place(x=350,y=200)

label1=Label(window, text ='Enter Website :' , font ='arial 13 bold')
label1.place(x=5 ,y=60)

enter_website = Text(window,font = 'arial',height='2', width = '40')
enter_website.place(x= 140,y = 60)

block_button = Button(window, text = 'Block',font = 'arial',pady = 5,command = Blocker ,width = 6, bg = 'royal blue1', activebackground = 'grey')
block_button.place(x = 230, y = 150)

unblock_button = Button(window, text = 'UnBlock',font = 'arial',pady = 5,command = Unblock ,width = 6, bg = 'royal blue1', activebackground = 'grey')
unblock_button.place(x = 350, y = 150)

window.mainloop()