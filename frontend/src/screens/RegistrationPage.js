import React, {useState, useEffect} from "react";

import {useDispatch, useSelector} from "react-redux";

import {Alert} from "react-bootstrap";

import {register} from "../actions/userActions.js";

import {
    Box,
    Button,
    Flex,
    FormControl,
    FormLabel,
    HStack,
    Icon,
    Input,
    Link,
    Switch,
    Text,
    useColorModeValue,
} from "@chakra-ui/react";

import bgSignUp from "../assets/img/bgSignUp.png";
import {FaApple, FaFacebook, FaGoogle} from "react-icons/fa";

import {
    validateEmail,
    validatePassword,
} from "../helpers/registerValidator.js";

const RegistrationPage = () => {
    const [mail, setMail] = useState("");
    const [name, setName] = useState("");
    const [surname, setSurname] = useState("");
    const [password, setPassword] = useState("");
    const [passwordRepeat, setPasswordRepeat] = useState("");
    const dispatch = useDispatch();

    const titleColor = useColorModeValue("maincolor");
    const textColor = useColorModeValue("gray.700", "white");
    const bgColor = useColorModeValue("white", "gray.700");
    const bgIcons = useColorModeValue("maincolor", "rgba(255, 255, 255, 0.5)");
    const userRegister = useSelector((state) => state.userRegister);
    const {error, userInfo} = userRegister;
    const [errorColor, setErrorColor] = useState("");

    const handleRegistration = () => {
        if (
            validateEmail(mail) &&
            validatePassword(password, passwordRepeat) &&
            name !== "" &&
            surname !== ""
        ) {
            dispatch(register(name, surname, mail, password));
        } else {
            setErrorColor("red.100");
        }
    };

    return (
        <Flex
            direction="column"
            alignSelf="center"
            justifySelf="center"
            overflow="hidden"
        >
            <Box
                position="absolute"
                minH={{base: "70vh", md: "50vh"}}
                w={{md: "calc(100vw - 50px)"}}
                borderRadius={{md: "15px"}}
                left="0"
                right="0"
                bgRepeat="no-repeat"
                overflow="hidden"
                zIndex="-1"
                top="0"
                bgImage={bgSignUp}
                bgSize="cover"
                mx={{md: "auto"}}
                mt={{md: "14px"}}
            ></Box>
            <Flex
                direction="column"
                textAlign="center"
                justifyContent="center"
                align="center"
                mt="6.5rem"
                mb="30px"
            >
                <Text fontSize="4xl" color={textColor} fontWeight="bold">
                    ?????????? ????????????????????!
                </Text>
                <Text
                    fontSize="md"
                    color={textColor}
                    fontWeight="normal"
                    mt="10px"
                    mb="26px"
                    w={{base: "90%", sm: "60%", lg: "40%", xl: "30%"}}
                >
                    ???????? ?? ?????? ?????? ?????? ????????????????, ????????????????????, ?????????????????? ??????????
                </Text>
            </Flex>
            <Flex
                alignItems="center"
                justifyContent="center"
                mb="60px"
                mt="20px"
            >
                <Flex
                    direction="column"
                    w="445px"
                    background="transparent"
                    borderRadius="15px"
                    p="40px"
                    mx={{base: "100px"}}
                    bg={bgColor}
                    boxShadow="0 20px 27px 0 rgb(0 0 0 / 5%)"
                >
                    <Text
                        fontSize="xl"
                        color={textColor}
                        fontWeight="bold"
                        textAlign="center"
                        mb="22px"
                    >
                        ?????????????????????? ??
                    </Text>
                    <HStack spacing="15px" justify="center" mb="22px">
                        <Flex
                            justify="center"
                            align="center"
                            w="75px"
                            h="75px"
                            borderRadius="15px"
                            border="1px solid lightgray"
                            cursor="pointer"
                            transition="all .25s ease"
                           _hover={{filter: "brightness(120%)", bg: bgIcons}}
                        >
                            <Link href="#">
                                <Icon
                                    as={FaFacebook}
                                    w="30px"
                                    h="30px"
                                   _hover={{filter: "brightness(120%)"}}
                                />
                            </Link>
                        </Flex>
                        <Flex
                            justify="center"
                            align="center"
                            w="75px"
                            h="75px"
                            borderRadius="15px"
                            border="1px solid lightgray"
                            cursor="pointer"
                            transition="all .25s ease"
                           _hover={{filter: "brightness(120%)", bg: bgIcons}}
                        >
                            <Link href="#">
                                <Icon
                                    as={FaApple}
                                    w="30px"
                                    h="30px"
                                   _hover={{filter: "brightness(120%)"}}
                                />
                            </Link>
                        </Flex>
                        <Flex
                            justify="center"
                            align="center"
                            w="75px"
                            h="75px"
                            borderRadius="15px"
                            border="1px solid lightgray"
                            cursor="pointer"
                            transition="all .25s ease"
                           _hover={{filter: "brightness(120%)", bg: bgIcons}}
                        >
                            <Link href="#">
                                <Icon
                                    as={FaGoogle}
                                    w="30px"
                                    h="30px"
                                   _hover={{filter: "brightness(120%)"}}
                                />
                            </Link>
                        </Flex>
                    </HStack>
                    <Text
                        fontSize="lg"
                        color="gray.400"
                        fontWeight="bold"
                        textAlign="center"
                        mb="22px"
                    >
                        ??????
                    </Text>
                    {error ? (
                        <FormControl display="flex" alignItems="center">
                            <FormLabel
                                htmlFor="remember-login"
                                color="red"
                                mb="0"
                                ms="1"
                                fontWeight="normal"
                            >
                                {error}
                            </FormLabel>
                        </FormControl>
                    ) : (
                        userInfo && (
                            <Alert
                                variant="primary"
                                className="d-flex justify-content-center"
                            >
                                ?????????????? ???? ??????????????????????! ?????????? ?????? ??????????
                                ???????????????????????? ??????????????. ?????? ???????????????????? ?? ?????? ????
                                ??????????.
                            </Alert>
                        )
                    )}
                    <FormControl>
                        <FormLabel ms="4px" fontSize="sm" fontWeight="normal">
                            ??????
                        </FormLabel>
                        <Input
                            bg={errorColor}
                            fontSize="sm"
                            ms="4px"
                            borderRadius="15px"
                            type="text"
                            placeholder="???????? ???????????? ??????"
                            mb="24px"
                            size="lg"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                        />
                        <FormLabel ms="4px" fontSize="sm" fontWeight="normal">
                            ??????????????
                        </FormLabel>
                        <Input
                            bg={errorColor}
                            fontSize="sm"
                            ms="4px"
                            borderRadius="15px"
                            type="text"
                            placeholder="???????? ??????????????"
                            mb="24px"
                            size="lg"
                            value={surname}
                            onChange={(e) => setSurname(e.target.value)}
                        />
                        <FormLabel ms="4px" fontSize="sm" fontWeight="normal">
                            Email
                        </FormLabel>
                        <Input
                            bg={errorColor}
                            fontSize="sm"
                            ms="4px"
                            borderRadius="15px"
                            type="email"
                            placeholder="?????? email"
                            mb="24px"
                            size="lg"
                            value={mail}
                            onChange={(e) => setMail(e.target.value)}
                        />
                        <FormLabel ms="4px" fontSize="sm" fontWeight="normal">
                            ????????????
                        </FormLabel>
                        <Input
                            bg={errorColor}
                            fontSize="sm"
                            ms="4px"
                            borderRadius="15px"
                            type="password"
                            placeholder="?????? ????????????"
                            mb="24px"
                            size="lg"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        <FormLabel ms="4px" fontSize="sm" fontWeight="normal">
                            ?????????????????? ????????????
                        </FormLabel>
                        <Input
                            bg={errorColor}
                            fontSize="sm"
                            ms="4px"
                            borderRadius="15px"
                            type="password"
                            placeholder="?????????????????? ?????? ????????????"
                            mb="24px"
                            size="lg"
                            value={passwordRepeat}
                            onChange={(e) => setPasswordRepeat(e.target.value)}
                        />
                        <FormControl
                            display="flex"
                            alignItems="center"
                            mb="24px"
                        >
                            <Switch
                                id="remember-login"
                                colorscheme="maincolor"
                                me="10px"
                            />
                            <FormLabel
                                htmlFor="remember-login"
                                mb="0"
                                fontWeight="normal"
                            >
                                ?????????????????? ????????
                            </FormLabel>
                        </FormControl>
                        <Button
                            type="submit"
                            bg="maincolor"
                            fontSize="10px"
                            color="white"
                            fontWeight="bold"
                            w="100%"
                            h="45"
                            mb="24px"
                            onClick={handleRegistration}
                           _hover={{
                                bg: "secondary",
                            }}
                            _active={{
                                bg: "secondary",
                            }}
                        >
                            ????????????????????????????????????
                        </Button>
                    </FormControl>
                    <Flex
                        flexDirection="column"
                        justifyContent="center"
                        alignItems="center"
                        maxW="100%"
                        mt="0px"
                    >
                        <Text color={textColor} fontWeight="medium">
                            ?? ?????? ?????? ???????? ???????????????
                            <Link
                                color={titleColor}
                                as="span"
                                ms="5px"
                                href="#"
                                fontWeight="bold"
                            >
                                ??????????
                            </Link>
                        </Text>
                    </Flex>
                </Flex>
            </Flex>
        </Flex>
    );
};

export default RegistrationPage;
