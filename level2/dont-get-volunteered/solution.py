def solution(src, dest):
    """
    We have an 8x8 grid, where each cell is a node.
    Nodes are connected with moves. Connected nodes
    form an undirected and unweighted graph.

    We have a Shortest Path Problem in our hands.

    (0,0) ---------- (7,0)
      |                |
      |                |
      |                |
      |                |
      |                |
      |                |
    (0,7) ---------- (7,7)
    """
    if not (0 <= src < 64 and 0 <= dest < 64):
        return None
    if src == dest:
        return 0

    rows, cols = 8, 8
    moves = [(1, 2), (-1, 2), (1, -2), (-1, -2),
             (2, 1), (-2, 1), (2, -1), (-2, -1)]

    conv = lambda num: (num % cols, num // cols)
    add = lambda node, move: (node[0] + move[0], node[1] + move[1])
    is_inside = lambda node: 0 <= node[0] < cols and 0 <= node[1] < rows
    neighbors = lambda node: [add(node, m) for m in moves if is_inside(add(node, m))]
        
    start, end = conv(src), conv(dest)

    # Finding the shortest path with BFS
    visited = set()
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node in visited:
            continue

        for neighbor in neighbors(node):
            path_ = path + [neighbor]
            queue.append(path_)

            if neighbor == end:
                return len(path_) - 1

        visited.add(node)

    return None