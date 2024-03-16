exec( open("docimages_core.py" ).read() )
import os
from os import listdir
from os.path import isfile, join
import random
import pyIMAPI
import PySimpleGUI as sg

from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
	
 
#----------------------------------------------------------#
#ONKO AJETTU AIEMMIN - MÄÄRITTELE KANSIOT	
#----------------------------------------------------------#
if not os.path.isfile("lahteet.txt"): 
	lahteet = open('lahteet.txt','w+')
	Tk().withdraw() 
	print("Millä kansioilla korvataan?")    # POHJAKANSIO korvaaville äänille -- SAA SISÄLTÄÄ ALIKANSIOT, MISSÄ ÄÄNET ERIKSEEN
	lahteet.write(''+os.path.abspath(askdirectory())+'\n')
	print("Pohja kansio?")  #path_org -->   Sisältää kaikki prosessin alikansiot
	Tk().withdraw() 
	lahteet.write(''+os.path.abspath(askdirectory())+'\n')
	print("MUMMEDIA?")  # MUMMEDIA, eli originaalitiedostojen pohjakansio
	Tk().withdraw()
	lahteet.write(''+os.path.abspath(askdirectory())+'\n') 
	print("Hiljaisuus?") # Tiedosto, mikä sisältää tyhjää ääntä
	lahteet.write(''+os.path.abspath(askopenfilename())+'\n')	
	lahteet.close()
else:
	input('OK')	
#----------------------------------------------------------#    
  
#----------------------------------------------------------#
#TYHJENNÄ VANHAT TIEDOSTOT
#----------------------------------------------------------#
tyhjennys="C:\\Users\\User\\Desktop\\tyo\\pidennetyt" # Tiedostoja on pidennetty hiljaisuudella, poistetaan. Poistaa esim. APESPILX kansiosta tiedostot
k = os.listdir(tyhjennys)
for i in k:
	u = os.path.join(tyhjennys,i)
	w = os.listdir(u)
	for j in w:
		m = os.path.join(u,j)
		os.remove(m)

tyhjennys="C:\\Users\\User\\Desktop\\tyo\\isoon\\MUMMEDIA\\" # Tiedostot, jotka aiemmin oli prepattu ISO tiedostoon siirtoon. Poistetaan vanhat kuin edellä.
for i in k:
	u =os.path.join(tyhjennys,i)
	w = os.listdir(u)
	for j in w:
		m = os.path.join(u,j)
		os.remove(m)

tyhjennys="C:\\Users\\User\\Desktop\\tyo\\Muumit" #
k = os.listdir(tyhjennys)
for i in k:
	u = os.path.join(tyhjennys,i)
	w = os.listdir(u)
	for j in w:
		m = os.path.join(u,j)
		os.remove(m)
tyhjennys="C:\\Users\\User\\Desktop\\tyo\\boost" #KORVAAVIA ÄÄNIÄ boostattu Audacitylla. Poistetaan muokatut äänet.
k = os.listdir(tyhjennys)
for i in k:
	u = os.path.join(tyhjennys,i)
	os.remove(u)
#----------------------------------------------------------#


#----------------------------------------------------------#
#LYÖDÄÄN TIEDOSTON POLUT PAIKOILLEEN; Korvaavat äänet, pohjakansio, MUMMEDIA ja hiljaisuus
#----------------------------------------------------------#
lahteet = open('lahteet.txt','r')
#path = "C:\\Users\\Miku\\Desktop\\tyo\\audio"	
tiedot = []
for i in range(0,4):
	tiedot.append(lahteet.readline())
#korvaavat_aanet = tiedot[0]
#korvaavat_aanet = path[:-1]
#path_org = tiedot[1]
#path_org = path_org[:-1]
korvaavat_aanet = tiedot[0][:-1]
pohjakansio = tiedot[1][:-1]
MUMMEDIA_kansio = tiedot[2][:-1]
hiljaisuus = tiedot[3][:-1]

#----------------------------------------------------------#
#Korvaavien äänien kasaaminen muuttujaan
#----------------------------------------------------------#
f = os.listdir(korvaavat_aanet)
kansiot = []
random_lista = []
for i in f:
	kansiot.append(os.path.join(korvaavat_aanet,i))
#----------------------------------------------------------#

#----------------------------------------------------------#
#ALUSTETAAN PROSESSI-IKKUNA	|| Historiallisista syistä pidän tämän projektissa, mutta ei mikään hirveän mukava moduuli tuo PySimpleGUI
#----------------------------------------------------------#
sg.ChangeLookAndFeel('GreenTan')
# sg.SetOptions(progress_meter_color=('red', 'white'))
MAX_PROG_BARS = 20              # number of training sessions
prog_layout = [[sg.T('Tulilla', size=(20, 1), font=('Helvetica', 17))],
					[sg.ProgressBar(100, size=(31,4), key='_prog1_')],
					[sg.ProgressBar(100, size=(30,4), key='_prog2_', bar_color=('red', 'white'))],
					[sg.RButton('Run')],
					]

window = sg.Window('Progress Bars', auto_size_text=True, default_element_size=(30, 2)).Layout(prog_layout)
#----------------------------------------------------------#

