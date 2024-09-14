from tkinter import*
from tkinter import filedialog , messagebox
import random
import time
import loginfinal                                        # user defined module
from PIL import ImageTk, Image


#-------functions-------------------------------------------------------------------

def save():

    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        url = filedialog.asksaveasfile(mode='w',defaultextension='.txt')    

        if url == None:
            pass
        else:
            bill_data=textReceipt.get(1.0,END)   #to get everything from starting to end
            url.write(bill_data)
            url.close()

            messagebox.showinfo('Information','Bill Saved Successfully')
    

def reset():

#------------- clicking on reset, the receipt area will be clear from all the text----------    
    textReceipt.delete(1.0,END)
#----------------to set the entry boxes to zero on resetting
    e_roti.set('0')
    e_daal.set('0')
    e_rice.set('0')
    e_fish.set('0')
    e_sabji.set('0')
    e_mutton.set('0')
    e_chicken.set('0')
    e_breadomlet.set('0')
    e_vegbiryani.set('0')

    e_tea.set('0')
    e_coke.set('0')
    e_soda.set('0')
    e_sattu.set('0')
    e_lassi.set('0')
    e_faluda.set('0')
    e_mattha.set('0')
    e_coffee.set('0')
    e_aamras.set('0')

    e_dosa.set('0')
    e_idli.set('0')
    e_vada.set('0')
    e_appam.set('0')
    e_uttapam.set('0')
    e_soup.set('0')
    e_noodles.set('0')
    e_chowmein.set('0')
    e_manchurian.set('0')

    e_kulfi.set('0')
    e_modak.set('0')
    e_halwa.set('0')
    e_barfi.set('0')
    e_ghewar.set('0')
    e_sandesh.set('0')
    e_pudding.set('0')
    e_rasmalai.set('0')
    e_shrikhand.set('0')

#-------------to again disable the entry boxes-------------

    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textrice.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textmutton.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    textbreadomlet.config(state=DISABLED)
    textvegbiryani.config(state=DISABLED)
    
    texttea.config(state=DISABLED)
    textcoke.config(state=DISABLED)
    textsoda.config(state=DISABLED)
    textsattu.config(state=DISABLED)
    textlassi.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textmattha.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textaamras.config(state=DISABLED)
    
    textdosa.config(state=DISABLED)
    textidli.config(state=DISABLED)
    textvada.config(state=DISABLED)
    textappam.config(state=DISABLED)
    textuttapam.config(state=DISABLED)
    textsoup.config(state=DISABLED)
    textnoodles.config(state=DISABLED)
    textchowmein.config(state=DISABLED)
    textmanchurian.config(state=DISABLED)
    
    textkulfi.config(state=DISABLED)
    textmodak.config(state=DISABLED)
    texthalwa.config(state=DISABLED)
    textbarfi.config(state=DISABLED)
    textghewar.config(state=DISABLED)
    textsandesh.config(state=DISABLED)
    textpudding.config(state=DISABLED)
    textrasmalai.config(state=DISABLED)
    textshrikhand.config(state=DISABLED)

#------to uncheck the checked checkbuttons---------------------------------

    var1.set('0')
    var2.set('0')
    var3.set('0')
    var4.set('0')
    var5.set('0')
    var6.set('0')
    var7.set('0')
    var8.set('0')
    var9.set('0')
    var10.set('0')
    var11.set('0')
    var12.set('0')
    var13.set('0')
    var14.set('0')
    var15.set('0')
    var16.set('0')
    var17.set('0')
    var18.set('0')
    var19.set('0')
    var20.set('0')
    var21.set('0')
    var22.set('0')
    var23.set('0')
    var24.set('0')
    var25.set('0')
    var26.set('0')
    var27.set('0')
    var28.set('0')
    var29.set('0')
    var30.set('0')
    var31.set('0')
    var32.set('0')
    var33.set('0')
    var34.set('0')
    var35.set('0')
    var36.set('0')


# ----to clear the total cost area on resetting----------------

    costoffoodvar.set('')
    costofbeveragesvar.set('')
    costofsouthindianvar.set('')
    costofdessertsvar.set('')
    subtotalvar.set('')
    servicechargesvar.set('')
    totalvar.set('')


def roti():
    if var1.get()==1:                   # if the roti checkbox is checked
        textroti.config(state=NORMAL)   # to update the disabled state to normal
        textroti.delete(0,END)           # to delete the previously exixsting zero
        textroti.focus()                 # for the cursor to blink cntsly in the qty box
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')                  #to set the state back to normal if checkbutton is not chckd


def daal():
    if var2.get()==1:
        textdaal.config(state=NORMAL)   
        textdaal.delete(0,END)           
        textdaal.focus()                 
    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')                 

def rice():
    if var3.get()==1:
        textrice.config(state=NORMAL)   
        textrice.delete(0,END)           
        textrice.focus()                 
    else:
        textrice.config(state=DISABLED)
        e_rice.set('0')                 

def fish():
    if var4.get()==1:
        textfish.config(state=NORMAL)   
        textfish.delete(0,END)           
        textfish.focus()                 
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')                 

def sabji():
    if var5.get()==1:
        textsabji.config(state=NORMAL)   
        textsabji.delete(0,END)           
        textsabji.focus()                 
    else:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')                 

def mutton():
    if var6.get()==1:
        textmutton.config(state=NORMAL)   
        textmutton.delete(0,END)           
        textmutton.focus()                 
    else:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')                 

def chicken():
    if var7.get()==1:
        textchicken.config(state=NORMAL)   
        textchicken.delete(0,END)           
        textchicken.focus()                 
    else:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')                 

