#Add the needed ADTs via

# ADT to store a single node 
class NodeC:
    def __init__(self, name, population, language):
        self._name = name
        self._population = population
        self._language = language
    def getname(self):
        return self._name
        
    def get_population(self):
        return self._population
        
    def get_language(self):
        return self._language

# ADT to model the Directed Graph
class DirectedGraph:
    def __init__(self, country_data):
        self.dictionary = {}
        self.nextm = {}
        self.inf = float("inf")
        for name, population, language in country_data:
            self.dictionary[name] = NodeC(name,population,language)
            self.nextm[name] = {i: self.inf for i in self.dictionary}
            self.nextm[name][name] = 0

        for j in self.dictionary:
            for i in self.dictionary:
                if i not in self.nextm[j]:
                    self.nextm[j][i] = self.inf

    def print_transition_matrix(self):
        head = [""] + list(self.dictionary.keys())
        print("\t".join(head))
        for i in self.dictionary.keys():
            index = [i] +[str(self.nextm[i][cols]) if self.nextm[i][cols] != self.inf else "*" for cols in self.dictionary]
            print("\t".join(index))




    

    def add_edge(self, start_country, end_country, distance): #O(1)

            if start_country == end_country:
                raise ValueError("Cannot connect a node to itself.")
            if distance <= 0:
                raise ValueError("Distance must be a positive integer.")

            self.nextm[start_country][end_country] = distance
    
    def find_path(self, start_country, end_country):
        if self.nextm[start_country][end_country] != 0:
            if self.nextm[start_country][end_country] != self.inf:
                return f"[{start_country}{end_country}], {self.nextm[start_country][end_country]}"
            elif self.nextm[start_country][end_country] == 0:
                return f"[{start_country}{end_country}], {self.nextm[start_country][end_country]}"


    def bubblesort(self, nonzero_values): #O(n^2)
        n = len(nonzero_values)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if nonzero_values[j] > nonzero_values[j + 1]:
                    nonzero_values[j], nonzero_values[j + 1] = nonzero_values[j + 1], nonzero_values[j]
        return nonzero_values




    def get_sorted_distances(self): #O(n^2)
        distances = []
        for i in self.dictionary:
            for j in self.dictionary.keys():
                dist = self.nextm[i][j]
                if i != j and dist != self.inf:
                    distances.append((self.nextm[i][j]))
        return self.bubblesort(distances)




    def sort_countries_by_population(self, ascending=True): #O(n^2)
            population = []
            for i in self.dictionary:
                population.append(self.dictionary[i]._population)
            if ascending:
                return self.bubblesort(population)
            if not ascending:
                reversepopulation = []
                x = self.bubblesort(population)

                for i in reversed(range(len(x))):
                    reversepopulation.append(x[i])
                return reversepopulation


            
            
