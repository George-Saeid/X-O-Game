import random,fontstyle,sys
first = True
second = True
nexMove = True
beggin = True
comp = ''
wins = 0
loses = 0
tie = 0
print('\n\t\t\t' + fontstyle.apply('X','green/bold') + fontstyle.apply(' O','red/bold') + fontstyle.apply(' NEW GAME','blue/bold') + '\t\t\t\n')
board = {
'topLeft': '#',
'topMiddle': '#',
'topRight' : '#',

'midLeft': '#',
'midMiddle': '#',
'midRight' : '#',

'lowLeft': '#',
'lowMiddle': '#',
'lowRight' : '#',
}

corners = ['topLeft','topRight','lowLeft','lowRight']

edges = ['topMiddle','midLeft','midRight','lowMiddle']

symbols = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']

def boardDisplay():
    #print('\nboardDdisplay\n')
    global board
    print('    1  2  3')
    
    print('A | '+board['topLeft'] + '  ' + board['topMiddle'] + '  ' + board['topRight'])
    print('B | '+board['midLeft'] + '  ' + board['midMiddle'] + '  ' + board['midRight'])
    print('C | '+board['lowLeft'] + '  ' + board['lowMiddle'] + '  ' + board['lowRight'])

def choice(pos):
    global board, first, nexMove
    if board[pos] == '#':
            board[pos] = 'X'
            first = True
            nexMove = False

    else:
        print('invalid move, please Try again')
        first = True
        nexMove = True
        
def ResultDisplay(W):
    print('\nResultDisplay\n')
    global board
    colour = ''
    if W == 'X':
        colour = 'green'
    elif W == 'O':
        colour = 'red'
    
    if (board['topLeft'] == board['topMiddle'] == board['topRight'] == W) :
        print('    1  2  3')
        
        print('A | '+fontstyle.apply(board['topLeft'],colour) + '  ' + fontstyle.apply(board['topMiddle'],colour) + '  ' + fontstyle.apply(board['topRight'],colour))
        print('B | '+board['midLeft'] + '  ' + board['midMiddle'] + '  ' + board['midRight'])
        print('C | '+board['lowLeft'] + '  ' + board['lowMiddle'] + '  ' + board['lowRight'])

    elif (board['midLeft'] == board['midMiddle'] == board['midRight'] == W):
        print('    1  2  3')
    
        print('A | '+board['topLeft'] + '  ' + board['topMiddle'] + '  ' + board['topRight'])
        print('B | '+fontstyle.apply(board['midLeft'],colour) + '  ' + fontstyle.apply(board['midMiddle'],colour)+ '  ' + fontstyle.apply(board['midRight'],colour))
        print('C | '+board['lowLeft'] + '  ' + board['lowMiddle'] + '  ' + board['lowRight'])
        
    elif (board['lowLeft'] == board['lowMiddle'] == board['lowRight'] == W):
        print('    1  2  3')

        print('A | '+board['topLeft'] + '  ' + board['topMiddle'] + '  ' + board['topRight'])
        print('B | '+board['midLeft'] + '  ' + board['midMiddle'] + '  ' + board['midRight'])
        print('C | '+fontstyle.apply(board['lowLeft'],colour) + '  ' + fontstyle.apply(board['lowMiddle'],colour) + '  ' + fontstyle.apply(board['lowRight'],colour))

    elif (board['topLeft'] == board['midMiddle'] == board['lowRight'] == W): 
        print('    1  2  3')
    
        print('A | '+fontstyle.apply(board['topLeft'],colour) + '  ' + board['topMiddle'] + '  ' + board['topRight'])
        print('B | '+board['midLeft'] + '  ' + fontstyle.apply(board['midMiddle'],colour) + '  ' + board['midRight'])
        print('C | '+board['lowLeft'] + '  ' + board['lowMiddle'] + '  ' + fontstyle.apply(board['lowRight'],colour))

    elif (board['topRight'] == board['midMiddle'] == board['lowLeft'] == W): 
        print('    1  2  3')
    
        print('A | '+board['topLeft'] + '  ' + board['topMiddle'] + '  ' + fontstyle.apply(board['topRight'],colour))
        print('B | '+board['midLeft'] + '  ' + fontstyle.apply(board['midMiddle'],colour) + '  ' + board['midRight'])
        print('C | '+fontstyle.apply(board['lowLeft'],colour) + '  ' + board['lowMiddle'] + '  ' + board['lowRight'])

    elif (board['topRight'] == board['midRight'] == board['lowRight'] == W):
        print('    1  2  3')
    
        print('A | '+board['topLeft'] + '  ' + board['topMiddle'] + '  ' + fontstyle.apply(board['topRight'],colour))
        print('B | '+board['midLeft'] + '  ' + board['midMiddle'] + '  ' + fontstyle.apply(board['midRight'],colour))
        print('C | '+board['lowLeft'] + '  ' + board['lowMiddle'] + '  ' + fontstyle.apply(board['lowRight'],colour))

    elif(board['topMiddle'] == board['midMiddle'] == board['lowMiddle'] == W):
        print('    1  2  3')
    
        print('A | '+board['topLeft'] + '  ' + fontstyle.apply(board['topMiddle'],colour) + '  ' + board['topRight'])
        print('B | '+board['midLeft'] + '  ' + fontstyle.apply(board['midMiddle'],colour) + '  ' + board['midRight'])
        print('C | '+board['lowLeft'] + '  ' + fontstyle.apply(board['lowMiddle'],colour) + '  ' + board['lowRight'])
    
    elif(board['topLeft'] == board['midLeft'] == board['lowLeft'] == W):
        print('    1  2  3')
    
        print('A | '+fontstyle.apply(board['topLeft'],colour) + '  ' + board['topMiddle'] + '  ' + board['topRight'])
        print('B | '+fontstyle.apply(board['midLeft'],colour) + '  ' + board['midMiddle'] + '  ' + board['midRight'])
        print('C | '+fontstyle.apply(board['lowLeft'],colour) + '  ' + board['lowMiddle'] + '  ' + board['lowRight'])
         
