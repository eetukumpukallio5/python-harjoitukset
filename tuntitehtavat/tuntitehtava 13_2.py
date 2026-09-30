import json

elokuvat = {
    "Inception": {
        "Nimi": "Inception",
        "Vuosi": "2010",
        "Näyttelijät": ["Leonardo Dicaprio", "Elliot Page"]
    },
    "Castaway": {
        "Nimi": "Castaway",
        "Vuosi": "1999",
        "Näyttelijät": ["Tom Hanks"]
    }
}

with open("elokuva.json", "w") as tiedosto:
    json.dump(elokuvat, tiedosto)