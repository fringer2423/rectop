import React, {useEffect} from 'react';

import {useDispatch, useSelector} from "react-redux";

import {useHistory} from 'react-router-dom';

import '../css/verificationScreen.css';

import {verify} from '../actions/userActions.js';

const VerificationScreen = (props) => {

    const code = props.match.params.code;

    const dispatch = useDispatch();

    const registrationSuccess = () => {
        dispatch(verify(code));
    }

    return(
        <div className="body-verify">
            <div className="block-message-verify">
                <div className="verify-message">
                    <button onClick={registrationSuccess}>
                        Пройдите верификацию
                    </button>
                </div>
            </div>
        </div>
    )
}

export default VerificationScreen
