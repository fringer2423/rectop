import React, {useState} from 'react';

import {
    Modal,
    Button,
    InputGroup,
    Form
} from 'react-bootstrap';

import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';

import {
    faGoogle,
    faVk,
    faYandex
} from '@fortawesome/free-brands-svg-icons';

import "../css/registration.css"

import {checkMail} from "../validator/validation.js"

import {LinkContainer} from 'react-router-bootstrap'


const LogIn = () => {

    const [mail, setMail] = useState('');
    const [mailError, setMailError] = useState(false);

    const handleErrorMail = () => {
        if (!checkMail.test(mail)) {
            setMailError(true);
        } else {
            setMailError(false);
        }
    }

    return (
        <div className="log-in-page">

            <h1>Вход</h1>

            <Form.Label className="mt-5"><b>Email</b></Form.Label>
            <InputGroup className=" mb-3 w-75 ">
                <Form.Control
                    placeholder="Email"
                    aria-label="Post"
                    aria-describedby="basic-addon1"
                    value={mail}
                    onChange={(e) => setMail(e.target.value)}
                />
            </InputGroup>
            <Form.Label><b>Пароль</b></Form.Label>
            <InputGroup className=" mb-5 w-75 ">
                <Form.Control
                    placeholder="Пароль"
                    aria-label="Password"
                    aria-describedby="basic-addon1"
                />
            </InputGroup>
            <div className="icons-of-registration-brands">
                <FontAwesomeIcon icon={faGoogle} className="icon-google"/>
                <FontAwesomeIcon icon={faVk} className="icon-vk"/>
                <FontAwesomeIcon icon={faYandex} className="icon-yandex"/>
            </div>

            {mailError && <h1>Неверный почтовый адрес</h1>}

            <LinkContainer to="/">
                <button className="white-button">
                    Выйти
                </button>
            </LinkContainer>
            <button className="blue-button" onClick={handleErrorMail}>
                Войти
            </button>
        </div>

    )
}

export default LogIn;
