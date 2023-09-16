from unidecode import unidecode
from datetime import datetime

def convert2tnt(data:list[str], ncompte_tnt, poids_par_defaut, code_produit_cr) -> list[str]:
    csv = [""]*47
    csv.insert(1, ncompte_tnt)
    csv.insert(2, datetime.now().strftime("%d/%m/%Y"))
    csv.insert(4, data[0])
    csv.insert(5, "1")
    csv.insert(6, poids_par_defaut)
    csv.insert(7, "1")
    csv.insert(8, poids_par_defaut)
    csv.insert(9, "E")
    csv.insert(11, data[1])
    csv.insert(12, unidecode(data[3].upper()))
    csv.insert(14, data[5])
    csv.insert(15, unidecode(data[6].upper()))
    csv.insert(21, data[8])
    csv.insert(22, data[8])
    csv.insert(23, data[9])
    csv.insert(37, code_produit_cr)
    csv.insert(38, "0.00")
    return csv[:47]
