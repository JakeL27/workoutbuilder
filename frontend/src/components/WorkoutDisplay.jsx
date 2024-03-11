import React, { useState, useEffect } from "react";
import axios from "axios";

function Questionnaire() {
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState({});
  const [completed, setCompleted] = useState(false);
  const [loadingPercentage, setLoadingPercentage] = useState(0);
  const [response, setResponse] = useState([]);

  const questions = [
    {
      text: "What is your focus?",
      options: ["Strength", "Hypertrophy"],
    },
    {
      text: "How many days do you want to spend in the gym?",
      options: ["4 days", "5 days", "6 days"],
    },
    {
      text: "How long have you been going to the gym?",
      options: ["less than 6 months", "less than 1 year", "1 year or more"],
    },
  ];

  const delay = (duration) => new Promise((resolve) => setTimeout(resolve, duration));

  const updateLoadingProgress = async () => {
    for (let progress = 0; progress <= 100; progress += 20) {
      setLoadingPercentage(progress);
      await delay(50);
    }
  };

  const handleSubmit = async () => {
    setCompleted(true);
    updateLoadingProgress(); // Start updating loading progress

    await delay(2000);
    try {
      const { data } = await axios.post(
        "http://127.0.0.1:5000/generate_workout",
        { data: answers }
      );
      console.log(data);
      setResponse(data); // Assuming data is the entire workout plan
    } catch (error) {
      console.error("Error submitting form:", error);
    }

    setCompleted(false);
    setLoadingPercentage(0);
  };

  const handleOptionClick = (option) => {
    setAnswers({ ...answers, [questions[currentQuestionIndex].text]: option });
    setCurrentQuestionIndex((prev) => prev + 1);
  };

  useEffect(() => {
    if (currentQuestionIndex === questions.length) {
      handleSubmit();
    }
  }, [currentQuestionIndex]);

  const renderDayExercises = (exercises, alternatives) => {
    return (
      <div className="day-exercises">
        <div className="exercises">
          {exercises.map((exercise, index) => (
            <p key={`exercise-${index}`}>{exercise}</p>
          ))}
        </div>
      </div>
    );
  };

  if (completed) {
    return (
      <div className="centered-message">
        <div className="starttext">Generating Your Routine...</div>
        <div className="loading-bar-container">
          <div
            className="loading-bar-fill"
            style={{ width: `${loadingPercentage}%` }}
          ></div>
        </div>
      </div>
    );
  }

  return (
    <div className="questionnaire">
      {currentQuestionIndex < questions.length ? (
        <div className="question-section">
          <div className="question-text">
            <h2>{questions[currentQuestionIndex].text}</h2>
          </div>
          <div className="options">
            {questions[currentQuestionIndex].options.map((option, index) => (
              <div
                key={index}
                className="option-item"
                onClick={() => handleOptionClick(option)}
              >
                {option}
              </div>
            ))}
          </div>
        </div>
      ) : (
        <div className="routinecontainer">
          {response.length > 0 ? (
            response.map((day, dayIndex) => (
              <div key={`day-container-${dayIndex}`} className="day-box">
                <h2 className="starttext">Day {dayIndex + 1}</h2>
                {renderDayExercises(day[0], day[1])}
              </div>
            ))
          ) : (
            <div className="starttext">Loading workout plan...</div>
          )}
        </div>
      )}
    </div>
  );
}

export default Questionnaire;
