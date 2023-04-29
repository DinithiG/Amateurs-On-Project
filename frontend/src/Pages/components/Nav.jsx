import React from 'react';
import './nav.css';

const Nav = () => {
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
        </div>
    );
};

export default Nav;