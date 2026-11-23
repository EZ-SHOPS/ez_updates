#!/usr/bin/env python3
"""Régénère versions.json depuis les fxmanifest.lua : python3 -I tools/gen_versions.py <dossier resources> [url_de_base]
Conserve les champs changelog / url déjà saisis. Lancer avant chaque publication."""
import os, re, sys, json
res = sys.argv[1]; base = sys.argv[2] if len(sys.argv) > 2 else ''
here = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'versions.json')
old = json.load(open(here)) if os.path.exists(here) else {}
out = {}
for n in sorted(os.listdir(res)):
    m = os.path.join(res, n, 'fxmanifest.lua')
    if n.startswith('_') or not os.path.isfile(m): continue
    v = re.search(r"version\s+['\"]([\d.]+)['\"]", open(m).read())
    if v:
        e = old.get(n, {})
        out[n] = {'version': v.group(1), 'changelog': e.get('changelog', ''), 'url': e.get('url') or (base.rstrip('/') + '/' + n if base else '')}
json.dump(out, open(here, 'w'), indent=2, ensure_ascii=False)
print(len(out), 'ressources')
