# Import des modules nécessaires
from tkinter import Tk, StringVar, Canvas, Label, Entry
from pystray import MenuItem as item
from threading import Thread
from yaml import safe_load
from PIL import Image
import pystray
import pickle
import signal
import time
import os
# Import de la fonction convert2tnt depuis le module convert
from convert import convert2tnt 
# Chargement de la configuration depuis un fichier YAML
config = safe_load(open(os.path.join(os.path.dirname(__file__), "config.yml"), "r"))
# Variable globale pour déterminer si l'application est en cours d'exécution
app_started = True
# Récupération de la taille d'entrée depuis la configuration
size_entry = config["gui"]["sizeEntry"]
# Création de la fenêtre principale de l'interface graphique
root = Tk()
root.title("LogiscrutPY by Game K")
root.resizable(False, False)
root.iconbitmap(os.path.join(os.path.dirname(__file__), "images", "icon.ico"))
# Détermination du chemin du fichier de configuration
config_file = os.path.join(os.path.dirname(__file__), "profile.pkl") if config["config"]["path"] is None else config["config"]["path"]
# Si le fichier de configuration existe, charge les valeurs, sinon utilise des valeurs par défaut du fichier `config.yml`
if os.path.exists(config_file):
    a, b, c, d, e, f, g, h, i = pickle.load(open(config_file, "rb"))
else:
    dflt = config["default"]
    a, b, c, d, e, f, g, h, i = [
        dflt["ncompteTNT"], dflt["poidsParDefaut"], dflt["assurance"], 
        dflt["heureLivreur"], dflt["ncompteTNTCR"], dflt["codeProduit"], 
        dflt["codeProduitCR"], dflt["mailNotif"], dflt["scanDossier"]
    ]
# Définition des variables liées aux champs de l'interface graphique
ncompte_tnt = StringVar(value=a)
poids_par_defaut = StringVar(value=b)
assurance = StringVar(value=c)
heure_livreur = StringVar(value=d)
ncompte_tnt_cr = StringVar(value=e)
code_produit = StringVar(value=f)
code_produit_cr = StringVar(value=g)
mail_notif = StringVar(value=h)
scan_dossier = StringVar(value=i)
# Fonction pour vérifier si un dossier existe
def check_dir():
    while app_started:
        while app_started:
            # Vérifie si le dossier spécifié par le chemin contenu dans scan_dossier existe
            if os.path.exists(scan_dossier.get()):
                break  # Sort de la boucle si le dossier existe
            # Attend pendant une demi-seconde avant de vérifier à nouveau
            time.sleep(0.5)
        # Parcourt tous les fichiers dans le dossier spécifié par scan_dossier
        for file in os.listdir(scan_dossier.get()):
            # Construit le chemin complet du fichier en utilisant le dossier de scan_dossier
            file = os.path.join(scan_dossier.get(), file)
            # Vérifie si le fichier est un fichier ordinaire (pas un dossier) et s'il se termine par la bonne extension
            if os.path.isfile(file) and file.lower().endswith(config["config"]["searchExtention"]):
                # Lit le contenu du fichier CSV (encodé en latin-1) dans une variable csv
                csv = open(file, "r", encoding='latin-1').read()
                # Divise le contenu CSV en une liste en utilisant le point-virgule comme séparateur
                csv = csv.split(";")
                # Construit un nouveau chemin de fichier pour le fichier de résultat avec un nom basé sur le contenu CSV
                result_file = f"{scan_dossier.get()}/scruttnt_{csv[0]}.csv"
                # Convertion des datas
                converted = convert2tnt(csv,
                                        ncompte_tnt=ncompte_tnt.get(),
                                        poids_par_defaut=poids_par_defaut.get(),
                                        code_produit_cr=code_produit_cr.get())
                # Écrit le contenu converti du fichier CSV dans le fichier de résultat (encodé en latin-1)
                open(result_file, "w", encoding="latin-1").write(";".join(converted))
                # Supprime le fichier original après avoir traité son contenu
                os.remove(file)
        # Attend pendant une demi-seconde avant de vérifier à nouveau les fichiers dans le dossier
        time.sleep(0.5)
