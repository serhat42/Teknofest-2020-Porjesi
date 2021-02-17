# =============================================================================
# ***************************
# ===================
# =============================================================================
# ***************************
# =============================================================================

"""Hamam Böceği ve Elma Tanımlama İşlemi"""


import cv2
from tkinter import *
from tkinter import messagebox

sayac=0
sayac1=0

cam = cv2.VideoCapture(1)

hamambocegı = cv2.CascadeClassifier("bbocek.xml")
elma =  cv2.CascadeClassifier("elma1.xml")

fontFace=cv2.FONT_HERSHEY_SIMPLEX

while 1 :
    
    _,frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    bocek = hamambocegı.detectMultiScale(gray,1.3,11)
    bıtkı = elma.detectMultiScale(gray,1.2,5)
    
        

    for (x,y,w,h) in bocek:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0 ,0,255),2)
        
        if hamambocegı is not None :
            sayac+=1
            cv2.putText(frame, "Danaburnu Bocegi", (x,y),fontFace,0.9 ,(0, 255, 0), 3)
            print(sayac)
            if sayac ==250:
                    pencere = Tk()
                    pencere.title("Tanımlama İşlem Sonucu")
                    pencere.geometry("700x400")
                    uygulama = Frame(pencere)
                    uygulama.grid()
                    etiket = Label(uygulama,text="""
Elma Bitkisi ile birlikte 
Danaburnu Böceği Tanımlanmıştır.
Danaburnu böceği, birçok bitkiye  zarar verir. 
Genç bitkilere zararı daha fazla olur, 
zarar gören bitki solar veya kurur. 
Tohum,kök,yumru gibi her tür
 bitkisel materyali kemirerek zarar verirler

DANABURNU KİMYASAL MÜCADELEDE KULLANILACAK İLAÇLAR 

Chlorpyrifos-ethyl  %25 oranında 
(400 g 10 kg kepek+ 500 g şeker-100 lt suya)-7gün

Parathion-methyl 360 g/l 
( 100ml -100 lt suya)-28 gün
 
*Günler, ilaçlama ile hasat arası süredir.

""",font="Verdana 13")
                    etiket.grid(padx=110, pady=10)
                    pencere.mainloop()

    for (a,b,c,d) in bıtkı:
        cv2.rectangle(frame,(a,b),(a+c,b+d),(255 ,0,0),2)
        if bıtkı is not None :
            sayac1+=1
            cv2.putText(frame, "Elma", (a,b),fontFace,0.9 ,(0, 255, 0), 3)   
            
            
    a=cv2.resize(frame,(800,650),fx=1.1, fy=1.1, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('video',a)   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()