graphedge = [(0, 1),
(0, 2),
(1, 3),
(1, 4),
(2, 4)]


# create a mapping list
node_connecting = dict()


for i,j in graphedge:
    node_connecting.setdefault(i,[])\
        .append(j)
    node_connecting.setdefault(j,[]).append(i)

# using setdefault will first get the item and if not available the it will set the default if nothing is returned.

visited = len(node_connecting)*[0]

visited[0]=1

queue = [0]
ulist = []
# to get the starting node

while len(queue)> 0:
    element = queue.pop(0)
    ulist.append(element)

    for i in node_connecting[element]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = 1


print(ulist)



