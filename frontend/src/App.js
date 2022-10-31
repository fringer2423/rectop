import logo from './logo.svg';

import './index.css'
import Header from './components/Header'
import Footer from './components/Footer'
import HomeScreen from './screens/HomeScreen'
import {Container} from 'react-bootstrap'

import {BrowserRouter as Router, Route} from 'react-router-dom'

function App() {
    return (
        <Router>
            <Header/>
            <Container>
                <Route path='/' component={HomeScreen}/>

            </Container>
            <Footer/>
        </Router>
    );
}

export default App;
