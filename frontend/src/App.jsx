import React, { useState, useEffect } from "react";
import "./App.css";
import Questionnaire from "./components/Questionnaire";
import WorkoutDisplay from "./components/WorkoutDisplay"; // Corrected import
import axios from "axios";

function App() {
  const [started, setStarted] = useState(false);
  const [workoutRoutine, setWorkoutRoutine] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const startQuiz = () => {
    setStarted(true);
  };

  const handleQuestionnaireCompleted = async (answers) => {
    setIsLoading(true);
    try {
      const response = await axios.post(
        "https://workoutbuilder-api.vercel.app/generate_workout",
        answers,
        {
          headers: { "Content-Type": "application/json" },
        }
      );

      if (response.status === 200) {
        setWorkoutRoutine(response.data);
      } else {
        throw new Error("Failed to fetch workout routine");
      }
    } catch (error) {
      setError(error.toString());
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      {!started ? (
        <div className="starttext">
          <h1 className="starttext h1">Create Your Custom Workout Routine!</h1>
          <p>Please click the button below to get started.</p>
          <button className="option-item" onClick={startQuiz}>
            Get Started
          </button>
        </div>
      ) : workoutRoutine ? (
        <WorkoutDisplay workoutRoutine={workoutRoutine} />
      ) : (
        <Questionnaire />
      )}
      {isLoading && <p>Loading...</p>}
      {error && <p>Error: {error}</p>}
    </div>
  );
}

export default App;