def MyMove():
    #print('\nMyMove\n')
    global nexMove,symbols
    while nexMove:
        #print('\nYour Turn \nyou are playing with X vs the Computer with O \nwhere did you want to play ?')
        play = input('\nYour Turn: ')

        if play in symbols:
        
            if play == 'a1':
                choice('topLeft')
            if play == 'a2':
                choice('topMiddle')
            if play == 'a3':
                choice('topRight')
            
            if play == 'b1':
                choice('midLeft')
            if play == 'b2':
                choice('midMiddle')
            if play == 'b3':
                choice('midRight')
            
            if play == 'c1':
                choice('lowLeft')
            if play == 'c2':
                choice('lowMiddle')
            if play == 'c3':
                choice('lowRight')
        else:
            print('\nInvalid input , Please Try again')
            nexMove =True

def again():
    #print('\nagain\n')
    global first,second,board
    while True:
        print('Do you want to play again ?\n1: Yes\n2: No') 
        ans = input()
        if ans == '1':
            first = True
            nexMove = True
            print('\n\t\t\t' + fontstyle.apply('X','green/bold') + fontstyle.apply(' O','red/bold') + fontstyle.apply(' NEW GAME','blue/bold') + '\t\t\t\n')
            print(fontstyle.apply(str(wins),'green') + ' Wins, ' + fontstyle.apply(str(loses),'red') + ' Loses, ' + fontstyle.apply(str(tie),'blue') + ' Ties\n')
            #second = True
            for i in board:
                board[i]= '#'
            break
        elif ans == '2':
            print(fontstyle.apply('\nSCORE:\n','purple/bold'))
            print(fontstyle.apply(str(wins),'green') + ' Wins, ' + fontstyle.apply(str(loses),'red') + ' Loses, ' + fontstyle.apply(str(tie),'blue') + ' Ties\n')
            print('\nThank You\n')
            first = False
            sys.exit()
            
        else:
            print('invalid choice please try again')
            continue
        
