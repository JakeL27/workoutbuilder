class MuscleGroup:
    def __init__(self, name):
        self.name = name
        self.strength= {'easy' : [], 'hard': []}
        self.hypertrophy = {'easy' : [], 'hard': []}

class WorkoutDay:
    def __init__(self, name, muscle_groups):
        self.name = name
        self.muscle_groups = muscle_groups 

#Define all muscle Groups
back_h = MuscleGroup("back_h")
back_h.strength['easy'] = [

    ("meadow row", "Make sure to keep your back straight and don't shrug your shoulders!"),
    ("chest supported row", "Make sure you set your shoulders and keep your back straight. Don't shrug your shoulders!"),
    ("machine t-bar row", "Make sure you keep your back straight and chest to the pad!")
]
back_h.hypertrophy['easy'] = [

    ("seated cable row", "Keep your chest and head up and make sure to go slow on the way down!"),
    ("chest supported machine row", "make sure to set your shoulders and avoid shrugging throughout.")
]
back_h.strength['hard'] = [

    ("meadow row", "Make sure to keep your back straight and don't shrug your shoulders!"),
    ("chest supported row", "Make sure you set your shoulders and keep your back straight. Don't shrug your shoulders!"),
    ("machine t-bar row", "Make sure you keep your back straight and chest to the pad!")
]
back_h.hypertrophy['hard'] = [

    ("seated cable row", "Keep your chest and head up and make sure to go slow on the way down!"),
    ("chest supported machine row", "make sure to set your shoulders and avoid shrugging throughout.")
]

back_v = MuscleGroup("back_v")
back_v.strength['easy'] = [

    ("assisted pullups", "Remember to pull toward your chest and keep your back straight"),
    ("lat pulldown", "Remember to pull toward your chest and keep your back straight")
]
back_v.hypertrophy['easy'] = [

    ("lat pulldown", "Remember to pull toward your chest and keep your back straight"),
    ("machine lat pulldown", "Remember to pull toward your chest and keep your back straight"),
    ("assisted pullups" "Remember to pull toward your chest and keep your back straight")
]
back_v.strength['hard'] = [

    ("assisted pullups", "Remember to pull toward your chest and keep your back straight"),
    ("lat pulldown", "Remember to pull toward your chest and keep your back straight")
]
back_v.hypertrophy['hard'] = [

    ("lat pulldown", "Remember to pull toward your chest and keep your back straight"),
    ("machine lat pulldown", "Remember to pull toward your chest and keep your back straight"),
    ("assisted pullups" "Remember to pull toward your chest and keep your back straight")
]

chest_compound = MuscleGroup("chest_compound")
chest_compound.strength['easy'] = [

    ("bench press", "plant your feet, pin your shoulders into the bench, and think about pushing yourself away from the bar"),
    ("push-ups", "Don't flare your elbows, make sure your arms are within ~45 degrees of your torso"),
    ("dips", "on the way down, take it slow and make sure to get a full range of motion.")
]
chest_compound.strength['hard'] = [

    ("bench press", "plant your feet, pin your shoulders into the bench, and think about pushing yourself away from the bar"),
    ("push-ups", "Don't flare your elbows, make sure your arms are within ~45 degrees of your torso"),
    ("dips", "on the way down, take it slow and make sure to get a full range of motion.")
]
chest_compound.hypertrophy['easy'] = [

    ("dumbbell bench press", "try not to arch your back too much. Ensure a full range of motion"),
    ("machine press", "plant your feet and ensure a full range of motion"),
    ("push-ups", "Don't flare your elbows, make sure your arms are within ~45 degrees of your torso")
]
chest_compound.hypertrophy['hard'] = [

    ("dumbbell bench press", "try not to arch your back too much. Ensure a full range of motion"),
    ("machine press", "plant your feet and ensure a full range of motion"),
    ("push-ups", "Don't flare your elbows, make sure your arms are within ~45 degrees of your torso")
]

chest_iso = MuscleGroup("chest_iso")
chest_iso.hypertrophy['easy'] = [

    ("peck deck", "ensure full range of motion."),
    ("machine cable fly", "when opening your arms, think about tearing something apart.")
]

chest_iso.hypertrophy['hard'] = [

   ( "cable fly", "when opening your arms, think about tearing something apart.")
]

front_delt = MuscleGroup("front_delt")
front_delt.strength['easy'] = [

    ("machine shoulder press", "try not to arch your back too much.")
]
front_delt.hypertrophy['easy'] = [

    ("dumbbell shoulder press", "try not to arch your back too much. Do it sitting or standing based on preference."),
    ("machine shoulder press", "try not to arch your back too much.")
]

