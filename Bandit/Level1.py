# Bandit Level 0 → Level 1
# Level Goal
# The password for the next level is stored in a file called readme
# located in the home directory. Use this password to log into bandit1
# using SSH. Whenever you find a password for a level, use SSH (on port
# 2220) to log into that level and continue the game.

# Commands you may need to solve this level
# ls, cd, cat, file, du, find

from BanditFunctions import connectToServerRunCMD
from Level0 import getPassword0


def getPassword1():
    username = 'bandit1'
    password = getPassword0()

    cmd = 'ls | cat ./-'

    print('Getting Password 1', flush=True)
    resp = connectToServerRunCMD(username, password, cmd)
    print('Received Password 1', flush=True)
    return(resp.strip())

print('Starting Level 1', flush=True)
resp = getPassword1()
print(resp)
