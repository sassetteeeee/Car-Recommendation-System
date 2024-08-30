import tkinter as tk
from tkinter import ttk
from tkinter import Spinbox, Button, Checkbutton
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
import numpy as np

# Load car data
car_data = pd.read_csv('CARS DATASET.csv')

# Create the main application window
root = tk.Tk()
root.title("Car Recommendation System")

# function to open page 2
def open_page2():
    root.withdraw()  # hide main page
    page2.deiconify()  # show Page 2

# function to open page 3
def open_page3():
    page2.withdraw()  # hide page 2
    page3.deiconify()  # show page 3

def open_page4():
    # Get user inputs
    budget_range = budget_combobox.get().strip()
    selected_body_types = [body_type for body_type, var in body_type_checkboxes.items() if var.get()]
    seat_capacity_text = spin.get().strip()

    # Validate user inputs
    if not budget_range or not selected_body_types or not seat_capacity_text:
        messagebox.showerror("Error", "Please enter budget, choose body type, and select capacity.")
        return

    # Filter car data based on user input
    recommended_cars = filter_cars(budget_range, selected_body_types, int(seat_capacity_text))

    # Display recommended cars
    display_recommended_cars(recommended_cars)

    page3.withdraw()
    page4.deiconify()

# function to open page 5
def open_page5():
    page4.withdraw()  # hide page 4
    page5.deiconify()  # show page 5

