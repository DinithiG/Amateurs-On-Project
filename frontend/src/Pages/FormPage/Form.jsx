import React from 'react';
import './Form.css';
import Nav from '../components/Nav';

const Form = () => {
  return (
    <div>
      <Nav/>
      <div id='form-container'>
        <form method='POST'>

          <div id='form-heading'>
            <h1>Predictor!</h1>
          </div>

          <div className='grid-container'>

            <div className='input-container'>
              <label htmlFor=""> Application Name:</label>
              <input type='text'/>
              <label htmlFor=""> Size Of Application:</label>
              <input/>
              <label htmlFor=""> Field:</label>
              <input/>
            </div>

            <div className='input-container'>
              <label htmlFor=""> Field:</label>
              <input/>
              <label htmlFor=""> Field:</label>
              <input/>
              <label htmlFor=""> Field:</label>
              <input/>
            </div>

          </div>

          <div id='button-container'>
            <button type='submit'>Submit</button>
          </div>


        </form>
      </div>
    </div>


  );
};

export default Form;
