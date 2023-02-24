
import random
import requests

def get_random_pokemon_name() -> str:
  pokemon_id =  random.randint(1, 898)
  pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
  pokemon = requests.get(pokemon_url, timeout=5).json()
  return str(pokemon["name"])

def main():
  print(get_random_pokemon_name())


if __name__ == "__main__":
  main()
