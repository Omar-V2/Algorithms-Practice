graph = {
    1: [2, 3],
    2: [4, 5],
    3: [5],
    4: [6],
    5: [6],
    6: [7],
    7 : []
}

def DFS_iterative(graph, start):
    stack = [start]
    visited = []
    while stack:
        current = stack.pop()
        for vertex in graph[current]:
            if vertex not in visited:
                stack.append(vertex)
        visited.append(current)
    return visited

def DFS_recursive(graph, start, visited=[]):
    visited += [start]
    for neighbour in graph[start]:
        if neighbour not in visited:
            visited = DFS_recursive(graph, neighbour)
    return visited

visited = [0]*(len(graph)+1)
def DFS_recursive2(graph, start, visited):
    if visited[start] == 1:
        return
    visited[start] = 1
    for neighbour in graph[start]:
            DFS_recursive2(graph, neighbour, visited)
    return visited




print(DFS_iterative(graph, 1))
print(DFS_recursive(graph, 1))
print(DFS_recursive2(graph, 1, visited))


