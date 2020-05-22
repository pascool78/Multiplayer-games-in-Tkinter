English:

Use:

Installation of the compiled game:

Mac:
```sh
$ /bin/bash -c "$(curl -O https://github-production-release-asset-2e65be.s3.amazonaws.com/265296127/dab0d880-9c24-11ea-8177-22f0f465ba38?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20200522%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200522T120022Z&X-Amz-Expires=300&X-Amz-Signature=0a8e8b3f9a09c9e22f261e4a9f1cb73165d08fc3e7f3d5de9f52e2e282f43dbd&X-Amz-SignedHeaders=host&actor_id=56075144&repo_id=265296127&response-content-disposition=attachment%3B%20filename%3Dinstallmac&response-content-type=application%2Foctet-stream)"
```
Linux:
```sh
$ /bin/bash -c "$(curl -O https://github-production-release-asset-2e65be.s3.amazonaws.com/265296127/dab0d880-9c24-11ea-8177-22f0f465ba38?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20200522%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200522T120022Z&X-Amz-Expires=300&X-Amz-Signature=0a8e8b3f9a09c9e22f261e4a9f1cb73165d08fc3e7f3d5de9f52e2e282f43dbd&X-Amz-SignedHeaders=host&actor_id=56075144&repo_id=265296127&response-content-disposition=attachment%3B%20filename%3Dinstalllinux&response-content-type=application%2Foctet-stream)"
```

Installation from sources:
<br/> Linux Ubuntu / Debian:

Go to https://github.com/pascool78/Super-simple-client-server-multiplayer-games-in-tkinter/releases
<br/> Take the most recent version look in assets debubuntuX.X.deb
<br/> Like here: https://raw.githubusercontent.com/pascool78/ImageandVideo/master/Install1.png
<br/> Small explanatory video to install the .deb: http://xxl1212.lescigales.org/azerty/vid.html
<br/> Then execute the command:
```sh
$ sudo dpkg -i debuntuX.X.d
```
In the directory where you have downloaded the .deb.

Linux and Mac:
<br/> For Mac you need to install: https://brew.sh. Then execute:
```sh
$ sudo brew install git
```
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
