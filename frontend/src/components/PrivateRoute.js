import React from 'react';

import {Redirect, Route} from 'react-router-dom';

import {useSelector} from "react-redux";

const PrivateRoute = ({component: Component, ...rest}) =>{

    const userVerifyLogin = useSelector(state => state.userVerifyLogin);

    const {isLoggedIn} = userVerifyLogin;

    return (
        <Route
            {...rest}
            render={props => (
                (!isLoggedIn) ?
                    <Redirect to='/auth'/> :
                    <Component {...props}/>
            )}
        />
    )

}

export default PrivateRoute;
