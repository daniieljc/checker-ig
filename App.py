import requests
from termcolor import colored

f = open('users.txt', 'r')
users = f.readlines()
f.close()

if __name__ == '__main__':
    for user in users:
        userlim = user.strip()
        url = 'https://www.instagram.com/' + userlim
        response = requests.get(url)

        if response.status_code == 200:
            print(colored('Usuario no disponible - ' + userlim, 'red'))
        if response.status_code == 404:
            print(colored('Usuario disponible - ' + userlim, 'green'))
