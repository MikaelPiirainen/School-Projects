"""
Tekijä: Mikael Piirainen
Ryhmä: TTV20S2
Harjoitustyö
"""
def user_name():
    nimi = input("Anna nimesi: ")
    print("Hei! {}. Tervetuloa elokuvakirjastoon!".format(nimi))
    print("Painamalla enteriä saat listan elokuvista. Valitsemalla elokuvan saat lisätietoja.")

user_name()

input("Paina enter jatkaaksesi: ")

filename = "elokuvat.txt"
file = open(filename, "r")
lines = file.readlines()
for i in lines:
    print(i)
file.close()

class Elokuva:
    def __init__(self, elokuva="", ohjaaja="", vuosi=""):
        self.elokuva = elokuva
        self.ohjaaja = ohjaaja
        self.vuosi = vuosi
    
    def __str__(self):
        return "elokuva=" + self.elokuva + " ohjaaja=" + self.ohjaaja + " vuosi=" +  self.vuosi
    
    elokuva = ""
    ohjaaja = ""
    vuosi = ""

movie1 = Elokuva("The Godfather", "Francis Ford Coppola", "1972")
movie2 = Elokuva("The Dark Knight", "Cristopher Nolan", "2008")
movie3 = Elokuva("Pulp Fiction", "Quentin Tarantino", "1994")
movie4 = Elokuva("Fight Club", "David Fincher", "1999")
movie5 = Elokuva("Forrest Gump", "Robert Zemeckis", "1994")
movie6 = Elokuva("Inception", "Cristopher Nolan", "2010")
movie7 = Elokuva("Matrix", "The Wachowskis", "1999")
movie8 = Elokuva("Se7en", "David Fincher", "1995")
movie9 = Elokuva("The Silence of the Lambs", "Jonathan Demme", "1991")
movie10 = Elokuva("Star Wars", "George Lucas", "1977")

moviename = input("Anna elokuvan nimi: ")
try:
    if moviename == "The Godfather":
        print(movie1)
    elif moviename == "The Dark Knight":
        print(movie2)
    elif moviename == "Pulp Fiction":
        print(movie3)
    elif moviename == "Fight Club":
        print(movie4)
    elif moviename == "Forrest Gump":
        print(movie5)
    elif moviename == "Inception":
        print(movie6)
    elif moviename == "Matrix":
        print(movie7)
    elif moviename == "Se7en":
        print(movie8)
    elif moviename == "The Silence of the Lambs":
        print(movie9)
    elif moviename == "Star Wars":
        print(movie10)
    else:
        print("Elokuvaa ei löytynyt.")
except:
    ValueError

näyttelijät = {
    "Jack Nicholson" : "79 Elokuvaa",
    "Robert De Niro" : "124 Elokuvaa",
    "Al Pacino" : "62 Elokuvaa",
    "Tom Hanks" : "59 Elokuvaa",
    "Brad Pitt" : "60 Elokuvaa",
    "Meryl Streep" : "93 Elokuvaa",
    "Julia Roberts" : "64 Elokuvaa",
    "Natalie Portman" : "65 Elokuvaa",
    "Helena Bonham Carter" : "100 Elokuvaa",
    "Scarlett Johansson" : "69 Elokuvaa",
}

print("Seuraavaksi voit tarkistaa näyttelijän kirjastosta. Jos näyttelijää ei löydy voit myös tarkistaa kokolistan")
input("Paina enter jatkaaksesi: ")

actorname = input("Anna näyttelijän nimi: ")
if actorname in näyttelijät:
    print(actorname + " on listattuna.")
    print()
else:
    print("Näyttelijä ei ole listattuna")

print("Halutko nähdä kokolistan näyttelijöistä?")
yesno = input("kyllä/ei: ")
try:
    if yesno == "kyllä":
        print("Valitsit: kyllä.")
        for x, y in näyttelijät.items():
            print(x, y)
    elif yesno == "ei":
        print("Valitsit: ei")
except:
    ValueError

print("Kiitos ohjelman käytöstä!")
