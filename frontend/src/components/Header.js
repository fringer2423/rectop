import React, {useState} from 'react';

import {
    Navbar,
    Nav,
    Container
} from 'react-bootstrap';

import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import { HashLink } from 'react-router-hash-link';
import {faCircleArrowRight} from '@fortawesome/free-solid-svg-icons';

import Registration from "../components/Registration";
import LogIn from "../components/LogIn";


import "../css/main.css"

function Header() {

    const [show, setShow] = useState(false);
    const [showlogin, setShowlogin] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const handleCloseLogIn = () => setShowlogin(false);
    const handleShowLogIn = () => setShowlogin(true);

    return (
        <>

            <Navbar bg="white" expand="lg" fixed="top">
                <Container>
                    <Navbar.Brand className="d-flex flex-row" href="/">
                        <img
                            src="/images/favicon.png"
                            width="50px"
                            height="50px"
                        />
                        <div className="fs-6">
                            <b>Rec<span>top</span></b> <br/>
                            Ваша репутация
                        </div>
                    </Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav"/>
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto w-100 justify-content-between mx-4">

                            <Nav.Item><HashLink to="/#top">Главная</HashLink></Nav.Item>


                            <Nav.Item><HashLink to="/#about">О нас</HashLink></Nav.Item>


                            <Nav.Item><HashLink to="/#work">Наши услуги</HashLink></Nav.Item>


                            <Nav.Item><HashLink to="/#tariffs">Тарифы</HashLink></Nav.Item>


                            <Nav.Item><HashLink to="/#contacts">Контакты</HashLink></Nav.Item>


                            <Nav.Item><HashLink to="/#questions">FAQ</HashLink></Nav.Item>

                        </Nav>
                        <button className="white-button" onClick={handleShow}>Регистрация</button>
                        <button className="button-log-in" onClick={handleShowLogIn}><FontAwesomeIcon
                            icon={faCircleArrowRight} className="arrow-in-button"/></button>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
            < Registration show={show} handleClose={handleClose}/>
            < LogIn show={showlogin} handleClose={handleCloseLogIn}/>
        </>

        

    )
}

export default Header