import pandas as pd
import numpy as np
data_address = "./gp-training-set.csv"
data = pd.read_csv(data_address, header = None)
new_data = np.array(data)
# print(new_data.shape)
# print(new_data[:,-1])

'''class of individuals: the single object in population'''
class indivdual:
    def __init__(self):
        self.weight = 0  # genome
        self.fitness_loss = 0  # fitness value
    def __eq__(self, other):
        self.weight = other.weight
        self.fitness_loss = other.fitness_loss


'''calculate the best fit type'''
def fitness(x, data=new_data):
    acc = 0
    for i in range(data.shape[0]):
        temp = np.sum(x[:-1]*data[i,:-1]) - x[-1]
        # if the neural is positive and label is positive too
        if (temp >= 0 and data[i,-1] == 1):
            acc +=1
        # if the neural is negative and label is negative too
        if (temp < 0 and data[i,-1] == 0):
            acc +=1
    return acc



'''Initial the Population with randomness'''
def initPopulation(pop, N):
    for i in range(N):
        ind = indivdual()  # initial individual
        ind.weight = np.random.uniform(low=-1,high=1, size=10)  # generate random weight
        # print(ind.weight)
        ind.fitness_loss = fitness(ind.weight)  # get fitness score
        pop.append(ind)  # append to population


'''selected for the best individual'''
def selection(POP):
    POP.sort(key=lambda ind: ind.fitness_loss, reverse=True)  # get the best individual
    return POP[0], POP[1]


'''do the k-crossover (a better form than crossover simply)'''
def crossover(parent1, parent2, POP):
    for ind in range(25):
        randomll = np.random.choice(10,10,replace=False)  # random choice of sequence from 1 to 10
        weight_new_1 = np.zeros_like(parent1.weight)  # initial new weight
        weight_new_2 = np.zeros_like(parent2.weight)  # initial new weight
        for i in range(6):
            weight_new_1[randomll[i]] += parent1.weight[randomll[i]]  # copy 6 gene from parent 1
            weight_new_2[randomll[i]] += parent2.weight[randomll[i]]  # copy 6 gene from parent 2
        for j in range(4):
            weight_new_1[randomll[j+5]] += parent1.weight[randomll[j+5]]  # copy 4 gene from parent 1
            weight_new_2[randomll[j+5]] += parent2.weight[randomll[j+5]]  # copy 4 gene from parent 2
        child1, child2 = indivdual(), indivdual()
        child1.weight = weight_new_1  # initial children 1 with new weight
        child2.weight = weight_new_2  # initial children 2 with new weight
        child1.fitness = fitness(child1.weight)
        child2.fitness = fitness(child2.weight)
        POP[10+ind], POP[10+ind]
    return POP  # return 2 children


'''do mutation on parents'''
def mutation(pop):
    for i in range(40):
        pop[60+i].weight = np.random.uniform(low=-2,high=2, size=10)  # random times 10
        # pop[90+i].weight = pop[90+i].weight.reshape(-1)
        pop[60+i].fitness_loss = fitness(pop[60+i].weight)  # get fitness score


'''evolve of the whole population'''
def evolve(POP, i):
    N = 100  # size of the population
    # POP = []  # the population
    iter_N = 100  # number of iterations
    mut_prob = 0.1  # mutate with prob mut_prob
    if  i == 0:
        if POP[0] == 1:
            pop.remove(POP[0])
            initPopulation(POP, N)
    acc_list = []
    for it in range(iter_N):
        father, mother = selection(POP) # parents
        crossover(father,mother,POP)
        mutation(POP)
        if it % 10 == 0:
            acc_list.append(POP[0].fitness_loss)
        # POP.sort(key=lambda ind: ind.fitness_loss, reverse=True) # sort by decreament on Population
    return POP, acc_list


'''main function here'''
best_acc = 0 # the best prediction
best_gen = indivdual() # initial a best individual
pop=[1]
for count in range(10000):
    # print("...still training...",count,best_acc, best_gen.fitness_loss)
    pop, list = evolve(pop, count)  # evolve and keep the best individual in the front

    # print(pop[0].fitness_loss)
    if best_acc <= pop[0].fitness_loss:
        best_acc = pop[0].fitness_loss  # get the best acc
        best_gen = pop[0] # get the best individual
        print("generaltion:",count,"\t","our best generation accuracy:", best_acc)
        print("generaltion:",count,"\t","our best generation:", best_gen.weight)
    print("...still training...", count, best_gen.fitness_loss, "loss list", list)
    if best_acc == 100:
        break
print("training end")