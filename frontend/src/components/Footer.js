import React from "react";
import {Navbar, Nav, Container} from "react-bootstrap";

import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

import {NavHashLink} from "react-router-hash-link";

import {faTelegram, faVk} from "@fortawesome/free-brands-svg-icons";

import "../css/footer.css";

function Footer() {
    const currentYear = new Date().getFullYear();

    return (
        <Navbar variant="dark" className="navbar-footer">
            <Container className="container-footer">
                <div className="footer-first-nav">
                    <div className="footer-navbar-logo">
                        <Navbar.Brand>
                            <img
                                src="/images/logofooter.svg"
                                alt="Rectop Logo"
                            />
                        </Navbar.Brand>
                        <Nav.Item>
                            Мы используем куки, это позволяет улучшить ваш
                            пользовательский опыт
                        </Nav.Item>
                    </div>
                    <div className="footer-contacts-navs-mobile">
                        <div className="nav-footer-mobile">
                            <Nav.Item>
                                <b>Навигация</b>
                            </Nav.Item>
                            <Nav.Item>
                                <NavHashLink to="/#top" className="link-footer">
                                    Главная
                                </NavHashLink>
                            </Nav.Item>
                            <Nav.Item>
                                <NavHashLink
                                    to="/#about"
                                    className="link-footer"
                                >
                                    О нас
                                </NavHashLink>
                            </Nav.Item>
                            <Nav.Item>
                                <NavHashLink
                                    to="/#work"
                                    className="link-footer"
                                >
                                    Как мы работаем
                                </NavHashLink>
                            </Nav.Item>
                            <Nav.Item>
                                <NavHashLink
                                    to="/#tariffs"
                                    className="link-footer"
                                >
                                    Тарифы
                                </NavHashLink>
                            </Nav.Item>
                            <Nav.Item>
                                <NavHashLink
                                    to="/#contacts"
                                    className="link-footer"
                                >
                                    Обратная связь
                                </NavHashLink>
                            </Nav.Item>
                            <Nav.Item>
                                <NavHashLink
                                    to="/#questions"
                                    className="link-footer"
                                >
                                    FAQ
                                </NavHashLink>
                            </Nav.Item>
                        </div>
                        <div className="contacts-footer-mobile">
                            <Nav.Item>
                                <b>Контакты</b>
                            </Nav.Item>
                            <Nav.Item>business@rectop.ru</Nav.Item>
                            <Nav.Item>+ 7 (999) 888-77-66</Nav.Item>
                            <Nav.Item>Политика конфиденциальности</Nav.Item>
                            <Nav.Item>Лицензионный договор</Nav.Item>
                            <div className="icons-footer">
                                <FontAwesomeIcon icon={faTelegram}/>
                                <FontAwesomeIcon icon={faVk}/>
                            </div>
                        </div>
                    </div>
                    <div className="footer-reference">
                        <Nav.Item>
                            © 2018–{currentYear} RecTop - агрегатор отзывов
                        </Nav.Item>
                    </div>
                </div>
                <div className="nav-footer-computer">
                    <Nav.Item>
                        <b>Навигация</b>
                    </Nav.Item>
                    <Nav.Item>
                        <NavHashLink to="/#top" className="link-footer">
                            Главная
                        </NavHashLink>
                    </Nav.Item>
                    <Nav.Item>
                        <NavHashLink to="/#about" className="link-footer">
                            О нас
                        </NavHashLink>
                    </Nav.Item>
                    <Nav.Item>
                        <NavHashLink to="/#work" className="link-footer">
                            Как мы работаем
                        </NavHashLink>
                    </Nav.Item>
                    <Nav.Item>
                        <NavHashLink to="/#tariffs" className="link-footer">
                            Тарифы
                        </NavHashLink>
                    </Nav.Item>
                    <Nav.Item>
                        <NavHashLink to="/#contacts" className="link-footer">
                            Обратная связь
                        </NavHashLink>
                    </Nav.Item>
                    <Nav.Item>
                        <NavHashLink to="/#questions" className="link-footer">
                            FAQ
                        </NavHashLink>
                    </Nav.Item>
                </div>
                <div className="contacts-footer-computer">
                    <Nav.Item>
                        <b>Контакты</b>
                    </Nav.Item>
                    <Nav.Item>business@rectop.ru</Nav.Item>
                    <Nav.Item>+ 7 (999) 888-77-66</Nav.Item>
                    <Nav.Item>
                        <u>Политика конфиденциальности</u>
                    </Nav.Item>
                    <Nav.Item>
                        <u>Лицензионный договор</u>
                    </Nav.Item>
                    <div className="icons-footer">
                        <FontAwesomeIcon icon={faTelegram}/>
                        <FontAwesomeIcon icon={faVk}/>
                    </div>
                </div>
            </Container>
        </Navbar>
    );
}

export default Footer;
