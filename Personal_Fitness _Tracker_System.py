

# Personal Fitness Tracker System 🏋️‍♂️

# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal


def log_workout(workout_type, duration):
    """
    Log a workout.
    - Append the workout type and duration to the workouts list.
    - Print a confirmation message.
    """
    if duration > 0:
        workouts.append((workout_type, duration))
        print(f"Logged: {workout_type} for {duration} minutes.")
    else:
        print("Duration must be a positive number.")


def log_calorie_intake(calories_consumed):
    """
    Log calorie intake for a meal.
    - Append the calorie amount to the calories list.
    - Print a confirmation message.
    """
    if calories_consumed > 0:
        calories.append(calories_consumed)
        print(f"Logged: {calories_consumed} calories.")
    else:
        print("Calorie intake must be a positive number.")


def view_progress():
    """
    Display a summary of the user's progress for the day.
    - Calculate the total workout time and total calories.
    - Print motivational feedback.
    """
    total_workout = sum(duration for _, duration in workouts)
    total_calories = sum(calories)

    print("\n---- Daily Progress ----")
    print(f"Total Workout Time: {total_workout} minutes")
    print(f"Total Calorie Intake: {total_calories} calories")

    if workout_goal > 0:
        if total_workout >= workout_goal:
            print("Great job! You've met your workout goal! 🏆")
        else:
            print(f"Keep going! You're {workout_goal - total_workout} minutes away from your workout goal.")

    if calorie_goal > 0:
        if total_calories >= calorie_goal:
            print("Well done! You're within your calorie goal! 🎉")
        else:
            print(f"Watch out! You've exceeded your calorie goal by {total_calories - calorie_goal} calories.")


def reset_progress():
    """
    Clear all data from the workouts and calories lists.
    - Print a confirmation message.
    """
    global workouts, calories
    workouts.clear()
    calories.clear()
    print("Progress has been reset for the day.")


def set_daily_goals(workout_minutes, calorie_limit):
    """
    Set daily goals for workout time and calorie intake.
    - Update the global variables workout_goal and calorie_goal.
    - Print a confirmation message.
    """
    global workout_goal, calorie_goal

    if workout_minutes >= 0 and calorie_limit >= 0:
        workout_goal = workout_minutes
        calorie_goal = calorie_limit
        print(f"Daily goals set: {workout_goal} minutes workout, {calorie_goal} calories.")
    else:
        print("Goals must be non-negative numbers.")


def encouragement_system():
    """
    Provide motivational feedback based on progress and goals.
    - Compare current totals to the daily goals.
    - Print encouragement messages.
    """
    total_workout = sum(duration for _, duration in workouts)
    total_calories = sum(calories)

    print("\n---- Encouragement System ----")

    if total_workout >= workout_goal and total_workout > 0:
        print("Amazing! You've smashed your workout goal today! Keep it up! 💪")
    elif workout_goal > 0:
        print(f"Just {workout_goal - total_workout} more minutes to reach your goal! You got this! 🏃")

    if total_calories <= calorie_goal and total_calories > 0:
        print("Great control on your diet! You're on track with your calorie goal! 🎉")
    elif calorie_goal > 0:
        print(f"Try to balance your next meals to stay within your goal. You're {total_calories - calorie_goal}"
              f" calories over.")


def main():
    """
    Main function to interact with the user.
    """
    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")

    while True:
        # Display menu options
        print("\n1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Encouragement System")
        print("7. Exit")

        # Prompt user for their choice
        choice = input("\nEnter your choice: ")

        if choice == '1':
            # Prompt for workout type and duration
            workout_type = input("Enter workout type (e.g., Running): ")
            try:
                duration = int(input("Enter duration in minutes: "))
                log_workout(workout_type, duration)
            except ValueError:
                print("Invalid input. Please enter a number for duration.")

        elif choice == '2':
            # Prompt for calories consumed
            try:
                calories_consumed = int(input("Enter calories consumed: "))
                log_calorie_intake(calories_consumed)
            except ValueError:
                print("Invalid input. Please enter a number for calories.")

        elif choice == '3':
            # Call view_progress function
            view_progress()

        elif choice == '4':
            # Call reset_progress function
            reset_progress()

        elif choice == '5':
            # Prompt for daily goals
            try:
                workout_minutes = int(input("Enter daily workout goal in minutes: "))
                calorie_limit = int(input("Enter daily calorie intake goal: "))
                set_daily_goals(workout_minutes, calorie_limit)
            except ValueError:
                print("Invalid input. Please enter numbers for the goals.")

        elif choice == '6':
            # Call encouragement system
            encouragement_system()

        elif choice == '7':
            # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
