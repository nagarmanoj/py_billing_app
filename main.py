from tkinter import *
# functionality part
def total():
    soapprice = int(bathsoapEntry.get())*20
    facecreamprice = int(facecreamEntry.get())*100
    facewashprice = int(facewashEntry.get())*150
    hairsprayprice = int(hairsprayEntry.get())*200
    hairgelprice = int(hairgelEntry.get())*250
    bodylotionprice = int(bodylotionEntry.get())*300

    totalcosmaticprice = soapprice+facecreamprice+facewashprice+hairgelprice+hairsprayprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'{totalcosmaticprice} RS')
    cosmetictex = totalcosmaticprice*0.15
    cosmeticstexEntry.delete(0,END)
    cosmeticstexEntry.insert(0,f'{cosmetictex} RS')


    riceprice = int(riceEntry.get()) * 30
    oilprice = int(oilEntry.get()) * 100
    daalprice = int(dallEntry.get()) * 120
    wheatprice = int(wheatEntry.get()) * 50
    suggerprice = int(sugerEntry.get()) * 140
    teaprice = int(teaEntry.get()) * 80

    totalgroceryprice = riceprice + oilprice + daalprice + wheatprice + suggerprice + teaprice
    grocerypriceEntry.delete(0, END)
    grocerypriceEntry.insert(0, f'{totalgroceryprice} RS')
    grocerytex = totalgroceryprice * 0.09
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, f'{grocerytex} RS')

    maazaprice = int(maazaEntry.get())*50
    frootyPrice = int(frootiEntry.get())*20
    dewprice  = int(dewEntry.get())*30
    pepsiprice = int(pepsiEntry.get())*20
    spriteprice = int(spriteEntry.get())*45
    cocacolaprice = int(cocacolaEntry.get())*90

    totaldrinksprice = maazaprice+frootyPrice+dewprice+pepsiprice+spriteprice+cocacolaprice
    colddrinkpriceEntry.delete(0,END)
    colddrinkpriceEntry.insert(0,f'{totaldrinksprice} RS')
    drinktex = totaldrinksprice*0.08
    colddrinktaxEntry.delete(0,END)
    colddrinktaxEntry.insert(0,f'{drinktex} RS')


# GUI PART
root = Tk()
root.title("Retail Billing System")
root.geometry('1270x685')
# root.iconbitmap('icon.ico')
headingLabel = Label(root,text='Retail Billing System',font=('times new roman',30,'bold')
                     ,bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

#Customer detail frame
customer_detail_frame = LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold')
                                   ,bg='gray20',bd=8,fg='gold',relief=GROOVE)
customer_detail_frame.pack(fill=X)

nameLabel = Label(customer_detail_frame,text='Name',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
nameLabel.grid(row=0,column=0,padx=20)
nameEntry = Entry(customer_detail_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel = Label(customer_detail_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry = Entry(customer_detail_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel = Label(customer_detail_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)
billnumberEntry = Entry(customer_detail_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton = Button(customer_detail_frame,text='SEARCH',font=('arial',12,'bold'),bd=7)
searchButton.grid(row=0,column=6,padx=20,pady=8)

#Product Frame
productsFrame = Frame(root)
productsFrame.pack(fill=X)

#cosmic frame
cosmeticsFrame = LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold')
                                   ,bg='gray20',bd=8,fg='gold',relief=GROOVE)
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel = Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
bathsoapEntry = Entry(cosmeticsFrame,font=('arial',15),bd=5,width=10)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel = Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
facecreamEntry = Entry(cosmeticsFrame,font=('arial',15),bd=5,width=10)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

facewashLabel = Label(cosmeticsFrame,text='Face Wash',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
facewashEntry = Entry(cosmeticsFrame,font=('arial',15),bd=5,width=10)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)

hairsprayLabel = Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
hairsprayEntry = Entry(cosmeticsFrame,font=('arial',15),bd=5,width=10)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)

hairgelLabel = Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
hairgelEntry = Entry(cosmeticsFrame,font=('arial',15),bd=5,width=10)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)

bodylotionLabel = Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
bodylotionEntry = Entry(cosmeticsFrame,font=('arial',15),bd=5,width=10)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)

#frame grosely
groceryFrame = LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold')
                                   ,bg='gray20',bd=8,fg='gold',relief=GROOVE)
groceryFrame.grid(row=0,column=1)

riceLabel = Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
riceEntry = Entry(groceryFrame,font=('arial',15),bd=5,width=10)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)

oilLabel = Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
oilEntry = Entry(groceryFrame,font=('arial',15),bd=5,width=10)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

