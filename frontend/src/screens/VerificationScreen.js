import React, {useEffect} from 'react';

import {useDispatch, useSelector} from "react-redux";

import {useHistory} from 'react-router-dom';

import '../css/verificationScreen.css';

import {Alert, Spinner} from 'react-bootstrap';

import {verify} from '../actions/userActions.js';

const VerificationScreen = (props) => {

    const code = props.match.params.code;

    const dispatch = useDispatch();
    const userVerify = useSelector(state => state.userVerify);
    const {error, userInfo} = userVerify;
    let history = useHistory();


    useEffect(() => {
        async function verify_user() {
            await dispatch(verify(code));
            if(localStorage.getItem('userInfo')){
                history.push('/');
            }
            console.log(localStorage.getItem('userInfo'));
        }
        verify_user();
    }, [history, userInfo]);

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
