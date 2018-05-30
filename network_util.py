import socket
import subprocess
import sys
from datetime import datetime

""" 
scport() scanne les ports sur une machine donnee et retourne la liste des ports ouverts
sous la forme d'une liste
"""

def scport(remoteServer):
	remoteServerIP = socket.gethostbyname(remoteServer) # gethostbyname() traduit le nom de l'hote en adresse ipv4, interface etendue
	openPortList = [] # va stocker la liste des port ouverts

	for port in range(1, 1025):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cree un stream socket, SOCK_STREAM est un socket de type TCP connexion
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openPortList.append(port)
		sock.close()

	return openPortList

"""
get_ip() retourne l'adresse ip de la machine sur laquelle le script est execute
"""
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

