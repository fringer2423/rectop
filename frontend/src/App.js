import logo from './logo.svg';

import './index.css';


import HomeScreen from './screens/HomeScreen';
import RegistrationPage from "./screens/RegistrationPage";
import LogInPage from "./screens/LogInPage";
import VerificationScreen from './screens/VerificationScreen'


import AuthLayout from "./layouts/Auth.js";
import AdminLayout from "./layouts/Admin.js";

import {Container} from 'react-bootstrap';


import {BrowserRouter as Router, Route} from 'react-router-dom';

function App() {
    return (
        <Router>
            <Route exact path='/' component={HomeScreen}/>
            <Route path='/auth' component={AuthLayout}/>
            <Route path='/admin' component={AdminLayout}/>
            <Route path='/auth/verify/:code' component={VerificationScreen}/>
        </Router>
    );
}

export default App;