def winner():
    #print('\nwinner\n')
    global board,wins,beggin, nexMove
    if (board['topLeft'] == board['topMiddle'] == board['topRight'] == 'X') or \
       (board['midLeft'] == board['midMiddle'] == board['midRight'] == 'X') or \
       (board['lowLeft'] == board['lowMiddle'] == board['lowRight'] == 'X') or \
       (board['topLeft'] == board['midMiddle'] == board['lowRight'] == 'X') or \
       (board['topRight'] == board['midMiddle'] == board['lowLeft'] == 'X') or \
       (board['topRight'] == board['midRight'] == board['lowRight'] == 'X') or \
       (board['topMiddle'] == board['midMiddle'] == board['lowMiddle'] == 'X') or \
       (board['topLeft'] == board['midLeft'] == board['lowLeft'] == 'X') :
       wins +=1
       beggin = True
       nexMove = True
       print(fontstyle.apply('\n\n********* CONGRATULATIONS YOU HAVE WON *********\n\n','green / bold'))
       ResultDisplay('X')
       print()
       again()
       return True
       
def Lose():
    #print('\nLose\n')
    global loses,beggin, nexMove
    if (board['topLeft'] == board['topMiddle'] == board['topRight'] == 'O') or \
       (board['midLeft'] == board['midMiddle'] == board['midRight'] == 'O') or \
       (board['lowLeft'] == board['lowMiddle'] == board['lowRight'] == 'O') or \
       (board['topLeft'] == board['midMiddle'] == board['lowRight'] == 'O') or \
       (board['topRight'] == board['midMiddle'] == board['lowLeft'] == 'O') or \
       (board['topRight'] == board['midRight'] == board['lowRight'] == 'O') or \
       (board['topMiddle'] == board['midMiddle'] == board['lowMiddle'] == 'O') or \
       (board['topLeft'] == board['midLeft'] == board['lowLeft'] == 'O')  :
        loses +=1
        beggin = False
        nexMove = False
        print(fontstyle.apply('\n\n######### Hard Luck you have Lost #########\n\n','red / bold'))
        ResultDisplay('O')
        print()
        again()
        return True

def Tie():
    #print('\nTie\n')
    global board, first,tie, beggin,nexMove
    if '#' not in board.values() and not winner() and not Lose():
        tie += 1
        boardDisplay()
        print(fontstyle.apply('\n+++++++++++ Tie +++++++++++\n','blue/bold'))
        again()
        c = random.getrandbits(1)
        beggin = bool(c)
        nexMove = bool(c)
        return True
    
