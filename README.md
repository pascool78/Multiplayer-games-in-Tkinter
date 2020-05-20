English:

Use:

Installation:
<br/> Linux Ubuntu / Debian:

Go to https://github.com/pascool78/Super-simple-client-server-multiplayer-games-in-tkinter/releases.
<br/>Take the most recent version look in assets debubuntuX.X.deb
<br/>Like here: https://raw.githubusercontent.com/pascool78/Super-simple-client-server-multiplayer-games-in-tkinter/master/Videosandscreenshot/Install1.png
<br/>Video to illustrate the installation of .deb: 
<br/>Then execute the command:
```sh
$ sudo dpkg -i debuntuX.X.deb
```
In the directory where you have downloaded the .deb.

Linux and Mac:
```sh
$ git clone https://github.com/pascool78/Super-simple-client-server-multiplayer-games-in-tkinter.git
$ cd Super-simple-client-server-multiplayer-games-in-tkinter
$ sudo pip3 install -r requiment.txt
```
For those who used the .deb for the installation, remove python3 from all the following commands.

Start the seveur:
```sh
$ cd bin
$ sudo python3 server.py
```

Start client 1:
```sh
$ python3 clienttk.py 1 2
```

Start client 2:
```sh
$ python3 clienttk.py 2 1
```
Warning: At the bottom of the server.py and clienttk.py files, an IP address is marked (192.168.0.2), please replace it with the server address.


Français:

Utilstaion:

Installation:
<br/>Linux Ubuntu/Debian:

Aller sur https://github.com/pascool78/Super-simple-client-server-multiplayer-games-in-tkinter/releases
<br/>Prenez la version la plus récente chercher dans assets debubuntuX.X.deb
<br/>Comme ici: https://raw.githubusercontent.com/pascool78/Super-simple-client-server-multiplayer-games-in-tkinter/master/Videosandscreenshot/Install1.png
<br/>Puis executer la commande:
```sh
$ sudo dpkg -i debuntuX.X.deb
```
Dans le répertoire ou vous avez télécharger le .deb.

Linux et Mac:
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