#----------------------------------------------------------#
#AJETAAN PÄÄOHJELMA(?)
#----------------------------------------------------------#
while True:
	button, values = window.Read() # Nappulat GUI-systeemiin
	if button is None:
		break
	if button == 'Run':
		MUMMEDIA_sisalto = os.listdir(MUMMEDIA_kansio)  #MUMMEDIA Kansion sisältö, eli pelin alikansiot
		muumit_kansio = os.path.join(pohjakansio,"Muumit")  #Muumit kansio, kopio MUMMEDIA:n ulkonäöstä (sis. alikansiot)
		for i in range((len(MUMMEDIA_sisalto))):    #OTA kansio MUMMEDIA kansiosta
			luettava_kansio = os.path.join(MUMMEDIA_kansio, ''+MUMMEDIA_sisalto[i]+'' )  #Luo ^ kansiolle muuttuja
			muumit_kansion_alikansio = os.path.join(muumit_kansio,MUMMEDIA_sisalto[i]) # MUMMEDIAN kaltainen alikansio
			kansio_sisalto = os.listdir(luettava_kansio) # .AFI TIEDOSTOT ALIKANSIOSSA
			kansio_sisalto = [w.replace('.AIF', '') for w in kansio_sisalto]    #Poista tiedostopääte
			n = 0
			while n < len(kansio_sisalto):    # Varmistetaan, että kaikki äänitiedostot käydään läpi
				random_korvaava_kansio = random.choice(kansiot)  #OTA satunnainen KORVAAVAN ÄÄNEN KANSIO
				valinta = random.choice(os.listdir(random_korvaava_kansio))  #OTA satunnainen KORVAAVA ÄÄNI
				korvaaja = os.path.join(random_korvaava_kansio,valinta)    #Tämän kyseisen valitun tiedoston reitti
				korvattava = os.path.join(muumit_kansion_alikansio,kansio_sisalto[n])  # Tiedosto, joka tullaan korvaamaan MUUMI kansiossa.
				if korvaaja in random_lista:    #JOS äänitiedosto on jo käytetty, kokeillaan uudelleen, kunnes saadaan UUSI korvaaja
					continue
				else:
					valinta = valinta[:-4]  #Korvaajan tiedostonimi, ei reittiä, ei tiedostopäätettä
				random_lista.append(korvaaja)
				boostattu = os.path.join(pohjakansio,'boost')
				boostattu_tiedosto = os.path.join(boostattu,valinta)    #Tulemme boostaamaan ääntä, ja tänne siirtyy se boostattu tiedosto
				makeWayForTracks()
				do ('Import2: Filename="'+korvaaja+'"')
				do ('Compressor: AttackTime="0.2" NoiseFloor="-40" Normalize="1" Ratio="10" ReleaseTime="1" Threshold="-58" UsePeak="0"')
				do ('Amplify: AllowClipping="1" Ratio="1.5"')
				do ('Stereo to Mono: ')
				do ('Export2: Filename="'+boostattu_tiedosto+'.wav"')
				os.system("ffmpeg -i "+boostattu_tiedosto+".wav -ar 22050 -acodec pcm_s8 "+korvattava+".AIF") #AVAIN! Boostasimme tiedostoa yllä, ja nyt se muunnetaan AIF muotoon
				f = open('mylist.txt','w+') #ffmpeg:n avulla yhdistetään ^ ääni sekä hiljaisuus, tehtävä välitiedoston kautta
				f.write("file '"+korvattava+".AIF'\n")
				f.write("file '"+hiljaisuus+"'")
				path_ulos = ''+pohjakansio+'\\isoon\\MUMMEDIA\\'+MUMMEDIA_sisalto[i]+'\\'+kansio_sisalto[n]+''  #LOPULLINEN tiedosto menee tänne
				#path_ulos =path_ulos[:-4]
				f.close()
				os.system('ffmpeg -f concat -safe 0 -i mylist.txt -c copy '+path_ulos+'.AIF')
				n = n+1
				window.FindElement('_prog2_').UpdateBar(n+1, max=len(kansio_sisalto))
			window.FindElement('_prog1_').UpdateBar(i+1, max=len(MUMMEDIA_sisalto))
#----------------------------------------------------------#
#TYHJENNYS			
			
path="C:\\Users\\User\\Desktop\\tyo\\Muumit"
k = os.listdir(path)
for i in k:
	u = os.path.join(path,i)
	w = os.listdir(u)
	for j in w:
		m = os.path.join(u,j)
		os.remove(m)
path2="C:\\Users\\User\\Desktop\\tyo\\boost"
k = os.listdir(path2)
for i in k:
	u = os.path.join(path2,i)
	os.remove(u)

print("Creating default ISO(CD)")
o = pyIMAPI.open("Taikurinhattu.iso")

k = os.listdir()
print(k)
p="C:\\Users\\User\\Desktop\\tyo\\isoon\\"
print(k)
for i in k:
    if i == "ASENNA.EXE" or i=="AUTORUN.INF":
        o.add(i)
    m = os.path.join(p,"MUMMEDIA")
    o.add(m)
o.close()
