## Préparation de l'environnement :
- Ce référentiel a été créé dans le but de mettre en œuvre une simulation d'un système de transactions bancaires.
- Pour tester le code, téléchargez le fichier compressé et décompressez-le sur votre ordinateur ou clonez le projet.
- Pour tester le système, Python et MySQL doivent être installés sur votre ordinateur.
- De plus, les bibliothèques Python suivantes sont nécessaires : requests, mysql-connector, tkinter et flask. Pour les installer à l'aide de pip, saisissez les commandes suivantes dans le terminal :
    ```bash
    pip install requests
    pip install mysql-connector-python
    pip install tkinter
    pip install flask
    ```

## Préparation de la base de données :
- Pour créer et configurer la base de données, un script a été créé. Cependant, pour l'exécuter, il est nécessaire de créer un utilisateur "daniel" avec le mot de passe "daniel".
- Pour ce faire, vous pouvez ouvrir le terminal, vous connecter avec un utilisateur existant dans une session MySQL et saisir la commande :
    ```sql
    CREATE USER 'daniel'@'localhost' IDENTIFIED BY 'daniel';
    ```
    Une fois l'utilisateur créé, accédez au dossier DB et exécutez le fichier 'create_db.py' :
    ```bash
    python create_db.py
    ```

## Préparation des serveurs :
- Pour l'exemple, 4 serveurs ont été créés : AmericanExpress, Visa, CreditMutuel, CreditAgricole.
- Pour exécuter les serveurs, ouvrez 4 terminaux et exécutez :
    ```bash
    python AmericanExpressServer.py
    python VisaServer.py
    python CreditAgricoleServer.py
    python CreditMutuelServer.py
    ```

## Exécution du programme :
- Pour voir le fonctionnement du système, exécutez le fichier main_terminal.py :
    ```bash
    python main_terminal.py
    ```
    Ce fichier ouvrira une fenêtre de connexion pour le compte qui recevra les paiements effectués dans le terminal. Pour faciliter le test, deux boutons ont été ajoutés : pattern1 et pattern2, qui représentent deux comptes créés, un dans chaque banque.
    Après vous être connecté, une fenêtre apparaîtra pour que les informations de paiement soient saisies. Le même système de boutons de modèle a été ajouté pour faciliter le test.

    De plus, il est possible d'exécuter le fichier main_account.py :
    ```bash
    python main_account.py
    ```
    Ce fichier ouvrira une interface visuelle où il est possible de suivre le solde des comptes à mesure que les transactions sont effectuées.
