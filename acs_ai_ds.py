import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

###########################################################################
# Main Program UI
###########################################################################
           
# Set appearance and theme

# ******** Customize ******** 
# Step 1: choose the appearance and theme
ctk.set_appearance_mode("Dark")  # Options: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # Options: "blue", "dark-blue", "green"

# Create main window
app = ctk.CTk()

# ******** Customize ******** 
# Step 2: add your name in between the "" on the next line
app.title("")

# Set the window size
app.geometry("700x500")

# Create tab view
tabview = ctk.CTkTabview(app, width=680, height=460)
tabview.pack(padx=10, pady=10)

# Add tabs
tabview.add("Advancing Computer Science")
tabview.add("Data Science")
tabview.add("Artificial Intelligence")


###########################################################################
# Computer Science Function
###########################################################################

# This function calculates how long it would take to travel to space based on distance and speed input.
def travel_to_space():

# ******** Customize ******** 
	# Step 1: Get the distance from the user using
	# distance_entry.get()
	# 
	# create a variable and set the value as the distance
	# distance = distance_entry.get()
	
	
	# Step 2: Get the speed from the user using
	# speed_entry.get()
	# 
	# then create a variable and set the value as the distance
	# speed = speed_entry.get()
	
	
	# Step 3: Calculate the time it would take to travel
	# Formula: time = distance / speed

	
	# Step 4: Convert time from hours to days
	# Formula = time_days = time / 24

	
	# Step 5: Print the result 
	time_output_label.configure(text=f"Number of days: {time_days:.2f}")
	


###########################################################################
# Data Science Function
###########################################################################

# Function to display the plot
def show_space_plot():
    # Example space data: average distances from Earth to planets (in millions of km)
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

    fig, axis = plt.subplots(figsize=(6, 4), dpi=100)
    
 # ******** Customize ******** 
	# Step 1: Add the planets and distances to the graph        
    # axis.bar(, , color='skyblue')

  
    # Step 2: Set the title using axis.set_title("")
    # Example text: Average Distance from Earth to Planets
    
    
    # Step 3: Set the y label using axis.set_ylabel("")
    # Example text: Distance (million miles)
    
    
    # Step 4: Set the x label using axis.set_xlabel("")
    # Example text: Planets


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
    # list words: 
    
    # Step 3: add your words here and then remove the #
    # elif any(word in description for word in []):
    
    # Step 4 come up with text to alert the user that they have thought of Earth and add between the "" and remove the #
    #    return ""
    
    else:
        return "I'm not sure... try giving more detail about the object."

        
# Button to classify
def on_classify():
	user_input = description_entry.get()
	result = classify_space_object(user_input)
	result_label.configure(text=result)


###########################################################################
# === Tab: Computer Science ===
###########################################################################

cs_tab = tabview.tab("Advancing Computer Science")

cs_label = ctk.CTkLabel(cs_tab, text="Welcome to Computer Science!", font=("Segoe UI", 16))
cs_label.pack(pady=20)

cs_subheading = ctk.CTkLabel(cs_tab, text="Calculate the time needed to travel to space", font=("Segoe UI", 14, "bold"))
cs_subheading.pack(pady=(20, 10))

# Distance input
distance_label = ctk.CTkLabel(cs_tab, text="Enter Distance (km):")
distance_label.pack(pady=(20, 5))
distance_entry = ctk.CTkEntry(cs_tab, width=200)
distance_entry.pack()

# Speed input
speed_label = ctk.CTkLabel(cs_tab, text="Enter Speed (km/h):")
speed_label.pack(pady=(20, 5))
speed_entry = ctk.CTkEntry(cs_tab, width=200)
speed_entry.pack()

# Output label
time_output_label = ctk.CTkLabel(cs_tab, text="")
time_output_label.pack(pady=10)

# Calculate button
calc_button = ctk.CTkButton(cs_tab, text="Calculate Time", command=travel_to_space)
calc_button.pack(pady=10)

###########################################################################
# === Tab: Data Science ===
###########################################################################

ds_tab = tabview.tab("Data Science")

ds_label = ctk.CTkLabel(ds_tab, text="Welcome to Data Science!", font=("Segoe UI", 16))
ds_label.pack(pady=10)

plot_label = ctk.CTkLabel(ds_tab, text="Click below to view distances to planets", font=("Segoe UI", 14))
plot_label.pack(pady=5)

# Button to trigger plot creation
plot_button = ctk.CTkButton(ds_tab, text="Show Plot", command=show_space_plot)
plot_button.pack(pady=10)


###########################################################################
# === Tab: AI ===
###########################################################################

ai_tab = tabview.tab("Artificial Intelligence")

ai_label = ctk.CTkLabel(ai_tab, text="Welcome to Artificial Intelligence!", font=("Segoe UI", 16))
ai_label.pack(pady=20)

    
# Instruction label
label = ctk.CTkLabel(ai_tab, text="Describe a space object, and I'll guess what it is!")
label.pack(pady=10)

# Entry box
description_entry = ctk.CTkEntry(ai_tab, width=400, placeholder_text="e.g., I am cold and have many rings")
description_entry.pack(pady=10)

# Result label
result_label = ctk.CTkLabel(ai_tab, text="")
result_label.pack(pady=10)

classify_button = ctk.CTkButton(ai_tab, text="Classify Space Object", command=on_classify)
classify_button.pack(pady=10)       




# Run the application
app.mainloop()