# Fonction pour gérer la fermeture de l'application
def close(icon, item):
    global app_started
    app_started = False
    os.kill(os.getppid(), signal.SIGTERM)
    os.kill(os.getpid(), signal.SIGTERM)
    root.destroy()
    icon.stop()
    exit()
# Fonction pour afficher la fenêtre de l'application depuis la barre système
def show_window(icon, item):
   icon.stop()
   root.deiconify()
   root.attributes("-topmost", True)
# Fonction pour sauvegarder la configuration dans un fichier pickle
def save():
    root.iconify()
    v = [ncompte_tnt.get(), poids_par_defaut.get(), assurance.get(), heure_livreur.get(), ncompte_tnt_cr.get(), code_produit.get(), code_produit_cr.get(), mail_notif.get(), scan_dossier.get()]
    pickle.dump(v, open(config_file, "wb"))
    root.withdraw()
    image = Image.open(os.path.join(os.path.dirname(__file__), "images", "icon.png"))
    menu = (item('Paramètre', show_window), item('Quit', close))
    tray_icon = pystray.Icon("LogiscrutPY", image, "LogiscrutPY", menu)
    Thread(target=lambda: tray_icon.run()).start()
# Création de l'interface graphique avec des étiquettes et des champs de saisie
Canvas(root, width=10, height=10).grid(row=0, column=0)
Canvas(root, width=10, height=10).grid(row=0, column=3)
Canvas(root, width=10, height=5).grid(row=6, column=6)
Label(root, text="N° Compte TnT : ").grid(row=1, column=1, sticky="w")
Entry(root, textvariable=ncompte_tnt, width=size_entry).grid(row=1, column=2, sticky="w")
Label(root, text="Poids par défaut : ").grid(row=2, column=1, sticky="w")
Entry(root, textvariable=poids_par_defaut, width=size_entry).grid(row=2, column=2, sticky="w")
Label(root, text="Assurance : ").grid(row=3, column=1, sticky="w")
Entry(root, textvariable=assurance, width=size_entry).grid(row=3, column=2, sticky="w")
Label(root, text="Heure Livreur : ").grid(row=4, column=1, sticky="w")
Entry(root, textvariable=heure_livreur, width=size_entry).grid(row=4, column=2, sticky="w")
Label(root, text="N° Compte Tnt CR : ").grid(row=1, column=4, sticky="w")
Entry(root, textvariable=ncompte_tnt_cr, width=size_entry).grid(row=1, column=5, sticky="w")
Label(root, text="Code Produit : ").grid(row=2, column=4, sticky="w")
Entry(root, textvariable=code_produit, width=size_entry).grid(row=2, column=5, sticky="w")
Label(root, text="Code Produit CR : ").grid(row=3, column=4, sticky="w")
Entry(root, textvariable=code_produit_cr, width=size_entry).grid(row=3, column=5, sticky="w")
Label(root, text="Mail de notification : ").grid(row=4, column=4, sticky="w")
Entry(root, textvariable=mail_notif, width=size_entry).grid(row=4, column=5, sticky="w")
Label(root, text="Scan Dossier : ").grid(row=5, column=1, sticky="w")
Entry(root, textvariable=scan_dossier, width=config["gui"]["sizeEntryPath"]).grid(row=5, column=2, columnspan=4, sticky="w", pady=10)
# Lancement du thread de vérification du dossier
Thread(target=check_dir).start()
# Configuration de la gestion de la fermeture de la fenêtre principale
root.protocol("WM_DELETE_WINDOW", save)
# Le logiciel est minimizer par défaut
save()
# Démarrage de la boucle principale de l'interface graphique
root.mainloop()
