import math


#2.2 Valeur future ou capitalisée d'un montant unique
def calculer_interet(principal, taux_interet, nombre_periodes, temps):

    # Calcul de l'intérêt composé discrètement
    montant_total_discret = principal * math.pow((1 + taux_interet / nombre_periodes), (nombre_periodes * temps))
    
    # Calcul de l'intérêt composé avec capitalisation continue
    montant_total_continue = principal * math.exp(taux_interet * temps)
    
    return montant_total_discret, montant_total_continue

# Exemple d'utilisation de la fonction
if __name__ == "__main__":
    # Montant initial investi
    principal = 10000  # en dollars
    
    # Taux d'intérêt annuel
    taux_interet = 0.1  # 15% en décimal
    
    # Nombre de fois que l'intérêt est composé par an (pour l'intérêt composé discret)
    nombre_periodes = 1  # Annuel
    
    # Durée de l'investissement en années
    temps = 10  # 10 ans
    
    # Calculer les montants totaux après intérêt composé
    montant_final_discret, montant_final_continue = calculer_interet(principal, taux_interet, nombre_periodes, temps)
    
    # Afficher les résultats
    print(f"\n2.2. Le montant total après {temps} ans avec capitalisation discrète est de: ${montant_final_discret:.2f}")
    print(f"Le montant total après {temps} ans avec capitalisation continue est de: ${montant_final_continue:.2f}\n")














# 2.3 La valeur future d'une annuité
def valeur_future_annuite_immediate(paiement, taux_interet, nombre_periodes):
    """
    Calculer la valeur future d'une annuité immédiate.
    
    Arguments:
    paiement -- montant de chaque paiement
    taux_interet -- taux d'intérêt par période (en décimal, par exemple 0.05 pour 5%)
    nombre_periodes -- nombre total de paiements
    
    Retourne:
    La valeur future de l'annuité.
    """
    valeur_future = paiement * ((1 + taux_interet)**nombre_periodes - 1) / taux_interet
    return valeur_future

def valeur_future_annuite_due(paiement, taux_interet, nombre_periodes):
    """
    Calculer la valeur future d'une annuité due.
    
    Arguments:
    paiement -- montant de chaque paiement
    taux_interet -- taux d'intérêt par période (en décimal, par exemple 0.05 pour 5%)
    nombre_periodes -- nombre total de paiements
    
    Retourne:
    La valeur future de l'annuité.
    """
    valeur_future = paiement * ((1 + taux_interet)**nombre_periodes - 1) / taux_interet * (1 + taux_interet)
    return valeur_future

# Exemple d'utilisation
paiement = 10000  # montant de chaque paiement
taux_interet = 0.1  # taux d'intérêt de 5%
nombre_periodes = 10  # nombre total de paiements (par exemple, sur 10 ans)

# Calculer la valeur future pour une annuité immédiate
vf_immediate = valeur_future_annuite_immediate(paiement, taux_interet, nombre_periodes)
print(f"2.3. Valeur future d'une annuité immédiate : ${vf_immediate:.2f}")

# Calculer la valeur future pour une annuité due
vf_due = valeur_future_annuite_due(paiement, taux_interet, nombre_periodes)
print(f"Valeur future d'une annuité due : ${vf_due:.2f}\n")








# 2.4. Calculer la valeur future pour une annuité due
def actualiser_valeur_future(valeur_future, taux_interet, nombre_annees, periodes_par_annee):
    """
    Cette fonction calcule la valeur présente d'une valeur future avec actualisation sur une base fractionnée.
    
    Arguments:
    valeur_future -- le montant futur à actualiser
    taux_interet -- le taux d'intérêt annuel (en décimal, par exemple 0.15 pour 15%)
    nombre_annees -- la durée en années avant que la valeur future ne soit reçue ou payée
    periodes_par_annee -- le nombre de fois par année où l'intérêt est composé
    
    Retourne:
    La valeur présente actualisée.
    """
    # Calculer le nombre total de périodes
    total_periodes = nombre_annees * periodes_par_annee
    
    # Taux d'intérêt par période
    taux_periode = taux_interet / periodes_par_annee
    
    # Calculer la valeur présente
    valeur_presente = valeur_future / math.pow((1 + taux_periode), total_periodes)
    return valeur_presente

