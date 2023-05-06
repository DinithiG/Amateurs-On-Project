import React from 'react';
import './SignInPage.css'; // assuming you have a CSS file for styling
import Nav from '../components/Nav.jsx';

function SignInPage() {
  return (
    <div>
        <Nav/>
        <div className="body">
            <div className="form-container">
              <h1>Sign In</h1>
              <form>
                <label htmlFor="email">Email</label>
                <input type="email" id="email" name="email" placeholder="Enter your email address" required />

                <label htmlFor="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required />

                <button type="submit">Sign In</button>
              </form>
              <p className="signup-text">Don't have an account? <a href="#">Sign up now</a></p>
            </div>
        </div>
        <div className="footer">
            © 2023 Your Website Name
        </div>
    </div>
  );
}

export default SignInPage;
