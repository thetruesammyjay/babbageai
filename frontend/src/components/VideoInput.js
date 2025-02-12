import React, { useState} from "react";
import axios from "axios";

function VideoInput() {
    const [videoUrl, setVideoUrl] = useState("");
    const [transcript, setTranscript] = useState("");

    const handleProcess = async () => {
        try {
            const response = await axios.post("http://localhost:8000/api/videos/process", { videoUrl });
            setTranscript(response.data.transcript);
        }
        catch(error){
            console.error("Error processing video:", error);
        }
    };

    return (
        <div>
            <input 
                type="text"
                placeholder="Enter the YouTube URL"
                value={videoUrl}
                onChange={(e) => setVideoUrl(e.target.value)}
            />
            <button onClick={handleProcess}>Process</button>
            <div>{transcript}</div>
        </div>
    );
}

export default VideoInput;