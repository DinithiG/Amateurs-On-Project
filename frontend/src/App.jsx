import {
  BrowserRouter as Router,
  Route,
  Routes,
  Link,
  BrowserRouter,
} from "react-router-dom";
import HomePage from './Pages/HomePage';
import Form from './Pages/FormPage/Form';
import SignInPage from './Pages/SignIn/SignInPage';


function App() {
  return (

    <BrowserRouter>
      <main>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="form" element={<Form/>} />
          <Route path="Signin" element={<SignInPage/>} />
        </Routes>
      </main>
      {/* <Footer /> */}
    </BrowserRouter>
  );
}

export default App;
