import student_code as sc

test = [0,5,2,4,1,3,7,8,6]

print("Original\n")
sc.print_board(test)

actions = [0, 1, 2, 3]
children = []
for action in actions:
    copy_board = test.copy()
    if sc.move(copy_board, action):
        children.append(copy_board)
print(children)
for child in children:
    sc.print_board(child)


