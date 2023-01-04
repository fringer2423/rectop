import logo from "./logo.svg";

import "./index.css";

import HomeScreen from "./screens/HomeScreen";

import PrivateRoute from "./components/PrivateRoute.js";

import AuthLayout from "./layouts/Auth.js";
import AdminLayout from "./layouts/Admin.js";


//<PrivateRoute path='/dashboard' component={() => (<AdminLayout/>)}/>

import {BrowserRouter as Router, Route} from "react-router-dom";

function App() {
    // const user = localStorage.getItem('userInfo');

    return (
        <Router>
            <Route exact path="/" component={HomeScreen}/>
            <Route path="/auth" component={AuthLayout}/>
            <PrivateRoute path="/dashboard" component={() => <AdminLayout/>}/>
        </Router>
    );
}

export default App;
