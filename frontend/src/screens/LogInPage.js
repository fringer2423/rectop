import React, {useState} from 'react';
import {useDispatch, useSelector} from 'react-redux';
import {validateEmail} from '../helpers/registerValidator.js';
import {login} from "../actions/userActions.js";

import {Spinner} from 'react-bootstrap';

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


import {LinkContainer} from 'react-router-bootstrap'


const LogIn = () => {

    const titleColor = useColorModeValue("maincolor");
    const textColor = useColorModeValue("gray.400", "white");
    const dispatch = useDispatch();

    const userLogin = useSelector(state => state.userLogin);

    const [mail, setMail] = useState('');
    const [password, setPassword] = useState('');
    const {error, loading} = userLogin;
    const [mailError, setMailError] = useState('');


    const loginButton = () => {
        if(validateEmail(mail) === true && password != '') {
            dispatch(login(mail, password));
        }
    }



    return (
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
                                value ={mail}
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
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                            />
                            <FormControl display='flex' alignItems='center'>
                                <Switch id='remember-login'  me='10px'/>
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
                                        fontWeight='normal'>
                                        {error}
                                    </FormLabel>
                                </FormControl>
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
                                У Вас ещё нет акаунта?
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

    );
}

export default LogIn;