def breadomlet():
    if var8.get()==1:
        textbreadomlet.config(state=NORMAL)   
        textbreadomlet.delete(0,END)           
        textbreadomlet.focus()                 
    else:
        textbreadomlet.config(state=DISABLED)
        e_breadomlet.set('0')                 

def vegbiryani():
    if var9.get()==1:
        textvegbiryani.config(state=NORMAL)   
        textvegbiryani.delete(0,END)           
        textvegbiryani.focus()                 
    else:
        textvegbiryani.config(state=DISABLED)
        e_vegbiryani.set('0')                 

def tea():
    if var10.get()==1:
        texttea.config(state=NORMAL)   
        texttea.delete(0,END)           
        texttea.focus()                 
    else:
        texttea.config(state=DISABLED)
        e_tea.set('0')                 

def coke():
    if var11.get()==1:
        textcoke.config(state=NORMAL)   
        textcoke.delete(0,END)           
        textcoke.focus()                 
    else:
        textcoke.config(state=DISABLED)
        e_coke.set('0')                 

def soda():
    if var12.get()==1:
        textsoda.config(state=NORMAL)   
        textsoda.delete(0,END)           
        textsoda.focus()                 
    else:
        textsoda.config(state=DISABLED)
        e_soda.set('0')                 

def sattu():
    if var13.get()==1:
        textsattu.config(state=NORMAL)   
        textsattu.delete(0,END)           
        textsattu.focus()                 
    else:
        textsattu.config(state=DISABLED)
        e_sattu.set('0')                 

def lassi():
    if var14.get()==1:
        textlassi.config(state=NORMAL)   
        textlassi.delete(0,END)           
        textlassi.focus()                 
    else:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')                 

def faluda():
    if var15.get()==1:
        textfaluda.config(state=NORMAL)   
        textfaluda.delete(0,END)           
        textfaluda.focus()                 
    else:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')                 

def mattha():
    if var16.get()==1:
        textmattha.config(state=NORMAL)   
        textmattha.delete(0,END)           
        textmattha.focus()                 
    else:
        textmattha.config(state=DISABLED)
        e_mattha.set('0')                 

def coffee():
    if var17.get()==1:
        textcoffee.config(state=NORMAL)   
        textcoffee.delete(0,END)           
        textcoffee.focus()                 
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')                 

def aamras():
    if var18.get()==1:
        textaamras.config(state=NORMAL)   
        textaamras.delete(0,END)           
        textaamras.focus()                 
    else:
        textaamras.config(state=DISABLED)
        e_aamras.set('0')                 

def dosa():
    if var19.get()==1:
        textdosa.config(state=NORMAL)   
        textdosa.delete(0,END)           
        textdosa.focus()                 
    else:
        textdosa.config(state=DISABLED)
        e_dosa.set('0')                 

def idli():
    if var20.get()==1:
        textidli.config(state=NORMAL)   
        textidli.delete(0,END)           
        textidli.focus()                 
    else:
        textidli.config(state=DISABLED)
        e_idli.set('0')                 

def vada():
    if var21.get()==1:
        textvada.config(state=NORMAL)   
        textvada.delete(0,END)           
        textvada.focus()                 
    else:
        textvada.config(state=DISABLED)
        e_vada.set('0')                 

def appam():
    if var22.get()==1:
        textappam.config(state=NORMAL)   
        textappam.delete(0,END)           
        textappam.focus()                 
    else:
        textappam.config(state=DISABLED)
        e_appam.set('0')                 

def uttapam():
    if var23.get()==1:
        textuttapam.config(state=NORMAL)   
        textuttapam.delete(0,END)           
        textuttapam.focus()                 
    else:
        textuttapam.config(state=DISABLED)
        e_uttapam.set('0')                 

def soup():
    if var24.get()==1:
        textsoup.config(state=NORMAL)   
        textsoup.delete(0,END)           
        textsoup.focus()                 
    else:
        textsoup.config(state=DISABLED)
        e_soup.set('0')                 

def noodles():
    if var25.get()==1:
        textnoodles.config(state=NORMAL)   
        textnoodles.delete(0,END)           
        textnoodles.focus()                 
    else:
        textnoodles.config(state=DISABLED)
        e_noodles.set('0')                 

def chowmein():
    if var26.get()==1:
        textchowmein.config(state=NORMAL)   
        textchowmein.delete(0,END)           
        textchowmein.focus()                 
    else:
        textchowmein.config(state=DISABLED)
        e_chowmein.set('0')                 

def manchurian():
    if var27.get()==1:
        textmanchurian.config(state=NORMAL)   
        textmanchurian.delete(0,END)           
        textmanchurian.focus()                 
    else:
        textmanchurian.config(state=DISABLED)
        e_manchurian.set('0')                 

def kulfi():
    if var28.get()==1:
        textkulfi.config(state=NORMAL)   
        textkulfi.delete(0,END)           
        textkulfi.focus()                 
    else:
        textkulfi.config(state=DISABLED)
        e_kulfi.set('0')                 

def modak():
    if var29.get()==1:
        textmodak.config(state=NORMAL)   
        textmodak.delete(0,END)           
        textmodak.focus()                 
    else:
        textmodak.config(state=DISABLED)
        e_modak.set('0')                 

def halwa():
    if var30.get()==1:
        texthalwa.config(state=NORMAL)   
        texthalwa.delete(0,END)           
        texthalwa.focus()                 
    else:
        texthalwa.config(state=DISABLED)
        e_halwa.set('0')                 

