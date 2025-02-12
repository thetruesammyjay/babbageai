import React from "react";
import { Link } from "react-router-dom";
import "../styles/Navbar.css";

function Navbar() {
    return (
        <nav className="navbar">
            <div className="navbar-brand">
                <Link to="/">BabbageAI</Link>
            </div>
            <div className="navbar-links">
                <Link to="/documents">Documents</Link>
                <Link to="/videos">Videos</Link>
                <Link to="/questions">Questions</Link>
            </div>
        </nav>
    );
}

export default Navbar;