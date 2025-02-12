import React, { useState} from "react";
import axios from "axios";

function DocumentUpload(){
    const [file, setFile] = useState(null);
    const [text, setText] = useState("");

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await axios.post("http://localhost:8000/api/document/upload", formData, {
                headers: { "Content-Type": "multipart/form-data"},
            });
            setText(response.data.text);
        }
        catch(error) {
            console.error("Error uploading file:", error);
        }
    };

    return (
        <div>
            <input type="file" onChange={(e) => setFile(e.target.files[0])} />
            <button onClick={handleUpload}>Upload</button>
            <div>{text}</div>
        </div>
    );
}

export default DocumentUpload;