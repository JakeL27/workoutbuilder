from flask import Flask, jsonify, request
from flask_cors import CORS
from builder import MuscleGroup, build_workout_day, day_to_muscle_groups, routine_builder

app = Flask(__name__)
CORS(app, origins='*')
@app.route('/generate_workout', methods=['POST'])
def generate_workout():
    req = request.json
    data = req["data"]
    days = int(data['How many days do you want to spend in the gym?'][0])
    focus = data['What is your focus?']
    difficulty = data['How long have you been going to the gym?']

    if difficulty == "less than 6 months":
        difficulty = "easy"
    else:
        difficulty= "hard"

    workout_plan = routine_builder(days, focus.lower(), difficulty)
    routine = []
    for i in range(len(workout_plan)):
        routine.append(workout_plan[i])

    return jsonify({"routine": routine})

if __name__ == "__main__":
    app.run(debug=True)


