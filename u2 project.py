# Food classification program with user interaction

# Food categories stored in a lists to show what it's impact is
food_data = {
    "High impact": ["beef", "burger", "fried chicken", "chocolate"],
    "Medium impact": ["pizza", "pasta", "ice cream", "tacos", "chicken"],
    "Low impact": ["vegetables", "rice", "bread"],
    "Variable impact": ["fish", "sushi"]
}
print("Welcome to Abdullahs food  ")
# Boolean variable to control the loop of when your exitting or not
keep_running = True

while keep_running:
    food = input("Enter a food item (or type 'exit' to quit): ").lower()

    # Check for exit condition to know if person is breakin gout of the loop
    if food == "exit":
        print("Exiting the program. Have a great day!")
        keep_running = False
        break

    classification = None

#
    for impact, foods in food_data.items():
        if food in foods:
            classification = impact
            break

# Using if-elif statements for classification messages
    if classification:
        print(f"Classification: {classification}")

        if classification == "High impact":
            print("Tip: Consider reducing the amount of times you take this food to lower environmental effects.")
        elif classification == "Medium impact":
            print("Tip: Lower this in your diet for a smaller footprint.")
        elif classification == "Low impact":
            print("Tip: Great choice! Plant based options are eco friendly try use these more.")
        elif classification == "Variable impact":
            print("Tip: Choose sustainably sourced options when possible.")

        # Example of different data types: int, float, string, boolean
        impact_level = {"High impact": 3, "Medium impact": 2, "Low impact": 1, "Variable impact": 2.5}
        level = impact_level.get(classification, 0)
        print(f"Environmental Impact Level: {level} (Scale: 1-Low, 3-High)")











    else:
        print("Food item not found in our database. Try another or try consider researching its impact!")