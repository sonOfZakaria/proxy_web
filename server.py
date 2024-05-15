# Client.py

import socket
import rsa

HOST = "127.0.0.1"  # Adresse de l’interface de bouclage standard (localhost)
PORT = 65432  # Port à écouter sur (ports non privilégiés > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            #message incomplet recu avec son cle prive
            data = conn.recv(1024)
            if not data:
                break
            
            #traitement du message incomplet recu
            cryptedMsg, pkstr = data.split("-----BEGIN".encode())
            pkstr = "-----BEGIN".encode()+pkstr

            #conversion du cle prive en integer
            privatekey = rsa.PrivateKey.load_pkcs1(pkstr)
            
            #decryption
            decryptedMsg = rsa.decrypt(cryptedMsg, privatekey).decode()
            print(f"Message incomplet reçu {decryptedMsg!r}")
            
            #message complet
            msg = decryptedMsg+"World!"
            print(f"Message complet envoyer {msg!r} chiffrer")
            
            #encryption
            publickey, privatekey = rsa.newkeys(1024)
            cryptedMsg = rsa.encrypt(msg.encode(), publickey)
            
            #conversion du cle prive en string
            pkstr = privatekey.save_pkcs1()

            #l'envoie de message complet et la cle prive
            conn.sendall(cryptedMsg+pkstr)
