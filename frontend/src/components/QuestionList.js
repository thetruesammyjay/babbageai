import React from "react";

function QuestionList({ questions }) {
    return (
        <div>
            {questions.map((q, questions) => (
                <div key={index}>
                    <strong>Q: {q.question}</strong>
                    <p>A: {q.answer}</p>
                </div>
            ))}
        </div>
    );
}

export default QuestionList;