front_delt.strength['hard'] = [

    ("barbbell shoulder press", "Brace before performing each rep by flexing your core - as if you're expecting a punch!")
]
front_delt.hypertrophy['hard'] = [

    ("front raises", "Ensure slow and controlled movement with every rep."),
    ("landmine press", "Use lower weights and focus on volume and control.")
]
rear_delt = MuscleGroup('rear_delt')
rear_delt.hypertrophy['hard'] = [

    ("reverse pec deck", "Ensure slow and controlled movements."),
    ("single arm reverse fly", "remember to keep your elbow fixed!")
]
rear_delt.hypertrophy['easy'] = [

   ( "cable reverse fly", "Ensure slow and controlled movements."),
    ("dumbbell reverse fly", "Ensure slow and controlled movements.")
]
lateral_delt = MuscleGroup('latera_delt')
lateral_delt.hypertrophy['easy'] = [

    ("machine lateral raise", "Ensure slow and controlled movements.")
]
lateral_delt.hypertrophy['hard'] = [

    ("dumbbell lateral raise", "raise your arms as if you're pouring a glass of water from up high. Lean forwards slightly and try not to shrug!"),
    ("cable lateral raise", "Ensure slow and controlled movements."),
]
lateral_delt.strength['easy'] = [

    ("dumbbell lateral raise", "raise your arms as if you're pouring a glass of water from up high. Lean forwards slightly and try not to shrug!"),
    ("cable lateral raise", "Ensure slow and controlled movements."),
]
lateral_delt.strength['hard'] = [

    ("dumbbell lateral raise", "raise your arms as if you're pouring a glass of water from up high. Lean forwards slightly and try not to shrug!"),
    ("cable lateral raise", "Ensure slow and controlled movements."),
]
biceps = MuscleGroup('biceps')
biceps.strength['easy'] = [

    ("ez bar curl", "Ensure slow and controlled movements."),
   ("single arm dumbbell preacher curl", "Ensure slow and controlled movements."),
]
biceps.hypertrophy['easy'] = [

    ("incline dumbbell curl", "Ensure your elbows are the only pivot point."),
    ("ez bar curl", "Ensure slow and controlled movements."),
    ("cable curl", "To make this a preacher curl, place your arms in front of you."),
    ("machine preacher curl", "Ensure slow and controlled movements.")
]
triceps = MuscleGroup('triceps')
triceps.strength['easy'] = [
    ("tricep dips", "Ensure a full range of motion!"),
    ("close grip bench press", "To increase difficulty, add a 1 second pause between each rep."),
    ("diamond push-ups", "To increase difficulty, place hands closer together and further down towards your hip")
]
triceps.hypertrophy['easy'] = [

    ("tricep pushdowns", "Ensure slow and controlled movements."),
    ("scull crushers", "This can be done with any free weight."),
    ("overhead tricep extentions", "This can be done with both a cable or free weight.")
]
triceps.strength['hard'] = [
    ("tricep dips", "Ensure a full range of motion!"),
    ("close grip bench press", "To increase difficulty, add a 1 second pause between each rep."),
    ("diamond push-ups", "To increase difficulty, place hands closer together and further down towards your hip")
]
triceps.hypertrophy['hard'] = [

    ("tricep pushdowns", "Ensure slow and controlled movements."),
    ("scull crushers", "This can be done with any free weight."),
    ("overhead tricep extentions", "This can be done with both a cable or free weight.")
]
quads = MuscleGroup('quads')
quads.hypertrophy['hard'] = [

    ("quad extention", "Each rep should be performed slowly, especially on the way down."),
    ("leg press", "Ensure your hip does not come off the pad. This is to prevent injury")
]
hams = MuscleGroup('hams')
hams.hypertrophy['easy'] = [

    ("leg curl", "There is no difference between the seated and laying verison. Choose basd on preference.")
]
hams.hypertrophy['hard'] = [

    ("leg curl", "There is no difference between the seated and laying verison. Choose basd on preference.")
]
hams.strength['easy'] = [

    ("leg curl", "There is no difference between the seated and laying verison. Choose basd on preference.")
]

hams.strength['hard'] = [

    ("romanian deadlifts", "To train explosive power, let the bar rest on the ground between each rep.")
]
glutes = MuscleGroup('glutes')
glutes.hypertrophy['easy'] = [

    ("single leg leg press", "Place your foot high up to really target the glutes."),
    ("glute kickback machine", "Start with your non-dominant leg to avoid muscle imbalance."),
    ("bulgarian split squats", "Perform reps slowly and ensure a full range of motion.")
]
glutes.hypertrophy['hard'] = [

    ("single leg leg press", "Place your foot high up to really target the glutes."),
    ("glute kickback machine", "Start with your non-dominant leg to avoid muscle imbalance."),
    ("bulgarian split squats", "Perform reps slowly and ensure a full range of motion.")
]
glutes.strength['easy'] = [

    ("weighted lunges", "Can be done with either dumbbells/kettlebells or a barbbell over the shoulder.")
]
glutes.strength['hard'] = [

    ("weighted lunges", "Can be done with either dumbbells/kettlebells or a barbbell over the shoulder.")
]
calves = MuscleGroup("calves")
calves.hypertrophy['easy'] = [

    ("standing calf raises", "To increase difficulty, add a pause between each rep."),
    ("seated calf raises", "To increase difficulty, add a pause between each rep."),
]
leg_compound = MuscleGroup("leg_compound")
leg_compound.hypertrophy['easy'] = [

    ("smith machine squat", "Make sure to balance the weight on the heels and balls of your feet."),
    ("hack squat", "Make sure your back stays on the pad throughout the entire exercise."),
]
leg_compound.hypertrophy['hard'] = [

    ("smith machine squat", "Make sure to balance the weight on the heels and balls of your feet."),
    ("hack squat", "Make sure your back stays on the pad throughout the entire exercise."),
]
leg_compound.strength['hard'] = [

    ("barbbell squat", "Make sure your knees don't go over your toes and are not narrorwer than your feet.")
]
leg_compound.strength['easy'] = [

   ("smith machine squat", "Make sure to balance the weight on the heels and balls of your feet.")
]

day_to_muscle_groups = {
    "upper": {
        "strength": [back_h, back_v, chest_compound, lateral_delt], 
        "hypertrophy": [back_v, back_h, chest_compound, chest_iso, lateral_delt],
    },
    "lower": {
        "strength": [leg_compound, hams, calves],
        "hypertrophy": [leg_compound, hams, quads, glutes, calves],
    },
    "push": {
        "strength": [chest_compound, triceps, front_delt,lateral_delt],
        "hypertrophy": [chest_compound, triceps, chest_iso,lateral_delt],
    },
    "pull": {
        "strength": [back_h, back_v, biceps],
        "hypertrophy": [back_h, back_v, biceps, rear_delt],
    }
    }