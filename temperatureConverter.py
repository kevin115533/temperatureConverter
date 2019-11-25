from tkinter import *

class Temperature(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Temperature Converter")
        self.grid()
        # fahrenheit
        self.farLabel = Label(self, text = "Fahrenheit")
        self.farLabel.grid(row = 0, column = 0)
        self.farVar = DoubleVar()
        self.farVar.set(32.0)
        self.farEntry = Entry(self, textvariable = self.farVar)
        self.farEntry.grid(row = 0, column = 1)
        # celsius
        self.celLabel = Label(self, text="Celsius")
        self.celLabel.grid(row = 1, column = 0)
        self.celVar = DoubleVar()
        self.celEntry = Entry(self, textvariable=self.celVar)
        self.celEntry.grid(row = 1, column = 1)
        #buttons
        self.fToCButton = Button(self, text = ">>>>>", command = self._fToC)
        self.fToCButton.grid(row = 2, column = 0)
        self.cToFButton = Button(self, text = "<<<<<", command = self._cToF)
        self.cToFButton.grid(row = 2, column = 1)

    def _fToC(self):
        fahrenheit = self.farVar.get()
        celsius = (fahrenheit - 32) * (5 / 9)
        self.celVar.set(celsius)

    def _cToF(self):
        celsius = self.celVar.get()
        fahrenheit = (celsius * (9 / 5)) + 32
        self.farVar.set(fahrenheit)


def main():
    Temperature().mainloop()

main()