def barfi():
    if var31.get()==1:
        textbarfi.config(state=NORMAL)   
        textbarfi.delete(0,END)           
        textbarfi.focus()                 
    else:
        textbarfi.config(state=DISABLED)
        e_barfi.set('0')                 

def ghewar():
    if var32.get()==1:
        textghewar.config(state=NORMAL)   
        textghewar.delete(0,END)           
        textghewar.focus()                 
    else:
        textghewar.config(state=DISABLED)
        e_ghewar.set('0')

def sandesh():
    if var33.get()==1:
        textsandesh.config(state=NORMAL)   
        textsandesh.delete(0,END)           
        textsandesh.focus()                 
    else:
        textsandesh.config(state=DISABLED)
        e_sandesh.set('0')     

def pudding():
    if var34.get()==1:
        textpudding.config(state=NORMAL)   
        textpudding.delete(0,END)           
        textpudding.focus()                 
    else:
        textpudding.config(state=DISABLED)
        e_pudding.set('0')

def rasmalai():
    if var35.get()==1:
        textrasmalai.config(state=NORMAL)   
        textrasmalai.delete(0,END)           
        textrasmalai.focus()                 
    else:
        textrasmalai.config(state=DISABLED)
        e_rasmalai.set('0')     

def shrikhand():
    if var36.get()==1:
        textshrikhand.config(state=NORMAL)   
        textshrikhand.delete(0,END)           
        textshrikhand.focus()                 
    else:
        textshrikhand.config(state=DISABLED)
        e_shrikhand.set('0')     




#===============================================================================================

def totalcost():

    global priceoffood, priceofbeverages, priceofsouthindian, priceofdesserts, subtotalofItems

    if (var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or \
       var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or\
       var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or\
       var19.get() != 0 or var20.get() != 0 or var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or\
       var25.get() != 0 or var26.get() != 0 or var27.get() != 0 or var28.get() != 0 or var29.get() != 0 or var30.get() != 0 or\
       var31.get() != 0 or var32.get() != 0 or var33.get() != 0 or var34.get() != 0 or var35.get() != 0 or var36.get() != 0 ):
    
        item1=int(e_roti.get())           #int() bcz .get() returns string value..so to convert it in int for mathematical operations
        item2=int(e_daal.get())
        item3=int(e_rice.get())
        item4=int(e_fish.get())
        item5=int(e_sabji.get())
        item6=int(e_mutton.get())
        item7=int(e_chicken.get())
        item8=int(e_breadomlet.get())
        item9=int(e_vegbiryani.get())

        item10=int(e_tea.get())
        item11=int(e_coke.get())
        item12=int(e_soda.get())
        item13=int(e_sattu.get())
        item14=int(e_lassi.get())
        item15=int(e_faluda.get())
        item16=int(e_mattha.get())
        item17=int(e_coffee.get())
        item18=int(e_aamras.get())

        item19=int(e_dosa.get())
        item20=int(e_idli.get())
        item21=int(e_vada.get())
        item22=int(e_appam.get())
        item23=int(e_uttapam.get())
        item24=int(e_soup.get())
        item25=int(e_noodles.get())
        item26=int(e_chowmein.get())
        item27=int(e_manchurian.get())

        item28=int(e_kulfi.get())
        item29=int(e_modak.get())
        item30=int(e_halwa.get())
        item31=int(e_barfi.get())
        item32=int(e_ghewar.get())
        item33=int(e_sandesh.get())
        item34=int(e_pudding.get())
        item35=int(e_rasmalai.get())
        item36=int(e_shrikhand.get())
    

        priceoffood=(item1*7)+(item2*35)+(item3*45)+(item4*105)+(item5*65)+(item6*210)+(item7*130)+(item8*60)+(item9*150)

        priceofbeverages=(item10*25)+(item11*50)+(item12*35)+(item13*40)+(item14*60)+(item15*75)+(item16*35)+(item17*60)+(item18*55)

        priceofsouthindian=(item19*70)+(item20*40)+(item21*55)+(item22*60)+(item23*65)+(item24*70)+(item25*85)+(item26*90)+(item27*75)

        priceofdesserts=(item28*45)+(item29*25)+(item30*55)+(item31*45)+(item32*80)+(item33*60)+(item34*50)+(item35*35)+(item36*60)

#------------individual cost of categories---------------------------------
    
        costoffoodvar.set(str(priceoffood)+ ' Rs')
        costofbeveragesvar.set(str(priceofbeverages)+ ' Rs')
        costofsouthindianvar.set(str(priceofsouthindian)+ ' Rs')
        costofdessertsvar.set(str(priceofdesserts)+ ' Rs')


        subtotalofItems=priceoffood + priceofbeverages + priceofsouthindian + priceofdesserts
        subtotalvar.set(str(subtotalofItems)+ ' Rs')


        servicechargesvar.set('50 Rs')

    
    
        totalcost=subtotalofItems + 50 
        totalvar.set(str(totalcost)+ ' Rs')

    else:
        
        messagebox.showerror('Error','No Item Is Selected !')
        


