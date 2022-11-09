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

function Footer() {
    return (
        <Navbar bg="primary" variant="dark">
            <Container>
                <Nav className="d-flex flex-column text-white w-25 me-5 gap-5 mb-5">
                    <Nav className="d-flex flex-column gap-3">
                        <Navbar.Brand>
                            <img
                                src="/images/logofooter.png"
                                alt="Rectop Logo"
                            />
                        </Navbar.Brand>
                        <Nav.Item>
                            Мы используем куки, это позволяет улучшить ваш пользовательский опыт
                        </Nav.Item>
                    </Nav>
                    <Nav className="d-flex flex-column gap-3">
                        <Nav.Item>
                            © 2018–2022 Rectop - агрегатор отзывов
                        </Nav.Item>
                        <Nav.Item>
                            Дизайнер - Чернев Максим (@maxim_235)
                        </Nav.Item>
                    </Nav>
                </Nav>
                <Nav className="me-auto d-flex flex-column mt-5  mb-5 text-white">
                    <Nav.Item><b>Навигация</b></Nav.Item>
                    <Nav.Link href="/">Главная</Nav.Link>
                    <Nav.Link>О нас</Nav.Link>
                    <Nav.Link>Как мы работаем</Nav.Link>
                    <Nav.Link>Тарифы</Nav.Link>
                    <Nav.Link>Обратная связь</Nav.Link>
                    <Nav.Link>FAQ</Nav.Link>
                </Nav>

            </Container>
        </Navbar>
    )
}

export default Footer
