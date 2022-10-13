import React from 'react'
import {useDispatch, useSelector} from 'react-redux'
import {Navbar, Nav, Container, NavDropdown, Image} from 'react-bootstrap'
import {LinkContainer} from 'react-router-bootstrap'
import NavbarCollapse from "react-bootstrap/NavbarCollapse";


function Header() {


    return (

            <Navbar fixed='top' variant='light' expand='lg' bg='white'>
                <Container fluid>
                    <Navbar.Brand href="/">
                        <Image id="LogoImage" src="/images/Logo.png"/>
                    </Navbar.Brand>

                    <Navbar.Toggle aria-controls="basic-navbar-nav" className=""/>



                    <Navbar.Collapse className="navbar-collapse collapse" id="navbarResponsive">
                        <Nav className="header-layout nav navbar-nav">
                                <Nav.Link href="/" className="nav-link active" aria-current="page">Главная</Nav.Link>
                                <Nav.Link href="/about" className="nav-link text-nowrap" aria-disabled="true">О нас</Nav.Link>


                                <Nav.Link  href="" className="nav-link">Наши услуги</Nav.Link >

                                <Nav.Link  href="/stores_list" className="nav-link">Тарифы</Nav.Link >


                                <Nav.Link  href="/stores_list" className="nav-link">Контакты</Nav.Link >


                                <Nav.Link href="/stores_list" className="nav-link">FAQ</Nav.Link>
                                </Nav>
                                <Nav >


                                    <button type="button" id="RegistrationButton"
                                            className="btn btn-outline-primary bg-gradient text-nowrap rounded-pill"
                                            data-bs-toggle="modal" data-bs-target="#modalReg">Регистрация
                                    </button>

                                    <button type="button" id="LogInButton"
                                            className="log-button btn-outline-primary bg-gradient rounded-circle"
                                            data-bs-toggle="collapse" data-bs-target="#collapseLogData"
                                            aria-expanded="false" aria-controls="collapseLogData">
                                        <i className="bi bi-arrow-right-circle-fill"></i>
                                    </button>
                                  </Nav>




                    </Navbar.Collapse>
                </Container>
            </Navbar>



    )
}

export default Header