def receipt():
    
    if ( costoffoodvar.get() != '' or costofbeveragesvar.get() != '' or costofsouthindianvar.get() != '' or costofdessertsvar.get() != 0):
        
        x=random.randint(1000,10000)
        billnumber='Bill'+str(x)
        date=time.strftime('%d-%m-%Y')
        textReceipt.insert(END,'Bill Ref:' + billnumber+ '\t\t'+ date + '\n')
        textReceipt.insert(END,'***************\n')

        textReceipt.insert(END,'Items:\t Cost of Items(Rs)\n')
        textReceipt.insert(END,'***************\n')

        if e_roti.get()!='0':
            textReceipt.insert(END,f'Roti\t\t{int(e_roti.get())*7}\n\n')

        if e_daal.get()!='0':
            textReceipt.insert(END,f'Daal\t\t{int(e_daal.get())*35}\n\n')

        if e_rice.get()!='0':
            textReceipt.insert(END,f'Rice\t\t{int(e_rice.get())*45}\n\n')

        if e_fish.get()!='0':
            textReceipt.insert(END,f'Fish\t\t{int(e_fish.get())*105}\n\n')

        if e_sabji.get()!='0':
            textReceipt.insert(END,f'Sabji\t\t{int(e_sabji.get())*65}\n\n')

        if e_mutton.get()!='0':
            textReceipt.insert(END,f'Mutton\t\t{int(e_mutton.get())*210}\n\n')

        if e_chicken.get()!='0':
            textReceipt.insert(END,f'Chicken\t\t{int(e_chicken.get())*130}\n\n')

        if e_breadomlet.get()!='0':
            textReceipt.insert(END,f'Bread Omlet\t\t{int(e_breadomlet.get())*60}\n\n')

        if e_vegbiryani.get()!='0':
            textReceipt.insert(END,f'Veg Biryani\t\t{int(e_vegbiryani.get())*150}\n\n')

        if e_tea.get()!='0':
            textReceipt.insert(END,f'Tea\t\t{int(e_tea.get())*25}\n\n')

        if e_coke.get()!='0':
            textReceipt.insert(END,f'Coke\t\t{int(e_coke.get())*50}\n\n')

        if e_soda.get()!='0':
            textReceipt.insert(END,f'Soda\t\t{int(e_soda.get())*35}\n\n')

        if e_sattu.get()!='0':
            textReceipt.insert(END,f'Sattu\t\t{int(e_sattu.get())*40}\n\n')

        if e_lassi.get()!='0':
            textReceipt.insert(END,f'Lassi\t\t{int(e_lassi.get())*60}\n\n')

        if e_faluda.get()!='0':
            textReceipt.insert(END,f'Faluda\t\t{int(e_faluda.get())*75}\n\n')

        if e_mattha.get()!='0':
            textReceipt.insert(END,f'Mattha\t\t{int(e_mattha.get())*35}\n\n')

        if e_coffee.get()!='0':
            textReceipt.insert(END,f'Coffee\t\t{int(e_coffee.get())*60}\n\n')

        if e_aamras.get()!='0':
            textReceipt.insert(END,f'Aamras\t\t{int(e_aamras.get())*55}\n\n')

        if e_dosa.get()!='0':
            textReceipt.insert(END,f'Dosa\t\t{int(e_dosa.get())*70}\n\n')

        if e_idli.get()!='0':
            textReceipt.insert(END,f'Idli\t\t{int(e_idli.get())*40}\n\n')

        if e_vada.get()!='0':
            textReceipt.insert(END,f'Vada\t\t{int(e_vada.get())*55}\n\n')

        if e_appam.get()!='0':
            textReceipt.insert(END,f'Appam\t\t{int(e_appam.get())*60}\n\n')

        if e_uttapam.get()!='0':
            textReceipt.insert(END,f'Uttapam\t\t{int(e_uttapam.get())*65}\n\n')

        if e_soup.get()!='0':
            textReceipt.insert(END,f'Soup\t\t{int(e_soup.get())*70}\n\n')

        if e_noodles.get()!='0':
            textReceipt.insert(END,f'Noodles\t\t{int(e_noodles.get())*85}\n\n')

        if e_chowmein.get()!='0':
            textReceipt.insert(END,f'Chowmein\t\t{int(e_chowmein.get())*90}\n\n')

        if e_manchurian.get()!='0':
            textReceipt.insert(END,f'Manchurian\t\t{int(e_manchurian.get())*75}\n\n')

        if e_kulfi.get()!='0':
            textReceipt.insert(END,f'Kulfi\t\t{int(e_kulfi.get())*45}\n\n')

        if e_modak.get()!='0':
            textReceipt.insert(END,f'Modak\t\t{int(e_modak.get())*25}\n\n')

        if e_halwa.get()!='0':
            textReceipt.insert(END,f'Halwa\t\t{int(e_halwa.get())*55}\n\n')

        if e_barfi.get()!='0':
            textReceipt.insert(END,f'Barfi\t\t{int(e_barfi.get())*45}\n\n')

        if e_ghewar.get()!='0':
            textReceipt.insert(END,f'Ghewar\t\t{int(e_ghewar.get())*80}\n\n')

        if e_sandesh.get()!='0':
            textReceipt.insert(END,f'Sandesh\t\t{int(e_sandesh.get())*60}\n\n')

        if e_pudding.get()!='0':
            textReceipt.insert(END,f'Pudding\t\t{int(e_pudding.get())*50}\n\n')

        if e_rasmalai.get()!='0':
            textReceipt.insert(END,f'Rasmalai\t\t{int(e_rasmalai.get())*35}\n\n')

        if e_shrikhand.get()!='0':
            textReceipt.insert(END,f'Shrikhand\t\t{int(e_shrikhand.get())*60}\n\n')


    
        textReceipt.insert(END,'***************\n')

        if costoffoodvar.get()!='0 Rs':
            textReceipt.insert(END,f'Food Total\t\t {priceoffood} Rs\n\n')
        if costofbeveragesvar.get()!='0 Rs':
            textReceipt.insert(END,f'Beverages Total\t\t {priceofbeverages} Rs\n\n')
        if costofsouthindianvar.get()!='0 Rs':
            textReceipt.insert(END,f'South Indian Total\t\t {priceofsouthindian} Rs\n\n')
        if costofdessertsvar.get()!='0 Rs':
            textReceipt.insert(END,f'Desserts Total\t\t {priceofdesserts} Rs\n\n')



        textReceipt.insert(END,f'Sub Total\t\t{subtotalofItems} Rs\n\n')
        textReceipt.insert(END,f'Service Charges\t\t{50} Rs\n\n')
        textReceipt.insert(END,f'Total\t\t{subtotalofItems+ 50} Rs\n\n')
    
        textReceipt.insert(END,'***************\n')

        textReceipt.insert(END,'            Have A Good Day :)\n')
        textReceipt.insert(END,'--------Thank You for visiting Us--------\n')

    else:
        messagebox.showerror('Error','No Item Is Selected')
    


