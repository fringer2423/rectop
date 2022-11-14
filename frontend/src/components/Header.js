import React, {useState} from 'react';

import {
    Navbar,
    Nav,
    Container
} from 'react-bootstrap';

import {LinkContainer} from 'react-router-bootstrap'

import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {NavHashLink} from 'react-router-hash-link';
import {faCircleArrowRight} from '@fortawesome/free-solid-svg-icons';
import {faBars} from '@fortawesome/free-solid-svg-icons';





import "../css/header.css"

function Header() {

    return (
        <>

            <Navbar bg="white" expand="lg" fixed="top">
                <Container className="container-for-navbar">
                    <Navbar.Brand className="brand-in-nav" href="/">
                        <img
                            src="/images/navbar_brand_computer.png"
                            className="logo-computer"
                            alt="logo"
                        />
                        <img
                            src="/images/favicon.png"
                            className="logo-mobile"
                            width="50px"
                            height="50px"
                            alt="logo"
                        />
                    </Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" className="border border-0">
                        <FontAwesomeIcon icon={faBars} className="bars"/>
                    </Navbar.Toggle>
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto w-100 justify-content-between mx-4">
                            <div className="link-block">
                                <NavHashLink activeClassName="active-link" className="link-for-nav" to="/#top">
                                    Главная
                                    <div className="dot"></div>
                                </NavHashLink>
                            </div>
                            <div className="link-block">
                                <NavHashLink activeClassName="active-link" className="link-for-nav" to="/#about">
                                    О нас
                                    <div className="dot"></div>
                                </NavHashLink>
                            </div>
                            <div className="link-block">
                                <NavHashLink activeClassName="active-link" className="link-for-nav" to="/#work">
                                    Наши услуги
                                    <div className="dot"></div>
                                </NavHashLink>

                            </div>
                            <div className="link-block">
                                <NavHashLink activeClassName="active-link" className="link-for-nav" to="/#tariffs">
                                    Тарифы
                                    <div className="dot"></div>
                                </NavHashLink>
                            </div>
                            <div className="link-block">
                                <NavHashLink activeClassName="active-link" className="link-for-nav" to="/#contacts">
                                    Контакты
                                    <div className="dot"></div>
                                </NavHashLink>

                            </div>
                            <div className="link-block">
                                <NavHashLink activeClassName="active-link" className="link-for-nav" to="/#questions">
                                    FAQ
                                    <div className="dot"></div>
                                </NavHashLink>
                            </div>
                        </Nav>
                         <LinkContainer to="/registration">
                            <button className="registration-button">Регистрация</button>
                         </LinkContainer>
                         <LinkContainer to="/log-in">
                            <div className="button-log-in"><FontAwesomeIcon
                                icon={faCircleArrowRight} className="arrow-in-button"/></div>
                         </LinkContainer>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>


    )
}

export default Header
