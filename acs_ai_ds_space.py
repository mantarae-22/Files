# Configuration Code - Skip ahead to Main Program UI
import importlib
import subprocess
import sys

# List of required packages
required_packages = ["customtkinter", "matplotlib"]

# Function to check and install missing packages
def install_if_missing(package):
    try:
        importlib.import_module(package)
    except ImportError:
        print(f"{package} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check all required packages
for pkg in required_packages:
    install_if_missing(pkg)

import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

###########################################################################
# Main Program UI
###########################################################################
           
# Set appearance and theme

# ******** Customize ******** 
# Step 1: choose the appearance and theme
# Example: ctk.set_appearance_mode("Dark")
ctk.set_appearance_mode("Dark")  # Options: "Light", "Dark", "System"

# Example: ctk.set_appearance_mode("blue")
ctk.set_default_color_theme("blue")  # Options: "blue", "dark-blue", "green"

# Create main window
app = ctk.CTk()

# ******** Customize ******** 
# Step 2: choose a title for the app
# Example: app.title("Tony's Space App")
app.title("") # add your name and a space-themed title for the app in between the ""

# Set the window size
app.geometry("900x700")

# Create tab view
tabview = ctk.CTkTabview(app, width=880, height=660)
tabview.pack(padx=10, pady=10)

# Add tabs
tabview.add("Advancing Computer Science")
tabview.add("Data Science")
tabview.add("Artificial Intelligence")


###########################################################################
# Computer Science Function
###########################################################################

# This function calculates how long it would take to travel to space based on distance and speed input.
def cs_calc_travel_to_space():
    # ******** Customize ********

	# Step 1: Get the distance that the user entered using txt_cs_distance.get()
	# create a variable and set the value as the distance and convert it to a whole number (int)
    #distance = int(txt_cs_distance.get())

    # Step 2: Get the speed that the user entered using txt_cs_speed.get()
	# create a variable and set the value as the distance and convert it to a whole number (int)
    #speed = int(txt_cs_speed.get())

	# Step 3: Calculate the time it would take to travel using the formula: time = distance / speed
    #time_hours = distance / speed

	# Step 4: Convert time from hours to days using the formula = time_days = time / 24
    #time_days = time_hours / 24
	
	# Step 5: Print the result on the label on the form
    lbl_cs_time_output.configure(text=f"Number of days: {time_days:.2f}")


###########################################################################
# Data Science Function
###########################################################################

# Function to display the graph
def ds_build_space_graph():
    # Space data to graph: average distances from Earth to planets (in millions of km)
    planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    distances_miles = [
        48.0,      # Mercury
        25.7,      # Venus
        48.7,      # Mars
        390.7,     # Jupiter
        793.3,     # Saturn
        1692.7,    # Uranus
        2702.7,    # Neptune
        3648.3     # Pluto
    ]

    # create the plot and set the size
    fig, axis = plt.subplots(figsize=(8, 6), dpi=100)
    
 # ******** Customize ******** 
	# Step 1: Customize the color of the bars on the graph 
	# Example: axis.bar(planets, distances_miles, color="blue")
    axis.bar(planets, distances_miles, color="")
  
    # Step 2: Set the title using axis.set_title("")    
    # Example: axis.set_title("Average Distance from Earth to Planets")
    axis.set_title("")
    
    # Step 3: Set the y label using axis.set_ylabel("")    
    # Example: axis.set_ylabel("Distance (million miles)")
    axis.set_ylabel("")
    
    # Step 4: Set the x label using axis.set_xlabel("")    
    # Example: axis.set_xlabel("Planets")
    axis.set_xlabel("")

    # Embed the plot in the tab
    canvas = FigureCanvasTkAgg(fig, master=ds_tab)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)


###########################################################################
# Artificial Intelligence Function
###########################################################################

def classify_space_object(description):
    description = description.lower()
# ******** Customize ********   
    # Step 1 - read through descriptive lists

    # Dictionaries of keywords that describe each planet
    if any(word in description for word in ["rings", "ice giant", "cold", "yellow", "titan"]):
        return "You're probably thinking of Saturn!"
    
    elif any(word in description for word in ["red", "dust", "iron", "rovers", "olympus", "dry", "thin atmosphere"]):
        return "That sounds like Mars!"
    
    elif any(word in description for word in ["gas", "largest", "storm", "jovian", "great red spot", "many moons"]):
        return "Could it be Jupiter?"
    
    elif any(word in description for word in ["blue", "methane", "cold", "far", "ice"]):
        return "Maybe you're describing Neptune or Uranus!"
    
    elif any(word in description for word in ["craters", "lunar", "grey", "orbit earth", "tides"]):
        return "Sounds like Earth's Moon!"
    
    elif any(word in description for word in ["hot", "bright", "plasma", "core", "fusion", "light", "sun"]):
        return "You're probably describing the Sun!"
    
    elif any(word in description for word in ["burning", "nuclear", "dying", "red giant", "supernova", "nebula"]):
        return "Sounds like you're talking about a star!"
    
    elif any(word in description for word in ["rocky", "closest", "venus", "hellish", "toxic"]):
        return "Possibly Venus!"
    
    elif any(word in description for word in ["smallest", "closest", "speed", "mercury"]):
        return "Maybe it's Mercury!"
    
    elif any(word in description for word in ["galaxy", "billions", "spiral", "milky way", "cluster"]):
        return "You're thinking on a galactic scale! That must be a galaxy."
    
    elif any(word in description for word in ["belt", "asteroids", "rocky debris", "between mars and jupiter"]):
        return "You’re probably thinking of the Asteroid Belt."
    
    elif any(word in description for word in ["ice", "tail", "orbit sun", "dirty snowball", "comet"]):
        return "That sounds like a comet!"
