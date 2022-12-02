import React, {useState, useEffect} from 'react';
import {useDispatch, useSelector} from 'react-redux';
import {validateEmail} from '../helpers/registerValidator.js';
import {login, verify, checkLogin, verifyLogin} from "../actions/userActions.js";
import {useHistory, Route, Redirect} from "react-router";

import {Spinner, Modal, InputGroup, Form, Alert} from 'react-bootstrap';

import store from '../store';

import {
    Box,
    Flex,
    Button,
    FormControl,
    FormLabel,
    Heading,
    Input,
    Link,
    Switch,
    Text,
    useColorModeValue,
} from "@chakra-ui/react";

import signInImage from "../assets/img/signInImage.png";

import {LinkContainer} from 'react-router-bootstrap';


const LogIn = () => {

    const titleColor = useColorModeValue("maincolor");
    const textColor = useColorModeValue("gray.400", "white");

    const dispatch = useDispatch();
    let history = useHistory();

    const userLogin = useSelector(state => state.userLogin);
    const userVerifyLogin = useSelector(state => state.userVerifyLogin);
    const {error, loading, userInfo} = userLogin;
    const {error: errorVerify, loading: loadingVerify, userInfo: userVerify} = userVerifyLogin;


    const [mail, setMail] = useState('');
    const [password, setPassword] = useState('');

    const [mailError, setMailError] = useState('');
    const [modal, setModal] = useState(false);
    const [code, setCode] = useState('');
    const [message, setMessage] = useState('');
    const [errorColor, setErrorColor] = useState('');


    const user = localStorage.getItem('userInfo');


    useEffect(() => {
        if (userInfo !== null && userInfo !== undefined && !user) {
            if (userInfo.is_verified) {
                setModal(true);
                dispatch(checkLogin());
            } else {
                setMessage('Пожалуйста, активируйте ваш аккаунт, вся информация у вас на почте.')
            }
        }
    }, [userInfo]);



    function loginButton() {
        if (validateEmail(mail) === true && password !== '') {
            dispatch(login(mail, password));
        }
        else {
            setErrorColor('red.100');
        }
    }

    function handleCheckCode() {
        dispatch(verifyLogin(code));
        setModal(false);

        if (!errorVerify) {
            history.push('/dashboard/');
            window.location.reload();
        }
        else {
            setMessage("Вы ввели не тот код");
        }


        //window.location.reload();
    }

    return (
        <>
            <Modal show={modal} animation={false}>
                <Modal.Header>
                    <Modal.Title>Введите код подтверждения, отправленный вам на почту</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <InputGroup>
                        <Form.Control
                            placeholder="Введите код"
                            aria-label="Code"
                            aria-describedby="basic-addon1"
                            value={code}
                            onChange={(e) => setCode(e.target.value)}
                        />
                    </InputGroup>
                    {loadingVerify &&
                        <Spinner animation="border" variant='primary'/>}
                </Modal.Body>
                <Modal.Footer>
                    <Button colorScheme="blue" variant="outline" onClick={handleCheckCode}>
                        Отправить код
                    </Button>
                </Modal.Footer>
            </Modal>
            <Flex position='relative' mb='40px'>
                <Flex
                    h={{sm: "initial", md: "75vh", lg: "85vh"}}
                    w='100%'
                    maxW='1044px'
                    mx='auto'
                    justifyContent='space-between'
                    mb='30px'
                    pt={{sm: "100px", md: "0px"}}>
                    <Flex
                        alignItems='center'
                        justifyContent='start'
                        style={{userSelect: "none"}}
                        w={{base: "100%", md: "50%", lg: "42%"}}>
                        <Flex
                            direction='column'
                            w='100%'
                            background='transparent'
                            p='48px'
                            mt={{md: "150px", lg: "80px"}}>
                            <Heading color={titleColor} fontSize='32px' mb='10px'>
                                Добро пожаловать
                            </Heading>
                            <Text
                                mb='36px'
                                ms='4px'
                                color={textColor}
                                fontWeight='bold'
                                fontSize='14px'>
                                Введите свой пароль и электронную почту, чтобы войти
                            </Text>
                            <FormControl>
                                <FormLabel ms='4px' fontSize='sm' fontWeight='normal'>
                                    Email
                                </FormLabel>
                                <Input
                                    borderRadius='15px'
                                    mb='24px'
                                    fontSize='sm'
                                    type='text'
                                    placeholder='Ваш email'
                                    size='lg'
                                    bg={errorColor}
                                    value={mail}
                                    onChange={(e) => setMail(e.target.value)}
                                />
                                <FormLabel ms='4px' fontSize='sm' fontWeight='normal'>
                                    Пароль
                                </FormLabel>
                                <Input
                                    borderRadius='15px'
                                    mb='36px'
                                    fontSize='sm'
                                    type='password'
                                    placeholder='Ваш пароль'
                                    size='lg'
                                    bg={errorColor}
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                />
                                <FormControl display='flex' alignItems='center'>
                                    <Switch id='remember-login' me='10px'/>
                                    <FormLabel
                                        htmlFor='remember-login'
                                        mb='0'
                                        ms='1'
                                        fontWeight='normal'>
                                        Запомнить меня
                                    </FormLabel>
                                </FormControl>
                                {loading &&
                                    <Spinner animation="border" variant='primary'/>}
                                {error &&
                                    <FormControl display='flex' alignItems='center'>
                                        <FormLabel
                                            htmlFor='remember-login'
                                            mb='0'
                                            ms='1'
                                            color='red'
                                            fontWeight='normal'>
                                            {error}
                                        </FormLabel>
                                    </FormControl>
                                }
                                {message != '' &&
                                    <Alert variant="primary" className="d-flex justify-content-center">
                                        {message}
                                    </Alert>
                                }
                                <Button
                                    onClick={loginButton}
                                    fontSize='10px'
                                    type='submit'
                                    bg='maincolor'
                                    w='100%'
                                    h='45'
                                    mb='20px'
                                    color='white'
                                    mt='20px'
                                    _hover={{
                                        bg: "secondary",
                                    }}
                                    _active={{
                                        bg: "secondary",
                                    }}>
                                    ВОЙТИ
                                </Button>
                            </FormControl>
                            <Flex
                                flexDirection='column'
                                justifyContent='center'
                                alignItems='center'
                                maxW='100%'
                                mt='0px'>
                                <Text color={textColor} fontWeight='medium'>
                                    У Вас ещё нет аккаунта?
                                    <Link color={titleColor} as='span' ms='5px' fontWeight='bold'>
                                        Регистрация
                                    </Link>
                                </Text>
                            </Flex>
                        </Flex>
                    </Flex>
                    <Box
                        display={{base: "none", md: "block"}}
                        overflowX='hidden'
                        h='100%'
                        w='40vw'
                        position='absolute'
                        right='0px'>
                        <Box
                            bgImage={signInImage}
                            w='100%'
                            h='100%'
                            bgSize='cover'
                            bgPosition='50%'
                            position='absolute'
                            borderBottomLeftRadius='20px'></Box>
                    </Box>
                </Flex>
            </Flex>
        </>
    );
}

export default LogIn;