# Exemple d'utilisation de la fonction
if __name__ == "__main__":
    # Valeur future à actualiser
    valeur_future = 10000  # en dollars
    
    # Taux d'intérêt annuel
    taux_interet = 0.10  # 15% en décimal
    
    # Durée en années
    nombre_annees = 10  # 10 ans
    
    # Nombre de fois par année où l'intérêt est composé
    periodes_par_annee = 1  # Par exemple, semestriellement
    
    # Calculer la valeur présente
    valeur_presente = actualiser_valeur_future(valeur_future, taux_interet, nombre_annees, periodes_par_annee)
    
    # Afficher le résultat
    print(f"2.4. La valeur présente de ${valeur_future:.2f} après {nombre_annees} ans à un taux d'intérêt annuel de {taux_interet*100:.2f}% composé {periodes_par_annee} fois par année est de: ${valeur_presente:.2f}\n")








#2.5. Valeur actuelle d'une annuitée
def valeur_actuelle_annuite(paiement, taux_interet, nombre_periodes, type_annuite='immediate'):
    """
    Cette fonction calcule la valeur actuelle d'une annuité immédiate ou due.
    Calculer la valeur actuelle d'une annuité donne une estimation de la valeur actuelle d'une série de paiements futurs en tenant compte d'un taux d'intérêt.

    Retourne:
    La valeur actuelle de l'annuité.
    """
    if type_annuite == 'immediate':
        valeur_presente = paiement * (1 - math.pow(1 + taux_interet, -nombre_periodes)) / taux_interet
    elif type_annuite == 'due':
        valeur_presente = paiement * (1 - math.pow(1 + taux_interet, -nombre_periodes)) / taux_interet * (1 + taux_interet)
    else:
        raise ValueError("Type d'annuité invalide. Utilisez 'immediate' ou 'due'.")
    
    return valeur_presente

# Exemple d'utilisation de la fonction
if __name__ == "__main__":
    # Montant de chaque paiement
    paiement = 10000  # en dollars
    
    # Taux d'intérêt par période
    taux_interet = 0.1  # 15% en décimal
    
    # Nombre total de paiements
    nombre_periodes = 10  # par exemple, sur 10 ans
    
    # Calculer la valeur actuelle pour une annuité immédiate
    valeur_presente_immediate = valeur_actuelle_annuite(paiement, taux_interet, nombre_periodes, 'immediate')
    print(f"2.5. La valeur actuelle d'une annuité immédiate est de: ${valeur_presente_immediate:.2f}")
    
    # Calculer la valeur actuelle pour une annuité due
    valeur_presente_due = valeur_actuelle_annuite(paiement, taux_interet, nombre_periodes, 'due')
    print(f"La valeur actuelle d'une annuité due est de: ${valeur_presente_due:.2f}\n") #paiement fait directement au début de l'année (on ne fait aucun intérêts sur la première année)



#2.6. La valeur actuele d'un flux monétaire périodique constant et perpétuel
def valeur_actuelle_perpetuite(paiement, taux_interet):
    """
    Cette fonction calcule la valeur actuelle d'un flux monétaire périodique constant et perpétuel.
    
    Arguments:
    paiement -- montant de chaque paiement périodique
    taux_interet -- taux d'intérêt par période (en décimal, par exemple 0.05 pour 5%)
    
    Retourne:
    La valeur actuelle de la perpétuité.
    """
    if taux_interet <= 0:
        raise ValueError("Le taux d'intérêt doit être supérieur à zéro.")
    
    valeur_presente = paiement / taux_interet
    return valeur_presente

# Exemple d'utilisation de la fonction
if __name__ == "__main__":
    # Montant de chaque paiement périodique
    paiement = 1000.0  # en dollars
    
    # Taux d'intérêt par période
    taux_interet = 0.05  # 5% en décimal
    
    # Calculer la valeur actuelle de la perpétuité
    valeur_presente = valeur_actuelle_perpetuite(paiement, taux_interet)
    print(f"La valeur actuelle d'une perpétuité avec des paiements de ${paiement:.2f} et un taux d'intérêt de {taux_interet*100:.2f}% est de: ${valeur_presente:.2f}\n")
