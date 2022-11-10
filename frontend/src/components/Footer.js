import React from 'react'
import {
    Navbar,
    Nav,
    Container
} from 'react-bootstrap'

import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';

import {
    faTelegram,
    faVk
} from '@fortawesome/free-brands-svg-icons';

import "../css/footer.css"

function Footer() {
    return (
        <Navbar variant="dark" className="navbar-footer">
            <Container className="container-footer">
                <div className="footer-first-nav">
                    <div className="footer-navbar-logo">
                        <Navbar.Brand>
                            <img
                                src="/images/logofooter.png"
                                alt="Rectop Logo"
                            />
                        </Navbar.Brand>
                        <Nav.Item>
                            Мы используем куки, это позволяет улучшить ваш пользовательский опыт
                        </Nav.Item>
                    </div>
                    <div className="footer-contacts-navs-mobile">
                        <div className="nav-footer-mobile">
                            <Nav.Item><b>Навигация</b></Nav.Item>
                            <Nav.Link href="/">Главная</Nav.Link>
                            <Nav.Link>О нас</Nav.Link>
                            <Nav.Link>Как мы работаем</Nav.Link>
                            <Nav.Link>Тарифы</Nav.Link>
                            <Nav.Link>Обратная связь</Nav.Link>
                            <Nav.Link>FAQ</Nav.Link>
                        </div>
                        <div className="contacts-footer-mobile">
                            <Nav.Item><b>Контакты</b></Nav.Item>
                            <Nav.Link>business@rectop.ru</Nav.Link>
                            <Nav.Link>+ 7 (999) 888-77-66</Nav.Link>
                            <Nav.Link>Политика конфиденциальности</Nav.Link>
                            <Nav.Link>Лицензионный договор</Nav.Link>
                            <div className="icons-footer">
                                <FontAwesomeIcon icon={faTelegram}/>
                                <FontAwesomeIcon icon={faVk}/>
                            </div>
                        </div>
                    </div>
                    <div className="footer-reference">
                        <Nav.Item>
                            © 2018–2022 Rectop - агрегатор отзывов
                        </Nav.Item>
                    </div>
                </div>
                    <div className="nav-footer-computer">
                        <Nav.Item><b>Навигация</b></Nav.Item>
                        <Nav.Link href="/">Главная</Nav.Link>
                        <Nav.Link>О нас</Nav.Link>
                        <Nav.Link>Как мы работаем</Nav.Link>
                        <Nav.Link>Тарифы</Nav.Link>
                        <Nav.Link>Обратная связь</Nav.Link>
                        <Nav.Link>FAQ</Nav.Link>
                    </div>
                    <div className="contacts-footer-computer">
                        <Nav.Item><b>Контакты</b></Nav.Item>
                        <Nav.Link>business@rectop.ru</Nav.Link>
                        <Nav.Link>+ 7 (999) 888-77-66</Nav.Link>
                        <Nav.Link>Политика конфиденциальности</Nav.Link>
                        <Nav.Link>Лицензионный договор</Nav.Link>
                        <div className="icons-footer">
                            <FontAwesomeIcon icon={faTelegram}/>
                            <FontAwesomeIcon icon={faVk}/>
                        </div>
                    </div>
            </Container>
        </Navbar>
    )
}

export default Footer
