Français:

Utilstaion:

Installation du jeu compilé:

Mac: 
```sh
$/bin/bash -c "$(curl -O https://github.com/pascool78/Super-simple-client-server-multiplayer-games-in-tkinter/releases/download/0.5/installmac)"
``` 
Linux:
```sh
$/bin/bash -c "$(curl -O https://github.com/pascool78/Super-simple-client-server-multiplayer-games-in-tkinter/releases/download/0.5/installlinux)"
``` 

Installation à partir des sources:
<br/>Linux Ubuntu/Debian:

Aller sur https://github.com/pascool78/Super-simple-client-server-multiplayer-games-in-tkinter/releases
<br/>Prenez la version la plus récente chercher dans assets debubuntuX.X.deb
<br/>Comme ici: https://raw.githubusercontent.com/pascool78/ImageandVideo/master/Install1.png
<br/>Petite vidéo éxplixative pour insaller le .deb: http://xxl1212.lescigales.org/azerty/vid.html
<br/>Puis executer la commande:
```sh
$ sudo dpkg -i debuntuX.X.deb
```
Dans le répertoire ou vous avez télécharger le .deb.

Linux et Mac:
<br/>Pour Mac il faut installer : https://brew.sh. Puis executer:
```sh
$ sudo brew install git
```
```sh
$ git clone https://github.com/pascool78/Super-simple-client-server-multiplayer-games-in-tkinter.git
$ cd Super-simple-client-server-multiplayer-games-in-tkinter
$ sudo pip3 install -r requiment.txt
```
Pour ceux qui ont utilisé le .deb pour l'installation enlever python3 à toute les commande qui suivent.

Démarrez le seveur:
```sh
$ cd bin
$ sudo python3 server.py
```

Démarrer le client 1:
```sh
$ python3 clienttk.py 1 2
```

Démarrez le client 2:
```sh
$ python3 clienttk.py 2 1
```
Avertissement: Au bas des fichiers server.py et clienttk.py, une adresse IP est marquée (192.168.0.2), veuillez la remplacer par l'adresse du serveur.
