"""
projekt2.py: druhý projekt do Engeto Online Python Akademie
author: Roman Loibl
email: r.Loibl@seznam.cz
discord: nathren.
"""
from random import choice
from time import sleep
from os import system


def generate_grid(grid_size):
    """generuje grid dle hodnoty grid_size a 
    vytvoří list v listu který naplní hodnotami (pozicemi)
      do jednotlivých buněk"""
    grid = []
    num = 1
    for row_index  in range(grid_size):
        row = []
        for column_index  in range(grid_size):
            row.append(str(num))
            num += 1
        grid.append(row)
    return grid


def display_grid(grid):
    """vykreslení gridu"""
    for row in grid:
        display_row = []
        for cell in row:
            if cell == "O":
                display_row.append(change_color(cell,"red"))  # Obarví "O" červeně
            elif cell == "X":
                display_row.append(change_color(cell,"blue"))  # Obarví "X" modře
            else:
                display_row.append(cell)
        print(f"| {' | '.join(display_row)} |")
        print("-" * (5 * len(row) - 1))


def change_color(text, color):
    """mění batvu textu za pomocí ANSI kodu bez
      použití instalovaní jiných balíčků jako je třeba colorama """
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",       
    }
    end_color = "\033[0m"  # Reset barvy
    if color in colors:
        return (colors[color] + text + end_color)
    else:
        return text  # Pokud je barva neplatná, vrátí se text bez formátování


def can_place_symbol(grid,pos,symbol):
    """hleda v gridu dle zadane pozice pos kam ma umistit symbol
      a vraci hodnotu True nebo False podle toho zda uz symbol na tomto miste je"""
    for sublist in grid:        
        if pos in sublist:            
            index = sublist.index(pos)
            sublist[index] = symbol                          
            return True            
    else:              
        return False


def check_winner(grid,symbol):
    """kontoroluje zda nějaký hráč nemá 3 stejné symboly
      za sebou v různých směrech. POZOR funguje pouze s gridem 3x3"""
    # kontroluje v řádku
    for row  in grid:
        if all(cell == symbol for cell in row):
            return True
    # kontroluje ve sloupcích
    for column in range(3):
        if all(grid[row][column] == symbol for row in range(3)):            
            return True
    # kontroluje diagonály
    if all(grid[i][i] == symbol for i in range(3)) or all(grid[i][2-i] == symbol for i in range(3)):
        return True
    return False


def check_game_over(grid, symbol, index_symbol):
    """kontrola zda některý z hráču nevyhral pomocí fukce check_winner() a nebo není remíza pomocí fukce check_draw()"""
    if check_winner(grid, symbol[index_symbol]):
        if symbol[index_symbol] == "O": # zde se zjistuje kdo vyhral O nebo X
            print(f"{separator}\nCongratulations, the player {change_color(symbol[index_symbol], 'red')} WON!\n{separator}")                       
        else:
            print(f"{separator}\nCongratulations, the player {change_color(symbol[index_symbol], 'blue')} WON!\n{separator}")                           
        return True
    if check_draw(grid):
        print("DRAW!")
        return True
    return False


def check_draw(grid):
    """kontroluje zda jdou všechny bunky v gridu 
    vypněné symboly pro zjištění zda je remíza"""
    for row in grid:
       if any(cell.isnumeric() for cell in row):
        return False
    return True
  

def player_turn(symbol):
    """informace že je na tahu hráč"""
    pos = input(f"Player {change_color(symbol, 'red')} | Please enter your move number: ")
    return pos


def AI_brain(cells_on_grid):
    """AI takové fake :) vybírá random hodnotu ze sekvence a dle této hodnoty vybíra pole na které umístí svůj symbol"""   
    pos = str(choice(cells_on_grid)) 
    return pos            


def AI_turn(cells_on_grid, symbol):
    """iformace že hraje AI"""
    pos = AI_brain(cells_on_grid)
    print(f"Player {change_color(symbol, 'blue')} | !!!AI is playing!!!\n{separator}")
    sleep(1) #prodleva 1s pro symulaci že AI přemýšlí :) 
    return pos

def initialize_game():
    "inicializování proměných"
    symbol = ("O","X") # symboly reprezentující jak hráče tak i jejich tahy v gridu
    index_symbol = 0 # index se využívá pro zjištění který z hráčů je na tahu
    game_over = False      
    grid_size = 3 # Rozměry gridu    
    cells_on_grid = list(range(1, grid_size ** 2 +1)) #počet bunek celkem v gridu
    
    grid = generate_grid(grid_size)  # Vygenerování mřížky     
    
    
    return symbol, index_symbol, game_over, grid_size, cells_on_grid, grid

def game(): 
    symbol, index_symbol, game_over, grid_size, cells_on_grid, grid = initialize_game() # inicializace proměnných

    display_grid(grid)  # vykreslení hracího pole

    # smyčka kde se hráči střídají v umistování svých znaků do gridu a úři splnění fce check_winner() případně check_draw() se hra ukončí
    while not game_over:        
        print(separator)
        #hraje hráč
        if index_symbol == 0:
            pos = player_turn(symbol[index_symbol])
        else:
            pos = AI_turn(cells_on_grid, symbol[index_symbol])
        
        if pos.isnumeric():
            if int(pos) <= grid_size ** 2 and int(pos) != 0:
                if can_place_symbol(grid,pos,symbol[index_symbol]):                                                  
                    display_grid(grid)   #překreslí grid                 
                    cells_on_grid.remove(int(pos)) # odstraní z listu cells_on_grid hodnotu pos aby AI na tuto pozici už nezkoušel umístit svůj symbol 
                    game_over = check_game_over(grid, symbol, index_symbol)# kontrola zda hra neskončila                           
                    index_symbol = (index_symbol + 1) % 2 #střídá hráče po ůspěšném umístění symbolu     
                else:
                    print(f"{separator}\nThe place is OCCUPIED!")
            else:
                print(f"{separator}\nTHE NUMBER IS NOT IN THE GRID!")
        else:
            print(f"{separator}\nYou didn't enter a NUMBER!!")  


if __name__ == "__main__":
    system('cls') #vyčistí obrazovku od předešlích výpisů 

    separator = "=" * 44

    print(f"""Welcome to Tic Tac Toe
{separator}
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
{separator}
Let's start the game
{separator}"""
    )   

    game()





