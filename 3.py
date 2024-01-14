class Countries:
    def __init__(self,davlat_nomi:str, poytaxti:str, aholi_soni:int, yer_maydoni:float, prezidenti):
        self.davlat_nomi=davlat_nomi
        self.poytaxti=poytaxti
        self.aholi_soni=aholi_soni
        self.yer_maydoni=yer_maydoni
        self.prezidenti=prezidenti
    def info(self):
        print(f'''
Davlat nomi:{self.davlat_nomi}
Poytaxti:{self.poytaxti}
Aholi soni:{self.aholi_soni}
Yer maydoni:{self.yer_maydoni}
Prezidenti:{self.prezidenti}
''')
countries=[]
for i in range(1,int(input())+1):
    davlat_nomi=input("\nDavlat nomi: ")
    poytaxti=input("Poytaxti: ")
    aholi_soni=int(input("Aholi soni: "))
    yer_maydoni=float(input("Yer maydoni: "))
    prezidenti=input('Prezidenti: ')
    country=Countries(davlat_nomi,poytaxti,aholi_soni,yer_maydoni,prezidenti)
    countries.append(country)
    sort_countries=sorted(countries,key=lambda country:country.davlat_nomi)
for country in sort_countries:
    country.info()
