import React, { useState } from 'react';

import { Navbar,
        Image,
        Nav,
        Button,
        Container,
        NavDropdown,
        NavbarCollapse } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';

import Registration from "../components/Registration";

import "../css/main.css"

function Header() {

    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

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
                      <Nav.Link href="/">Главная</Nav.Link>
                      <Nav.Link >О нас</Nav.Link>
                      <Nav.Link >Наши услуги</Nav.Link>
                      <Nav.Link >Тарифы</Nav.Link>
                      <Nav.Link >Контакты</Nav.Link>
                      <Nav.Link >FAQ</Nav.Link>
                    </Nav>
                 <button className="white-button" onClick={handleShow}>Регистрация</button>
             </Navbar.Collapse>
         </Container>
       </Navbar>
       < Registration show={show} handleClose={handleClose}/>
   </>


    )
}

export default Header
