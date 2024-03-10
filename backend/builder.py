from Exercises import MuscleGroup, day_to_muscle_groups, WorkoutDay

#takes in the training day (based on how many days they want to be in the gym)
#focus is given by user
#difficulty calculated based on user input
#this function is used to create the exercises for a single day with the 
#function routine_builder() which makes every day needed in a split
def build_workout_day(training_day, focus, difficulty):
    muscle_groups = day_to_muscle_groups[training_day][focus]
    workout_day = []
    workout_alts = []
    subsitude = []

    if focus == "strength":
        for group in muscle_groups:
            if(len(group.strength[difficulty]) != 0):
                workout_day.append((group.strength[difficulty][0]))
            if(len(group.strength[difficulty]) > 1):
                subsitude.append(group.strength[difficulty][1:][0])
                workout_alts.append(subsitude)
                subsitude = []
            else:
                workout_alts.append(([]))
    else:
        for group in muscle_groups:
            if(len(group.hypertrophy[difficulty]) != 0):
                workout_day.append((group.hypertrophy[difficulty][0]))
            if(len(group.hypertrophy[difficulty]) > 1):
                subsitude.append(group.hypertrophy[difficulty][1:][0])
                workout_alts.append(subsitude)
                subsitude = []
            else:
                workout_alts.append(([]))
    return (workout_day, workout_alts)

#converts the user's input and feeds into builder_workout_day() and then 
#creates the schedule for every day of the split
def routine_builder(days, focus, difficulty):
    workout_plan = []
    if days == 4:
        for i in range(4):
            if i == 0 or i == 2:
                day = build_workout_day('upper', focus, difficulty)
            elif i == 1 or i == 3:
               day = build_workout_day("lower", focus, difficulty)
            workout_plan.append(day)
    elif days == 5:
        day1 = build_workout_day("push", focus, difficulty)
        workout_plan.append(day1)
        day2 = build_workout_day("pull", focus, difficulty)
        workout_plan.append(day2)
        day3 = build_workout_day("lower", focus, difficulty)
        workout_plan.append(day3)
        day4 = build_workout_day("upper", focus, difficulty)
        workout_plan.append(day4)
        day5 = build_workout_day("lower", focus, difficulty)
        workout_plan.append(day5)
    elif days == 6:
        for i in range(6):
            if i == 0 or i == 3:
                day = build_workout_day('push', focus, difficulty)
            elif i == 1 or i == 4:
                day = build_workout_day('pull', focus, difficulty)
            elif i == 2 or i == 5:
                day = build_workout_day('lower', focus, difficulty)
            workout_plan.append(day)
            
    return workout_plan

print(routine_builder(5, 'strength', 'hard'))