import math
#For INF
def dijkstra(graph, n, src):
    distance = [math.inf] * n
    distance[src] = 0
    final_selected = [(src, distance[src])]
    curr_vertex = src

    while len(final_selected) < n:
        min_vertex, min_dist = -1, math.inf
        for neighbor in graph[curr_vertex]:
            vertex, weight = neighbor
            distance[vertex] = min(
                distance[curr_vertex] + weight, distance[vertex])

        for vertex in range(n):
            if distance[vertex] <= min_dist and (vertex, distance[vertex]) not in final_selected:
                min_vertex, min_dist = vertex, distance[vertex]

        final_selected.append((min_vertex, min_dist))
        curr_vertex = min_vertex

    print('Vertex\tDistance')
    [print(f'{v}\t{d}') for v, d in final_selected]
if __name__ == "__main__":
    n = int(input("Enter no of vertices: "))
    e = int(input("Enter no of edges: "))
    graph_dict = {}
    print("Enter the edges as follows: [start] [end] [weight]")
    for i in range(e):
        start, end, weight = [int(j) for j in input().split()]
        if not graph_dict.get(start):
            graph_dict[start] = [(end, weight)]
        else:
            graph_dict[start].append((end, weight))
    
        if not graph_dict.get(end):
            graph_dict[end] = [(start, weight)]
        else:
            graph_dict[end].append((start, weight))
    for i in range(n):
        print(f'Source {i}: ')
        dijkstra(graph_dict, n, i)
