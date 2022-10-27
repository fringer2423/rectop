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
                  placeholder="Логин"
                  aria-label="Username"
                  aria-describedby="basic-addon1"
                />
            </InputGroup>
            <InputGroup className="mb-4 w-75 ms-5">
                <Form.Control
                  placeholder="Почта"
                  aria-label="Username"
                  aria-describedby="basic-addon1"
                />
            </InputGroup>
            <InputGroup className="mb-5 w-75 ms-5">
                <Form.Control
                  placeholder="Пароль"
                  aria-label="Username"
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
          <Button variant="secondary" onClick={handleClose}>
            Закрыть
          </Button>
          <Button variant="primary" onClick={handleClose}>
            Регистрация
          </Button>
        </Modal.Footer>
      </Modal>
    )
}

export default Registration;
