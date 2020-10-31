class Sudoku:
    def __init__(self, sudoku = None):
        self.__puzzle__ = []
        self.__originalPuzzle__ = []
        self.__input__ = [' ','1','2','3','4','5','6','7','8','9']    # 0 index is used for the representing empty value in sudoku
        self.__validInput__ = []
        self.__index__ = [0,1,2,3,4,5,6,7,8]
        self.__terminal__ = True
        if sudoku == None or len(sudoku) != 9 or len(sudoku[0]) != 9:
            self.initPuzzle()
        else:
            self.__puzzle__ = sudoku.copy()

        if not self.isCorrect():
            if self.__terminal__:
                print('Board is incorrectly setup')

    def puzzle(self):
        '''Return a copy of puzzle'''
        return self.__puzzle__.copy()

    def originalPuzzle(self):
        return self.__originalPuzzle__.copy()

    def getDefaultElement(self):
        return self.__input__[0]

    def setDefaultElement(self, value=''):
        self.__input__[0] = value

    def get(self,i,j):
        '''Return a value of puzzle at (i,j) index'''
        return self.__puzzle__[i][j]

    def getOriginal(self,i,j):
        '''Return value of original puzzle at (i,j) index'''
        return self.__originalPuzzle__[i][j]

    def set(self, i, j, value=None):
        '''
        Set index (i,j) to value without checking the validity of value
        '''
        if value == None:
            value = self.__input__[0]
        self.__puzzle__[i][j] = value
        self.__originalPuzzle__[i][j] = value

    def getTermainal(self):
        return self.__terminal__

    def setTerminal(self, value=True):
        self.__terminal__ = value

    def toggleTerminal(self):
        self.__terminal__ = not self.__terminal__

    def getUnitIndex(self, i,j):
        '''
        Whole Sudoku Board divided into 9 3x3 martix know as units and these units are given index like
        0 1 2
        3 4 5
        6 7 8
        '''
        return (i//3)*3 + j//3

    def getUnit(self, i, j):
        '''
        Return all index of the unit in which (i,j) belong to
        '''
        r = (i//3)*3
        c = (j//3)*3
        unit = []
        for a in range(0,3):
            for b in range(0,3):
                unit.append([r+a, c+b])
        return unit

    def getRow(self,i,j = 0):
        '''
        Return all index of the row in which (i,j) belong
        '''
        return [[i,a] for a in self.__index__.copy()]

    def getCol(self, i,j):
        '''
        Return all index of the column in which (i,j) belong
        '''
        return [[a, j] for a in self.__index__.copy()]

    def getCol(self, j):
        '''
        Return all index of the column in which (i,j) belong
        '''
        return [[a, j] for a in self.__index__.copy()]

    def getRowElements(self, i, j, includeThis=False):
        '''
        Return all value of the row in which (i,j) belong and whether to include (i,j) element depends on includeThis value
        '''
        indexes = self.getRow(i) # [[0,1],[0,2], ...]
        elements = []
        for index in indexes:
            if not includeThis and index == [i,j]:
                continue
            elements.append(self.get(index[0], index[1]))
        return elements

    def getColElements(self, i, j, includeThis=False):
        '''
        Return all value of the column in which (i,j) belong and whether to include (i,j) element depends on includeThis value
        '''
        indexes = self.getCol(j) # [[0,1],[0,2], ...]
        elements = []
        for index in indexes:
            if not includeThis and index == [i,j]:
                continue
            elements.append(self.get(index[0], index[1]))
        return elements

    # def getColElements(self, j):
    #     indexes = self.getCol(j) # [[0,1],[0,2], ...]
    #     elements = []
    #     for index in indexes:
    #         elements.append(self.get(index[0], index[1]))
    #     return elements

    def getUnitElements(self, i, j, includeThis=False):
        '''
        Return all value of the unit in which (i,j) belong and whether to include (i,j) element depends on includeThis value
        '''
        indexes = self.getUnit(i, j) # [[0,1],[0,2], ...]
        elements = []
        for index in indexes:
            if not includeThis and index == [i,j]:
                continue
            elements.append(self.get(index[0], index[1]))
        return elements

    def getUnfilledElement(self):
        '''
        Return the list of all index which are empty i.e. assign with default value along with a zero value
        which tell us about what is the current value is assign to that index it is the index of list self.__input__
        '''
        stack = []
        for i in range(0,9):
            for j in range(0,9):
                if self.get(i,j) == self.__input__[0]:
                    stack.append([i,j,0])
        return stack

    def fill(self, i, j, value, forceSet=False):
        '''
        It will first check the validity of value in given location
        If valid then it set value and return True
        Else return False and seting the value depends on forceSet
        '''
        if self.isValidElement(i,j,value):
            self.__puzzle__[i][j] = value
            return True
        elif forceSet:
            self.__puzzle__[i][j] = value
        return False

    def initPuzzle(self, CONST_RANDOM=False):
        '''
        Delete Previous Puzzle (as it me wrongly formated) and then initialize to default
        and if CONST_RANDOM is True then it assign random value to random index of random number between 10 to 30
        '''
        # for row in self.__puzzle__:
        #     row.clear()
        self.__puzzle__.clear()

        for i in range(0,9):
            temp = []
            for j in range(0,9):
                temp.append(self.__input__[0])
            self.__puzzle__.append(temp)

        if not CONST_RANDOM:
            self.setOriginalPuzzle()
            return

        from random import randint
        elem_to_init = randint(10,30)
        i = 0
        while i <= elem_to_init:
            pointer = randint(0,80)
            index = [pointer//9, pointer%9]
            if self.get(index[0],index[1]) == self.__input__[0] and self.fill(index[0], index[1], str(randint(1,9))):
                # print(index[0],index[1],i)
                i+=1
            # else:
            #     print(index[0],index[1])
        self.setOriginalPuzzle()
        del randint

    def readPuzzle(self):
        '''
        Delete Previous Puzzle (because it might be in wrong format) and then read in the specific Format
        '''
        if not self.__terminal__:
            return

        self.initPuzzle()

        print('Enter Sudoku in following Format :\n\tColumn\t->\tLeave Space\n\tRow\t->\tNew Line\n')
        for i in range(0,9):
            line = input().split()
            for j in range(0,9):
                self.__puzzle__[i][j] = line[j]
        self.setOriginalPuzzle()

    def setOriginalPuzzle(self):
        self.__originalPuzzle__.clear()

        for row in self.__puzzle__:
            self.__originalPuzzle__.append(row.copy())

    def reset(self):
        self.__puzzle__.clear()

        for row in self.__originalPuzzle__:
            self.__puzzle__.append(row.copy())

    def log(self, message):
        '''
        Display message in a specific format
        '''
        if not self.__terminal__:
            return
        print('+',end='')
        for i in range(0,len(message)+2):
            print('-',end='')
        print('+')
        print('| ',end='')
        print(message,end='')
        print(' |')
        print('+',end='')
        for i in range(0,len(message)+2):
            print('-',end='')
        print('+')

    def show(self, original=False):
        '''Function to display our Sudoku on the Terminal'''
        if not self.__terminal__:
            return

        if original:
            puzzle = self.__originalPuzzle__
        else:
            puzzle = self.__puzzle__

        for i in range(0,9):
            for j in range(0,9):
                print(puzzle[i][j], end=" ")
                if not (j+1)%3 and j != 8:
                    print(end="| ")
            if not (i+1)%3 and i != 8:
                print()
                for j in range(0,11):
                    if j == 10:
                        print("-", end="")
                    elif (j+1)%4:
                        print("--", end="")
                    else:
                        print("+-", end= "")
            print()

    def isValid(self, update=False, showError=False):
        '''
        It return whether the board is correctly filled or not
        If update is true -> reset incorrect value to 0 Else leave it
        '''
        valid = True
        for i in range(0,9):
            for j in range(0,9):
                if self.get(i,j) not in self.__input__:
                    if showError:
                        print(i,j,self.get(i,j))
                    if update:
                        self.set(i,j,self.__input__[0])
                    else:
                        valid = False
        return valid

    def isCorrect(self, checkBoard=False, showError=False):
        '''
        Check whether a given sudoku is correct or not
        '''
        if checkBoard and not self.isValid(): # check board only if optaion is enabled and return is filled with invalid Characters
            return False
        correct = True
        for i in range(0,9):
            for j in range(0,9):
                if self.get(i,j) != self.__input__[0] and not self.isValidElement(i,j):
                    correct = False
                    if showError:
                        print(i,j,self.get(i,j))
                    else:
                        return False
        return correct

    def isComplete(self,showError=False):
        '''
        Check if all element are filled or not.
        '''
        stack = self.getUnfilledElement()
        complete = True
        if not stack:
            complete = True
        else:
            complete = False

        if showError:
            print(stack)

        return complete, stack.copy()

    def isValidElement(self, i, j, element=None):
        '''
        It will return whether the value at index (i,j) is correct or not
        If element is None then it check whether the filled value is correct or not
        else it check whether the provided value is valid in the given location
        '''
        if element == None:
            element = self.get(i,j)

        if self.__terminal__ and False:
            print('isValidElement->Element : ',i,j,element)
            print(self.getRowElements(i,j))
            print(self.getColElements(i,j))
            print(self.getUnitElements(i,j))

        if element == self.__input__[0]:
            return True
        elif element not in self.__input__:
            if self.__terminal__:
                print('Invalid Element : ',element)
            return False
        elif element in self.getUnitElements(i,j):
            return False                    # i,j element found in the unit excluding itself
        elif element in self.getRowElements(i,j):
            return False                    # i,j element found in the Row excluding itself
        elif element in self.getColElements(i,j):
            return False                    # i,j element found in the Col excluding itself
        return True

    def beforeSolve(self):
        '''
        Check all the necessary condition before solving the Sodoku.
        '''
        valid = True
        if not self.isValid():
            self.show()
            if self.__terminal__:
                print('Board is not correctly setup. It contain invalid Characters.')
                correct = input('Can I correct it : ')
                if correct.strip().lower() in ['yes','y','of course','yaah', 'why not','why not?']:
                    self.isValid(True)
                else:
                    return False, None
            else:
                return False, None

        complete, stack = self.isComplete()
        if complete:
            self.log('Sudoku is Already Completed')
        if not self.isCorrect():
            self.log('Sodoku is INCORRECT.')
            valid = False
        return valid, stack.copy()

    def autoSolve(self):
        '''
        Solve the puzzle using backtracking method by using a list
        By iterating the list we assign a valid value to the current index and
        If no valid value found then change the previous set value and iterate the whole list.
        '''
        valid, stack = self.beforeSolve()
        if not valid or not stack:
            return valid

        # from random import shuffle
        # shuffle(stack)
        # del shuffle

        pointer = 0
        iteration = 0
        totalIteration = 0
        while pointer < len(stack):
            '''
            If pointer is < 0 then Unsolvable Sudoku break

            -> If we try all input chaacters then change the previous set pointer and update to default value which can be update in next iteration
            -> self.fill Function update pointer value is the provided value is correct. So if above IF statement is correct fill function definately set the value
                but return false so we don't change the pointer value
            -> If value is correct then set to puzzle(while will set by fill function itself) and update the pointer
                Else do nothing
            '''
            if pointer < 0:
                valid = False
                break

            stack[pointer][2] += 1
            if stack[pointer][2] >= len(self.__input__):
                # print('1', pointer, stack[pointer][2])
                iteration += 1
                stack[pointer][2] = 0
                self.fill(stack[pointer][0],stack[pointer][1],self.__input__[stack[pointer][2]])
                # self.show()
                pointer -= 1
                continue

            if self.fill(stack[pointer][0],stack[pointer][1],self.__input__[stack[pointer][2]], forceSet=True):
                # print('2', pointer, stack[pointer][2])
                # self.show()
                pointer +=1
                iteration += 1
            else:
                # print('3',pointer,stack[pointer][2])
                # self.show()
                totalIteration += 1

            # if False:
            #     if (totalIteration+iteration)%10000 == 0:
            #         print(pointer,iteration+totalIteration, end=' <=> ')

            # if False and self.__terminal__:
            #     # print('final',pointer,stack[pointer][2])
            #     print(pointer,iteration+totalIteration)
            #     # input()

        if valid:
            self.log('Sodoku is Solved.')
        else:
            self.log('This Sodoku is Unsolvable.')
        return valid, iteration, totalIteration+iteration

    def test(self):
        '''
        Randomly initialize puzzle and then solve that
        '''
        a = int(input())
        for aa in range(0,a):
            self.initPuzzle(True)
            self.show()
            print(self.autoSolve())
