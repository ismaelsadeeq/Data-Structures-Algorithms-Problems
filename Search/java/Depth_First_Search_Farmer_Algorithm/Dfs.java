package Search.java.Depth_First_Search_Farmer_Algorithm;

// A farmer has to cross a river with his fox,goose and grain.Each trip,his boat can only carry himself and one of his possessions.How can he cross the river if an unguarded fox eats the goose and an unguarded goose eats the grain.–Perform Depth-first search–Perform Breadth-first search

class Main {
    // let us assume Farmer = Fa(0), Fox = Fo(1), Goat = Go(2), Grain = Gr(3)
    // linkedlist with strings.
    // a - fa, fo, go, gr | none
    // b - fo gr fa | go
    // c - gr | fa fo go
    // d - gr go fa | fo
    // e - go | fo fa gr
    // f - fo | fa go gr
    // g - fa go fo | gr
    // h - fo fa | fo gr
    // i - fo gr | fa go
    // j - none | fo gr fa fo

    public static void main(String[] args) {
        // System.out.println("test");
        Graph graph = new Graph(10);

        graph.addNote(new Node('A'));
        graph.addNote(new Node('B'));
        graph.addNote(new Node('C'));
        graph.addNote(new Node('D'));
        graph.addNote(new Node('E'));
        graph.addNote(new Node('F'));
        graph.addNote(new Node('G'));
        graph.addNote(new Node('H'));
        graph.addNote(new Node('I'));
        graph.addNote(new Node('J'));

        graph.addEdge(0, 7);
        graph.addEdge(7, 1);
        graph.addEdge(1, 2);
        graph.addEdge(1, 5);
        graph.addEdge(2, 3);
        graph.addEdge(3, 4);
        graph.addEdge(4, 8);
        graph.addEdge(8, 9);
        graph.addEdge(8, 6);

        graph.print();
        graph.depthFirstSearch(0);
    }
}