import React from 'react'
import {useDispatch, useSelector} from 'react-redux'
import {Navbar, Nav, Container, NavDropdown} from 'react-bootstrap'
import {LinkContainer} from 'react-router-bootstrap'


function Footer() {


    return (
        <footer className="w-100 bg-primary">
            <div className="row mt-5 p-lg-4 p-5 w-100">
                <div className="col-lg-4 col-10">
                    <img id="whiteLogoImage" className="mb-4" src="/images/whiteLogo.png"/>
                        <div className="col-lg-6 col-11 mb-5 mb-lg-0"><small className="text-light logo-txt">Мы
                            используем куки, это позволяет улучшить ваш пользовательский опыт</small></div>
                </div>

                <ul className="nav flex-column col-lg-3 col-9 text-white">
                    <li className="nav-item">
                        <h5 className="nav-link text-light">Навигация</h5>
                    </li>
                    <li className="nav-item col-lg-3 mt-1">
                        <a className="nav-txt nav-link text-light" href="">Главная</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-txt nav-link text-light" href="">О нас</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-txt nav-link text-light" href="">Как мы работаем</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-txt nav-link text-light" href="">Тарифы</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-txt nav-link text-light" href="">Обратная связь</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-txt nav-link text-light" href="">FAQ</a>
                    </li>
                </ul>

                <ul className="nav flex-column col-lg-3 col-9 text-white mt-3 mt-lg-0">
                    <li className="nav-item">
                        <h5 className="nav-link text-light">Контакты</h5>
                    </li>
                    <li className="nav-item col-lg-3 mt-1">
                        <span className="nav-txt nav-link text-light" href="">business@rectop.ru</span>
                    </li>
                    <li className="nav-item">
                        <span className="nav-txt nav-link text-light" href="">+7 (999) 888-77-66</span>
                    </li>
                    <li className="nav-item">
                        <a className="nav-txt nav-link text-light text-decoration-underline" href="">Политика
                            конфиденциальности</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-txt nav-link text-light text-decoration-underline" href="">Лицензионный
                            договор</a>
                    </li>

                    <li className="nav-item m-3">
                        <div className="row mt-3">
                            <div className="col-lg-2 col-4 m-2 m-lg-1">
                                <i id="tgButtonImage" className="bi bi-telegram"></i>
                            </div>
                            <div id="vkButtonImage" className="col-lg-2 col-4 rounded-circle bg-white m-2 m-lg-1">
                                <i className="fab fa-vk text-primary"></i>
                            </div>
                        </div>
                    </li>
                </ul>

                <span className="col-lg-10 col-9 text-light logo-txt mt-3">© 2018–2022 Rectop - агрегатор отзывов</span>
            </div>
        </footer>
    )
}

export default Footer