root = Tk()



root.geometry('1270x680')
def submit(name, email, phone, city, add, gen):
    print(name)
    print(email)
    print(phone)
    print(city)
    print(add)
    print(gen)
    
def openLoginScreen():
    loginscreen =Toplevel(root)
    
    loginscreen.geometry('500x650')
    loginscreen.maxsize(500,650)
    loginscreen.minsize(500,650)
    
    img=Image.open("C:\\Users\\Neha\\Downloads\\user.png")
    img = img.resize((90,90))
    my = ImageTk.PhotoImage(img)
    label = Label(loginscreen, image = my)
    label.place(x=220,y=10)
    
    l1=Label(loginscreen, text='Zaayka Registration Panel',font=('algerian',20,'bold'),fg='firebrick4')
    l1.place(x = 50, y = 120)
    
    l2=Label(loginscreen, text='Enter Name',font=('times new roman',15,'bold'))
    l2.place(x=30,y=190)
    
    e1= Entry(loginscreen,width=30,bd=3)
    e1.place(x=260 , y=190)
    
    l3=Label(loginscreen, text='Enter Email',font=('times new roman',15,'bold'))
    l3.place(x=30,y=230)
    
    e2= Entry(loginscreen,width=30,bd=3)
    e2.place(x=260 , y=230)
    
    l4=Label(loginscreen, text='Enter Mobile No',font=('times new roman',15,'bold'))
    l4.place(x=30,y=270)
    
    e3= Entry(loginscreen,width=30,bd=3)
    e3.place(x=260 , y=270)
    
    l5 = Label(loginscreen, text = 'Select City',font=('times new roman',15,'bold'))
    l5.place(x = 30, y =310)
    
    lists = ['Kanpur','Prayag Raj','Varanasi','Patna','Agra','Mirzapur','Jhansi','Lucknow','Mathura','Noida','Meerut']
    listcity = StringVar(loginscreen)
    listcity.set('Select Your City')
    menu= OptionMenu(loginscreen, listcity, *lists)
    menu.place(x=260, y=310, width = 190)
    
    l6=Label(loginscreen, text='Enter Address',font=('times new roman',15,'bold'))
    l6.place(x=30,y=350)
    e4= Entry(loginscreen,width=30,bd=3)
    e4.place(x=260 , y=350)
    
    l7 = Label(loginscreen, text ='Select Gender',font=('times new roman',15,'bold'))
    l7.place(x = 30, y =390)
    gender=StringVar()
    g1 =  Radiobutton(loginscreen, text='Male',variable=gender,value='Male',font=('times new roman',15,'bold'))
    g1.select()
    g1.place(x=260, y= 390)
    
    g2 =  Radiobutton(loginscreen, text='Female',variable=gender,value='Female',font=('times new roman',15,'bold'))
    g2.deselect()
    g2.place(x=360, y= 390)
    
    
    l8 = Label(loginscreen, text = 'Select Service Type',font=('times new roman',15,'bold'))
    l8.place(x = 30, y =430)
    
    var1 = StringVar()
    var2 = StringVar()
    
    l9 = Checkbutton(loginscreen, text = 'Pick- up',font=('times new roman',15,'bold'))
    l9.deselect()
    l9.place(x = 260, y =430)
    
    l10 = Checkbutton(loginscreen, text = 'Packing',font=('times new roman',15,'bold'))
    l10.select()
    l10.place(x = 360, y =430)
    
    button = Button(loginscreen, text = 'Submit',font=('times new roman',15,'bold'),fg='white',cursor='hand2',bg='blue',width=34,command=lambda:submit(e1.get(), e2.get(), e3.get(), listcity.get(), e4.get(), gender.get()))
    button.place(x = 32, y =520)
    
    button2 = Button(loginscreen, text = 'Exit',font=('times new roman',15,'bold'),cursor='hand2',fg='white',bg='firebrick4',width=34, command =quit)
    button2.place(x = 32, y =570)

#root.resizable(0,0)
root.title("Restaurant Management and Billing System by Neha")
root.config(bg="darkgreen")

topFrame = Frame(root,bd=10,relief=RIDGE)
topFrame.pack(side=TOP)
labelTitle=Label(topFrame,text="Zaayka Restaurant welcomes you.....\n since 1980s",font=('algerian',30,'bold'),fg='white',bd=9,bg='red4',width=51)
labelTitle.grid(row=0,column=0)


#frames

menuFrame=Frame(root,bd=10,relief=RIDGE, bg='firebrick4')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='firebrick4',pady=20)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',17,'bold'),bd=10,relief=RIDGE,fg='red4')
foodFrame.pack(side=LEFT)

beveragesFrame=LabelFrame(menuFrame,text='Beverages',font=('arial',17,'bold'),bd=10,relief=RIDGE,fg='red4')
beveragesFrame.pack(side=LEFT)

