from fonctions import tangente, sigmoide

class Reseau:
    def __init__(self, name = 'Unknown', learn = 'sigmoide', error = 0.001):

        # INITIALISATION : 
        ## Le nom du reseau
        ## La fonction d'activation
        ## L'erreur désirée

        self.name = name
        if str.lower(learn) == 'sigmoide':
            self.fun_learn = sigmoide
        elif str.lower(learn) == 'tanh':
            self.fun_learn = tangente
        self.name_fun_learn = learn

        self.error = error
        self.couche = [] # nombre de neurones par couche
        self.link = [] # matrice de poids 
        self.values = [] # valeurs des neurones

        self.control = 0 # empeche l'ajout de couche et de neurones en vérifiant que le réseau n'est pas initialisé
    
    # ACCESSEURS : 

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def setLearn(self, learn):
        self.fun_learn = learn
    
    def getNameFunLearn(self):
        return self.name_fun_learn
    
    def getLearn(self):
        return self.fun_learn

    def setError(self, error):
        if error > 0 : 
            self.error = error
    
    def getError(self):
        return self.error

    def getData(self):
        return [self.getName(), self.getNameFunLearn(), self.getError(), self.getNbrCouche()]
    
    def getNbrCouche(self):
        return len(self.couche)
    
    def getLastCouche(self):
        return self.values[-1]
    
    # Fonctions pour créer le réseau :
    
    def setCouche(self, value = 4):
        if (self.control == 0):
            if (value >= 2):
                for i in range(0, value):
                    self.couche.append(0)
            else:
                print('Erreur : le nombre de couches doit être supérieur ou égal à 2')
        else: 
            print('Erreur : le réseau est déjà initialisé')
    

    def add_couche(self, pos):
        
        if (self.control == 0):
            if (pos > 0 and pos < len(self.couche)):
                self.couche.insert(pos, 0)
            else:
                print('Erreur : la position doit être comprise entre 1 et', len(self.couche) - 1)

    def add_neurone(self, couche, nbr=1):
        if (self.control == 0):
            if (couche >= 0  and couche<=len(self.couche)-1 and nbr >0):
                self.couche[couche] += nbr
        else:
            print('Erreur : le réseau est déjà initialisé')