import React from 'react';
import './HomePage.css'; // assuming you have a CSS file for styling

function HomePage() {
  return (
    <div>
        <nav className="navbar">
            <ul className="nav-links">
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Contact</a></li>
            <li><a href="#">Sign In</a></li>
            <li><a href="#">Inputs</a></li>
            </ul>
        </nav>
        <div className="body">
            <div className="left-section">
            <h1 className="focus-text">FORECASTER</h1>
            <div className="white-bars">
                <div className="white-bar"></div>
                <div className="white-bar"></div>
                <div className="white-bar"></div>
                <div className="white-bar"></div>
            </div>
            </div>
            <div className="right-section">
            <p className="forecast-text">
                Forecaster is a website that provides predictive analytics
                on the success of mobile applications. By analyzing
                various factors such as market trends, user feedback, and
                competitor analysis, Forecaster can accurately forecast
                the likelihood of an app's success. With its user-friendly
                interface and customizable parameters, Forecaster is the
                go-to tool for developers looking to optimize their app's
                potential.
            </p>
            <button className="forecast-btn">PREDICT NOW</button>
            </div>
        </div>
        <div className="footer">
            © 2023 Your Website Name
        </div>
    </div>
  );
}

export default HomePage;
