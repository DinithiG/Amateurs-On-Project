import './Form.css';

const Form = () => {
    return (
        <div id='form-container'>
            <form method='POST'>

                <div id='form-heading'>
                    <h1 >Predictor!</h1>
                </div>
                
                <div className='grid-container'>

                    <div className='input-container'>
                        <label for=""> Application Name:</label>
                        <input type='text'/>
                        <label for=""> Size Of Application:</label>
                        <input/>
                        <label for=""> Field:</label>
                        <input/>
                    </div>

                    <div className='input-container'>
                        <label for=""> Field:</label>
                        <input/>
                        <label for=""> Field:</label>
                        <input/>
                        <label for=""> Field:</label>
                        <input/>
                    </div>

                </div>

                <div id='button-container'>
                    <button type='submit'>Submit</button>
                </div>
                

            </form>
        </div>
        
    );
};

export default Form;