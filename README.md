# ez_updates
Fichier `versions.json` lu par le `version.lua` de chaque script EZ : `{ "nom_ressource": { "version", "changelog", "url" } }`.
- Publier une mise à jour : `python3 -I tools/gen_versions.py <resources> <url de la boutique>` puis commit + push sur `main`.
- Le dépôt doit être **public** (lecture via raw.githubusercontent.com).
- Côté serveur client : `set ez_updates_check false` désactive la vérification. Aucune donnée n'est envoyée.
