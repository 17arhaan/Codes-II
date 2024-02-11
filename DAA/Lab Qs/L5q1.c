#include <stdio.h>
#include <stdlib.h>
#define MAX_VERTICES 100

typedef struct Node {
    int vertex;
    struct Node* next;
} Node;

typedef struct {
    Node* adjLists[MAX_VERTICES];
    int numVertices;
} Graph;

Node* createNode(int v) {
    Node* newNode = malloc(sizeof(Node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}

Graph* createGraph(int vertices) {
    Graph* graph = malloc(sizeof(Graph));
    graph->numVertices = vertices;
    for (int i = 0; i < vertices; i++)
        graph->adjLists[i] = NULL;
    return graph;
}

void addEdge(Graph* graph, int src, int dest) {
    Node* newNode = createNode(dest);
    newNode->next = graph->adjLists[src];
    graph->adjLists[src] = newNode;
}

void dfs(int v, Graph* graph, int visited[], int* stack, int* index) {
    visited[v] = 1;
    for (Node* temp = graph->adjLists[v]; temp != NULL; temp = temp->next)
        if (!visited[temp->vertex])
            dfs(temp->vertex, graph, visited, stack, index);
    stack[(*index)++] = v;
}

void topologicalSortDFS(Graph* graph) {
    int visited[MAX_VERTICES] = {0}, stack[MAX_VERTICES], index = 0;
    for (int i = 0; i < graph->numVertices; i++)
        if (!visited[i]) dfs(i, graph, visited, stack, &index);
    printf("Topological Sort using DFS: ");
    for (int i = index - 1; i >= 0; i--) printf("%d ", stack[i]);
}

void topologicalSortSourceRemoval(Graph* graph) {
    int inDegree[MAX_VERTICES] = {0}, queue[MAX_VERTICES], front = 0, rear = -1;
    for (int i = 0; i < graph->numVertices; i++)
        for (Node* temp = graph->adjLists[i]; temp != NULL; temp = temp->next) inDegree[temp->vertex]++;
    for (int i = 0; i < graph->numVertices; i++)
        if (inDegree[i] == 0) queue[++rear] = i;
    printf("\nTopological Sort using Source Removal: ");
    while (front <= rear) {
        int vertex = queue[front++];
        printf("%d ", vertex);
        for (Node* temp = graph->adjLists[vertex]; temp != NULL; temp = temp->next)
            if (--inDegree[temp->vertex] == 0) queue[++rear] = temp->vertex;
    }
}

int main() {
    int numVertices, numEdges;
    printf("Enter the number of vertices: ");
    scanf("%d", &numVertices);
    printf("Enter the number of edges: ");
    scanf("%d", &numEdges);
    Graph* graph = createGraph(numVertices);
    printf("Enter the edges (source destination):\n");
    for (int i = 0, src, dest; i < numEdges; i++) {
        scanf("%d %d", &src, &dest);
        addEdge(graph, src, dest);
    }
    topologicalSortDFS(graph);
    topologicalSortSourceRemoval(graph);
    return 0;
}
