import random as r
import math as m
import matplotlib.pyplot as plt
from pandas import*
import copy

#f solution

def create_population(total): #création de la population
    population=[]
    for i in range(total):
        individu=[r.uniform(-100, 100),r.uniform(-100, 100),r.uniform(-100, 100),r.uniform(-100, 100),r.uniform(-100, 100),r.uniform(-100, 100)]
        population.append(individu)
    return population

#f fitness

def fitness(population,t,valExactX, valExactY):
    
    resultat = []
    
    for i in range(len(population)):
        
        indiv = population[i]
        score = 0
        
        for j in range(len(t)):
            
            x = indiv[0]*m.sin(indiv[1]*t[j]+indiv[2])
            y = indiv[3]*m.sin(indiv[4]*t[j]+indiv[5])
            
            score += (valExactX[j]-x)**2 + (valExactY[j]-y)**2
            
        resultat.append([m.sqrt(score),population[i]]) 
          
    return sorted(resultat)
          
    return 

#f selection des meilleurs et des nazes

def selection(population,k=1):
    l=[]
    for i in range(k):
        l.append(population[i][1])
    return l

#f crossover

def croisement(population):
    
    l=[]
    #pop = copy.deepcopy(population)
    for i in range(len(population)):
        
        indiv1 = population[r.randint(0, len(population)-1)]
        indiv2 = population[r.randint(0, len(population)-1)]
        NEWindiv = []
        
        for j in range(3):
            NEWindiv.append(indiv1[j])
        for t in range(3,6):
            NEWindiv.append(indiv2[t])
        
        l.append(NEWindiv)
        
    return l

#f mutation

def mutation(population):

    pop = copy.deepcopy(population)
    
    for i in range(len(pop)):
        
        a = r.randint(0,5)
        b = r.uniform(-1,1)
        
        if population[i][a]<100 and population[i][a]>-100:
            
            population[i][a]+=b
            
    return pop



#écriture fichier

data = read_csv('position_sample.csv', sep=";")

t = data['#t'].tolist()
x = data['x'].tolist()
y = data['y'].tolist()


pop = create_population(10000)
nb = 0
fit = fitness(pop,t,x,y)


while m.sqrt(fit[0][0]) > 1.5 :
    
    fit = fitness(pop,t,x,y)
    
    print("Génération", nb, " : ", m.sqrt(fit[0][0]))
    
    sel_pop = selection(fit,500)
    r.shuffle(pop)
    mut_pop = mutation(pop[:4000])
    r.shuffle(pop)
    crois_pop = croisement(pop[:4000])
    new_pop = create_population(1500)
    
    pop = sel_pop + new_pop + mut_pop + crois_pop 
    r.shuffle(pop)
    
    nb += 1
    
print("Distance euclidienne", fit[0][0])


#problemes

l=selection(fitness(pop,t,x,y))[0]

print("Liste des paramètres p : ", l)
print("Génération finale : ", nb)


