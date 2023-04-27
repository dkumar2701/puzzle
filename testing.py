import student_code as sc

test = [3,5,2,4,1,0,7,8,6]

sc.print_board(test)
result = sc.Manhattan_Dist(test)
tieResult = sc.compute_tie(test)
print(result)
print(tieResult)
print(tieResult+4)

print(sc.move(test, 1))
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


