# test-data-engineering

## Rapport de Mission - Intégration de données avec PostgreSQL

Dans le cadre de cette mission, ma responsabilité principale a été d'établir une base de données PostgreSQL et d'importer des fichiers CSV qui m'ont été confiés. La mise en place du fichier `docker-compose` pour l'installation de PostgreSQL faisait également partie de mes missions. Bien que la sélection de PostgreSQL ne relève pas de ma compétence directe, elle a été motivée par sa fiabilité et ses performances, justifiant ainsi ce choix.

### Commandes Docker

Pour exécuter le `docker-compose` :
`docker-compose up -d` 

Pour arrêter les services :  
`docker-compose down`  

En parallèle, j'ai configuré pgAdmin4 pour créer une interface conviviale avec notre base de données PostgreSQL, facilitant ainsi la visualisation et la gestion des opérations.  
![Alt text](images\pgAdmin4.png)  

### Intégration des données  
En ce qui concerne l'intégration des données, deux fichiers CSV m'ont été remis. Avant leur incorporation dans la base de données PostgreSQL, j'ai identifié des erreurs telles qu'une colonne superflue, ainsi que des incohérences au niveau des noms de colonnes (uniquement dans le fichier data_consumers.csv). Cela a nécessité la suppression de la colonne indésirable et des permutations au niveau des colonnes, utilisant pour cela Pandas.  

### Insertion des données  
Pour établir les connexions avec notre base de données, j'ai fait appel à SQL Alchemy, tandis que l'insertion des données s'est déroulée avec les méthodes de Pandas, exploitant le module psyco2 dédié à la communication avec les bases de données PostgreSQL.  

Pour insérer les données, utilisez le script Python suivant :  
`python src/insert_the_data_into_the_database.py --db_host --db_port --db_user --db_password --database_name --data_folder_path`  
avec :  
`--db_host : L'adresse IP ou le nom d'hôte du serveur PostgreSQL.`  
`--db_port : Le port sur lequel PostgreSQL écoute.`  
`--db_user : Le nom d'utilisateur pour se connecter à la base de données.`  
`--db_password : Le mot de passe associé à l'utilisateur.`  
`--database_name : Le nom de la base de données PostgreSQL.`  
`--data_folder_path : Le chemin vers le dossier contenant les fichiers CSV.`  

### Requêtes SQL
Respectant scrupuleusement les directives du cahier des charges, j'ai élaboré des requêtes SQL pour extraire les données nécessaires, les testant avec succès dans l'onglet dédié aux requêtes SQL de pgAdmin4.  

