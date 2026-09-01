"""Main app for the Athletes module. It creates teams, athletes, and simulates a game between them. """
from .Game import Game
from .Team import Team
from .Sports import Sport
from .Athlete import Athlete
import json

def load_json(file_path):
    """Loads JSON data from a file."""
    data = None
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def main():
    """Main function to create teams, athletes, and simulate a game."""
    #Load data from JSON files
    tournament_data = load_json(r"C:\\Users\\Lenovo\Documents\\desarrollo4\\curso_ds4_2026\\Athletes\\tournament.json")
    print("Tournament:", tournament_data)

if __name__ == "__main__":
    main()