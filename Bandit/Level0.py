# Level 0
# Level Goal
# The goal of this level is for you to log into the game using SSH. The
# host to which you need to connect is bandit.labs.overthewire.org, on
# port 2220. The username is bandit0 and the password is bandit0. Once
# logged in, go to the Level 1 page to find out how to beat Level 1.

# Commands you may need to solve this level
# ssh

# Helpful Reading Material
# Secure Shell(SSH) on Wikipedia
# How to use SSH on wikiHow

from BanditFunctions import connectToServerRunCMD


def getPassword0():
    username = 'bandit0'
    password = 'bandit0'

    cmd = 'ls | cat readme'

    print('Getting Password 0', flush=True)
    resp = connectToServerRunCMD(username, password, cmd)
    print('Received Password 0', flush=True)
    return(resp.strip())

# print('Starting Level 0', flush=True)
# resp = getPassword0()
# print(resp)
