def containsNearbyDuplicate( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    for i in range(0, len(nums), 1):
        if nums[i] in nums[i+1:i+k+1] and (i + k) < len(nums) and i+1 < len(nums):
            return True
    return False


nums = [1,2,3,1,2,3]

#input('X' || 'O') -> choose Pos[i][j] -> turn2nd input




# def display_board(board):
#     play_board = [['', ' ', ''], [' ', ' ', ' '], [' ', ' ', ' ']]
#     k = 0
#     for i in range(0,len(play_board),1):
#         for j in range(0,3,1):
#             play_board[i][j] = board[k]
#             k+=1
#     print(play_board)
#     pass



def m_input():
    mark = ''
    while mark != 'X' and mark != 'O':
        print("Please input X or O")
        mark = input()
    return mark

def r_input():
    row_p = 3
    while(row_p > 2):
        print("Please input row position")
        row_p = int(input())
    return row_p

def c_input():
    col_p = 3
    while(col_p > 2):
        print("Please input column position")
        col_p = int(input())
    return col_p


def displayboard(mark, row_p, col_p, board):
    #board = [['', ' ', ''], [' ', '', ' '], [' ', '', '']]
    board[row_p][col_p] = mark
    print(board[0])
    print(board[1])
    print(board[2])

    return board

def check_turn(oldchar, newchar):
    if oldchar == newchar:
        return False
    return True

def check_logic(board, check_mark):
    mc_top = 0
    mc_diagonal = 0
    mc_bot = 0
    for i in range(0,len(board),1): #2. Bot direction
        for j in range(0,3,1): #1. Top direction
            if board[i][j] == check_mark:
                mc_top += 1
            if mc_top == 3: return True
        mc_top = 0
        if board[i][0] == check_mark: mc_bot += 1
        if mc_bot == 3: return True

        if board[i][i] == check_mark: mc_diagonal += 1 #3. Diagonal Direction
        if mc_diagonal == 3: return True






test = [['X','O','X'],
        ['X','-','O'],
        ['X','O','O']]


print("Welcome to Tic Toc Toe")
default_board = [['', ' ', ''], [' ', ' ', ' '], [' ', ' ', ' ']]
Uboard = displayboard('-',0,0,default_board)
mark2 = ''
while (True):
    #First Turn
    print("1st Player Turn")
    mark = m_input()
    while check_turn(mark, mark2) == False:
        print("Please input right MARK")
        mark = m_input()
    row = r_input()
    col = c_input()
    Uboard = displayboard(mark,row,col,Uboard)
    if (check_logic(Uboard, mark)):
        print("Player 1 win ")
        break

    #Second Turn
    print("2nd Player Turn")
    mark2 = m_input()
    while check_turn(mark, mark2) == False:
        print("Please input right MARK")
        mark2 = m_input()
    row2 = r_input()
    col2 = c_input()
    Uboard = displayboard(mark2, row2, col2, Uboard)
    if(check_logic(Uboard,mark2)):
        print("Player 2 win ")
        break







