# modules are files tha contain python code and you can use in other modules.

countries = ['mexico', 'chile']

def addNewCountry(newCountry:str):
    countries.append(newCountry)
    print(countries)

