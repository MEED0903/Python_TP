class Patient:
    def __init__(self, nom, poids, taille):
        self.nom = nom
        self.poids = poids
        self.taille = taille
    
    def imc(self):
        return round(self.poids / self.taille**2, 2)

class ManagePatients:
    def __init__(self):
        self.patients = []

    def import_lines(self, file):
        with open(file, 'r') as ligne:
            return ligne.readlines()

    def create_patient(self, ligne):
        info = ligne.strip().split()
        return Patient(info[0], float(info[1]), float(info[2]))
    
    def liste_patients_from_nom_fichier(self, file):
        lignes = self.import_lines(file)
        self.patients = [self.create_patient(ligne) for ligne in lignes]
        return self.patients
    
    def imc_moy(self):
        if not self.patients:
            return 0
        total = sum(patient.imc() for patient in self.patients)
        return round(total / len(self.patients), 2)
    
    def liste_noms_patients_en_corpulence_normale(self):
        return [patient.nom for patient in self.patients if 18.5 <= patient.imc() <= 25]
        
    def produire_chaine(self, patient):
        return f"{patient.nom} {patient.imc()}\n"
    
    def ecrire_imc(self, dest):
        with open(dest, 'a') as file:
            for patient in self.patients:
                file.write(self.produire_chaine(patient))
            file.write(f"IMC Moyen = {self.imc_moy()}\n")
            
            normal = self.liste_noms_patients_en_corpulence_normale()
            file.write("Noms des patients en corpulence normale :\n")
            if normal:
                file.writelines([f"{nom}\n" for nom in normal])
            else:
                file.write("Aucun patient en corpulence normale.\n")

    def traitement_complet_donnees(self, src, dest):
        self.liste_patients_from_nom_fichier(src)
        self.ecrire_imc(dest)


manager = ManagePatients()
manager.traitement_complet_donnees('mohamed.txt', 'mabrouk.txt')
