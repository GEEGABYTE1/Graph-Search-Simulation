from test_values import dictionary 

def dfs(graph, current_vertex, target, visited=None):
    if visited == None:
        visited = []
    visited.append(current_vertex)
    if current_vertex == target:
        return visited 
    else:
        for neighbour in graph[current_vertex]:
            print(visited)
            if not neighbour in visited:
                path = dfs(graph, neighbour, target, visited)

                if path:
                    return path
    
            