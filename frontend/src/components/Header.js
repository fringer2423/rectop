import React, { useState } from 'react';

import { Navbar,
        Image,
        Nav,
        Button,
        Container,
        NavDropdown,
        NavbarCollapse } from 'react-bootstrap';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

import Registration from "../components/Registration";
import LogIn from "../components/LogIn";
import {faCircleArrowRight} from '@fortawesome/free-solid-svg-icons';

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

        <Navbar bg="white" expand="lg" fixed="top" >
            <Container>
                <Navbar.Brand >
                    <img
                     src="/images/favicon.png"
                     width="50px"
                     height="50px"
                     />
                    <b>Rec<span>top</span></b> <br/>
                    Ваша репутация
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto w-100 justify-content-between mx-4">

                          <Nav.Link>Главная</Nav.Link>


                          <Nav.Link>О нас</Nav.Link>


                          <Nav.Link>Наши услуги</Nav.Link>


                          <Nav.Link>Тарифы</Nav.Link>


                          <Nav.Link>Контакты</Nav.Link>


                          <Nav.Link>FAQ</Nav.Link>

                    </Nav>
                 <button className="white-button" onClick={handleShow}>Регистрация</button>
                 <button className="button-log-in" onClick={handleShowLogIn}><FontAwesomeIcon icon={faCircleArrowRight} className="arrow-in-button"/></button>
             </Navbar.Collapse>
         </Container>
       </Navbar>
       < Registration show={show} handleClose={handleClose}/>
       < LogIn show={showlogin} handleClose={handleCloseLogIn}/>
   </>


    )
}

export default Header