dallLabel = Label(groceryFrame,text='Dall',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
dallLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
dallEntry = Entry(groceryFrame,font=('arial',15),bd=5,width=10)
dallEntry.grid(row=2,column=1,pady=9,padx=10)
dallEntry.insert(0,0)

wheatLabel = Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
wheatEntry = Entry(groceryFrame,font=('arial',15),bd=5,width=10)
wheatEntry.grid(row=3,column=1,pady=9,padx=10)
wheatEntry.insert(0,0)

sugerLabel = Label(groceryFrame,text='Suger',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
sugerLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
sugerEntry = Entry(groceryFrame,font=('arial',15),bd=5,width=10)
sugerEntry.grid(row=4,column=1,pady=9,padx=10)
sugerEntry.insert(0,0)

teaLabel = Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
teaEntry = Entry(groceryFrame,font=('arial',15),bd=5,width=10)
teaEntry.grid(row=5,column=1,pady=9,padx=10)
teaEntry.insert(0,0)

#cold drinks frame
colddrinkFrame = LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold')
                                   ,bg='gray20',bd=8,fg='gold',relief=GROOVE)
colddrinkFrame.grid(row=0,column=2)

maazaLabel = Label(colddrinkFrame,text='Maaza',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
maazaEntry = Entry(colddrinkFrame,font=('arial',15),bd=5,width=10)
maazaEntry.grid(row=0,column=1,pady=9,padx=10)
maazaEntry.insert(0,0)

pepsiLabel = Label(colddrinkFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
pepsiEntry = Entry(colddrinkFrame,font=('arial',15),bd=5,width=10)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)

spriteLabel = Label(colddrinkFrame,text='Sprite',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
spriteEntry = Entry(colddrinkFrame,font=('arial',15),bd=5,width=10)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)

dewLabel = Label(colddrinkFrame,text='Dew',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
dewEntry = Entry(colddrinkFrame,font=('arial',15),bd=5,width=10)
dewEntry.grid(row=3,column=1,pady=9,padx=10)
dewEntry.insert(0,0)

frootiLabel = Label(colddrinkFrame,text='Frooti',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
frootiEntry = Entry(colddrinkFrame,font=('arial',15),bd=5,width=10)
frootiEntry.grid(row=4,column=1,pady=9,padx=10)
frootiEntry.insert(0,0)

cocacolaLabel = Label(colddrinkFrame,text='Coca Cola',font=('times new roman',15,'bold'),bg='gray20',
                  fg='white')
cocacolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
cocacolaEntry = Entry(colddrinkFrame,font=('arial',15),bd=5,width=10)
cocacolaEntry.grid(row=5,column=1,pady=9,padx=10)
cocacolaEntry.insert(0,0)

#bill frame
billFrame = LabelFrame(productsFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=10)
billareaLabel = Label(billFrame,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar = Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea = Text(billFrame,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

#bill menu frame
billmenuFrame = LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),
                           fg='gold',bd=8,relief=GROOVE,bg='gray20')
billmenuFrame.pack(fill=X)
cosmeticpriceLabel = Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',13,'bold'),bg='gray20',
                  fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')
cosmeticpriceEntry = Entry(billmenuFrame,font=('arial',15),bd=5,width=10)
cosmeticpriceEntry.grid(row=0,column=1,pady=6,padx=10)
cosmeticpriceEntry.insert(0,0)

grocerypriceLabel = Label(billmenuFrame,text='Grocery Price',font=('times new roman',13,'bold'),bg='gray20',
                  fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')
grocerypriceEntry = Entry(billmenuFrame,font=('arial',15),bd=5,width=10)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10)
grocerypriceEntry.insert(0,0)

colddrinkpriceLabel = Label(billmenuFrame,text='Cold Drink Price',font=('times new roman',13,'bold'),bg='gray20',
                  fg='white')
colddrinkpriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')
colddrinkpriceEntry = Entry(billmenuFrame,font=('arial',15),bd=5,width=10)
colddrinkpriceEntry.grid(row=2,column=1,pady=6,padx=10)
colddrinkpriceEntry.insert(0,0)

cosmeticstexLabel = Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',13,'bold'),bg='gray20',
                  fg='white')
cosmeticstexLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')
cosmeticstexEntry = Entry(billmenuFrame,font=('arial',15),bd=5,width=10)
cosmeticstexEntry.grid(row=0,column=3,pady=6,padx=10)
cosmeticstexEntry.insert(0,0)

grocerytaxLabel = Label(billmenuFrame,text='Grocery Tax',font=('times new roman',13,'bold'),bg='gray20',
                  fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')
grocerytaxEntry = Entry(billmenuFrame,font=('arial',15),bd=5,width=10)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10)
grocerytaxEntry.insert(0,0)

colddrinktaxLabel = Label(billmenuFrame,text='Cold Drink Tax',font=('times new roman',13,'bold'),bg='gray20',
                  fg='white')
colddrinktaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')
colddrinktaxEntry = Entry(billmenuFrame,font=('arial',15),bd=5,width=10)
colddrinktaxEntry.grid(row=2,column=3,pady=6,padx=10)
colddrinktaxEntry.insert(0,0)


buttonFrame = Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalBotton = Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',
                     bd=5,width=8,pady=10,command=total)
totalBotton.grid(row=0,column=0,pady=20,padx=5)

billBotton = Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',
                     bd=5,width=8,pady=10)
billBotton.grid(row=0,column=1,pady=20,padx=5)

emailBotton = Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',
                     bd=5,width=8,pady=10)
emailBotton.grid(row=0,column=2,pady=20,padx=5)

printBotton = Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',
                     bd=5,width=8,pady=10)
printBotton.grid(row=0,column=3,pady=20,padx=5)

clearBotton = Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',
                     bd=5,width=8,pady=10)
clearBotton.grid(row=0,column=4,pady=20,padx=5)


root.mainloop()