southindianFrame=LabelFrame(menuFrame,text='South Indian/Chinese',font=('arial',17,'bold'),bd=10,relief=RIDGE,fg='red4')
southindianFrame.pack(side=LEFT)

dessertsFrame=LabelFrame(menuFrame,text='Desserts',font=('arial',17,'bold'),bd=10,relief=RIDGE,fg='red4')
dessertsFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

receiptFrame=Frame(rightFrame,bd=4,relief=RIDGE)
receiptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,padx=45)
buttonFrame.pack(side=TOP)


#Variables

#---food variables---

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()

#---entry food quantity-------

e_roti=StringVar()
e_daal=StringVar()
e_rice=StringVar()
e_fish=StringVar()
e_sabji=StringVar()
e_mutton=StringVar()
e_chicken=StringVar()
e_breadomlet=StringVar()
e_vegbiryani=StringVar()

#------for initially setting to 0--------

e_roti.set('0')
e_daal.set('0')
e_rice.set('0')
e_fish.set('0')
e_sabji.set('0')
e_mutton.set('0')
e_chicken.set('0')
e_breadomlet.set('0')
e_vegbiryani.set('0')

#---beverages variables---

var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()

#----entry beverages quantity----

e_tea=StringVar()
e_coke=StringVar()
e_soda=StringVar()
e_sattu=StringVar()
e_lassi=StringVar()
e_faluda=StringVar()
e_mattha=StringVar()
e_coffee=StringVar()
e_aamras=StringVar()

#----------for initially setting to zero-------

e_tea.set('0')
e_coke.set('0')
e_soda.set('0')
e_sattu.set('0')
e_lassi.set('0')
e_faluda.set('0')
e_mattha.set('0')
e_coffee.set('0')
e_aamras.set('0')

#-----south indian ---------

var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

#-----entry south indian quantity-----

e_dosa=StringVar()
e_idli=StringVar()
e_vada=StringVar()
e_appam=StringVar()
e_uttapam=StringVar()
e_soup=StringVar()
e_noodles=StringVar()
e_chowmein=StringVar()
e_manchurian=StringVar()

#------for initially setting to zero-----

e_dosa.set('0')
e_idli.set('0')
e_vada.set('0')
e_appam.set('0')
e_uttapam.set('0')
e_soup.set('0')
e_noodles.set('0')
e_chowmein.set('0')
e_manchurian.set('0')

#-----desserts------------------

var28=IntVar()
var29=IntVar()
var30=IntVar()
var31=IntVar()
var32=IntVar()
var33=IntVar()
var34=IntVar()
var35=IntVar()
var36=IntVar()

#--------entry desserts----------

e_kulfi=StringVar()
e_modak=StringVar()
e_halwa=StringVar()
e_barfi=StringVar()
e_ghewar=StringVar()
e_sandesh=StringVar()
e_pudding=StringVar()
e_rasmalai=StringVar()
e_shrikhand=StringVar()


#------------for initially setting to zero--------

e_kulfi.set('0')
e_modak.set('0')
e_halwa.set('0')
e_barfi.set('0')
e_ghewar.set('0')
e_sandesh.set('0')
e_pudding.set('0')
e_rasmalai.set('0')
e_shrikhand.set('0')


#----------cost label-----------------------

costoffoodvar=StringVar()
costofbeveragesvar=StringVar()
costofsouthindianvar=StringVar()
costofdessertsvar=StringVar()
subtotalvar=StringVar()
packingchargesvar=StringVar()
servicechargesvar=StringVar()
totalvar=StringVar()




#----------food-----