# ******** Customize ********        
    # Step 2 - think of words that describe Earth and list them here
    # Example list of words: "ocean", "trees", "cities"
    
    # Step 3: add your words here and then remove the #
    # Example: elif any(word in description for word in ["ocean", "trees", "cities"]):
    #elif any(word in description for word in []):
    
    # Step 4 come up with text to alert the user that they have thought of Earth and add between the "" and remove the #
    #	 Example: return "You must be thinking of Earth!"
    #    return ""
    
    else:
        return "I'm not sure... try giving more detail about the object."

        
# Button to classify
def ai_classify():
    user_input = txt_ai_question.get()
    result = classify_space_object(user_input)
    lbl_ds_result.configure(text=result)


###########################################################################
# === Tab: Computer Science ===
###########################################################################

# tab text
cs_tab = tabview.tab("Advancing Computer Science")

# form title
lbl_cs_info_title = ctk.CTkLabel(cs_tab, text="Welcome to Computer Science!", font=("Segoe UI", 16))
lbl_cs_info_title.pack(pady=20)

# subheading title
lbl_cs_info_subheading = ctk.CTkLabel(cs_tab, text="Calculate the time needed to travel to space", font=("Segoe UI", 14, "bold"))
lbl_cs_info_subheading.pack(pady=(20, 10))

# Distance input label
lbl_cs_distance = ctk.CTkLabel(cs_tab, text="Enter Distance (miles):")
lbl_cs_distance.pack(pady=(20, 5))
# Distance input text
txt_cs_distance = ctk.CTkEntry(cs_tab, width=200)
txt_cs_distance.pack()

# Speed input label
lbl_cs_speed = ctk.CTkLabel(cs_tab, text="Enter Speed (miles/hour):")
lbl_cs_speed.pack(pady=(20, 5))
# Speed input text
txt_cs_speed = ctk.CTkEntry(cs_tab, width=200)
txt_cs_speed.pack()

# Output Time Result label
lbl_cs_time_output = ctk.CTkLabel(cs_tab, text="")
lbl_cs_time_output.pack(pady=10)

# Calculate Time button
btn_cs_calc = ctk.CTkButton(cs_tab, text="Calculate Time", command=cs_calc_travel_to_space)
btn_cs_calc.pack(pady=10)

###########################################################################
# === Tab: Data Science ===
###########################################################################

ds_tab = tabview.tab("Data Science")

# form title
lbl_ds_info_title = ctk.CTkLabel(ds_tab, text="Welcome to Data Science!", font=("Segoe UI", 16))
lbl_ds_info_title.pack(pady=10)

# subheading title
lbl_ds_info_subheading = ctk.CTkLabel(ds_tab, text="Click below to view distances to other planets from Earth", font=("Segoe UI", 14))
lbl_ds_info_subheading.pack(pady=5)

# Button to trigger plot creation
btn_ds_plot = ctk.CTkButton(ds_tab, text="Show Graph", command=ds_build_space_graph)
btn_ds_plot.pack(pady=10)


###########################################################################
# === Tab: AI ===
###########################################################################

ai_tab = tabview.tab("Artificial Intelligence")

# form title
lbl_ai_info_title = ctk.CTkLabel(ai_tab, text="Welcome to Artificial Intelligence!", font=("Segoe UI", 16))
lbl_ai_info_title.pack(pady=20)

# subheading title
lbl_ai_info_subheading = ctk.CTkLabel(ai_tab, text="Describe a space object, and I'll guess what it is!")
lbl_ai_info_subheading.pack(pady=10)

# entry box for user's guess
txt_ai_question = ctk.CTkEntry(ai_tab, width=400, placeholder_text="e.g., I am cold and have many rings")
txt_ai_question.pack(pady=10)

# result label
lbl_ds_result = ctk.CTkLabel(ai_tab, text="")
lbl_ds_result.pack(pady=10)

# button to guess the planet
btn_ds_classify = ctk.CTkButton(ai_tab, text="Classify Space Object", command=ai_classify)
btn_ds_classify.pack(pady=10)


# Run the application
app.mainloop()
