import React, {useState} from 'react';

import {
    Button,
    InputGroup,
    Form
} from 'react-bootstrap';

import {LinkContainer} from 'react-router-bootstrap'

import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';

import {
    faGoogle,
    faVk,
    faYandex
} from '@fortawesome/free-brands-svg-icons';

import "../css/registration.css"
import {checkMail} from "../validator/validation.js"


const RegistrationPage = () => {
    const [mail, setMail] = useState('');
    const [mailError, setMailError] = useState(false);

    const handleErrorMail = () => {
        if (!checkMail.test(mail)){
            setMailError(true);
        }
        else{
            setMailError(false);
        }
    }


    return (
        <div className="registration-page">
                <h1><b>Регистрация</b></h1>

                <Form.Label className="mt-5"><b>Имя</b></Form.Label>
                <InputGroup className="mb-4 w-75">
                    <Form.Control
                        placeholder="Имя"
                        aria-label="Username"
                        aria-describedby="basic-addon1"
                    />
                </InputGroup>
                <Form.Label><b>Фамилия</b></Form.Label>
                <InputGroup className="mb-4 w-75">
                    <Form.Control
                        placeholder="Фамилия"
                        aria-label="Surname"
                        aria-describedby="basic-addon1"
                    />
                </InputGroup>
                <Form.Label><b>Email</b></Form.Label>
                <InputGroup className="mb-5 w-75">
                    <Form.Control
                        placeholder="Email"
                        aria-label="Post"
                        aria-describedby="basic-addon1"
                        value={mail}
                        onChange = {(e) => setMail(e.target.value)}
                    />
                </InputGroup>
                <Form.Label><b>Пароль</b></Form.Label>
                <InputGroup className=" mb-4 w-75  ">
                    <Form.Control
                        placeholder="Пароль"
                        aria-label="Password"
                        aria-describedby="basic-addon1"
                    />
                </InputGroup>
                <Form.Label><b>Повторите пароль</b></Form.Label>
                <InputGroup className="mb-5 w-75">
                    <Form.Control
                        placeholder="Повторите пароль"
                        aria-label="PasswordAgain"
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
                    Регистрация
                </button>
            </div>

    )
}

export default RegistrationPage;
