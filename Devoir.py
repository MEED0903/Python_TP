def import_ligne(name):
    with open(name,'r') as file:
        return file.readlines()

def create_patient(ligne):
    info = ligne.strip().split()
    if len(info)!=3:
        raise ValueError("The ligne should have 3 elements : name,weight,height.")
    patient = {'nom':info[0],'poids':float(info[1]),'taille':float(info[2])}
    return patient

def  liste_patients_from_nom_fichier(name):
    patient = []
    try:
        with open(name,'r') as ligne:
            for ligne in ligne:
                if ligne.strip():
                    patient.append(create_patient(ligne))
    except FileNotFoundError:
        print(f"Error : {name} not found")
    return patient

def imc(patient):
    nbr = patient['poids']/(patient['taille']**2)
    return round(nbr,2)

def imcmoyen(patients):
    if not patients:
        return 0
    total = 0
    for patient in patients:
        total += imc(patient)
    moyen = total/len(patients)
    return round(moyen,2)

def liste_noms_patients_en_corpulence_normale(patients):
    imc_normal = []
    for patient in patients:
        imc_pat = imc(patient)
        if (imc_pat>=18.5 and imc_pat<=25):
            imc_normal.append(patient['nom'])
    return imc_normal

def produire_chaine(patient):
    return f"{patient['nom']} {round(imc(patient),2)}\n"

def ecrire_imc(patients,dest):
    with open(dest,'w') as file:
        for patient in patients:
            file.write(produire_chaine(patient))

        file.write(f"IMC moyen = {imcmoyen(patients)}\n")

        normal = liste_noms_patients_en_corpulence_normale(patients)
        if normal:
            file.write(f"Noms des patients en corpulence normale : {normal}\n")
        else:
            file.write("Aucun patient en corpulence normale.\n")

def  traitement_complet_donnees(src,dest):
    patients = liste_patients_from_nom_fichier(src)
    ecrire_imc(patients,dest)