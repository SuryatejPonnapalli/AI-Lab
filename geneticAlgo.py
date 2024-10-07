import random
import numpy as np
from typing import List, Tuple, Dict

# Define cities and distances
CITIES = {
    'Bucharest': (44.4268, 26.1025),
    'Cluj-Napoca': (46.7712, 23.6236),
    'Timisoara': (45.7489, 21.2087),
    'Iasi': (47.1585, 27.6014),
    'Constanta': (44.1598, 28.6348),
    'Craiova': (44.3302, 23.7949),
    'Brasov': (45.6427, 25.5887),
    'Galati': (45.4353, 28.0080)
}

def calculate_distance(city1: Tuple[float, float], city2: Tuple[float, float]) -> float:
    """Calculate Euclidean distance between two cities"""
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def create_distance_matrix() -> Dict:
    """Create a dictionary of distances between all cities"""
    distances = {}
    for city1 in CITIES:
        for city2 in CITIES:
            if city1 != city2:
                coord1 = CITIES[city1]
                coord2 = CITIES[city2]
                distances[f"{city1}-{city2}"] = calculate_distance(coord1, coord2)
    return distances

class TSPGeneticAlgorithm:
    def __init__(self, 
                 cities: List[str], 
                 distances: Dict, 
                 population_size: int = 100, 
                 elite_size: int = 20, 
                 mutation_rate: float = 0.01):
        self.cities = cities
        self.distances = distances
        self.population_size = population_size
        self.elite_size = elite_size
        self.mutation_rate = mutation_rate

    def create_route(self) -> List[str]:
        """Create a random route"""
        return random.sample(self.cities, len(self.cities))

    def initial_population(self) -> List[List[str]]:
        """Create initial population"""
        return [self.create_route() for _ in range(self.population_size)]

    def route_distance(self, route: List[str]) -> float:
        """Calculate total distance of a route"""
        total_distance = 0
        for i in range(len(route)):
            from_city = route[i]
            to_city = route[(i + 1) % len(route)]
            total_distance += self.distances[f"{from_city}-{to_city}"]
        return total_distance

    def rank_routes(self, population: List[List[str]]) -> List[Tuple[List[str], float]]:
        """Rank all routes in population"""
        results = [(route, self.route_distance(route)) for route in population]
        return sorted(results, key=lambda x: x[1])

    def selection(self, ranked_population: List[Tuple[List[str], float]]) -> List[List[str]]:
        """Select the best routes for breeding"""
        selection_results = [route for route, _ in ranked_population[:self.elite_size]]
        
        # Roulette wheel selection for remaining spots
        total_fitness = sum(1 / dist for _, dist in ranked_population)
        probabilities = [(1 / dist) / total_fitness for _, dist in ranked_population]
        
        while len(selection_results) < self.population_size:
            pick = np.random.choice(len(ranked_population), p=probabilities)
            selection_results.append(ranked_population[pick][0])
        
        return selection_results

    def breed(self, parent1: List[str], parent2: List[str]) -> List[str]:
        """Create a child route from two parent routes using ordered crossover"""
        child = [''] * len(self.cities)
        start, end = sorted(random.sample(range(len(self.cities)), 2))
        
        # Copy a segment from parent1
        child[start:end] = parent1[start:end]
        
        # Fill remaining positions with cities from parent2
        p2_index = 0
        for i in range(len(child)):
            if i < start or i >= end:
                while parent2[p2_index] in child:
                    p2_index += 1
                child[i] = parent2[p2_index]
                p2_index += 1
        
        return child

    def breed_population(self, selected: List[List[str]]) -> List[List[str]]:
        """Create a new population through breeding"""
        children = selected[:self.elite_size]  # Keep elite routes
        
        # Breed remaining routes
        pool = random.sample(selected, len(selected))
        for i in range(self.elite_size, len(selected)):
            child = self.breed(pool[i], pool[len(selected)-i-1])
            children.append(child)
        
        return children

    def mutate(self, route: List[str]) -> List[str]:
        """Potentially swap two cities in a route"""
        for i in range(len(route)):
            if random.random() < self.mutation_rate:
                j = random.randint(0, len(route) - 1)
                route[i], route[j] = route[j], route[i]
        return route

    def mutate_population(self, population: List[List[str]]) -> List[List[str]]:
        """Mutate all routes in population"""
        return [self.mutate(route[:]) if i >= self.elite_size else route[:] 
                for i, route in enumerate(population)]

    def next_generation(self, current_pop: List[List[str]]) -> List[List[str]]:
        """Create the next generation of routes"""
        ranked_pop = self.rank_routes(current_pop)
        selected = self.selection(ranked_pop)
        children = self.breed_population(selected)
        next_gen = self.mutate_population(children)
        return next_gen

    def solve(self, generations: int) -> Tuple[List[str], float]:
        """Run the genetic algorithm for a specified number of generations"""
        pop = self.initial_population()
        print(f"Initial distance: {self.route_distance(pop[0]):.2f}")
        
        for i in range(generations):
            pop = self.next_generation(pop)
            
            if (i + 1) % 10 == 0:
                best_route = self.rank_routes(pop)[0]
                print(f"Generation {i+1}: Best distance = {best_route[1]:.2f}")
        
        best_route = self.rank_routes(pop)[0]
        return best_route

def main():
    # Create distance matrix
    distances = create_distance_matrix()
    
    # Initialize and run genetic algorithm
    ga = TSPGeneticAlgorithm(
        cities=list(CITIES.keys()),
        distances=distances,
        population_size=100,
        elite_size=20,
        mutation_rate=0.01
    )
    
    # Solve TSP
    best_route, best_distance = ga.solve(generations=100)
    
    # Print results
    print("\nBest Route:")
    for i, city in enumerate(best_route[0], 1):
        print(f"{i}. {city}")
    print(f"\nTotal Distance: {best_distance:.2f}")

if __name__ == "__main__":
    main()