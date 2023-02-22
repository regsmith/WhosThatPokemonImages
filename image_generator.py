import requests
import os
from PIL import Image

dir = "images"
lastPokeNum = 1009 # offset by 1

def getPokemonSprite(num: int) -> str:
    apiUrl = f"https://pokeapi.co/api/v2/pokemon/{num}"
    apiResponse = requests.get(apiUrl)
    pokeEntry = apiResponse.json()
    spriteURL = pokeEntry["sprites"]["other"]["official-artwork"]["front_default"]
    r = requests.get(spriteURL)

    with open(f"{dir}/{num}.png", "wb") as f:
        f.write(r.content)
        f.close()
    r.close()

def hidePokemon(filename: str):
    hiddenFilename = f"{filename[:-4]}-masked.png"
    im = Image.open(f"{filename}")
    alpha = im.getchannel('A')
    masked = Image.new('RGBA', im.size, color=(42,42,134))
    masked.putalpha(alpha)
    masked.save(hiddenFilename)
    os.remove(f"{filename}")

for pokeNum in range(906, lastPokeNum + 1):
    filename = f"{dir}/{pokeNum}.png"
    print(filename)
    getPokemonSprite(num=pokeNum)
    hidePokemon(filename=filename)