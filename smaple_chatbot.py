# input
name = input("Hello User! Welcome to our Mini FitBoT \nPlease enter your name: ")
print(f"Nice to meet you {name}")
print(f"Please give me some basic information for your diet plan, {name}")

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# BMI Function
def bmi_fun(height, weight):
    bmi = weight / height**2

    if bmi < 18.5:
        print(f'''Not bad {name}, you are underweight. Focus on eating nutritious, calorie-rich foods like eggs, 
        nuts, whole grains, and fruits, and eat small meals every 2–3 hours. Combine this with strength training exercises 
        like push-ups, squats, and light weights to build muscle. Also, stay hydrated, sleep well, and be consistent for healthy weight gain.
        so if you want to gain weight i will  help you by choosing the below statement
        which one you want 
        1.diet plan
        2.workout plan (hard)
        3.Yoga plan for flexibility''')

    elif bmi <= 24.9:
        print(f'''Good {name}, your weight is normal. Focus on maintaining a balanced diet with proteins,
         carbs, healthy fats, fruits, and vegetables. Exercise regularly with a mix of strength training and cardio
          to stay fit and healthy. Also, drink enough water, get proper sleep, and keep a consistent routine to maintain your weight.
          so if you want to gain weight i will  help you by choosing the below statement
        which one you want 
        1.diet plan
        2.workout plan (hard)
        3.Yoga plan for flexibility ''')

    elif bmi <= 29.9:
        print(f'''{name}, you are overweight. Focus on eating a balanced, 
        low-calorie diet with plenty of vegetables, fruits, lean proteins, 
        and whole grains while avoiding sugary and fried foods. Exercise regularly with a mix of cardio and strength 
        training to burn fat and build muscle. Also, stay hydrated, get enough sleep, and maintain consistency for healthy weight loss.''')

    else:  # bmi >= 30
        print(f'''{name}, you are obese. It’s important to follow a healthy,
         low-calorie diet rich in vegetables, fruits, lean proteins, and whole grains while avoiding 
         sugary and fried foods. Regular exercise, including both cardio and strength training, 
         is essential to burn fat and improve fitness. Also, stay hydrated, get enough sleep, and maintain a 
         consistent healthy routine to reduce health risks.
         so if you want to gain weight i will  help you by choosing the below statement
        which one you want 
        1.diet plan
        2.workout plan (hard)
        3.Yoga plan for flexibility''')

# Call the function with proper arguments
bmi_fun(height, weight)

choice = int( input("Enter your choice(1/2/3): "))
if choice == "1":
    print("Great! Here's a sample Diet Plan for you:")
    print("""
    - Early Morning: Milk + 5-6 soaked almonds
    - Breakfast: 3-4 eggs + oats with fruits
    - Mid-Morning Snack: Banana or nuts
    - Lunch: 150-200g grilled chicken/fish/paneer + rice/chapati + vegetables
    - Evening Snack: Smoothie with milk, banana, peanut butter
    - Dinner: Grilled protein + chapati/rice + vegetables
    - Before Bed: Warm milk with almonds
    """)

elif choice == "2":
    print("Awesome! Here's a Hard Workout Plan for you:")
    print("""
- Monday: Full body strength training (squats, push-ups, pull-ups)
- Tuesday: Cardio (running/cycling) 30-45 mins
- Wednesday: Rest or light activity
- Thursday: Strength training (chest, arms, shoulders)
- Friday: Cardio + core exercises
- Saturday: Legs & back strength training
- Sunday: Rest or light yoga/stretching
""")
elif choice == "3":
    print("Great! Here's a Yoga Plan for Flexibility:")
    print("""
- Morning: Sun Salutation (5 rounds)
- Cat-Cow Stretch (10 reps)
- Downward Dog (hold 30 sec)
- Cobra Pose (hold 20-30 sec)
- Seated Forward Bend (hold 30 sec)
- Evening: Gentle stretching & deep breathing
""")
else:
    print("Invalid choice! Please select 1, 2, or 3.")

print()



