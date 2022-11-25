import React, {useEffect} from 'react';

import {useDispatch, useSelector} from "react-redux";

import {useHistory} from 'react-router-dom';

import '../css/verificationScreen.css';

import {Alert, Spinner} from 'react-bootstrap';

import {verify} from '../actions/userActions.js';

const VerificationScreen = (props) => {

    const code = props.match.params.code;

    const dispatch = useDispatch();
    const userRegister = useSelector(state => state.userRegister);
    const {error} = userRegister;
    let history = useHistory();


    useEffect(() => {
        dispatch(verify(code));
        if(!error){
            history.push("/admin");
        }
    }, [history]);

    return(
        <div className="body-verify">
            <Alert>
                Подтверждение через почту
                <Spinner animation="border"/>
                {error}
            </Alert>
        </div>
    )
}

export default VerificationScreen