def defence():
    #print('\ndefence\n')
    global board, first, second, comp,nexMove
    nexMove = True
    #third = True
    #print('\nComputer Turn\n')

    # Horizontaly to right
    if board['topLeft'] == board['topMiddle'] == 'X' and board['topRight'] != 'O':
            board['topRight'] = 'O'
            comp = 'a3'
            
            
    elif board['midLeft'] == board['midMiddle'] == 'X' and board['midRight'] != 'O':
        board['midRight'] = 'O'
        comp = 'b3'
        

    elif board['lowLeft'] == board['lowMiddle'] == 'X' and board['lowRight'] != 'O':
        board['lowRight'] = 'O'
        comp = 'c3'
        
    # Horizontaly to left
    elif board['topRight'] == board['topMiddle'] == 'X' and board['topLeft'] != 'O':
        board['topLeft'] = 'O'
        comp = 'a1'
        
        
    elif board['midRight'] == board['midMiddle'] == 'X' and board['midLeft'] != 'O':
        board['midLeft'] = 'O'
        comp = 'b1'
        

    elif board['lowRight'] == board['lowMiddle'] == 'X' and board['lowLeft'] != 'O':
        board['lowLeft'] = 'O'
        comp = 'c1'
        
    ######################################### 
    
    # Verticaly Down
    elif board['topLeft'] == board['midLeft'] == 'X' and board['lowLeft'] != 'O':
        board['lowLeft'] = 'O'
        comp = 'c1'
        
    
    elif board['topMiddle'] == board['midMiddle'] == 'X' and board['lowMiddle'] != 'O':
        board['lowMiddle'] = 'O'
        comp = 'c2'
        
    
    elif board['topRight'] == board['midRight'] == 'X' and board['lowRight'] != 'O':
        board['lowRight'] = 'O'
        comp = 'c3'
        
    # Verticaly Up
    elif board['lowLeft'] == board['midLeft'] == 'X' and board['topRight'] != 'O':
        board['topRight'] = 'O'
        comp = 'a3'
        
    
    elif board['lowMiddle'] == board['midMiddle'] == 'X' and board['topMiddle'] != 'O':
        board['topMiddle'] = 'O'
        comp = 'a2'
        
    
    elif board['lowRight'] == board['midRight'] == 'X' and board['topRight'] != 'O':
        board['topRight'] = 'O'
        comp = 'a3'
        
    ##########################################
    
    # Diagonally UP-Down
    elif board['topLeft'] == board['midMiddle'] == 'X' and board['lowRight'] != 'O':
        board['lowRight'] = 'O'
        comp = 'c3'
        
    elif board['topRight'] == board['midMiddle'] == 'X' and board['lowLeft'] != 'O':
        board['lowLeft'] = 'O'
        comp = 'c1'
        
    # Diagonally Down-Up
    elif board['lowRight'] == board['midMiddle'] == 'X' and board['topLeft'] != 'O':
        board['topLeft'] = 'O'
        comp = 'a1'
        
    
    elif board['lowLeft'] == board['midMiddle'] == 'X' and board['topRight'] != 'O':
        board['topRight'] = 'O'
        comp = 'a3'    
    ###########################################
    
    ###########################################
    
    # Horizontally Middle
    elif board['topLeft'] == board['topRight'] == 'X' and board['topMiddle'] != 'O':
        board['topMiddle'] = 'O' 
        comp = 'a2'
        

    elif board['midLeft'] == board['midRight'] == 'X' and board['midMiddle'] != 'O':
        board['midMiddle'] = 'O' 
        comp = 'b2'
        

    elif board['lowLeft'] == board['lowRight'] == 'X' and board['lowMiddle'] != 'O':
        board['lowMiddle'] = 'O'
        comp = 'c2'
         
    # Vertically Middle
    elif board['topLeft'] == board['lowLeft'] == 'X' and board['midLeft'] != 'O':
        board['midLeft'] = 'O' 
        comp = 'b1'
        

    elif board['topMiddle'] == board['lowMiddle'] == 'X' and board['midMiddle'] != 'O':
        board['midMiddle'] = 'O'
        comp = 'b2' 
        

    elif board['topRight'] == board['lowRight'] == 'X' and board['midRight'] != 'O':
        board['midRight'] = 'O'
        comp = 'b3'

    # Diagonally Middle
    elif board['topLeft'] == board['lowRight'] == 'X' and board['midMiddle'] != 'O':
        board['midMiddle'] = 'O'
        comp = 'b2'
        
    elif board['topRight'] == board['lowLeft'] == 'X' and board['midMiddle'] != 'O':
        board['midMiddle'] = 'O'
        comp = 'b2'
        
        
    #############################################
    #############################################
    
    else:
        #attackTactics()
        DefTactics()
    
    print('\nComputer Turn: ' + comp + '\n')

