# Depth First Search - Farmer riddle ALGORIGHM

// A farmer has to cross a river with his fox,goose and grain.Each trip,his boat can only carry himself and one of his possessions.How can he cross the river if an unguarded fox eats the goose and an unguarded goose eats the grain.–Perform Depth-first search–Perform Breadth-first search

📌 **Time Complexity:** O(V2) <br>
📌 **Space Complexity:** O(V) <br>

<!-- reference -->

https://www.simplilearn.com/tutorials/data-structure-tutorial/dfs-algorithm

<!-- explanation -->

If a graph is represented as an adjacency matrix(which is of our case)
then the whole row in the matrix will have to be transversed in the matrix, which means each row corresponds to a node in the graph and will store information about each edges it merges from that vertex.

Therefore, resulting as time complexity will be considered as O(V.V) = O(v2)
Since we have to keep track of last visited vertex, resulting in our stack increasing by the graph's vertices, the space complexity would be O(V)
