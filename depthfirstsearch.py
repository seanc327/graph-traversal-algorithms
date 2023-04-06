def depthFirst(g, start_node):
    visited = []  # tracks visited nodes
    stack = [start_node]

    # remove last node from stack
    while stack:
        v = stack.pop()
        # add node to visited list, add unvisited to stack
        if v not in visited:
            visited.append(v)
            stack.extend(g[v] - set(visited))
    # for print just write out function w/ params
    return print(visited)

        # for neighbor in g[start_node]:
        #     depthFirst(g, neighbor)
# label = [str(c) for c in visited]

if __name__ == "__main__":
    # test
    g = {
        '1': set(['2', '3']),
        '2': set(['1', '3']),
        '3': set(['1', '2'])
    }

    start_node = '1'
    # result
    depthFirst(g, start_node)