from difflib import diff_bytes
from webbrowser import get
from typing import List, Tuple
import requests
import json
import random

def __read_data() -> dict:
    with open("data/sudokus.json", "r") as outfile:
        current_dict = json.load(outfile)
    return current_dict

def get_new_random_sudoku() -> Tuple[list, str]:
    result = requests.get("https://sudoku-api.vercel.app/api/dosuku")

    if not 200 <= result.status_code <= 299: 
        raise Exception("Error in requesting a sudoku.")

    response_dict = json.loads(result.text)["newboard"]["grids"][0]
    return response_dict["value"], response_dict["difficulty"]

def get_random_sudoku() -> Tuple[list, str]:
    current_dict = __read_data()
    random_difficulty = random.choice(["Easy", "Medium", "Hard"])
    current_dict = current_dict[random_difficulty]

    return random.choice(current_dict), random_difficulty

def get_random_sudoko_difficulty(difficulty : str) -> list:
    if difficulty.lower() not in ("easy", "medium", "hard"):
        raise Exception("Difficulty does not exist")

    current_dict = __read_data()
    return random.choice(current_dict[difficulty])

def safe_sudoku(grid : list, difficulty : str) -> None:
    #read data
    current_dict = __read_data()
    
    #insert new sudoku
    current_dict[difficulty].append(grid)

    #write data
    json_object = json.dumps(current_dict, indent=4)
    with open("data/sudokus.json", "w") as outfile:
        outfile.write(json_object)

if __name__ == "__main__":
    grid = get_random_sudoko_difficulty("Easy")
    print(grid)