def Attack():
    #print('\nAttack\n')
    global board, first, second, comp
    # Horizontaly to right
    if board['topLeft'] == board['topMiddle'] == 'O' and board['topRight'] == '#':
            board['topRight'] = 'O'
            comp = 'a3'
            
            
    elif board['midLeft'] == board['midMiddle'] == 'O' and board['midRight'] == '#':
        board['midRight'] = 'O'
        comp = 'b3'
        

    elif board['lowLeft'] == board['lowMiddle'] == 'O' and board['lowRight'] == '#':
        board['lowRight'] = 'O'
        comp = 'c3'
        
    # Horizontaly to left
    elif board['topRight'] == board['topMiddle'] == 'O' and board['topLeft'] == '#':
        board['topLeft'] = 'O'
        comp = 'a1'
        
        
    elif board['midRight'] == board['midMiddle'] == 'O' and board['midLeft'] == '#':
        board['midLeft'] = 'O'
        comp = 'b1'
        

    elif board['lowRight'] == board['lowMiddle'] == 'O' and board['lowLeft'] == '#':
        board['lowLeft'] = 'O'
        comp = 'c1'
        
    ######################################### 
    
    # Verticaly Down
    elif board['topLeft'] == board['midLeft'] == 'O' and board['lowLeft'] == '#':
        board['lowLeft'] = 'O'
        comp = 'c1'
        
    
    elif board['topMiddle'] == board['midMiddle'] == 'O' and board['lowMiddle'] == '#':
        board['lowMiddle'] = 'O'
        comp = 'c2'
        
    
    elif board['topRight'] == board['midRight'] == 'O' and board['lowRight'] == '#':
        board['lowRight'] = 'O'
        comp = 'c3'
        
    # Verticaly Up
    elif board['lowLeft'] == board['midLeft'] == 'O' and board['topRight'] == '#':
        board['topRight'] = 'O'
        comp = 'a3'
        
    
    elif board['lowMiddle'] == board['midMiddle'] == 'O' and board['topMiddle'] == '#':
        board['topMiddle'] = 'O'
        comp = 'a2'
        
    
    elif board['lowRight'] == board['midRight'] == 'O' and board['topRight'] == '#':
        board['topRight'] = 'O'
        comp = 'a3'
        
    ##########################################
    
    # Diagonally UP-Down
    elif board['topLeft'] == board['midMiddle'] == 'O' and board['lowRight'] == '#':
        board['lowRight'] = 'O'
        comp = 'c3'
        
    elif board['topRight'] == board['midMiddle'] == 'O' and board['lowLeft'] == '#':
        board['lowLeft'] = 'O'
        comp = 'c1'
        
    # Diagonally Down-Up
    elif board['lowRight'] == board['midMiddle'] == 'O' and board['topLeft'] == '#':
        board['topLeft'] = 'O'
        comp = 'a1'
        
    
    elif board['lowLeft'] == board['midMiddle'] == 'O' and board['topRight'] == '#':
        board['topRight'] = 'O'
        comp = 'a3'    
    ###########################################
    
    ###########################################
    
    # Horizontally Middle
    elif board['topLeft'] == board['topRight'] == 'O' and board['topMiddle'] == '#':
        board['topMiddle'] = 'O' 
        comp = 'a2'
        

    elif board['midLeft'] == board['midRight'] == 'O' and board['midMiddle'] == '#':
        board['midMiddle'] = 'O' 
        comp = 'b2'
        

    elif board['lowLeft'] == board['lowRight'] == 'O' and board['lowMiddle'] == '#':
        board['lowMiddle'] = 'O'
        comp = 'c2'
         
    # Vertically Middle
    elif board['topLeft'] == board['lowLeft'] == 'O' and board['midLeft'] == '#':
        board['midLeft'] = 'O' 
        comp = 'b1'
        

    elif board['topMiddle'] == board['lowMiddle'] == 'O' and board['midMiddle'] == '#':
        board['midMiddle'] = 'O'
        comp = 'b2' 
        

    elif board['topRight'] == board['lowRight'] == 'O' and board['midRight'] == '#':
        board['midRight'] = 'O'
        comp = 'b3' 
    
    # Diagonally Middle
    elif board['topLeft'] == board['lowRight'] == 'O' and board['midMiddle'] == '#':
        board['midMiddle'] = 'O'
        comp = 'b2'
        
    elif board['topRight'] == board['lowLeft'] == 'O' and board['midMiddle'] == '#':
        board['midMiddle'] = 'O'
        comp = 'b2'
    
    else: 
        defence()

