import random

POPULATION_SIZE = 100
MAX_GENERATIONS = 100
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.1
TOURNAMENT_SIZE = 5


def calculate_fitness(destinos, conexoes, cromossomo):
    tempo_atual = 0
    lucro_total = 0

    for entrega in cromossomo:
        tempo_saida, destino, bonus = entrega
        tempo_viagem = conexoes[destinos.index('A')][destinos.index(destino)]

        if tempo_atual + tempo_viagem <= tempo_saida:
            tempo_atual += 2 * tempo_viagem
            lucro_total += bonus

    return lucro_total


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1_part1 = parent1[:crossover_point]
    child1_part2 = [entrega for entrega in parent2 if entrega not in child1_part1]

    child2_part1 = parent2[:crossover_point]
    child2_part2 = [entrega for entrega in parent1 if entrega not in child2_part1]

    child1 = child1_part1 + child1_part2
    child2 = child2_part1 + child2_part2

    return child1, child2


def mutate(cromossomo):
    index1 = random.randint(0, len(cromossomo) - 1)
    index2 = random.randint(0, len(cromossomo) - 1)
    cromossomo[index1], cromossomo[index2] = cromossomo[index2], cromossomo[index1]


def tournament_selection(population, fitness_values):
    selected = random.sample(list(zip(population, fitness_values)), TOURNAMENT_SIZE)
    selected.sort(key=lambda x: x[1], reverse=True)
    return selected[0][0]


def leilao_v3_genetico(destinos, conexoes, entregas):
    entregas.sort(key=lambda x: x[0])

    population = [random.sample(entregas, len(entregas)) for _ in range(POPULATION_SIZE)]

    for generation in range(MAX_GENERATIONS):
        fitness_values = [calculate_fitness(destinos, conexoes, cromossomo) for cromossomo in population]

        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1 = tournament_selection(population, fitness_values)
            parent2 = tournament_selection(population, fitness_values)

            if random.random() < CROSSOVER_RATE:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2

            if random.random() < MUTATION_RATE:
                mutate(child1)

            if random.random() < MUTATION_RATE:
                mutate(child2)

            new_population.extend([child1, child2])

        population = new_population

    best_cromossomo = max(population, key=lambda c: calculate_fitness(destinos, conexoes, c))
    lucro_total = calculate_fitness(destinos, conexoes, best_cromossomo)

    return best_cromossomo, lucro_total


def leilao_v3(destinos, conexoes, entregas):
    return leilao_v3_genetico(destinos, conexoes, entregas)
