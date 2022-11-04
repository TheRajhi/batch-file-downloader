import requests
import os
import colorama
from colorama import Fore
colorama.init(autoreset=True)

cwd = os.getcwd()

try:
    os.mkdir(fr"{cwd}\Downloads")
    os.chdir(fr"{cwd}\Downloads")
except OSError as error:
    os.chdir(fr"{cwd}\Downloads")

user_file_name = input('what do you want the name to be: ')

name = user_file_name
extension = input('what is the extension? eg. (.jpg),(.png):')
with open(fr"{cwd}\Links.txt") as f:
    urls = f.read().splitlines()

number_of_files = len(urls)
print(f'{number_of_files} files for download...')
x = 0

while x < number_of_files:
    file_name = (name + str(x + 1))
    request = requests.get(urls[x])
    open(file_name + extension, 'wb').write(request.content)
    print(urls[x] + Fore.GREEN + ' done')
    x = x + 1
print()
print(Fore.GREEN + 'Process finished successfully')
input('Press ENTER to exit')
