import copy

'''template'''
# sudoku_list = [[0,8,5,0,0,0,2,1,0],
#                [0,9,4,0,1,2,0,0,3],
#                [0,0,0,3,0,0,7,0,4],
#                [5,0,3,4,0,9,0,0,0],
#                [0,4,0,2,0,6,0,3,0],
#                [0,0,0,1,0,3,9,0,7],
#                [6,0,8,0,0,5,0,0,0],
#                [1,0,0,8,4,0,3,6,0],
#                [0,2,7,0,0,0,8,9,0]]

sudoku_list = []
for n in range(9):
    sudoku_list.append(list(map(int, input(f'Enter {n+1}th line(use SPACE to separate numbers, use 0 to represent BLANK):').split())))

def is_valid_sudoku(data):
    '''Validate the sukodu'''

    for y in range(9):
        for x in range(9):

            '''Every number should be between 0 and 9'''
            if data[y][x] > 9 or data[y][x] < 0: 
                return False
            '''If not BLANK, then check if the number is repeated in the row'''
            if data[y][x] != 0 and data[y].count(data[y][x]) > 1:
                return False
            '''If not BLANK, then check if the number is repeated in the column'''
            for col in range(9):
                if data[y][x] != 0 and col != y:
                    if data[col][x] == data[y][x]:
                        return False
            '''In every 3 by 3, check if the number is repeated'''
            for i in range(3):
                for j in range(3):
                    if data[y][x] != 0 and (i+3*(y//3), j+3*(x//3)) != (y, x):
                        if data[i+3*(y//3)][j+3*(x//3)] == data[y][x]:
                            return False
    return True


def init_candidate_list(data):
    '''Initialize a candidate list. Every BLANK will be filled with 1-9 as candidates and its coordinate'''
    data_list = []
    for y in range(9):
        for x in range(9):
            if data[y][x] == 0:
                data_list.append([(x, y), [1, 2, 3, 4, 5, 6, 7, 8, 9]])
    return data_list


def init_candidate_list(data):
    '''Initialize a candidate list. Every BLANK will be filled with 1-9 as candidates and its coordinate'''
    data_list = []
    for y in range(9):
        for x in range(9):
            if data[y][x] == 0:
                data_list.append([(x, y), [1, 2, 3, 4, 5, 6, 7, 8, 9]])
    return data_list

def filter_candidate_list(data, data_list, start):
    '''filter the candidate list'''
    for blank_index in range(start, len(data_list)):
        data_list[blank_index][1] = []
        for num in range(1,10):
            if is_valid_num(data, data_list[blank_index][0][0], data_list[blank_index][0][1], num):
                data_list[blank_index][1].append(num)
    return data_list

def is_valid_num(data, x, y, num):
    '''validate the number'''
    if data[y].count(num) > 0:   # row
        return False
                                                                                       
    for col in range(9):   # column
        if data[col][x] == num:
            return False

    for a in range(3):   # 3 by 3
        for b in range(3):
            if data[a+3*(y//3)][b+3*(x//3)] == num:
                return False
    return True

def fill_blank(data, data_list, start):
    '''
    main function, use recursion method to fill in the blank with the number in the finalized candidate list 
    If a BLANK returns True (validated by the function is_valid_num), then move on to the next blank, or return to the last step
    
    data: sudoku matrix, 2dimensional list
    data_list: candidate list, 2dimensional list
    start: where the recursion is processing
    '''
    all_data = []
    if start < len(data_list):
        one = data_list[start]
        for num in one[1]:
            if is_valid_num(data, one[0][0], one[0][1], num):
                data[one[0][1]][one[0][0]] = num   
                tem_data = fill_blank(data, data_list, start+1)   # start+1
                if tem_data:   
                    return tem_data
        data[one[0][1]][one[0][0]] = 0   
    else:
        return data

def print_sudoku(data):
    print('>>> SOLUTION:')
    for i in range(9):
        for j in range(9):
            print('{:^3}'.format(data[i][j]), end='')
        print('')
    print('')


def solve_it(sudoku=sudoku_list): # main function
    init_sudoku = copy.deepcopy(sudoku) 
    candidate_list = filter_candidate_list(init_sudoku, init_candidate_list(init_sudoku), start=0)   
    cracked_sudoku = fill_blank(init_sudoku, candidate_list, start=0) 
    print_sudoku(cracked_sudoku)  
    return cracked_sudoku
  

if __name__ == '__main__':
    solve_it()

