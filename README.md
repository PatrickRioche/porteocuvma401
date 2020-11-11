# porteocuvma401

Projet PorteOculaireVMA401 : Pilotage a distance d'un porte oculaire avec un moteur pas a pas Welleman VMA401

methode d'installation du projet sur un Raspberry

git init

git clone https://github.com/PatrickRioche/porteocuvma401.git

_creation struture /porteocuvma401_

cd porteocuvma401<br>

vi porteocuvma401.py<br>
```
print("Hello PorteOculaireVMA401");
```
 
 git add .<br>
 git config --global user.email "patrick.rioche@gmail.com"<br>
 git config --global user.name "PatrickRioche/porteocuvma401"
 
git commit -m "1er commit"
```
[master 82b62a2] 1er commit<br>
 1 file changed, 1 insertion(+)<br>
 create mode 100644 sensor.py<br>
```

git push
```
Username for 'https://github.com': patrick.rioche@gmail.com
Password for 'https://patrick.rioche@gmail.com@github.com': 
Énumération des objets: 4, fait.
Décompte des objets: 100% (4/4), fait.
Compression par delta en utilisant jusqu'à 4 fils d'exécution
Compression des objets: 100% (2/2), fait.
Écriture des objets: 100% (3/3), 301 bytes | 150.00 KiB/s, fait.
Total 3 (delta 1), réutilisés 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/PatrickRioche/CPPSLT.git
   0609a0b..82b62a2  master -> master
```

git pull
```
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 9 (delta 4), reused 0 (delta 0), pack-reused 0
Dépaquetage des objets: 100% (9/9), fait.
Depuis https://github.com/PatrickRioche/CPPSLT
   82b62a2..13ca05d  master     -> origin/master
Mise à jour 82b62a2..13ca05d
Fast-forward
 README.md | 41 ++++++++++++++++++++++++++++++++++++++++-
 1 file changed, 40 insertions(+), 1 deletion(-)
```

#Fin
