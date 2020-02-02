import paramiko


def connectToServerRunCMD(username, password, cmd):
    host = 'bandit.labs.overthewire.org'
    port = 2220
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)

    stdin, stdout, stderr = ssh.exec_command(cmd)
    outlines = stdout.readlines()
    resp = ''.join(outlines)
    return(resp)
