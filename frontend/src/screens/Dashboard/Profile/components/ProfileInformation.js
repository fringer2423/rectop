// Chakra imports
import {Flex, Icon, Link, Text, useColorModeValue} from "@chakra-ui/react";
// Custom components
import Card from "../../../../components/components/Card/Card";
import CardBody from "../../../../components/components/Card/CardBody";
import CardHeader from "../../../../components/components/Card/CardHeader";
import React from "react";
import {FaFacebook, FaInstagram, FaTwitter} from "react-icons/fa";

const ProfileInformation = ({
                                title,
                                description,
                                mobile,
                                rate,
                                job,
                                name,
                                email,
                            }) => {
    // Chakra color mode
    const textColor = useColorModeValue("gray.700", "white");

    return (
        <Card p='16px' my={{sm: "24px", xl: "0px"}}>
            <CardHeader p='12px 5px' mb='12px'>
                <Text fontSize='lg' color={textColor} fontWeight='bold'>
                    {title}
                </Text>
            </CardHeader>
            <CardBody px='5px'>
                <Flex direction='column'>
                    <Text fontSize='md' color='gray.500' fontWeight='400' mb='30px'>
                        {description === "" ? "Придумайте себе описание профиля" : description}
                    </Text>
                    <Flex align='center' mb='18px'>
                        <Text fontSize='md' color={textColor} fontWeight='bold' me='10px'>
                            Полное имя:{" "}
                        </Text>
                        <Text fontSize='md' color='gray.500' fontWeight='400'>
                            {name}
                        </Text>
                    </Flex>
                    <Flex align='center' mb='18px'>
                        <Text fontSize='md' color={textColor} fontWeight='bold' me='10px'>
                            Email:{" "}
                        </Text>
                        <Text fontSize='md' color='gray.500' fontWeight='400'>
                            {email}
                        </Text>
                    </Flex>
                    { mobile !== "" &&
                        <Flex align='center' mb='18px'>
                            <Text fontSize='md' color={textColor} fontWeight='bold' me='10px'>
                                Мобильный телефон:{" "}
                            </Text>
                            <Text fontSize='md' color='gray.500' fontWeight='400'>
                                {mobile}
                            </Text>
                        </Flex>
                    }
                    { rate &&
                        <Flex align='center' mb='18px'>
                            <Text fontSize='md' color={textColor} fontWeight='bold' me='10px'>
                                Информация о тарифе:{" "}
                            </Text>
                            <Text fontSize='md' color='gray.500' fontWeight='400'>
                                {email}
                            </Text>
                        </Flex>
                    }
                    { job !== "" &&
                        <Flex align='center' mb='18px'>
                            <Text fontSize='md' color={textColor} fontWeight='bold' me='10px'>
                                Информация о тарифе:{" "}
                            </Text>
                            <Text fontSize='md' color='gray.500' fontWeight='400'>
                                {job}
                            </Text>
                        </Flex>
                    }
                    <Flex align='center' mb='18px'>
                        <Text fontSize='md' color={textColor} fontWeight='bold' me='10px'>
                            Социальные сети:{" "}
                        </Text>
                        <Flex>
                            <Link
                                href='#'
                                color='maincolor'
                                fontSize='lg'
                                me='10px'
                                _hover={{color: "maincolor"}}>
                                <Icon as={FaFacebook}/>
                            </Link>
                            <Link
                                href='#'
                                color='maincolor'
                                fontSize='lg'
                                me='10px'
                                _hover={{color: "maincolor"}}>
                                <Icon as={FaInstagram}/>
                            </Link>
                            <Link
                                href='#'
                                color='maincolor'
                                fontSize='lg'
                                me='10px'
                                _hover={{color: "maincolor"}}>
                                <Icon as={FaTwitter}/>
                            </Link>
                        </Flex>
                    </Flex>
                </Flex>
            </CardBody>
        </Card>
    );
};

export default ProfileInformation;
