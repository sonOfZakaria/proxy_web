# echo-client.py

import socket
import rsa

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msg = "Hello "
    print(f"Message incomplet envoyer {msg!r} chiffrer")

    #encryption
    publickey, privatekey = rsa.newkeys(1024)
    cryptedMsg = rsa.encrypt(msg.encode(), publickey)
    
    #conversion du cle prive en string
    pkstr = privatekey.save_pkcs1()
    
    #l'envoie de message incomplet et la cle prive
    s.sendall(cryptedMsg+pkstr)

    #message complet recu avec son cle prive
    data = s.recv(1024)

    #traitement du message complet recu
    cryptedMsg, pkstr = data.split("-----BEGIN".encode())
    pkstr = "-----BEGIN".encode()+pkstr
    
    #conversion du cle prive en integer
    privatekey = rsa.PrivateKey.load_pkcs1(pkstr)

    #decryption
    decryptedMsg = rsa.decrypt(cryptedMsg, privatekey).decode()
    

#resultat
print(f"Message complet reçu {decryptedMsg!r}")
