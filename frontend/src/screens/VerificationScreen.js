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
    const {error, userInfo, loading} = userVerify;
    let history = useHistory();
    const user = localStorage.getItem('userInfo');


    useEffect(() => {
        async function verify_user() {
            await dispatch(verify(code));
            if (user) {
                history.push('/dashboard/');
                window.location.reload();
            }
            console.log(user);
        }

        verify_user();
    }, [history, user]);

    return (
        <div className="body-verify">
            <Alert>
                {error ? error : "Подтверждение через почту"}
                {loading &&
                    <Spinner animation="border"/>}
            </Alert>
        </div>
    )
}

export default VerificationScreen
