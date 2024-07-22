# Setup un Serveur de Messagerie
Nous avons besoins de plusieurs composants pour pouvoir créer un serveur de messagerie. [Cliquez sur ce lien pour en savoir plus](https://docker-mailserver.github.io/docker-mailserver/latest/introduction/).
Le projet contient trois façon de configurer un serveur de messagerie. 

## Postfix
Postfix est un serveur de messagerie électronique et un logiciel libre. c'est un MTA (Mail transfer Agent) , sa principale mission est d'envoyer les emails.
Dans le dossier [postfix](postfix/), nous avons les configs pour mettre en place un MTA avec Docker.

## Docker Mailserver
Un serveur de messagerie conteneurisé simple mais complet, prêt pour la production (SMTP, IMAP, LDAP, Antispam, Antivirus, etc.). Seulement des fichiers de configuration, pas de base de données SQL. Le garder simple et versionné. Facile à déployer et à mettre à jour.
Dans le dossier [docker-mailserver](mailserver/), nous avons tous les configs pour mettre en place un serveur de messagerie complète avec Docker. Nous vous recommendaons de lire le [README.md](docker-mailserver/README.md) à l'intérieur du docker-mailserver pour pouvoir mettre en place le service.

## Service Email Managé
Un serveur email géré par un fournisseur de services cloud est un service où le fournisseur cloud prend en charge l'hébergement, la maintenance, la sécurité et la gestion de l'infrastructure de serveur de messagerie pour ses clients.
Nous avons utilisé Transactional Email de Scaleway pour la mise en place d'une messagerie électronique. [Voir la documentation](https://www.scaleway.com/en/transactional-email-tem/).
Une fois que vous avez ajouté un domaine dans Transaction Email, 
    - Vous devez ajouter les records DNS (MX, SPF, DKIM) dans votre Zone DNS.
    - Créer une clé API.
Voici un exemple d'un script python [test_scaleway](test_scaleway.py) pour envoyer un mail à partir de votre service email managé.