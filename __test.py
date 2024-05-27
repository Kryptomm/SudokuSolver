# Using colorama
from colorama import Fore, Back, Style, init
from termcolor import colored

# Initialize colorama
init()

# Colorama examples
print(Fore.RED + 'This is red text (colorama)')
print(Fore.GREEN + 'This is green text (colorama)')
print(Back.YELLOW + 'This has a yellow background (colorama)')
print(Style.DIM + 'This is dim text (colorama)')
print(Style.RESET_ALL + 'Back to normal text (colorama)')

# Termcolor examples
print(colored('This is red text (termcolor)', 'red'))
print(colored('This is green text (termcolor)', 'green'))
print(colored('This text is on a yellow background (termcolor)', 'white', 'on_yellow'))
print(colored('This is blue text with underlined style (termcolor)', 'blue', attrs=['underline']))

# Custom combinations
print(colored('This text is bold and red with a yellow background (termcolor)', 'red', 'on_yellow', ['bold']))
print(colored('This text is blue and underlined (termcolor)', 'blue', attrs=['underline']))
print(colored('This text is green with reversed colors (termcolor)', 'green', attrs=['reverse']))
