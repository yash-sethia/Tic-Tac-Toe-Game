# class node:
#     data = -1
#     successors = []
#     mark = False
#     solved =False
#
# edge_cost = 0
#
# def insert (root):
#     root.data = input("Enter the data of node :")
#     n_or = int(input("Enter number of branches of the node "))
#     for i in range(0, n_or):
#         ans = []
#         and_nodes = int(input("Enter number of AND nodes for " + str(i + 1) + "th node of value = " + str(root.data) + " = "))
#         for j in range(0, and_nodes):
#             n = node()
#             insert(n)
#             ans.append(n)
#
#         root.successors.append(ans)
#
#
# def ao_star(root):
#     min_ans = []
#     min_ans.append(root)
#
#     while(root.solved == False):
#         next_node = root
#
#         stack = []
#
#         while(next_node and next_node.mark == True):
#             if len(next_node.successors) == 0:
#                 root.solved = True
#                 return
#
#             cost = 99999
#
#             stack.push(next_node)
#
#             for i in range(0, len(next_node)):
#                 ans = next_node.successors[i]
#                 ans_v = ans
#
#                 temp_cost = 0
#
#                 for j in range(0, len(ans_v)):
#                     n = ans_v[j]
#                     temp_cost += n.data
#
#                 if(temp_cost < cost):
#                     min_ans = ans
#                     cost = temp_cost
#
#             min_ans_v = min_ans
#
#             next_node = None
#             for j in range(0, len(min_ans_v)):
#                 if min_ans_v[j].mark == True:
#                     next_node = min_ans_v[j]
#                     break
#
#
#             min_ans_v = min_ans
#
#             for j in range(0, len(min_ans_v)):
#                 n = min_ans_v[j]
#                 print("Exploring : " + n.data)
#                 final_cost = 99999
#
#                 if len(n.successors) == 0:
#                     n.mark = True
#                 else:
#                     for i in range(0, len(n.successors)):
#                         ans = n.successors[i]
#                         ans_v = ans
#                         temp_cost = 0
#                         for j in range(0, len(ans_v)):
#                             n = ans_v[j]
#                             temp_cost += n.data
#                             temp_cost += edge_cost
#
#                         if temp_cost < final_cost:
#                             final_cost = temp_cost
#
#                     n.data = final_cost
#                     n.mark = True
#
#                 printf("Marked : " + n.data)
#
#             print("***************************************")
#             while len(stack) != 0:
#                 n = stack[len(stack) - 1]
#
#                 print(n.data, end=" ")
#                 stack.pop()
#                 final_cost = 99999
#
#                 for i in range(0, len(n.successors)):
#                     ans = n.successors[i]
#                     ans_v = ans
#                     temp_cost = 0
#
#                     for j in range(0, len(ans_v)):
#                         n = ans_v[j]
#                         temp_cost += n.data
#                         temp_cost += edge_cost
#
#
#                     if(temp_cost < final_cost):
#                         min_ans = ans
#                         final_cost = temp_cost
#
#                 n.data = final_cost
#
#             print('\n')
#
#             next_node = root
#
#
# def print_solution(root):
#     if(root):
#         print(root.data, end=" ")
#         vec = root.successors
#         for i in range(0, len(root.successors)):
#              ans = root.successors[i]
#              ans_v = ans
#
#              for j in range(0, len(ans_v)):
#                  n = ans_v[j]
#                  print(n.data, end=" ")
#              print(" ")
#
#
#     return
#
#
#
#
# root = node()
# insert(root)
#
# print(' ')
#
# edge_cost = input("Enter the edge cost ")
# print("The tree is as follows ")
#
# print_solution(root)
#
# ao_star(root)
#
# print("The minimum cost is = " + root.data)
#
#
#
#
#
#
#
#
#
#
#





def ao_star(g, h, s, n, l):
    # Goodness value of child nodes
    f = []
    # Parent array
    parent = []
    for i in range(0, n):
        f.append(0)
        parent.append(0)

    parent[s] = -1

    def new_heuristic(s):
        blank = []
        for i in g[s]:
            x = 0
            if isinstance(i, list):
                for j in i:
                    x = x + h[j] + 1  # edge weight is 1
                    parent[j] = s
            else:
                x = x + h[i] + 1
                parent[i] = s
            blank.append(x)
        f[s] = blank

    def hset():
        if len(f[s]) == 0:
            return 0
        if f[s][0] < f[s][1]:
            h[s] = f[s][0]
        else:
            h[s] = f[s][1]
        return 1

    def pick_successor(s):
        # jh is like a flag telling us that it is a list or value
        jh = 0
        if f[s][0] < f[s][1]:
            h[s] = f[s][0]
            if isinstance(g[s][0], list):
                s = g[s][0][0]
                jh = 1
            else:
                s = g[s][0]
        else:
            h[s] = f[s][1]
            if isinstance(g[s][1], list):
                s = g[s][1][0]
                jh = 1
            else:
                s = g[s][1]
        return [s, jh]


    it = 1

    # answer's path
    ans = [s]

    while it < l:
        # print(f)
        for i in range(0, it):
            new_heuristic(s)
            garbage = hset()
            temp = pick_successor(s)
            s = temp[0]
            # print(s)
            jh = temp[1]
            if s not in ans:
                ans.append(s)
            if jh == 1:
                if s+1 not in ans:
                    ans.append(s+1)
        new_heuristic(s)
        t = hset()
        m = h[0]
        if parent[s] != -1:
            while parent[s] != -1:
                s = parent[s]
                new_heuristic(s)
                z = hset()
        if m == h[s]:
            it = it+1
        else:
            ans = [s]
        if t == 0:
            break

    cost = 0
    if f[s][0] < f[s][1]:
        cost = f[s][0]
    else:
        cost = f[s][1]
    print("Minimum Cost = ")
    print(cost)
    print("Minimum Cost Path is as follows be: ")
    print(ans)



n = int(input("Enter the # of nodes in graph (including Source node(node 0): "))
e = n-1
graph = []
l = int(input("Enter the # of levels in the graph"))

for i in range(0, n):
    x = int(input("Enter the # of edges from node "+ str(i) +": "))
    graph.append([])
    for j in range(0, x):
        s = int(input("Enter the "+ str(j+1) +"th node having edge from node "+ str(i) +": "))
        graph[i].append(s)

    if x != 0:
        ch = int(input("If there is an AND arc at node "+ str(i) +", enter the # of vertices involved in the AND arc(iF there is no AND arc, enter 0): "))
        blank = []
        for k in range(0, ch):
            m = int(input("Enter the vertices involved in the AND arc: "))
            graph[i].remove(m)
            blank.append(m)
        if ch != 0:
            graph[i].append(blank)

heuristic = [-1]
start = 0
for i in range(1, n):
    heuristic.append(int(
        input("Enter the heuristic value for the node " + str(i) + " :")))
ao_star(graph, heuristic, start, n, l)








