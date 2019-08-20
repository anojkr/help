# cook your dish here
from sys import stdin, stdout
from collections import defaultdict


def bfs_matrix(matrix, i, visited):
    t = []
    u = i
    visited[u] = 1
    q = []
    q.append(u)
    t.append(u+1)
    while len(q)!= 0:
        # print(q)
        u = q.pop(0)
        for i in range(0, n):
            if (visited[i] != 1 and matrix[u][i] > 0):
                t.append(i+1)
                visited[i] = 1
                q.append(i)
    print(t)
    # print(visited)
    
def bfs_list(adj_list, i, visited):
    u = i
    visited[u] = 1
    t = []
    q = []
    q.append(u)
    t.append(u)
    # print(adj_list[u])
    while len(q) != 0:
        u = q.pop(0)
        # print(adj_list[u])
        for node, weight in adj_list[u]:
            # print(node+1)
            if (visited[node] != 1 and weight > 0):
                q.append(node)
                t.append(node)
                visited[node] = 1
    print(t)
    # print(visited)
    

def bfs(matrix, adj_list, edges, n, e):
    visited_matrix = [0]*n
    visited_list = [0]*(n+1)
    # for i in range(0, n):
    node = 3-1
    bfs_matrix(matrix, node, visited_matrix)
    bfs_list(adj_list, 3, visited_list)
        
        

        
if __name__ == '__main__':
    n = int(stdin.readline())
    e = int(stdin.readline())
    graph_matrix = [[int(0) for j in range(n)] for i in range(0, n)]
    edges = []
    
    graph_adj_list = defaultdict(list)
    while e > 0:
        i, j, w = [int(x) for x in stdin.readline().split()]
        graph_adj_list[i].append((j,w))
        graph_matrix[i-1][j-1] = w
        e-= 1
    # print(graph_adj_list)
    bfs(graph_matrix, graph_adj_list, edges, n, e)
    