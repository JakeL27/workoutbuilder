import React, { useState, useEffect } from "react";
import axios from "axios";

function Questionnaire() {
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState({});
  const [completed, setCompleted] = useState(false);
  const [loadingPercentage, setLoadingPercentage] = useState(0);
  const [response, setResponse] = useState([]);
  const [tooltipContent, setTooltipContent] = useState("");
  const [tooltipVisible, setTooltipVisible] = useState(false);
  const [tooltipPosition, setTooltipPosition] = useState({ top: 0, left: 0 });

  const handleMouseEnter = (exerciseTip, e) => {
    setTooltipContent(exerciseTip);
    setTooltipVisible(true);
    setTooltipPosition({
      top: e.clientY,
      left: e.clientX,
    });
  };

  const handleMouseLeave = () => {
    setTooltipVisible(false);
  };

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

  const delay = (duration) =>
    new Promise((resolve) => setTimeout(resolve, duration));

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
        "https://workoutbuilder-api.vercel.app/generate_workout",
        { data: answers }
      );
      console.log(data);
      setResponse(data.routine); // Store the full workout routine
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

  const renderDayExercises = (day) => {
    return (
      <div className="endingbody">
        {day[0].map((exercise, index) => (
          <p
            key={`exercise-${index}`}
            className="exercise"
            onMouseEnter={(e) => handleMouseEnter(exercise[1], e)}
            onMouseLeave={handleMouseLeave}
          >
            {exercise[0]}
          </p>
        ))}
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

  const introMessage = answers["What is your focus?"] ? (
    <span>
      Your focus is:{" "}
      <span className="focus-highlight">{answers["What is your focus?"]}</span>.
      Based on your responses, here's your custom workout routine designed to
      help you achieve your goals.
    </span>
  ) : (
    "Loading your custom workout routine..."
  );

  return (
    <div className="questionnaire">
      {/* Tooltip display */}
      {tooltipVisible && (
        <div
          className="tooltip"
          style={{
            top: tooltipPosition.top + 15,
            left: tooltipPosition.left + 15,
            position: "fixed", // Change to 'absolute' if needed
          }}
        >
          {tooltipContent}
        </div>
      )}

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
          <div className="starttext">
            <h2 className="infoheader">{introMessage}</h2>
            <p className="infobody">
              The routine is to be completed weekly. It is up to you which day
              of the week to allot each of the given training days. Don't forget
              to stretch after each workout!
              <p>
                Each exercise should be trained until failure each set for a
                total of 3 sets. Aim to fail around{" "}
                <span className="focus-highlight">8-10</span> reps each set.
              </p>
            </p>
          </div>
          {response && response.length > 0 ? (
            response.map((day, dayIndex) => (
              <div key={`day-container-${dayIndex}`} className="day-box">
                <h2 className="endingheader">Day {dayIndex + 1}</h2>
                {renderDayExercises(day)}
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
