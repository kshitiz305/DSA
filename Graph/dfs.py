graphedge = [(0, 1),
             (0, 2),
             (1, 3),
             (1, 4),
             (2, 4)]

graphedge = [
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 0),
    (2, 3),
    (3, 3)]

#        0 - 1 - 3
#        |   |
#        2 - 4

# create a mapping list
node_connecting = dict()

for i, j in graphedge:
    node_connecting.setdefault(i, []) \
        .append(j)
    node_connecting.setdefault(j, []).append(i)

visited = len(node_connecting) * [0]
visited[0] = 1

ulist = []
stack = [0]

while stack.__len__() > 0:
    node = stack.pop()
    ulist.append(node)

    for i in node_connecting[node]:
        if visited[i] == 0:
            visited[i] = 1
            stack.append(i)

print(ulist)
