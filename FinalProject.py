import tkinter as tk
from tkinter import ttk
from tkinter import *

#===================================Window Class========================


class Windows(tk.Tk):

  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
    self.title('restaurant')
    container = tk.Frame(self, height=400, width=200)
    container.pack(side="top", fill="both", expand=True)

    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    self.frames = {}

    for F in (MainPage, SidePage, CompletionScreen):
      frame = F(
        container,
        self,
      )

      self.frames[F] = frame
      frame.grid(row=0, column=0, sticky="nsew")

      # Using a method to switch frames
    self.show_frame(MainPage)

  def show_frame(self, cont):
    frame = self.frames[cont]
    # raises the current frame to the top
    frame.tkraise()

#=========================================First Class==============================


class MainPage(tk.Frame):

  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent, border=10)


    
    label = tk.Label(self, text="Inventory", border=3)
    label.grid(
      row=0,
      column=0,
      columnspan=5,
      pady=10,
      padx=20,
      ipady=5,
      ipadx=5,
    )
    label.config(highlightbackground="black",
                 highlightcolor="black",
                 highlightthickness=2)


    self.PRODUCTS = []
    self.list = list
    self.list = tk.Listbox(self,
                           width=15,
                           height=15,
                           background='white',
                           border=3)
    self.list.grid(row=1,
                   column=0,
                   columnspan=10,
                   pady=10,
                   padx=10,
                   ipady=5,
                   ipadx=5,
                   sticky="nsew")

    
    
    self.PRODUCTS = [
      ('chicken', 5),
      ('beef', 7),
      ('potatoes', 2),
      ('carrots', 3),
      ('green Beans', 8) 
    ]
    
    for self.item in self.PRODUCTS:
      self.list.insert(END, self.item)
      

    def remove():
      for self.item in self.list.curselection():
        self.item = self.list.get(self.item)[1]
        
        self.remove = self.item - 1
        for self.item in self.PRODUCTS:
           self.list.insert(END, self.remove)[1]
        self.showRemove = tk.Label(self, text=self.item[0])
        self.showRemove.grid(row=3, column=4)
       
       
    self.btn = tk.Button(self, text="remove", command=remove, border=3)
    self.btn.grid(row=2, column=1)


   # We use the switch_window_button in order to call the show_frame() method as a lambda function
    switch_window_button = tk.Button(
      self,
      text="Next Window",
      command=lambda: controller.show_frame(SidePage))
    switch_window_button.grid(row=6, column=3, padx=10, pady=5, sticky="nsew")


#===============================Second Class=====================================


class SidePage(tk.Frame):

  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent, border=10)
  #code between here~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



    
          #goodLuck!



    

  #and here^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
    switch_window_button = tk.Button(
      self,
      text="Next window",
      command=lambda: controller.show_frame(CompletionScreen),
    )
    switch_window_button.grid(row=6, column=3, padx=10, pady=5, sticky="nsew")


#===================================Third Class===============================


class CompletionScreen(tk.Frame):

  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent, border=10)
    #code between here~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    self.chicken = int(5)
    self.beef = int(5)
    self.potatoes =int(5)
    self.carrots =  int(5)
    self.greenBeans = int(5)

    
    label = tk.Label(self, text="Menu", border=3)
    label.grid(
      row=0,
      column=0,
      columnspan=5,
      pady=10,
      padx=20,
      ipady=5,
      ipadx=5,
    )
    label.config(highlightbackground="black",
                 highlightcolor="black",
                 highlightthickness=2)


    self.PRODUCTS = []
    self.list = list
    self.list = tk.Listbox(self,
                           width=15,
                           height=15,
                           background='white',
                           border=3)
    self.list.grid(row=1,
                   column=0,
                   columnspan=10,
                   pady=10,
                   padx=10,
                   ipady=5,
                   ipadx=5,
                   sticky="nsew")

    self.prod_labels= [
      "Chicken  ---  $6.99",
      "Beef  ---  $8.99",
      'Potatoes  ---  $3.99',
      'Carrots  ---  $2.99',
      'Green Beans  ---  $2.99'
    ]
    
    self.PRODUCTS = [
      (self.chicken),
      (self.beef),
      (self.potatoes),
      (self.carrots),
      (self.greenBeans),
    ]
    for self.items, self.prod_labels in zip(self.prod_labels, self.PRODUCTS):
      self.list.insert(END, self.items)
      

    def remove():
      for self.items in self.list.curselection():
        self.used = [self.PRODUCTS]
        for items in self.PRODUCTS:
          print(self.PRODUCTS)

    btn = tk.Button(self, text="remove", command=remove, border=3)
    btn.grid(row=2, column=1)
    

    
          #goodLuck!

    

    #and here^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
    switch_window_button = ttk.Button(
      self,
      text="Return to First window",
      command=lambda: controller.show_frame(MainPage))
    switch_window_button.grid(row=6, column=3, padx=10, pady=5, sticky="nsew")

if __name__ == "__main__":
  app = Windows()
  app.mainloop()
