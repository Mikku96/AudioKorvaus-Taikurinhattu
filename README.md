# AudioKorvaus- Muumit ja Taikurinhattu (PC)

Hyvin vanhan projektin tarkoituksena oli korvata Muumit ja Taikurinhattu (PC) pelin äänitiedostot omilla huumoritarkoituksella.

Vaikka tämä projekti on julkisesti nähtävillä, ei sitä voi suoraan ajaa tällä hetkellä, sillä:
* Projekti oli tarkoitettu ajettavaksi vain kerran ja hyvin tietyissä olosuhteissa - scripti olettaa kansiorakenteita.
* Audacityn ja FFMPEG tulisi viritellä kuntoon, ja tämä on to-do listalla tänne.
* Tekijänoikeussyistä en pelin tiedostoja jakele tässä.

Tässä kuitenkin vähän tietoa projektin sisällöstä
---

#1 Pelin äänitiedostot ovat säilöttyny .AIF formaattiin, pcm8 koodekilla ja 22050 kHz taajuudella. Omat tiedostot tulee siis säätää tähän muotoon.

#2 Jokaisen pelin minipelin äänet ovat pakattuna omiin alikansioihin.

* Esimerkiksi Piisamirotan kellopelissä äänitiedostot ovat pakattuna "BISAMX" kansioon.

#3 Omat äänitiedostoni valitsen erillisestä lähdekansiosta täysin satunnaisesti.

#4 Äänitiedostot prosessoidaan aluksi Audacityn avulla (vahvistus, kompressointi ja stereo->mono muunnos).

* Pythonin ja Audacityn välille on mahdollista saada pipeline yhteys, joten tämä on järkevä automatisoida (satoja prosessoitavia äänitiedostoja).

* Audacity 2.3.2 versiota sovellettiin tässä projektissa

#5 Käytyään Audacityn prosessoinnin läpi, uudet äänitiedostot muunnetaan .AIF muotoon FFMPEG:n avulla ja lähetetään lopputulosten kansioon.

#6 Lopuksi välitiedostot poistetaan
