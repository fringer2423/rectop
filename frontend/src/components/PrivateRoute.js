import React from 'react';

import {Redirect, Route } from 'react-router-dom';

import {useSelector} from "react-redux";

const PrivateRoute = ({component: Component, user, ...rest}) => (

    <Route
        {...rest}
        render={props => (
            (user) ?
            <Component {...props}/>:
            <Redirect to='/auth'/>
        )}
    />
)

export default PrivateRoute;
