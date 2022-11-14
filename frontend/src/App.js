import logo from './logo.svg';

import './index.css'
import Header from './components/Header'
import Footer from './components/Footer'
import HomeScreen from './screens/HomeScreen'
import RegistrationPage from "./screens/RegistrationPage"
import LogInPage from "./screens/LogInPage"

import {Container} from 'react-bootstrap'


import {BrowserRouter as Router, Route} from 'react-router-dom'

function App() {
    return (
        <Router>
            <Header/>
            <Container>
                <Route exact path='/' component={HomeScreen}/>
                <Route path='/registration' component={RegistrationPage}/>
                <Route path='/log-in' component={LogInPage}/>
            </Container>
            <Footer/>
        </Router>
    );
}

export default App;
