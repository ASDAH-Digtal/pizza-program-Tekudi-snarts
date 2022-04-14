import tkinter as tk
from tkinter import ttk     

root = tk.Tk()

#Name of the ordering system, name of pizza lists
title_label = ttk.Label(root, text="Pizza ordering system", font='ComicSansMS 16 bold')
title_label.grid(row=1, column=0, columnspan=4, padx=100, pady=25)

regular_pizza_label = ttk.Label(root, text="Regular Pizza ($8.50)", font='ComicSansMS 12 bold')
regular_pizza_label.grid(row=2, column=0, padx=50, pady=15)

gourmet_pizza_label = ttk.Label(root, text="Gourmet Pizza $12", font='ComicSansMS 12 bold')
gourmet_pizza_label.grid(row=2, column=3, padx=50, pady=15)

#Labels for the normal pizza's
cheese_pizza_label = ttk.Label(root, text="Cheese Pizza")
cheese_pizza_label.grid(row=3, column=0, pady=10)

garlic_pizza_label = ttk.Label(root, text="Cheesey Garlic Pizza")
garlic_pizza_label.grid(row=4, column=0, pady=10)

pineapple_pizza_label = ttk.Label(root, text="Pineapple and Sausage Pizza")
pineapple_pizza_label.grid(row=5, column=0, pady=10)

chocolate_pizza_label = ttk.Label(root, text="Chocolate Pizza")
chocolate_pizza_label.grid(row=6, column=0, pady=10)

racism_pizza_label = ttk.Label(root, text="Racism (half burnt half raw) Pizza")
racism_pizza_label.grid(row=7, column=0, pady=10)

vegan_pizza_label = ttk.Label(root, text="The Mr Malaitai (Vegan) Pizza")
vegan_pizza_label.grid(row=8, column=0, pady=10)

vegetarian_pizza_label = ttk.Label(root, text="End of Vegetales Pizza")
vegetarian_pizza_label.grid(row=9, column=0, pady=10)


#This is all the labels for the gourmet pizza's
guilty_pizza_label = ttk.Label(root, text="The Guilty Pleasure Pizza")
guilty_pizza_label.grid(row=3, column=3, pady=10)

anti_pizza_label = ttk.Label(root, text="The Anti Vegan Pizza")
anti_pizza_label.grid(row=4, column=3, pady=10)

big_pizza_label = ttk.Label(root, text="The Big Boy Banger Pizza")
big_pizza_label.grid(row=5, column=3, pady=10)

fortnite_pizza_label = ttk.Label(root, text="The Fortnite Pizza")
fortnite_pizza_label.grid(row=6, column=3, pady=10)

cat_pizza_label = ttk.Label(root, text="The Doja 'Cat' Pizza")
cat_pizza_label.grid(row=7, column=3, pady=10)

#buttons for delievery or takeaway
var = tk.IntVar()
delivery_rb = ttk.Radiobutton(root , text="Delivery", variable=var, value=1)
delivery_rb.grid(row=10, column=0, pady=25)

takeaway_rb = ttk.Radiobutton(root , text="Takeaway", variable=var, value=2)
takeaway_rb.grid(row=10, column=3, pady=25)

#enter details
name_entry = ttk.Entry(root)
name_entry.grid(row=11, column=3, padx=5, pady=10)

name_label = ttk.Label(root, text="Name:")
name_label.grid(row=11, column=0, padx=5, pady=10)

phone_entry = ttk.Entry(root)
phone_entry.grid(row=12, column=3, padx=5, pady=10)

phone_label = ttk.Label(root, text="Phone number:")
phone_label.grid(row=12, column=0, padx=5, pady=10)

address_entry = ttk.Entry(root)
address_entry.grid(row=13, column=3, padx=5, pady=10)

address_label = ttk.Label(root, text="Address:")
address_label.grid(row=13, column=0, padx=5, pady=10)


#Select pizza combobox
selected_pizza = tk.StringVar()
selected_pizza.set("Select a pizza!")
pizza_menu = ttk.Combobox(root, textvariable=selected_pizza)
pizza_menu.grid(row=14, column=0, padx=10, pady=5)
pizza_menu['values'] = ["Cheese", "Cheesy Garlic", "Pineapple, sausage", "Chocolate", "Racism", "Mr.Malaitai", "vegetales", "Guilty Pleasure", "Anti-Vegan", "Big Boy Banger", "Fortnite", "Doja 'CAT'"]
pizza_menu['state'] = 'readonly'

selected_pizza = tk.StringVar()
selected_pizza.set("Select a pizza!")
pizza2_menu = ttk.Combobox(root, textvariable=selected_pizza)
pizza2_menu.grid(row=15, column=0, padx=10, pady=5)
pizza2_menu['values'] = ["Cheese", "Cheesy Garlic", "Pineapple, sausage", "Chocolate", "Racism", "Mr.Malaitai", "vegetales", "Guilty Pleasure", "Anti-Vegan", "Big Boy Banger", "Fortnite", "Doja 'CAT'"]
pizza2_menu['state'] = 'readonly'

selected_pizza = tk.StringVar()
selected_pizza.set("Select a pizza!")
pizza3_menu = ttk.Combobox(root, textvariable=selected_pizza)
pizza3_menu.grid(row=16, column=0, padx=10, pady=5)
pizza3_menu['values'] = ["Cheese", "Cheesy Garlic", "Pineapple, sausage", "Chocolate", "Racism", "Mr.Malaitai", "vegetales", "Guilty Pleasure", "Anti-Vegan", "Big Boy Banger", "Fortnite", "Doja 'CAT'"]
pizza3_menu['state'] = 'readonly'

selected_pizza = tk.StringVar()
selected_pizza.set("Select a pizza!")
pizza4_menu = ttk.Combobox(root, textvariable=selected_pizza)
pizza4_menu.grid(row=17, column=0, padx=10, pady=5)
pizza4_menu['values'] = ["Cheese", "Cheesy Garlic", "Pineapple, sausage", "Chocolate", "Racism", "Mr.Malaitai", "vegetales", "Guilty Pleasure", "Anti-Vegan", "Big Boy Banger", "Fortnite", "Doja 'CAT'"]
pizza4_menu['state'] = 'readonly'

selected_pizza = tk.StringVar()
selected_pizza.set("Select a pizza!")
pizza5_menu = ttk.Combobox(root, textvariable=selected_pizza)
pizza5_menu.grid(row=18, column=0, padx=10, pady=5)
pizza5_menu['values'] = ["Cheese", "Cheesy Garlic", "Pineapple, sausage", "Chocolate", "Racism", "Mr.Malaitai", "vegetales", "Guilty Pleasure", "Anti-Vegan", "Big Boy Banger", "Fortnite", "Doja 'CAT'"]
pizza5_menu['state'] = 'readonly'

#Total, etc

total_label = ttk.Label(root, text="TOTAL", font='ComicSansMS 12 bold')
total_label.grid(row=19, column=0)

total_money_label = ttk.Label(root, text="$$$", font='ComicSansMS 12 bold')
total_money_label.grid(row=19, column=3)
root.mainloop()