def attackTactics():
    #print('\nattackTac\n')
    global board, comp, first,corners
    third = True
    fourth = True

    if board['topLeft'] == 'O' and board['midMiddle'] == 'X' and board['lowRight'] == '#':
        board['lowRight'] = 'O'
        comp = 'c3'
            
    elif board['topRight'] == 'O' and board['midMiddle'] == 'X' and board['lowLeft'] == '#':
        board['lowLeft'] = 'O'
        comp = 'c1'
        
    
    elif board['lowLeft'] == 'O' and board['midMiddle'] == 'X' and board['topRight'] == '#':
        board['topRight'] = 'O'
        comp = 'a3'
        
    
    elif board['lowRight'] == 'O' and board['midMiddle'] == 'X' and board['topLeft'] == '#':
        board['topLeft'] = 'O'
        comp = 'a1'
    
    
    
    else:
        while fourth:    
            #print('\nrandom loop\n')
            comp = random.choice(corners)
            if board[comp] == '#' :
                board[comp] = 'O'
                fourth = False
            
            elif board[comp] != '#':
                fourth = True
            

            elif board['topLeft'] != '#' and board['topRight'] != '#' and \
            board['lowLeft'] != '#' and board['lowRight'] != '#':
                
                while third:
                    comp = random.choice(list(board))
                    if board[comp] == '#' :
                        board[comp] = 'O'
                        first = True
                        third = False
                    else:
                        #second = True
                        third = True
                fourth = False
                
            else:
                attackTac2()
        
def attackTac2():
    global board, corners, edges, comp
    for v in corners:
        if board[v] == 'O' and board['midMiddle'] == '#':
            board['midMiddle'] = 'O'
            comp = 'b2'
            break
        elif board[v] == 'O' :
            for n in corners:
                if board[n] == 'X':
                    while True:
                        comp = random.choice(corners)
                        if board[comp] == '#':
                            board[comp] = 'O'
                            break
                        else:
                            continue


                    break
            break
        

def DefTactics():
    #print('\ndefTactics\n')
    global  board, comp
    #Top-Left Edge
    #print('\nDefTactics\n')
    if 'O' not in board.values():
        if (board['topLeft'] == 'X' or  board['topRight'] == 'X' or board['lowLeft'] == 'X' or board['lowRight'] == 'X') \
            and board['midMiddle'] == '#':
            
            board['midMiddle'] = 'O'
            comp = 'b2'
        else:
            attackTactics()
    elif (board['topLeft'] == board['lowRight'] == 'X' and board['midMiddle'] == 'O') or \
         (board['topRight'] == board['lowLeft'] == 'X' and board['midMiddle'] == 'O'):
        while True:
            comp = random.choice(edges)
            if board[comp] == '#':
                board[comp] = 'O'
                break
            else:
                continue
    else:
        attackTactics()

while first:
    #print('\nprogram beggin\n')

    while beggin:
        #print('\nwinner loop\n')
        boardDisplay()

        MyMove()
        
        if Tie():
            break

        
        elif winner():
            break
        

        elif Lose():
            break

        Attack()
        
        if Tie():
            break

        
        elif winner():
            break
        

        elif Lose():
            break

    while not beggin :
        #print('\nloser loop\n')
        

        Attack()

        
        
        if Tie():
            break

        
        elif winner():
            break
        

        elif Lose():
            break

        boardDisplay()

        MyMove()
        
        if Tie():
            break

        
        elif winner():
            break
        

        elif Lose():
            break
