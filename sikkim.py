#imported library tkinter
from tkinter import *
#impoted library for inserting photo
from PIL import ImageTk, Image


def click():
    entered_text= clicked.get()
    
    output.delete(0.0,END)
    try:
        clickeda = my_compdictionary[entered_text]
    except:
        clickeda ='Sorry no place found'
    output.insert(END,clickeda)

#main
window=Tk()
window.title("Sikkim")
window.geometry("700x650")
window.configure(background='#99ff99')

# photo inserted
photo1 = ImageTk.PhotoImage(file="download.jpg")
Label(window,image=photo1,bg='black').grid(row=0,column=0,sticky=E,pady="20")

#create label
Label(window,text='Enter the place of Sikkim to know about ',bg='black',fg='white',font='none 12 bold').grid(row=1,column=0,sticky=W,padx="20",pady ="10")
typeOption = Entry(window,width=30,bg='white')

#drop down
clicked = StringVar()

choices = ['Gangtok','Lachen','Gurudongmar Lake','Ravangla','Lachung','Yuksom']
clicked.set("PLACES")
typeOption = OptionMenu(window ,clicked, *choices,command = click ).grid(row=2,column=0,sticky=W,padx="20",pady="10")

Button(window, text='SUBMIT',width=14,command=click).grid(row=2,column=1,sticky=W, padx="20",pady ="10")


Label(window,text ='Information',bg='black',fg='white',font='none 12 bold').grid(row=3,column=0,sticky=W,padx="20",pady ="10")

output=Text(window,width=75,height=6,wrap=WORD,background='white',padx="20",pady ="10")
output.grid(row=5,column=0,columnspan=2,sticky=W ,padx="20",pady ="10")

#places information in dictionary
my_compdictionary={
    'Gangtok':'Area=19.2 km2 (7.4 sq mi)\n Elevation= 1,650 m (5,410 ft).\n Gangtok is a city, municipality, the capital and the largest town of the Indian state of Sikkim. It is also the headquarters of the East Sikkim district.\n For further details see the link : "https://en.wikipedia.org/wiki/Gangtok"',
    'Lachen':'Elevation: 2,600 m\n Languages : Nepali, Bhutia, Lepcha, Limbu, Newari, Rai, Gurung, Mangar, Sherpa, Tamang and Sunwar\n Lachen valley has almost everything a traveler could wish for a land of fairs and festivals, snow-clad mountains, lakes, valley of flora, fauna and a vibrant local culture. ',
    'Gurudongmar Lake': 'Surface elevation: 5,154 \n Area: 118 ha\n The lake, fed by glaciers, is located to the north of the Kangchengyao range, in a high plateau area connected with the Tibetan Plateau \n It provides one of the source streams which joins the Tso Lahmu and then form the source of the Teesta River.',
    'Ravangla': 'Ravangla or Rawangla or Ravongla is a small tourist town situated at an elevation of 8000 ft in South Sikkim district of the Indian state of Sikkim.\n Ravangla attracts a lot of Himalayan birds and is a bird watchers paradise. Birds like verditer flycatchers, blue-fronted redstarts, grey bushchats, dark-throated thrush, blue whistling-thrush, green-backed tit and white-browed fantails can be easily spotted.',
    'Lachung':'Lachung is a town and hill station in northeast Sikkim, India. It is located in the North Sikkim district near the border with Tibet.\n Lachung is at an elevation of about 9,600 feet (2,900 m) and at the confluence of the lachen and Lachung Rivers, both tributaries of the River Teesta.\n The word Lachung means "small pass". The town is approximately 125 kilometres (78 mi) from the capital Gangtok.',
    'Yuksom': 'Yuksom is a historical town in Geyzing subdivision of West Sikkim district in the Northeast Indian state of Sikkim.\n It was the first capital of Sikkim established in 1642 AD by Phuntsog Namgyal who was the first Chogyal of Sikkim. '
    }
Label(window,text='FUN FACT : SIKKIM IS THE LEAST POPULATED STATE IN INDIA.',bg='Blue',fg='white',font='none 12 bold').grid(row=6,column=0,sticky=W,padx="20",pady ="10")


Label(window,text='Click To Exit',bg='black',fg='white',font='none 12 bold').grid(row=9,column=0,sticky=W,padx="20",pady ="10")

#exit function
def close_window():
    window.destroy()
    exit()

Button(window,text='EXIT',width=14,command=close_window).grid(row=9,column=1,sticky=E,padx="20",pady ="10")

#run the mainloop
window.mainloop()
    
##DB-codes
