import logo from './logo.svg';

import './css/bootstrap.min.css'
import './css/header_layout.css'
import './css/main.css'
import './index.css'
import Header from './components/Header'
import Footer from './components/Footer'
import HomeScreen from './screens/HomeScreen'
import DashboardScreen from "./screens/DashboardScreen";
import {Container} from 'react-bootstrap'
import {BrowserRouter as Router, Route} from 'react-router-dom'

function App() {
    return (
        <Router>
            <body>
                <Header/>
                <Route path='/' component={HomeScreen} exact/>
                <Route path='/dashboard' component={DashboardScreen}/>
                <Footer/>
            </body>
        </Router>
    );
}

export default App;