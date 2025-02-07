-BUT DU PROGRAMME-
Le programme est un jeu d'argent simple.

-COMMENT EXECUTER-
Vous pouvez executer le code en utilisant un code editor (par example: VsCode) ou en le compilant utilisant la library PyInstaller et utiliser la fonction onefile ou onedir. Vous pouvez aussi utiliser un interpreteur python en ligne.
Vous pouvez compiler en utilisant pyinstaller avec ces lignes de codes dans le cmd :
1. pyinstaller --onedir supergambler.py 
2. pyinstaller --onefile supergambler.py

-ENTRÉES(INPUT) ET SORTIES(OUTPUT)-
Le joueur entre 3 variables:
1. La mise. Qui représente l'argent misé.
2. 2 nombres entre 1 et 100. C'est nombres seront utilisés pour déterminé la victoire ou défaite du joueur.

Le jeu ressort 2 sorties:
1. Le message annonçant la victoire ou défaite du joueur.
2. La nouvelle balance du joueur (lorsque le jeu recommence).