roti=Checkbutton(foodFrame,text='Roti   7/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)

daal=Checkbutton(foodFrame,text='Daal   35/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var2,command=daal)
daal.grid(row=1,column=0,sticky=W)

rice=Checkbutton(foodFrame,text='Rice   45/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var3,command=rice)
rice.grid(row=2,column=0,sticky=W)

fish=Checkbutton(foodFrame,text='Fish   105/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var4,command=fish)
fish.grid(row=3,column=0,sticky=W)

sabji=Checkbutton(foodFrame,text='Sabji     65/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var5,command=sabji)
sabji.grid(row=4,column=0,sticky=W)

mutton=Checkbutton(foodFrame,text='Mutton   210/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var6,command=mutton)
mutton.grid(row=5,column=0,sticky=W)

chicken=Checkbutton(foodFrame,text='Chicken   130/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var7,command=chicken)
chicken.grid(row=6,column=0,sticky=W)

breadomlet=Checkbutton(foodFrame,text='Bread Omlet   60/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var8,command=breadomlet)
breadomlet.grid(row=7,column=0,sticky=W)

vegbiryani=Checkbutton(foodFrame,text='Veg Biryani   150/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var9,command=vegbiryani)
vegbiryani.grid(row=8,column=0,sticky=W)




#ENTRY FIELDS FOR FOOD ITEMS--------------------

textroti=Entry(foodFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textdaal=Entry(foodFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=1,column=1)

textrice=Entry(foodFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_rice)
textrice.grid(row=2,column=1)

textfish=Entry(foodFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_fish)
textfish.grid(row=3,column=1)

textsabji=Entry(foodFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_sabji)
textsabji.grid(row=4,column=1)

textmutton=Entry(foodFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_mutton)
textmutton.grid(row=5,column=1)

textchicken=Entry(foodFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_chicken)
textchicken.grid(row=6,column=1)

textbreadomlet=Entry(foodFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_breadomlet)
textbreadomlet.grid(row=7,column=1)

textvegbiryani=Entry(foodFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_vegbiryani)
textvegbiryani.grid(row=8,column=1)



#beverages name display-------

tea=Checkbutton(beveragesFrame,text='Tea  25/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var10,command=tea)
tea.grid(row=0,column=0,sticky=W)

coke=Checkbutton(beveragesFrame,text='Coke   50/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var11,command=coke)
coke.grid(row=1,column=0,sticky=W)

soda=Checkbutton(beveragesFrame,text='Soda   35/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var12,command=soda)
soda.grid(row=2,column=0,sticky=W)

sattu=Checkbutton(beveragesFrame,text='Sattu   40/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var13,command=sattu)
sattu.grid(row=3,column=0,sticky=W)

lassi=Checkbutton(beveragesFrame,text='Lassi   60/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var14,command=lassi)
lassi.grid(row=4,column=0,sticky=W)

faluda=Checkbutton(beveragesFrame,text='Faluda     75/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var15,command=faluda)
faluda.grid(row=5,column=0,sticky=W)

mattha=Checkbutton(beveragesFrame,text='Mattha     35/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var16,command=mattha)
mattha.grid(row=6,column=0,sticky=W)

coffee=Checkbutton(beveragesFrame,text='Coffee     60/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var17,command=coffee)
coffee.grid(row=7,column=0,sticky=W)

aamras=Checkbutton(beveragesFrame,text='Aamras     55/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var18,command=aamras)
aamras.grid(row=8,column=0,sticky=W)


#ENTRY FIELDS FOR beverages ITEMS---------------------------------------------------------------------------------------------------
texttea=Entry(beveragesFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_tea)
texttea.grid(row=0,column=1)

textcoke=Entry(beveragesFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_coke)
textcoke.grid(row=1,column=1)

textsoda=Entry(beveragesFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_soda)
textsoda.grid(row=2,column=1)

textsattu=Entry(beveragesFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_sattu)
textsattu.grid(row=3,column=1)

textlassi=Entry(beveragesFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_lassi)
textlassi.grid(row=4,column=1)

textfaluda=Entry(beveragesFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_faluda)
textfaluda.grid(row=5,column=1)

textmattha=Entry(beveragesFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_mattha)
textmattha.grid(row=6,column=1)

textcoffee=Entry(beveragesFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=7,column=1)

textaamras=Entry(beveragesFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_aamras)
textaamras.grid(row=8,column=1)

#SOUTH INDIAN FOOD-------

dosa=Checkbutton(southindianFrame,text='Dosa   70/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var19,command=dosa)
dosa.grid(row=0,column=0,sticky=W)

idli=Checkbutton(southindianFrame,text='Idli   40/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var20,command=idli)
idli.grid(row=1,column=0,sticky=W)

vada=Checkbutton(southindianFrame,text='Vada   55/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var21,command=vada)
vada.grid(row=2,column=0,sticky=W)

appam=Checkbutton(southindianFrame,text='Appam   60/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var22,command=appam)
appam.grid(row=3,column=0,sticky=W)

uttapam=Checkbutton(southindianFrame,text='Uttapam   65/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var23,command=uttapam)
uttapam.grid(row=4,column=0,sticky=W)

soup=Checkbutton(southindianFrame,text='Soup   70/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var24,command=soup)
soup.grid(row=5,column=0,sticky=W)

noodles=Checkbutton(southindianFrame,text='Noodles   85/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var25,command=noodles)
noodles.grid(row=6,column=0,sticky=W)

chowmein=Checkbutton(southindianFrame,text='Chowmein   90/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var26,command=chowmein)
chowmein.grid(row=7,column=0,sticky=W)

manchurian=Checkbutton(southindianFrame,text='Manchurian   75/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var27,command=manchurian)
manchurian.grid(row=8,column=0,sticky=W)



#ENTRY FIELDS FOR SOUTH INDIAN ITEMS----------------

textdosa=Entry(southindianFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_dosa)
textdosa.grid(row=0,column=1)

textidli=Entry(southindianFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_idli)
textidli.grid(row=1,column=1)

textvada=Entry(southindianFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_vada)
textvada.grid(row=2,column=1)

textappam=Entry(southindianFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_appam)
textappam.grid(row=3,column=1)

textuttapam=Entry(southindianFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_uttapam)
textuttapam.grid(row=4,column=1)

textsoup=Entry(southindianFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_soup)
textsoup.grid(row=5,column=1)

textnoodles=Entry(southindianFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_noodles)
textnoodles.grid(row=6,column=1)

textchowmein=Entry(southindianFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_chowmein)
textchowmein.grid(row=7,column=1)

textmanchurian=Entry(southindianFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_manchurian)
textmanchurian.grid(row=8,column=1)




#desserts------------------------------------------------------

kulfi=Checkbutton(dessertsFrame,text='Kulfi   45/-',font=('arial',14,'bold'),onvalue=1,offvalue=0,variable=var28,command=kulfi)
kulfi.grid(row=0,column=0,sticky=W)

modak=Checkbutton(dessertsFrame,text='Modak   25/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var29,command=modak)
modak.grid(row=1,column=0,sticky=W)

halwa=Checkbutton(dessertsFrame,text='Halwa   55/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var30,command=halwa)
halwa.grid(row=2,column=0,sticky=W)

barfi=Checkbutton(dessertsFrame,text='Barfi   45/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var31,command=barfi)
barfi.grid(row=3,column=0,sticky=W)

ghewar=Checkbutton(dessertsFrame,text='Ghewar   80/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var32,command=ghewar)
ghewar.grid(row=4,column=0,sticky=W)

sandesh=Checkbutton(dessertsFrame,text='Sandesh     60/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var33,command=sandesh)
sandesh.grid(row=5,column=0,sticky=W)

pudding=Checkbutton(dessertsFrame,text='Pudding     50/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var34,command=pudding)
pudding.grid(row=6,column=0,sticky=W)

rasmalai=Checkbutton(dessertsFrame,text='Rasmalai     35/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var35,command=rasmalai)
rasmalai.grid(row=7,column=0,sticky=W)

shrikhand=Checkbutton(dessertsFrame,text='Shrikhand   60/-',font=('Monotype Corsiva',14,'bold'),onvalue=1,offvalue=0,variable=var36,command=shrikhand)
shrikhand.grid(row=8,column=0,sticky=W)


#--------------------entry desserts----------------------------------

textkulfi=Entry(dessertsFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_kulfi)
textkulfi.grid(row=0,column=1)

textmodak=Entry(dessertsFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_modak)
textmodak.grid(row=1,column=1)

texthalwa=Entry(dessertsFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_halwa)
texthalwa.grid(row=2,column=1)

textbarfi=Entry(dessertsFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_barfi)
textbarfi.grid(row=3,column=1)

textghewar=Entry(dessertsFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_ghewar)
textghewar.grid(row=4,column=1)

textsandesh=Entry(dessertsFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_sandesh)
textsandesh.grid(row=5,column=1)

textpudding=Entry(dessertsFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_pudding)
textpudding.grid(row=6,column=1)

textrasmalai=Entry(dessertsFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_rasmalai)
textrasmalai.grid(row=7,column=1)

textshrikhand=Entry(dessertsFrame,font=('arial',14,'bold'),bd=7,width=4,state=DISABLED,textvariable=e_shrikhand)
textshrikhand.grid(row=8,column=1)

#cost labels and entry fields---------------

labelCostofFood=Label(costFrame,text='Food',font=('arial',12,'bold'),bg='firebrick4',fg='white')
labelCostofFood.grid(row=0,column=0)
textCostofFood=Entry(costFrame,font=('arial',12,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=41)

labelCostofBeverages=Label(costFrame,text='Beverages',font=('arial',12,'bold'),bg='firebrick4',fg='white')
labelCostofBeverages.grid(row=1,column=0)
textCostofBeverages=Entry(costFrame,font=('arial',12,'bold'),bd=6,width=14,state='readonly',textvariable=costofbeveragesvar)
textCostofBeverages.grid(row=1,column=1,padx=45)

labelCostofSouthIndian=Label(costFrame,text='South Indian / Chinese',font=('arial',12,'bold'),bg='firebrick4',fg='white')
labelCostofSouthIndian.grid(row=2,column=0)
textCostofSouthIndian=Entry(costFrame,font=('arial',12,'bold'),bd=6,width=14,state='readonly',textvariable=costofsouthindianvar)
textCostofSouthIndian.grid(row=2,column=1,padx=45)

labelCostofDesserts=Label(costFrame,text='Desserts',font=('arial',12,'bold'),bg='firebrick4',fg='white')
labelCostofDesserts.grid(row=3,column=0)
textCostofDesserts=Entry(costFrame,font=('arial',12,'bold'),bd=6,width=14,state='readonly',textvariable=costofdessertsvar)
textCostofDesserts.grid(row=3,column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',12,'bold'),bg='firebrick4',fg='white')
labelSubTotal.grid(row=0,column=2)
textSubTotal=Entry(costFrame,font=('arial',12,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=60)

labelServiceCharges=Label(costFrame,text='Service Charges',font=('arial',12,'bold'),bg='firebrick4',fg='white')
labelServiceCharges.grid(row=1,column=2)
textServiceCharges=Entry(costFrame,font=('arial',12,'bold'),bd=6,width=14,state='readonly',textvariable=servicechargesvar)
textServiceCharges.grid(row=1,column=3,padx=60)

labelTotal=Label(costFrame,text='Total',font=('arial',12,'bold'),bg='firebrick4',fg='white')
labelTotal.grid(row=2,column=2)
textTotal=Entry(costFrame,font=('arial',12,'bold'),bd=6,width=14,state='readonly',textvariable=totalvar)
textTotal.grid(row=2,column=3,padx=60)


#--------buttons--------------------------------------------------

buttonTotal=Button(buttonFrame,text='Total',font=('arial',12,'bold'),fg='white',bg='red4',bd=3,command=totalcost,cursor='hand2')
buttonTotal.grid(row=0,column=0,padx=0)

buttonReceipt=Button(buttonFrame,text=' Receipt',font=('arial',12,'bold'),fg='white',bg='red4',bd=3,command=receipt,cursor='hand2')
buttonReceipt.grid(row=0,column=1,padx=3)

buttonSave=Button(buttonFrame,text=' Save ',font=('arial',12,'bold'),fg='white',bg='red4',bd=3,command=save,cursor='hand2')
buttonSave.grid(row=0,column=2,padx=0)

buttonSend=Button(buttonFrame,text='Send',font=('arial',12,'bold'),fg='white',bg='red4',bd=3,cursor='hand2')
buttonSend.grid(row=1,column=0)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',12,'bold'),fg='white',bg='red4',bd=3,command = reset,cursor='hand2')
buttonReset.grid(row=1,column=1)

buttonAddMore=Button(buttonFrame,text='Add More',font=('arial',12,'bold'),fg='white',bg='red4',bd=3,cursor='hand2')
buttonAddMore.grid(row=1,column=2)

#------------text area for receipt---------------------------------

textReceipt=Text(receiptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)



root.mainloop()
       