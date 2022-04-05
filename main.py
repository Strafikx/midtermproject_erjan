import tkinter as tk
import random
import copy


class Matrix:
    Height = 960
    Width = 960

    def __init__(self, a, b, canvas: tk.Canvas, vaccine):
        self.a = a
        self.b = b
        self.canvas = canvas
        self.__height1 = self.Height / b
        self.__width1 = self.Width / a
        self.c = []
        self.vaccine1 = vaccine
        self.vaccines = []
        self.numvaccines = 0

        self.c.append([2 for i in range(b + 2)])

        for i in range(a):
            row = [2]
            for j in range(b):
                row.append(random.choice([0, 1]))

            row.append(2)

            self.c.append(row)

        self.c.append([2 for i in range(b + 2)])

        self.draw()

    def draw(self):
        y = 0
        self.canvas.delete("all")
        for i in range(1, self.a + 1):
            x = 0
            for j in range(1, self.b + 1):
                if self.c[i][j] == 1:
                    colour = "darkred"
                elif self.c[i][j] == 3:
                    colour = "steelblue"
                else:
                    colour = "burlywood3"
                self.canvas.create_rectangle(
                    x, y, x + self.__width1, y + self.__height1, fill=colour
                    )

                x += self.__width1
            y += self.__height1
        self.virus()
        self.canvas.after(100, self.draw)
        self.vaccine_m()
        self.inject()

    def virus(self):
        matrixc = copy.deepcopy(self.c)
        for i in range(1, self.a + 1):
            for j in range(1, self.b + 1):
                Neis = 0
                if matrixc[i + 1][j] == 1:
                    Neis += 1
                if matrixc[i + 1][j + 1] == 1:
                    Neis += 1
                if matrixc[i][j + 1] == 1:
                    Neis += 1
                if matrixc[i - 1][j + 1] == 1:
                    Neis += 1
                if matrixc[i - 1][j] == 1:
                    Neis += 1
                if matrixc[i - 1][j - 1] == 1:
                    Neis += 1
                if matrixc[i][j - 1] == 1:
                    Neis += 1
                if matrixc[i + 1][j - 1] == 1:
                    Neis += 1

                if self.c[i][j] == 0 and Neis == 3:
                    self.c[i][j] = 1
                elif matrixc[i][j] == 1:
                    if Neis not in (2, 3):
                        self.c[i][j] = 0

    def inject(self):
        if self.numvaccines > 20:
            return
        for i in range(self.vaccine1):
            q, w = random.randint(0, self.a), random.randint(0, self.b)

            self.vaccines.append((q, w))
            self.c[q][w] = 3
            self.numvaccines += 1

    def vaccine_m(self):
        for i in range(self.vaccine1):
            c1 = random.choice([0, -1, 1])
            try:
                self.c[self.vaccines[i][0]][self.vaccines[i][1]] = 0
                self.vaccines[i] = (
                    self.vaccines[i][0] + c1, self.vaccines[i][1] + c1
                    )
                self.c[self.vaccines[i][0]][self.vaccines[i][1]] = 3
            except:
                pass


root = tk.Tk()
root.geometry('960x960')
canvas = tk.Canvas(root, width=960, height=960)
canvas.pack()

bc = Matrix(50, 50, canvas, 5)
root.mainloop()
