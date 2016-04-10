class Adresar:
    def __init__(self, ime, priimek, naslov, telefon, email):
        self.ime = ime
        self.priimek = priimek
        self.naslov = naslov
        self.telefon = telefon
        self.email = email

    def ime_uporabnika(self):
        print "Ime in priimek:", self.ime, self.priimek

    def podatki(self):
        print "Naslov:", self.naslov
        print "Telefon:", self.telefon
        print "Email:", self.email

zbrani_kontakti = []

while True:
    dodaj_kontakt = (raw_input("Zelite dodati nov kontakt? da/ne: ").lower())
    if dodaj_kontakt == "da":
        nov_kontakt = Adresar(ime=raw_input("Ime:"),
                              priimek=raw_input("Priimek:"),
                              naslov=raw_input("Naslov:"),
                              telefon=raw_input("Telefon:"),
                              email=raw_input("Email:"))

        zbrani_kontakti.append(nov_kontakt)

    elif dodaj_kontakt == "ne":
        break

for kontakt in zbrani_kontakti:
    kontakt.ime_uporabnika(), kontakt.podatki()