if __name__ == "__main__":
    # Test 1: European countries with populations (in millions) and their main language
    print(f"Test 1:")
    europe_data = [
        ("France", 67, "French"),
        ("Germany", 83, "German"),
        ("Italy", 60, "Italian"),
        ("Spain", 47, "Spanish"),
        ("Portugal", 10, "Portuguese")
    ]

    europe_graph = DirectedGraph(europe_data)

    # Add connections
    europe_graph.add_edge("France", "Germany", 500)
    europe_graph.add_edge("Germany", "Italy", 800)
    europe_graph.add_edge("Italy", "Spain", 1000)
    europe_graph.add_edge("Spain", "Portugal", 400)
    europe_graph.add_edge("France", "Spain", 900)
    europe_graph.add_edge("Portugal", "France", 1200)
    
    print("Transition Matrix for European Countries:")
    europe_graph.print_transition_matrix()
    """
	        France	Germany	Italy	Spain	Portuga
    France	0	    500	    ∞	    900	    ∞
    Germany	∞	    0	    800	    ∞	    ∞
    Italy	∞	    ∞	    0	    1000	∞
    Spain	∞	    ∞	    ∞	    0	    400
    Portuga	1200	∞	    ∞	    ∞	    0
    """

    # Test path finding with more cases
    print("\nPath from France to Portugal:", europe_graph.find_path("France", "Portugal"))
    # Possible: (['France', 'Spain', 'Portugal'], 1300) or (['France', 'Germany', 'Italy', 'Spain', 'Portugal'], 2700)

    print("Path from Germany to France:", europe_graph.find_path("Germany", "France"))
    # Expected:  (['Germany', 'Italy', 'Spain', 'Portugal', 'France'], 3400)

    print("Path from Italy to Italy:", europe_graph.find_path("Italy", "Italy"))
    # Expected: (['Italy'], 0)
        
    # Test sorted distances
    print("\nAll distances in Europe graph:", europe_graph.get_sorted_distances())
    # [400, 500, 800, 900, 1000, 1200]
    
    # Test sort countries by population
    print("European Countries by Population (Ascending):")
    print(europe_graph.sort_countries_by_population())
    # Expected: ['Portugal', 'Spain', 'Italy', 'France', 'Germany']
    
    print("\nEuropean Countries by Population (Descending):")
    print(europe_graph.sort_countries_by_population(ascending=False))
    # Expected: ['Germany', 'France', 'Italy', 'Spain', 'Portugal']
    
    # Test 2: Is the internal direct graph implementation agnostic to the nodes naming?
    print(f"Test 2:")
    # Another test with European countries with populations (in millions) and their main language.
    # We can reuse the same variables.
    europe_data = [
        ("Germany", 83, "German"),
        ("France", 67, "French"),
        ("Portugal", 10, "Portuguese"),
        ("Spain", 47, "Spanish"),
        ("Italy", 60, "Italian")
    ]
    europe_graph = DirectedGraph(europe_data)

    # Add connections
    europe_graph.add_edge("France", "Germany", 500)
    europe_graph.add_edge("Germany", "Italy", 800)
    europe_graph.add_edge("Italy", "Spain", 1000)
    europe_graph.add_edge("Spain", "Portugal", 400)
    europe_graph.add_edge("France", "Spain", 900)
    europe_graph.add_edge("Portugal", "France", 1200)
    
    print("Transition Matrix for European Countries:")
    europe_graph.print_transition_matrix()
    """
		    Germany	France	Portuga	Spain	Italy
    Germany	0	    ∞	    ∞	    ∞	    800
    France	500	    0	    ∞	    900	    ∞
    Portuga	∞	    1200	0	    ∞	    ∞
    Spain	∞	    ∞	    400	    0	    ∞
    Italy	∞	    ∞	    ∞	    1000	0
     
    """

    # Test path finding with more cases
    print("\nPath from France to Portugal:", europe_graph.find_path("France", "Portugal"))
    # Possible: (['France', 'Spain', 'Portugal'], 1300) or (['France', 'Germany', 'Italy', 'Spain', 'Portugal'], 2700)

    print("Path from Germany to France:", europe_graph.find_path("Germany", "France"))
    # Expected:  (['Germany', 'Italy', 'Spain', 'Portugal', 'France'], 3400)

    print("Path from Italy to Italy:", europe_graph.find_path("Italy", "Italy"))
    # Expected: (['Italy'], 0)
        
    # Test sorted distances
    print("\nAll distances in Europe graph:", europe_graph.get_sorted_distances())
    # [400, 500, 800, 900, 1000, 1200]
    
    # Test sort countries by population
    print("European Countries by Population (Ascending):")
    print(europe_graph.sort_countries_by_population())
    # Expected: ['Portugal', 'Spain', 'Italy', 'France', 'Germany']
    
    print("\nEuropean Countries by Population (Descending):")
    print(europe_graph.sort_countries_by_population(ascending=False))
    # Expected: ['Germany', 'France', 'Italy', 'Spain', 'Portugal']


    # Test 3: Asian countries with populations (in millions) and their main language.
    # A directed graph with more nodes and edges.
    print(f"Test 3:")
    asia_data = [
        ("Japan", 126, "Japanese"),
        ("China", 1400, "Mandarin*"),
        ("India", 1366, "Hindi"),
        ("Thailand", 70, "Thai"),
        ("Vietnam", 97, "Vietnamese"),
        ("Malaysia", 32, "Malay"),
        ("Indonesia", 273, "Bahassa Indonesia"),
        ("Philippines", 110, "Tagalog")
    ]
    asia_graph = DirectedGraph(asia_data)

    # Add connections
    asia_graph.add_edge("Japan", "China", 2100)
    asia_graph.add_edge("China", "India", 3000)
    asia_graph.add_edge("India", "Thailand", 2000)
    asia_graph.add_edge("Thailand", "Vietnam", 800)
    asia_graph.add_edge("Vietnam", "China", 1200)
    asia_graph.add_edge("China", "Malaysia", 3500)
    asia_graph.add_edge("Malaysia", "Indonesia", 1100)
    asia_graph.add_edge("Indonesia", "Philippines", 2400)
    asia_graph.add_edge("Philippines", "Japan", 3000)
    asia_graph.add_edge("Thailand", "Malaysia", 600)
    
    print("Transition Matrix for European Countries:")
    asia_graph.print_transition_matrix() 
    """
	        Japan	China	India	Thailan	Vietnam	Malaysi	Indones	Philipp
    Japan	0	    2100	∞	    ∞	    ∞	    ∞	    ∞	    ∞
    China	∞	    0	    3000	∞	    ∞	    3500	∞	    ∞
    India	∞	    ∞	    0	    2000	∞	    ∞	    ∞	    ∞
    Thailan	∞	    ∞	    ∞	    0	    800	    600	    ∞	    ∞
    Vietnam	∞	    1200	∞	    ∞	    0	    ∞	    ∞	    ∞
    Malaysi	∞	    ∞	    ∞	    ∞	    ∞	    0	    1100	∞
    Indones	∞	    ∞	    ∞	    ∞	    ∞	    ∞	    0	    2400
    Philipp	3000	∞	    ∞	    ∞	    ∞	    ∞	    ∞   	0
    """

    # Test path finding in Asia graph
    print("\nPath from Japan to Indonesia:", asia_graph.find_path("Japan", "Indonesia"))
    # Possible: (['Japan', 'China', 'India', 'Thailand', 'Malaysia', 'Indonesia'], 8800)

    print("Path from Thailand to Japan:", asia_graph.find_path("Thailand", "Japan"))
    # Possible: (['Thailand', 'Vietnam', 'China', 'Malaysia', 'Indonesia', 'Philippines', 'Japan'], 12000)

    print("Path from Malaysia to Philippines:", asia_graph.find_path("Malaysia", "Philippines"))
    # Expected:  (['Malaysia', 'Indonesia', 'Philippines'], 3500)

    print("\nAll distances in Asia graph:", asia_graph.get_sorted_distances())
    # [600, 800, 1100, 1200, 2000, 2100, 2400, 3000, 3000, 3500]
    
    print("\nAsian Countries by Population (Ascending):")
    print(asia_graph.sort_countries_by_population())
    # Expected: ['Malaysia', 'Thailand', 'Vietnam', 'Philippines', 'Japan', 'Indonesia', 'India', 'China']
    print("\nAsian Countries by Population (Descending):")
    print(asia_graph.sort_countries_by_population(ascending=False))
    # Expected: ['China', 'India', 'Indonesia', 'Japan', 'Philippines', 'Vietnam', 'Thailand', 'Malaysia']


