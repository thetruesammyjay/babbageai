import React, { useState } from "react";
import axios from "axios";

function ImageUpload(){
    const [file, setFile]= useState(null);
    const [questions, setQuestions] =useState([]);

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append("image", file);

        try {
            const response = await axios.post("http://localhost:8000/api/ocr/upload", formData, {
                headers: {"Content-Type": "multipart/form-data"},
            });
            setQuestions(response.data.questions);
        }
        catch (error) {
            console.error("Error uploading image:", error);
        }
    };

    return (
        <div>
            <input type="file" onChange={(e) => setFile(e.target.files[0])} />
            <button onClick={handleUpload}>Upload</button>
            <div>
                {questions.map((q, index) => (
                    <div key={index}>
                        <strong>Q: {q.question}</strong>
                        <p>A: {q.answer}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default ImageUpload;