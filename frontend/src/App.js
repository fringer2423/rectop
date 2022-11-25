import logo from './logo.svg';

import './index.css';


import HomeScreen from './screens/HomeScreen';
import RegistrationPage from "./screens/RegistrationPage";
import LogInPage from "./screens/LogInPage";
import VerificationScreen from './screens/VerificationScreen';
import PrivateRoute from './components/PrivateRoute.js'


import AuthLayout from "./layouts/Auth.js";
import AdminLayout from "./layouts/Admin.js";

import {Container} from 'react-bootstrap';
import {useSelector} from 'react-redux';


import {BrowserRouter as Router, Route} from 'react-router-dom';

function App() {

    const user = localStorage.getItem('userInfo');

    return (
        <Router>
            <Route exact path='/' component={HomeScreen}/>
            <Route path='/auth' component={AuthLayout}/>
            <PrivateRoute path='/admin' user={user} component={() => (<AdminLayout/>)}/>
        </Router>
    );
}

export default App;
