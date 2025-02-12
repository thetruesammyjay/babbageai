import React from "react";
import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import HomePage from "./pages/HomePage";
import DocumentsPage from "pages/DocumentsPage";
import VideosPage from "./pages/VideosPage";
import QuestionsPage from "./pages/QuestionsPage";
import "./styles/App.css";

function App() {
    return (
        <div className="App">
            <Navbar />
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/documents" element={<DocumentsPage />} />
                <Route path="/videos" element={<VideosPage />} />
                <Route path="/questions" element={<QuestionsPage />} />
            </Routes>
            <Footer/>
        </div>
    );
}

export default App;