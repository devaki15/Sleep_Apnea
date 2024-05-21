import tkinter as tk
from tkinter import messagebox
import joblib
import pandas as pd

# Load trained model
model = joblib.load('sleep_apnea_model.pkl')

# Function to validate numerical input
def validate_numeric_input(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

# Function to predict sleep disorder based on user input
def detect_sleep_apnea():
    # Get user inputs
    age = entry_age.get()
    heart_rate = entry_heart_rate.get()
    oxygen_level = entry_oxygen_level.get()
    hypertension = entry_hypertension.get()

    # Validate input values
    if not all(validate_numeric_input(val) for val in [age, heart_rate, oxygen_level, hypertension]):
        messagebox.showerror("Error", "Invalid input. Please enter numerical values.")
        return

    # Convert input values to appropriate types
    age = float(age)
    heart_rate = float(heart_rate)
    oxygen_level = float(oxygen_level)
    hypertension = int(hypertension)

    # Create DataFrame with user input
    input_data = pd.DataFrame({
        'Age': [age],
        'HeartRate': [heart_rate],
        'OxygenLevel': [oxygen_level],
        'Hypertension': [hypertension]
    })

    # Make prediction using the model
    prediction = model.predict(input_data)

    # Show prediction result
    if prediction[0] == 2:
        messagebox.showinfo("Prediction Result", "Severe Sleep Apnea detected!\nSuggestions : Consult a sleep specialist immediately. Consider using a CPAP machine.")

    elif prediction[0] == 1:
        messagebox.showinfo("Prediction Result", "Mild Sleep Apnea detected!\nSuggestions :Make lifestyle changes such as losing weight and avoiding sleeping on your back.")
    else:
        messagebox.showinfo("Prediction Result", "No Sleep Apnea detected!\nSuggestions : Maintain a healthy lifestyle")

# Create GUI window
window = tk.Tk()
window.title("Sleep Apnea Detector")

# Set window size
window.geometry("400x300")

# Add input fields and labels
tk.Label(window, text="Age:").grid(row=0, column=0, padx=10, pady=5)
entry_age = tk.Entry(window)
entry_age.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Heart Rate (bpm):").grid(row=1, column=0, padx=10, pady=5)
entry_heart_rate = tk.Entry(window)
entry_heart_rate.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Oxygen Level (%):").grid(row=2, column=0, padx=10, pady=5)
entry_oxygen_level = tk.Entry(window)
entry_oxygen_level.grid(row=2, column=1, padx=10, pady=5)

tk.Label(window, text="Hypertension (0=No, 1=Yes):").grid(row=3, column=0, padx=10, pady=5)
entry_hypertension = tk.Entry(window)
entry_hypertension.grid(row=3, column=1, padx=10, pady=5)

# Add some space before the button
tk.Label(window, text="").grid(row=4, column=0, padx=10, pady=5)

# Add detect button
detect_button = tk.Button(window, text="Detect Sleep Apnea", command=detect_sleep_apnea)
detect_button.grid(row=5, columnspan=2, pady=10)

# Start GUI main loop
window.mainloop()
