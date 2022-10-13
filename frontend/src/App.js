import logo from './logo.svg';

import './index.css'
import Header from './components/Header'
import Footer from './components/Footer'
import HomeScreen from './screens/HomeScreen'

import {BrowserRouter as Router, Route} from 'react-router-dom'

function App() {
    return (
        <Router>
        <Header/>
              <Route path='/' component={HomeScreen} exact/>
        </Router>
    );
}

export default App;
