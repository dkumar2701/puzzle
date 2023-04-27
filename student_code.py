import copy

#astar search
def astar(board):
    #your code here
    expanded = [] #nodes removed from frontier
    path_frontier = []
    frontier = []
    depth = [] #how deep a node is in the search tree
    heuristic = []

    #put start node in frontier
    frontier.append(board)
    depth.append(0)
    path_frontier.append([])
    heuristic.append(Manhattan_Dist(board))

    step = 0
    #expand
    while len(frontier) != 0:
        step += 1
        #print(step)
        i = 0
        f_i = depth[0] + heuristic[0]
        for idx in range(len(frontier)):
            if idx != 0:
                if (depth[idx]+heuristic[idx]) < f_i:
                    i = idx
                    f_i = depth[idx] + heuristic[idx]
                elif (depth[idx] + heuristic[idx]) == f_i:
                    f_i_tie = compute_tie(frontier[i])
                    curr_tie = compute_tie(frontier[idx])
                    if curr_tie > f_i_tie:
                        i = idx
                        f_i = depth[idx] + heuristic[idx]
        curr_board = frontier[i].copy()
        if heuristic[i] == 0:
            return depth[i], step, path_frontier[i]
        actions = [0, 1, 2, 3]
        children = []
        for action in actions:
            copy_board = curr_board.copy()
            if move(copy_board, action):
                children.append((copy_board, action))
        for child, action in children:
            if child not in expanded:
                frontier.append(child)
                depth.append(depth[i]+1)
                heuristic.append(Manhattan_Dist(child))
                curr_path = path_frontier[i].copy()
                curr_path.append(action)
                path_frontier.append(curr_path)

        #remove parent from frontier data
        
        path_frontier.pop(i)
        frontier.pop(i)
        heuristic.pop(i)
        depth.pop(i)

        expanded.append(curr_board)
        while curr_board in frontier:
            m = frontier.index(curr_board)
            path_frontier.pop(m)
            frontier.pop(m)
            heuristic.pop(m)
            depth.pop(m)


        





    #return depth,expansions,path

def Manhattan_Dist(board):
    dist = 0
    Array2d = board.copy()
    for i in range(len(board)):
        if board[i] != 0:
            curr2d = ((i)//3, (i)%3)
            correct2d = ((board[i]-1)//3, (board[i]-1)%3)
            thisDist = abs(correct2d[0]-curr2d[0])+abs(correct2d[1]-curr2d[1])
            dist = dist+thisDist
    return dist
            
def compute_tie(board):
    return(int(''.join(str(x) for x in board)))

def move(board, action):
    for i in range(len(board)):
        if board[i] == 0:
            pos0 = i
    location0 = ((pos0)//3, (pos0)%3)
    if action == 0: #up
        if location0[0] == 0:
            return 0
        else:
            newNumber = board[pos0-3]
            board[pos0-3] = 0
            board[pos0] = newNumber
            return 1
    if action == 1: #right
        if location0[1] == 2:
            return 0
        else:
            newNumber = board[pos0+1]
            board[pos0+1] = 0
            board[pos0] = newNumber
            return 1
    if action == 2: #down
        if location0[0] == 2:
            return 0
        else:
            newNumber = board[pos0+3]
            board[pos0+3] = 0
            board[pos0] = newNumber
            return 1
    if action == 3: #left
        if location0[1] == 0:
            return 0
        else:
            newNumber = board[pos0-1]
            board[pos0-1] = 0
            board[pos0] = newNumber
            return 1



#graphic print of board, feel free to use, or not
def print_board(board):
    print("\n")
    print("------------")
    print(
        "{:02d}".format(board[0]),
        "|",
        "{:02d}".format(board[1]),
        "|",
        "{:02d}".format(board[2]),
    )
    print("------------")

    print(
        "{:02d}".format(board[3]),
        "|",
        "{:02d}".format(board[4]),
        "|",
        "{:02d}".format(board[5]),
    )
    print("------------")

    print(
        "{:02d}".format(board[6]),
        "|",
        "{:02d}".format(board[7]),
        "|",
        "{:02d}".format(board[8]),
    )
    print("------------")



