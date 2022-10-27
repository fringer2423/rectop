import React from 'react';

import { Modal,
         Button,
         InputGroup,
         Form} from 'react-bootstrap';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

import { faGoogle,
         faVk,
         faYandex } from '@fortawesome/free-brands-svg-icons';

import "../css/registration.css"



const Registration = ({ show, handleClose }) => {
    return (
        <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title><b>Регистрация</b></Modal.Title>
        </Modal.Header>
        <Modal.Body>
            <InputGroup className="mt-5 mb-4 w-75 ms-5">
                <Form.Control
                  placeholder="Имя"
                  aria-label="Username"
                  aria-describedby="basic-addon1"
                />
            </InputGroup>
            <InputGroup className="mb-4 w-75 ms-5">
                <Form.Control
                  placeholder="Фамилия"
                  aria-label="Surname"
                  aria-describedby="basic-addon1"
                />
            </InputGroup>
            <InputGroup className="mb-5 w-75 ms-5">
                <Form.Control
                  placeholder="Почта"
                  aria-label="Post"
                  aria-describedby="basic-addon1"
                />
            </InputGroup>
            <InputGroup className=" mb-4 w-75 ms-5">
                <Form.Control
                  placeholder="Пароль"
                  aria-label="Password"
                  aria-describedby="basic-addon1"
                />
            </InputGroup>
            <InputGroup className="mb-5 w-75 ms-5">
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
        </Modal.Body>
        <Modal.Footer>
          <button className="white-button" onClick={handleClose}>
            Закрыть
          </button>
          <button className="blue-button" onClick={handleClose}>
            Регистрация
          </button>
        </Modal.Footer>
      </Modal>
    )
}

export default Registration;
