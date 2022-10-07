import React from 'react'
import {useDispatch, useSelector} from 'react-redux'
import {Navbar, Nav, Container, NavDropdown, Image} from 'react-bootstrap'
import {LinkContainer} from 'react-router-bootstrap'
import NavbarCollapse from "react-bootstrap/NavbarCollapse";


function Header() {


    return (

            <Navbar fixed='top' variant='light' expand='lg' bg='white'
                className="border-bottom">
                <Container fluid>
                    <Navbar.Brand className="m-2 m-lg-3 pb-1" href="/">
                        <Image id="LogoImage" src="/images/Logo.png"/>
                    </Navbar.Brand>

                    <Navbar.Toggle aria-controls="basic-navbar-nav" className=""/>



                    <Navbar.Collapse className="navbar-collapse collapse" id="navbarResponsive">
                        <ul className="header-layout nav navbar-nav">
                            <li className="nav-item active m-2">
                                <Nav.Link href="/" className="nav-link active" aria-current="page">Главная</Nav.Link>
                            </li>
                            <li className="nav-item m-2">
                                <Nav.Link
                                    href="/about" className="nav-link text-nowrap" aria-disabled="true">О нас</Nav.Link>
                            </li>
                            <li className="nav-item m-2">
                                <a href="" className="nav-link">Наши услуги</a>
                            </li>
                            <li className="nav-item m-2">
                                <a href="/stores_list" className="nav-link">Тарифы</a>
                            </li>
                            <li className="nav-item m-2">
                                <a href="/stores_list" className="nav-link">Контакты</a>
                            </li>
                            <li className="nav-item m-2">
                                <a href="/stores_list" className="nav-link">FAQ</a>
                            </li>
                            <li className="nav-item reg-block pt-lg-1 m-1">
                                <div className="row flex-nowrap m-0 p-0 h-100">
                                    <div className="row pb-0 mb-0 mt-1 mx-2 collapse" id="collapseLogData">
                                        <form id="authorizationUserForm" className="w-50 pb-0 mb-0">
                                            <div className="row col-lg-8 col-12 mb-0 pb-0 flex-lg-nowrap g-2">
                                                <button id="EnterButton" type="submit"
                                                        className="btn btn-sm btn-primary col-2 p-0 mx-2">
                                                    <span id="logInSpinner"
                                                          className="spinner-border spinner-border-sm d-none"
                                                          role="status" aria-hidden="true"></span>
                                                    <i className="bi bi-box-arrow-in-right mr-3"></i>
                                                </button>
                                                <input className="form-control form-control-sm col-lg-4 col-6"
                                                       type="text" name="username" placeholder="Логин"/>
                                                <input
                                                    className="form-control form-control-sm col-lg-4 col-6 mx-lg-2"
                                                    type="password" name="password" placeholder="Пароль"/>
                                                <a href="/social/login/vk-oauth2"
                                                   className="btn btn-primary col-3 mx-1">
                                                    <i className="fab fa-vk"></i>
                                                </a>
                                                <a href="/social/login/google-oauth2"
                                                   className="btn btn-danger col-3 mx-2">
                                                    <i className="bi bi-google"></i>
                                                </a>
                                                <a href=""
                                                   className="btn btn-light col-3 mx-1">
                                                    <i className="fab fa-yandex text-danger"></i>
                                                </a>
                                            </div>
                                            <div
                                                className="errorAuthMessage text-danger form-text w-100 fade position-absolute">Sometext
                                            </div>
                                        </form>
                                    </div>

                                    <button type="button" id="LogInButton"
                                            className="log-button btn btn-outline-primary bg-gradient rounded-circle m-2 m-lg-0"
                                            data-bs-toggle="collapse" data-bs-target="#collapseLogData"
                                            aria-expanded="false" aria-controls="collapseLogData">
                                        <i className="bi bi-arrow-right-circle-fill"></i>
                                    </button>
                                    <button type="button" id="RegistrationButton"
                                            className="btn btn-outline-primary bg-gradient text-nowrap rounded-pill m-2 mt-lg-0 p-0 col-5 col-md-3 col-lg-12"
                                            data-bs-toggle="modal" data-bs-target="#modalReg">Регистрация
                                    </button>
                                </div>
                            </li>
                        </ul>
                    </Navbar.Collapse>
                </Container>
            </Navbar>



    )
}

export default Header