package Search.java.Depth_First_Search_Farmer_Algorithm;

import java.util.ArrayList;

public class Graph {
    ArrayList<Node> nodes;
    int[][] matrix;

    Graph(int size) {
        nodes = new ArrayList<Node>();
        matrix = new int[size][size];
    }

    public void addNote(Node node) {
        nodes.add(node);
    }

    public void addEdge(int source, int destination) {
        matrix[source][destination] = 1;
    }

    public boolean checkEdge(int source, int destination) {
        if (matrix[source][destination] == 1) {
            return true;
        }
        return false;
    }

    public void print() {
        System.out.print("");
        for (Node node : nodes) {
            System.out.print(node.data + "");
        }
        System.out.println("");
    }

    public void depthFirstSearch(int source) {
        boolean[] visited = new boolean[matrix.length];
        dfsHelper(source, visited);
    }

    private void dfsHelper(int source, boolean[] visited) {
        if (visited[source] == true) {
            return;
        } else {
            visited[source] = true;
            System.out.println(nodes.get(source).data + " = visted");
        }
        for (int i = 0; i < matrix[source].length; i++) {
            if (matrix[source][i] == i) {
                dfsHelper(i, visited);
            }
        }
        return;
    }
}