# Page 1: home page
image_path = 'car images\\home.jpg' 
image = Image.open(image_path)
image = image.resize((850,480), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.pack(pady=20)

# button to open page 2
next_button = tk.Button(root, text="Next", command=open_page2)
next_button.pack(pady=10)

# Page 2: Company information
page2 = tk.Toplevel()
page2.title("CAR FINDR")
page2.geometry("850x500")
page2.withdraw()  # Hide Page 2 initially

page2.configure(bg='#5CACEE')  

# title label
title_label = tk.Label(page2, text="About Us", font=('Helvetica', 16, 'bold'), bg='#5CACEE')
title_label.pack(pady=10)

logo_image_path = 'car images\\logo.png' 
logo_image = Image.open(logo_image_path)
logo_image = logo_image.resize((250, 150), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(page2, image=logo_photo, bg='#5CACEE')
logo_label.pack(pady=20)

company_info_label = tk.Label(
    page2, text='''Welcome to CARFINDR , where we redefine your car experience.Click Read More to know more about us.''',
    bg='#5CACEE'
)
company_info_label.pack(pady=20)

company_info_text = """For the majority of us, experiencing the world of cars has been a common experience. Introducing the Car 
Recommendation System,an innovative approach to expedited car exploration. Our car discovery platform was 
created for all users,regardless of whether they are car lovers or just someone looking for the ideal vehicle. With the help 
of this system, you may find the ideal car without having to wait in lines, make phone calls,or send messages. Just enter 
your spending limit, preferred car type, brand, and the number of seats, and let our technology take care of the complicated details of conventional
automobile searches."""

def show_company_info_message_box():
    messagebox.showinfo("About Us", company_info_text)

message_box_button = tk.Button(page2, text="Read More", command=show_company_info_message_box)
message_box_button.pack(pady=10)

# Button to open Page 3
next_button_page2 = tk.Button(page2, text="Next", command=open_page3)
next_button_page2.pack()

# Page 3: Find Your Car
page3 = tk.Toplevel()
page3.title("Find Your Car")
page3.geometry("850x500")
page3.withdraw()  # Hide Page 3 initially

page3.configure(bg='#5CACEE')  

# title label
title_label = tk.Label(page3, text="Find Your Car", font=('Helvetica', 16, 'bold'), bg='#5CACEE')
title_label.pack(pady=20)

# budget frame
budget_frame = tk.Frame(page3, bg='#5CACEE')
budget_frame.pack(padx=20, pady=20)

budget_label = tk.Label(budget_frame, text="Budget(RM):", bg='#5CACEE')
budget_label.pack(side=tk.LEFT)

# Use ttk.Combobox for dropdown menu
budget_options = ["rm30000", "rm40000", "rm50000", "rm60000", "rm70000", "rm80000", "rm90000", "rm100000", "rm110000", "rm120000", "rm130000",  "rm140000"]
budget_combobox = ttk.Combobox(budget_frame, values=budget_options)
budget_combobox.pack(side=tk.LEFT)

# Cbody type frame
frame = tk.Frame(page3, bg='#5CACEE')
frame.pack()

body = tk.Label(frame, text="Body Type:", bg='#5CACEE')
body.grid(row=0, column=0)

body_type_checkboxes = {}
body_types = ["Hatchback", "Sedan", "SUV", "MPV"]
for col, body_type in enumerate(body_types, start=1):
    var = tk.IntVar()
    checkbox = Checkbutton(frame, text=body_type, variable=var, onvalue=1, offvalue=0, bg='#5CACEE')
    checkbox.grid(row=0, column=col)
    body_type_checkboxes[body_type] = var
    
# capacity frame
frame = tk.Frame(page3)
frame.pack(padx=20, pady=20)

label_capacity = tk.Label(frame, text="Capacity:", bg='#5CACEE')
label_capacity.pack(side=tk.LEFT)

capacity_values = (5, 6, 7)
spin = Spinbox(frame, values=capacity_values)
spin.pack(side=tk.LEFT)

# button to open Page 4
next_button_page3 = tk.Button(page3, text="Next", command=open_page4)
next_button_page3.pack()


# Page 4: Recommended Car
page4 = tk.Toplevel()
page4.title("Recommended Car")
page4.geometry("580x500")
page4.withdraw()  # Hide Page 4 initially

page4.configure(bg='#5CACEE') 


# Function to display recommended cars
def display_recommended_cars(recommended_cars):
    # canvas
    canvas = tk.Canvas(page4, bg='#5CACEE')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # scrollbar
    scrollbar = tk.Scrollbar(page4, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    # frame inside the canvas to hold car information
    frame = tk.Frame(canvas,  bg='#5CACEE')
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # title label
    title_label = tk.Label(frame, text="Recommended Car For You", font=('Helvetica', 16, 'bold'), fg='black', bg='#5CACEE')
    title_label.pack(pady=20)

    # button open page 5
    next_button_page4 = tk.Button(frame, text="Next", command=open_page5)
    next_button_page4.pack(pady=10)

    # display recommended cars
    if not recommended_cars.empty:
        for index, row in recommended_cars.iterrows():
            car_name = row['car name']
            car_price = row['price']
            brand = row['brand']
            image_path = f"car images\\{car_name}.png"

            # display car information function
            display_car_info(frame, car_name, car_price, brand, image_path)
    else:
        # if no car match user input
        no_match_label = tk.Label(frame, text="No cars match the criteria.", fg='black', font=('Helvetica', 14), bg='#5CACEE')
        no_match_label.pack(pady=20)

    # pudate the Tkinter canvas & process any pending idle task
    canvas.update_idletasks()

    # set the canvas size based on the frame size
    canvas.config(scrollregion=canvas.bbox("all"))


def filter_cars(budget_range, selected_body_types, seat_capacity):
    selected_body_types = np.array(selected_body_types)
    
    # Extract budget range from the selected option
    min_budget = int(budget_range.replace('rm', '').strip())
    
    # Calculate the maximum budget based on the selected option
    max_budget = min_budget + 10000 
    
    # filter cars based on conditions
    filtered_cars = car_data[
        # find cars that are priced within the budget range
        (car_data["price"] >= min_budget) & (car_data["price"] <= max_budget) &
        # find cars with body types selected by the user
        (np.isin(car_data["body type"].values, selected_body_types)) &
        # find cars with seat capacity matching user preference
        (car_data["seat capacity"] == seat_capacity)
    ]   
    return filtered_cars

# function to display car information
def display_car_info(frame, car_name, car_price, brand, image_path):
    car_info_frame = tk.Frame(frame)
    car_info_frame.pack(pady=20, padx=20)

    car_info_label = tk.Label(
    car_info_frame,
    text=f"Car Name: {car_name}\nBrand: {brand}\nPrice: RM{car_price}",fg='black',height=3,width=50)
    car_info_label.pack(side=tk.LEFT)


    image = Image.open(image_path)
    image = image.resize((150, 140), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(car_info_frame, image=photo)
    image_label.image = photo
    image_label.pack(side=tk.RIGHT)


# Page 5: Contact
page5 = tk.Toplevel()
page5.title("Contact Us")
page5.geometry("850x500")
page5.withdraw()  # Hide Page 5 initially

# set background color
page5.configure(bg='#5CACEE') 

# title label
title_label = tk.Label(page5, text="Contact Us", font=('Helvetica', 16, 'bold'), fg='black', bg='#5CACEE')
title_label.pack(pady=20)

# Function to open websites
def open_website(website_url):
    import webbrowser
    webbrowser.open(website_url)

# Button open website Perodua
button_website1 = tk.Button(page5, text="Get Perodua Now!", command=lambda: open_website(" https://perodua.my"))
button_website1.pack(pady=10)

# Button open website Proton
button_website2 = tk.Button(page5, text="Get Proton Now!", command=lambda: open_website(" https://www.proton.com"))
button_website2.pack(pady=10)

# Button open website Mazda
button_website3 = tk.Button(page5, text="Get Mazda Now!", command=lambda: open_website("https://www.carbase.my/mazda"))
button_website3.pack(pady=10)

# Button open website Honda
button_website4 = tk.Button(page5, text="Get Honda Now!", command=lambda: open_website("https://www.honda.com.my"))
button_website4.pack(pady=10)

# Button open website Toyota
button_website5 = tk.Button(page5, text="Get Toyota Now!", command=lambda: open_website("https://www.toyota.com.my/en/price-and-model-tools/price-list.html"))
button_website5.pack(pady=10)

# Exit button
exit_button = tk.Button(page5, text="Exit", command=root.destroy, bg='red', fg='white')
exit_button.pack(pady=20)

root.mainloop()
