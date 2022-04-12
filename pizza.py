import tkinter as tk
from tkinter import ttk     

root = tk.Tk()

#Name of the ordering system, name of pizza lists
title_label = ttk.Label(root, text="Pizza ordering system", font='ComicSansMS 14 bold')
title_label.grid(row=0, column=0, columnspan=2)

regular_pizza_label = ttk.Label(root, text="Regular Pizza ($8.50)", font='ComicSansMS 12 bold')
regular_pizza_label.grid(row=1, column=0)

gourmet_pizza_label = ttk.Label(root, text="Gourmet Pizza $12", font='ComicSansMS 12 bold')
gourmet_pizza_label.grid(row=1, column=1)

#Labels for the normal pizza's
cheese_pizza_label = ttk.Label(root, text="Cheese Pizza")
cheese_pizza_label.grid(row=2, column=0)

garlic_pizza_label = ttk.Label(root, text="Cheesey Garlic Pizza")
garlic_pizza_label.grid(row=3, column=0)

pineapple_pizza_label = ttk.Label(root, text="Pineapple and Sausage Pizza")
pineapple_pizza_label.grid(row=4, column=0)

chocolate_pizza_label = ttk.Label(root, text="Chocolate Pizza")
chocolate_pizza_label.grid(row=5, column=0)

racism_pizza_label = ttk.Label(root, text="Racism (half burnt half raw) Pizza")
racism_pizza_label.grid(row=6, column=0)

vegan_pizza_label = ttk.Label(root, text="The Mr Malaitai (Vegan) Pizza")
vegan_pizza_label.grid(row=7, column=0)

vegetarian_pizza_label = ttk.Label(root, text="End of Vegetales Pizza")
vegetarian_pizza_label.grid(row=8, column=0)

#This is all the labels for the gourmet pizza's
guilty_pizza_label = ttk.Label(root, text="The Guilty Pleasure Pizza")
guilty_pizza_label.grid(row=2, column=1)

anti_pizza_label = ttk.Label(root, text="The Anti Vegan Pizza")
anti_pizza_label.grid(row=3, column=1)

big_pizza_label = ttk.Label(root, text="The Big Boy Banger Pizza")
big_pizza_label.grid(row=4, column=1)

fortnite_pizza_label = ttk.Label(root, text="The Fortnite Pizza")
fortnite_pizza_label.grid(row=5, column=1)

cat_pizza_label = ttk.Label(root, text="The Doja 'Cat' Pizza")
cat_pizza_label.grid(row=6, column=1)


root.mainloop()