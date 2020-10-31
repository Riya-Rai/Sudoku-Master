from tkinter import *
from tkinter import messagebox
import sudoku

class Application(Tk):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.__puzzle__ = sudoku.Sudoku()
        self.geometry('1600x800+0+0')
        self.title('Sudoku Solver')

        self.createFrames()
        self.createTopView()
        self.createLeftView()
        self.createSudokuView()
        self.createRightView()

        self.bindSudokuElement()

    def createFrames(self):
        self.topFrame = Frame(self, width=1600, height=100)
        self.middleFrame = Frame(self, width=1600, height=500)
        self.bottomFrame = Frame(self, width=1600, height=200)
        
        self.leftFrame = Frame(self.middleFrame, width=200, height=500)
        self.sudokuFrame = Frame(self.middleFrame, width=600, height=500)
        self.rightFrame = Frame(self.middleFrame, width=200, height=500)

        self.topFrame.pack(side=TOP)
        self.middleFrame.pack(side=TOP)
        self.bottomFrame.pack(side=TOP)

        self.leftFrame.pack(side=LEFT)
        self.sudokuFrame.pack(side=LEFT)
        self.rightFrame.pack(side=LEFT)

    def createTopView(self):
        self.labelInfo = Label(self.topFrame, font=('arial',30, 'bold'), text="Sudoku Solver", fg= 'gray', bd=10, anchor=W)
        self.labelInfo.grid(row=0, column=0)

    def createLeftView(self):
        self.defaultValueVar = StringVar()
        self.defaultValueVar.set(self.__puzzle__.getDefaultElement())
        self.labelDefault = Label(self.leftFrame, font=('arial',10, 'bold'), text="Default Value", fg= 'gray', bd=4, anchor=W)
        self.lableDefaultValue = Label(self.leftFrame,width=5, font=('arial',18,'bold'),bg='cyan', textvariable=self.defaultValueVar, bd =4, anchor=CENTER)
        self.labelDefault.grid(row=0)
        self.lableDefaultValue.grid(row=1)
            
    def createSudokuView(self):
        self.editSudokuFrame = Frame(self.sudokuFrame, bg="white", bd=20)
        self.editSudokuUnit = []
        for i in range(0,3):
            temp = []
            for j in range(0,3):
                frame = Frame(self.editSudokuFrame,bd=4, bg="black")
                frame.grid(row=i, column=j)
                temp.append(frame)
            self.editSudokuUnit.append(temp)
        self.editSudokuEntry = []
        self.inputSudokuEntry = []
        for i in range(0,9):
            temp_entry = []
            temp_input = []
            for j in range(0,9):
                text_input = StringVar()
                entry = Entry(self.editSudokuUnit[i//3][j//3], width=2, bd=4, font=('arial',16,'bold'), textvariable=text_input, insertwidth=2, bg='white',justify='center')
                entry.grid(row=i%3, column=j%3)
                temp_entry.append(entry)
                temp_input.append(text_input)
            self.editSudokuEntry.append(temp_entry)
            self.inputSudokuEntry.append(temp_input)
        self.editSudokuFrame.pack(fill=X)

    def createRightView(self):
        bg = 'cyan'
        fg = 'black'
        bd = 2
        padx = None
        pady = None
        font = ('arial',14,'bold')
        
        self.isValidButton = Button(self.rightFrame, padx=padx, pady=pady, bd=bd, font=font, fg=fg, text="Validity", bg=bg, command=self.btnIsValid)
        self.isCorrectButton = Button(self.rightFrame, padx=padx, pady=pady, bd=bd, font=font, fg=fg, text="Correctness", bg=bg, command=self.btnIsCorrect)
        self.isCompleteButton = Button(self.rightFrame, padx=padx, pady=pady, bd=bd, font=font, fg=fg, text="Completeness", bg=bg, command=self.btnIsComplete)
        self.setButton = Button(self.rightFrame, padx=padx, pady=pady, bd=bd, font=font, fg=fg, text="Set", bg="yellow", command=self.btnSetPuzzle)
        self.resetButton = Button(self.rightFrame, padx=padx, pady=pady, bd=bd, font=font, fg=fg, text="Reset", bg="orange", command=self.btnReset)
        self.clearButton = Button(self.rightFrame, padx=padx, pady=pady, bd=bd, font=font, fg=fg, text="Clear", bg="red", command=lambda: self.btnInitlize(False))
        self.randomButton = Button(self.rightFrame, padx=padx, pady=pady, bd=bd, font=font, fg=fg, text="Random", bg="red", command=lambda: self.btnInitlize(True))
        self.solveButton = Button(self.rightFrame, padx=padx, pady=pady, bd=bd, font=font, fg=fg, text="Solve", bg="green", command=self.btnSolve)
        
        self.isValidButton.pack(fill=X)
        self.isCorrectButton.pack(fill=X)
        self.isCompleteButton.pack(fill=X)
        self.setButton.pack(fill=X)
        self.resetButton.pack(fill=X)
        self.clearButton.pack(fill=X)
        self.randomButton.pack(fill=X)
        self.solveButton.pack(fill=X)

    def bindSudokuElement(self):
        '''
        While using loop when we pass i,j value to setPuzzleValue function then it send the
        current value of i,j instead of required so it always goint to send 8,8 and if after
        loop we somehow change i,j value then that is going to transfer to the function
        '''
        self.editSudokuEntry[0][0].bind('<Key-Return>',lambda _ : self.setPuzzleValue(0,0))
        self.editSudokuEntry[0][1].bind('<Key-Return>',lambda _ : self.setPuzzleValue(0,1))
        self.editSudokuEntry[0][2].bind('<Key-Return>',lambda _ : self.setPuzzleValue(0,2))
        self.editSudokuEntry[0][3].bind('<Key-Return>',lambda _ : self.setPuzzleValue(0,3))
        self.editSudokuEntry[0][4].bind('<Key-Return>',lambda _ : self.setPuzzleValue(0,4))
        self.editSudokuEntry[0][5].bind('<Key-Return>',lambda _ : self.setPuzzleValue(0,5))
        self.editSudokuEntry[0][6].bind('<Key-Return>',lambda _ : self.setPuzzleValue(0,6))
        self.editSudokuEntry[0][7].bind('<Key-Return>',lambda _ : self.setPuzzleValue(0,7))
        self.editSudokuEntry[0][8].bind('<Key-Return>',lambda _ : self.setPuzzleValue(0,8))
        self.editSudokuEntry[1][0].bind('<Key-Return>',lambda _ : self.setPuzzleValue(1,0))
        self.editSudokuEntry[1][1].bind('<Key-Return>',lambda _ : self.setPuzzleValue(1,1))
        self.editSudokuEntry[1][2].bind('<Key-Return>',lambda _ : self.setPuzzleValue(1,2))
        self.editSudokuEntry[1][3].bind('<Key-Return>',lambda _ : self.setPuzzleValue(1,3))
        self.editSudokuEntry[1][4].bind('<Key-Return>',lambda _ : self.setPuzzleValue(1,4))
        self.editSudokuEntry[1][5].bind('<Key-Return>',lambda _ : self.setPuzzleValue(1,5))
        self.editSudokuEntry[1][6].bind('<Key-Return>',lambda _ : self.setPuzzleValue(1,6))
        self.editSudokuEntry[1][7].bind('<Key-Return>',lambda _ : self.setPuzzleValue(1,7))
        self.editSudokuEntry[1][8].bind('<Key-Return>',lambda _ : self.setPuzzleValue(1,8))
        self.editSudokuEntry[2][0].bind('<Key-Return>',lambda _ : self.setPuzzleValue(2,0))
        self.editSudokuEntry[2][1].bind('<Key-Return>',lambda _ : self.setPuzzleValue(2,1))
        self.editSudokuEntry[2][2].bind('<Key-Return>',lambda _ : self.setPuzzleValue(2,2))
        self.editSudokuEntry[2][3].bind('<Key-Return>',lambda _ : self.setPuzzleValue(2,3))
        self.editSudokuEntry[2][4].bind('<Key-Return>',lambda _ : self.setPuzzleValue(2,4))
        self.editSudokuEntry[2][5].bind('<Key-Return>',lambda _ : self.setPuzzleValue(2,5))
        self.editSudokuEntry[2][6].bind('<Key-Return>',lambda _ : self.setPuzzleValue(2,6))
        self.editSudokuEntry[2][7].bind('<Key-Return>',lambda _ : self.setPuzzleValue(2,7))
        self.editSudokuEntry[2][8].bind('<Key-Return>',lambda _ : self.setPuzzleValue(2,8))
        self.editSudokuEntry[3][0].bind('<Key-Return>',lambda _ : self.setPuzzleValue(3,0))
        self.editSudokuEntry[3][1].bind('<Key-Return>',lambda _ : self.setPuzzleValue(3,1))
        self.editSudokuEntry[3][2].bind('<Key-Return>',lambda _ : self.setPuzzleValue(3,2))
        self.editSudokuEntry[3][3].bind('<Key-Return>',lambda _ : self.setPuzzleValue(3,3))
        self.editSudokuEntry[3][4].bind('<Key-Return>',lambda _ : self.setPuzzleValue(3,4))
        self.editSudokuEntry[3][5].bind('<Key-Return>',lambda _ : self.setPuzzleValue(3,5))
        self.editSudokuEntry[3][6].bind('<Key-Return>',lambda _ : self.setPuzzleValue(3,6))
        self.editSudokuEntry[3][7].bind('<Key-Return>',lambda _ : self.setPuzzleValue(3,7))
        self.editSudokuEntry[3][8].bind('<Key-Return>',lambda _ : self.setPuzzleValue(3,8))
        self.editSudokuEntry[4][0].bind('<Key-Return>',lambda _ : self.setPuzzleValue(4,0))
        self.editSudokuEntry[4][1].bind('<Key-Return>',lambda _ : self.setPuzzleValue(4,1))
        self.editSudokuEntry[4][2].bind('<Key-Return>',lambda _ : self.setPuzzleValue(4,2))
        self.editSudokuEntry[4][3].bind('<Key-Return>',lambda _ : self.setPuzzleValue(4,3))
        self.editSudokuEntry[4][4].bind('<Key-Return>',lambda _ : self.setPuzzleValue(4,4))
        self.editSudokuEntry[4][5].bind('<Key-Return>',lambda _ : self.setPuzzleValue(4,5))
        self.editSudokuEntry[4][6].bind('<Key-Return>',lambda _ : self.setPuzzleValue(4,6))
        self.editSudokuEntry[4][7].bind('<Key-Return>',lambda _ : self.setPuzzleValue(4,7))
        self.editSudokuEntry[4][8].bind('<Key-Return>',lambda _ : self.setPuzzleValue(4,8))
        self.editSudokuEntry[5][0].bind('<Key-Return>',lambda _ : self.setPuzzleValue(5,0))
        self.editSudokuEntry[5][1].bind('<Key-Return>',lambda _ : self.setPuzzleValue(5,1))
        self.editSudokuEntry[5][2].bind('<Key-Return>',lambda _ : self.setPuzzleValue(5,2))
        self.editSudokuEntry[5][3].bind('<Key-Return>',lambda _ : self.setPuzzleValue(5,3))
        self.editSudokuEntry[5][4].bind('<Key-Return>',lambda _ : self.setPuzzleValue(5,4))
        self.editSudokuEntry[5][5].bind('<Key-Return>',lambda _ : self.setPuzzleValue(5,5))
        self.editSudokuEntry[5][6].bind('<Key-Return>',lambda _ : self.setPuzzleValue(5,6))
        self.editSudokuEntry[5][7].bind('<Key-Return>',lambda _ : self.setPuzzleValue(5,7))
        self.editSudokuEntry[5][8].bind('<Key-Return>',lambda _ : self.setPuzzleValue(5,8))
        self.editSudokuEntry[6][0].bind('<Key-Return>',lambda _ : self.setPuzzleValue(6,0))
        self.editSudokuEntry[6][1].bind('<Key-Return>',lambda _ : self.setPuzzleValue(6,1))
        self.editSudokuEntry[6][2].bind('<Key-Return>',lambda _ : self.setPuzzleValue(6,2))
        self.editSudokuEntry[6][3].bind('<Key-Return>',lambda _ : self.setPuzzleValue(6,3))
        self.editSudokuEntry[6][4].bind('<Key-Return>',lambda _ : self.setPuzzleValue(6,4))
        self.editSudokuEntry[6][5].bind('<Key-Return>',lambda _ : self.setPuzzleValue(6,5))
        self.editSudokuEntry[6][6].bind('<Key-Return>',lambda _ : self.setPuzzleValue(6,6))
        self.editSudokuEntry[6][7].bind('<Key-Return>',lambda _ : self.setPuzzleValue(6,7))
        self.editSudokuEntry[6][8].bind('<Key-Return>',lambda _ : self.setPuzzleValue(6,8))
        self.editSudokuEntry[7][0].bind('<Key-Return>',lambda _ : self.setPuzzleValue(7,0))
        self.editSudokuEntry[7][1].bind('<Key-Return>',lambda _ : self.setPuzzleValue(7,1))
        self.editSudokuEntry[7][2].bind('<Key-Return>',lambda _ : self.setPuzzleValue(7,2))
        self.editSudokuEntry[7][3].bind('<Key-Return>',lambda _ : self.setPuzzleValue(7,3))
        self.editSudokuEntry[7][4].bind('<Key-Return>',lambda _ : self.setPuzzleValue(7,4))
        self.editSudokuEntry[7][5].bind('<Key-Return>',lambda _ : self.setPuzzleValue(7,5))
        self.editSudokuEntry[7][6].bind('<Key-Return>',lambda _ : self.setPuzzleValue(7,6))
        self.editSudokuEntry[7][7].bind('<Key-Return>',lambda _ : self.setPuzzleValue(7,7))
        self.editSudokuEntry[7][8].bind('<Key-Return>',lambda _ : self.setPuzzleValue(7,8))
        self.editSudokuEntry[8][0].bind('<Key-Return>',lambda _ : self.setPuzzleValue(8,0))
        self.editSudokuEntry[8][1].bind('<Key-Return>',lambda _ : self.setPuzzleValue(8,1))
        self.editSudokuEntry[8][2].bind('<Key-Return>',lambda _ : self.setPuzzleValue(8,2))
        self.editSudokuEntry[8][3].bind('<Key-Return>',lambda _ : self.setPuzzleValue(8,3))
        self.editSudokuEntry[8][4].bind('<Key-Return>',lambda _ : self.setPuzzleValue(8,4))
        self.editSudokuEntry[8][5].bind('<Key-Return>',lambda _ : self.setPuzzleValue(8,5))
        self.editSudokuEntry[8][6].bind('<Key-Return>',lambda _ : self.setPuzzleValue(8,6))
        self.editSudokuEntry[8][7].bind('<Key-Return>',lambda _ : self.setPuzzleValue(8,7))
        self.editSudokuEntry[8][8].bind('<Key-Return>',lambda _ : self.setPuzzleValue(8,8))

    def colorPuzzleValue(self):
        for i in range(0,9):
            for j in range(0,9):
                if self.__puzzle__.get(i,j) != self.__puzzle__.getDefaultElement():
                    self.editSudokuEntry[i][j].config(fg='red')
                else:
                    self.editSudokuEntry[i][j].config(fg='black')
        
    def syncPuzzle(self):
        # print('syncPUzzle')
        for i in range(0,9):
            for j in range(0,9):
                self.inputSudokuEntry[i][j].set(self.__puzzle__.get(i,j))

    def btnReset(self):
        # print('reset button')
        self.__puzzle__.reset()
        self.syncPuzzle()

    def btnInitlize(self, check):
        # print('initlizing puzzle')
        self.__puzzle__.initPuzzle(check)
        self.colorPuzzleValue()
        self.syncPuzzle()

    def btnSolve(self):
        # print('solve button')
        # self.__puzzle__.autoSolve()
        # self.syncPuzzle()

        if not self.btnIsValid(False):
            return
        if not self.btnIsCorrect(False):
            return
        _ , stack = self.btnIsComplete(False)
        if not stack:
            return
            
        valid = True
        pointer = 0
        iteration = 0
        totalIteration = 0
        from time import sleep
        while pointer < len(stack):
            if pointer < 0:
                valid = False
                break

            stack[pointer][2] += 1
            if stack[pointer][2] >= len(self.__puzzle__.__input__):
                iteration += 1
                stack[pointer][2] = 0
                if self.__puzzle__.fill(stack[pointer][0],stack[pointer][1],self.__puzzle__.__input__[stack[pointer][2]]):
                    self.fillPuzzleValue(stack[pointer][0], stack[pointer][1], self.__puzzle__.__input__[stack[pointer][2]])
                pointer -= 1
                continue

            if self.__puzzle__.fill(stack[pointer][0],stack[pointer][1],self.__puzzle__.__input__[stack[pointer][2]], forceSet=True):
                self.fillPuzzleValue(stack[pointer][0], stack[pointer][1], self.__puzzle__.__input__[stack[pointer][2]])
                # print(stack[pointer][0],stack[pointer][1],self.__puzzle__.__input__[stack[pointer][2]])
                pointer +=1
                iteration += 1
            else:
                # self.show()
                totalIteration += 1
            self.__puzzle__.show()
            # sleep(1)
        del sleep

        if not valid:
            messagebox.showinfo("Sudoku's Completeness", 'This Sodoku is Unsolvable.')
        
        

    def btnSetPuzzle(self):
        # print('set button')
        invalid = []
        for i in range(0,9):
            for j in range(0,9):
                # self.__puzzle__.set(i,j,self.editSudokuEntry[i][j].get().strip())
                if self.__puzzle__.isValidElement(i,j,self.editSudokuEntry[i][j].get().strip()):
                    self.__puzzle__.set(i,j,self.editSudokuEntry[i][j].get().strip())
                else:
                    invalid.append([i,j,self.editSudokuEntry[i][j].get()])
        incorrect = 'Following are Incoorect:\n'
        for a in invalid:
            incorrect += '(' + str(a[0]) + ',' + str(a[1]) + ')' + ' => ' + str(a[2]) + '\n'
        
        if invalid:
            print('invalid','\n',incorrect)
            messagebox.showerror('Invalid', incorrect)

        self.colorPuzzleValue()
        self.syncPuzzle()

    def fillPuzzleValue(self,i, j, value):
        self.inputSudokuEntry[i][j].set(value)


    def setPuzzleValue(self,i,j):
        if self.__puzzle__.isValidElement(i,j,self.editSudokuEntry[i][j].get().strip()):
            self.__puzzle__.set(i,j,self.editSudokuEntry[i][j].get().strip())
            if self.editSudokuEntry[i][j].get().strip() == self.__puzzle__.getDefaultElement():
                self.editSudokuEntry[i][j].config(fg='black')
            else:
                self.editSudokuEntry[i][j].configure(fg='red')
        else:
            messagebox.showerror('Invalid','Invalid Entry.\n'+'('+str(i)+','+str(j)+') => '+ str(self.editSudokuEntry[i][j].get()))
            self.inputSudokuEntry[i][j].set(self.__puzzle__.get(i,j))

    def btnIsComplete(self, show=True):
        complete, stack = self.__puzzle__.isComplete()
        message = ' Not'
        if complete:
            message = ''
        if show or complete:
            messagebox.showinfo("Sudoku's Completeness", 'Sudoku is'+message+' Complete')
        return complete, stack
    
    def btnIsCorrect(self, show=True):
        correct = self.__puzzle__.isCorrect()
        message = ' Not'
        if correct:
            message = ''
        if show or not correct:
            messagebox.showinfo("Sodoku's Correctness", 'Sudoku is'+ message + ' Correct')
        return correct

    def btnIsValid(self, show=True):
        valid = self.__puzzle__.isValid()
        message = ' Not'
        if valid:
            message = ''
        if show or not valid:
            messagebox.showinfo('Sodoku Validity', 'Sudoku is'+ message + ' Valid')
        return valid

    def btnSetDefaultValue(self):
        pass
