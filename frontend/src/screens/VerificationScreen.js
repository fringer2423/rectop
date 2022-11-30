import React, {useEffect, useState} from 'react';

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
    const [message, setMessage] = useState('Подождите, пожалуйста...')


    useEffect(() => {
        async function verify_user() {
            await dispatch(verify(code));
            if (user) {
                setMessage('Ваша почта успечно подтверждена. Сейчас вы перейдете в личный кабинет');
                await new Promise((resolve, reject) => setTimeout(resolve, 3000));
                history.push('/dashboard/');
                window.location.reload();
            }

        }

        verify_user();
    }, [history, user]);



    return (
        <div className="body-verify">
            <Alert>
                {error ? error : message}
                {loading &&
                    <Spinner animation="border"/>}
            </Alert>
        </div>
    )
}

export default VerificationScreen
