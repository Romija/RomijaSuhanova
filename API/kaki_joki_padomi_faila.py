import requests

def saglabat(teksts):
    with open("mana_izvele.txt", "a") as file:
        file.write(teksts+"\n")

def get_advice():
    url = "https://api.adviceslip.com/advice"
    try:
        response = requests.get(url)
        if response.status_code==200:
            #pārvērš json par python vārdnīcu
            advice = response.json()['slip']['advice'] #gatavi no mājaslapas
            print(f"Padoms: {advice}")

            if input("Saglabāt pie izlases?(j/n)").lower()=="j":
                saglabat("Padoms: "+advice)
        else:
            print("Neizdevās saņemt padomu.")
    except:
        print("Kļūda")

#iegūt joku
def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    try:
        response = requests.get(url)
        if response.status_code==200:
            #pārvērš json par python vārdnīcu
            joke = response.json()['joke'] #gatavi no mājaslapas
            print(f"Joks: {joke}")

            if input("Saglabāt pie izlases?(j/n)").lower()=="j":
                saglabat("Joks: "+joke)
        else:
            print("Neizdevās saņemt joku.")
    except:
        print("Kļūda")

def kakis():
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url)
        if response.status_code==200:
            #pārvērš json par python vārdnīcu
            kakis = response.json().get("fact")#gatavi no mājaslapas
            print(f"Kaķu fakts: {kakis}")

            if input("Saglabāt pie izlases?(j/n)").lower()=="j":
                saglabat("Kaķu fakts: "+kakis)
        else:
            print("Neizdevās.")
    except:
        print("Kļūda")

get_advice()
get_joke()
kakis()
