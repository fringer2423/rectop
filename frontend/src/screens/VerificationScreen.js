import React from 'react';

import {useDispatch} from "react-redux";

import '../css/verificationScreen.css'

import {verify} from '../actions/userActions.js'

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
