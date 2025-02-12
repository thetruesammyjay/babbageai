
---
# BabbageAI

**BabbageAI** is an AI-powered educational web application designed to help university students study more efficiently. It allows students to upload documents (PDFs/DOCX), input YouTube video URLs, or scan question papers to get AI-generated answers based on the content.

## Features
- **Document Processing**: Upload and extract text from PDFs or DOCX files.
- **Video Processing**: Fetch transcripts from YouTube videos.
- **Question Paper Scanning**: Upload images of question papers and get answers.
- **AI-Powered Answers**: Uses DeepSeek API to generate context-aware answers.

## Technologies Used
### Backend
- **FastAPI**: Python web framework for building APIs.
- **Tesseract OCR**: For extracting text from images.
- **YouTube Transcript API**: For fetching video transcripts.
- **DeepSeek API**: For generating AI-powered answers.

### Frontend
- **React**: JavaScript library for building user interfaces.
- **Axios**: For making HTTP requests to the backend.
- **React Router**: For routing and navigation.
- **CSS**: For styling the application.

## Setup Instructions

### Backend
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/thetruesammyjay/babbageai.git
   cd babbageai/backend
   ```
2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Set Up Environment Variables**:
- Create a .env file in the backend directory and add the following:
    ```env
    DEEPSEEK_API_KEY=your_deepseek_api_key
    UPLOAD_FOLDER=storage
    ```
4. **Run the Backend**:
    ```bash
    uvicorn app:app --reload
    ```
### Frontend
1. **Navigate to the Frontend Directory**:
    ```bash
    cd ../frontend
    ```
2. **Install Dependencies**:
    ```bash
    npm install
    ```
3. **Set Up Environment Variables**:
    ```env
    REACT_APP_API_URL=http://localhost:8000/api
    ```
4. **Run the Frontend**:
    ```bash
    npm start
    ```
5. **Open in Browser**:
- Visit http://localhost:3000 in your browser.

### Contributing
- Contributions are welcome! Please open an issue or submit a pull request.

### License
- This project is licensed under the MIT License.

### Contact Me
- thetruesammyjay@gmail.com
- x.com/thatbwoysammyj
