donnees = [
    ("Sara", "Math", 12, "G1"), ("Sara", "Info", 14, "G1"),
    ("Ahmed", "Math", 9, "G2"), ("Adam", "Chimie", 18, "G1"),
    ("Sara", "Math", 11, "G1"), ("Bouchra", "Info", "abc", "G2"),
    ("", "Math", 10, "G1"), ("Yassine", "Info", 22, "G2"),
    ("Ahmed", "Info", 13, "G2"), ("Adam", "Math", None, "G1"),
    ("Sara", "Chimie", 16, "G1"), ("Adam", "Info", 7, "G1"),
    ("Ahmed", "Math", 9, "G2"), ("Hana", "Physique", 15, "G3"),
    ("Hana", "Math", 8, "G3")
] # [cite: 16-34]

def valider(enregistrement):
    nom, matiere, note, groupe = enregistrement
    if not (str(nom).strip() and str(matiere).strip() and str(groupe).strip()):
        return (False, "raison: note/nom/matière erronés") # [cite: 44-45]
    try:
        n = float(note)
        if not (0 <= n <= 20):
            return (False, "raison: note/nom/matière erronés") # [cite: 46]
    except (ValueError, TypeError):
        return (False, "raison: note/nom/matière erronés") # [cite: 46]
    return (True, "") # [cite: 44]

valides = [] # [cite: 48]
erreurs = [] # [cite: 49]
doublons_exact = set() # [cite: 50]
vus = set()

for e in donnees:
    if e in vus:
        doublons_exact.add(e)
    vus.add(e)
    est_valide, raison = valider(e)
    if est_valide:
        valides.append((e[0], e[1], float(e[2]), e[3]))
    else:
        erreurs.append({"ligne": e, "raison": raison})

matieres_distinctes = {e[1] for e in valides} # [cite: 52-53]

hierarchie = {} # [cite: 54]
for nom, matiere, note, groupe in valides:
    if nom not in hierarchie:
        hierarchie[nom] = {}
    if matiere not in hierarchie[nom]:
        hierarchie[nom][matiere] = []
    hierarchie[nom][matiere].append(note) # [cite: 55]

groupes_pedagogiques = {} # [cite: 56]
for nom, matiere, note, groupe in valides:
    if groupe not in groupes_pedagogiques:
        groupes_pedagogiques[groupe] = set()
    groupes_pedagogiques[groupe].add(nom)

def somme_recursive(liste):
    if not liste:
        return 0
    return liste[0] + somme_recursive(liste[1:]) # [cite: 58]

def calculer_moyenne(liste):
    if not liste:
        return 0
    return somme_recursive(liste) / len(liste) # [cite: 59]

moyennes = {}
for etudiant, matieres in hierarchie.items():
    toutes_notes = []
    m_mat = {}
    for m, n in matieres.items():
        m_mat[m] = calculer_moyenne(n)
        toutes_notes.extend(n)
    moyennes[etudiant] = {
        "par_matiere": m_mat,
        "generale": calculer_moyenne(toutes_notes)
    } # [cite: 60]

alertes = {
    "doublons_saisie": [], "profils_incomplets": [],
    "groupes_faibles": [], "performances_instables": []
} # [cite: 69-71]

for etudiant, matieres in hierarchie.items():
    for m, n in matieres.items():
        if len(n) > 1:
            alertes["doublons_saisie"].append((etudiant, m)) # [cite: 72]
    if set(matieres.keys()) != matieres_distinctes:
        alertes["profils_incomplets"].append(etudiant) # [cite: 73]
    t_n = [v for s in matieres.values() for v in s]
    if max(t_n) - min(t_n) > 10:
        alertes["performances_instables"].append(etudiant) # [cite: 75-76]

seuil = 10
for grp, membres in groupes_pedagogiques.items():
    n_grp = []
    for m in membres:
        for ns in hierarchie[m].values():
            n_grp.extend(ns)
    if calculer_moyenne(n_grp) < seuil:
        alertes["groupes_faibles"].append(grp) # [cite: 74]

print("--- PARTIE 1: NETTOYAGE ---")
print("Valides:", valides)
print("Erreurs:", erreurs)
print("Doublons Exacts:", doublons_exact)
print("\n--- PARTIE 2: STRUCTURATION ---")
print("Matières:", matieres_distinctes)
print("Groupes:", groupes_pedagogiques)
print("\n--- PARTIE 3: STATISTIQUES ---")
print("Moyennes:", moyennes)
print("\n--- PARTIE 4: ALERTES ---")
print(alertes)