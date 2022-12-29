// Chakra imports
import {
    Flex,
    Switch,
    Text,
    Input,
    InputGroup,
    useColorModeValue,
    Button
} from "@chakra-ui/react";
// Custom components
import Card from "../../../../components/components/Card/Card";
import CardBody from "../../../../components/components/Card/CardBody";
import CardHeader from "../../../../components/components/Card/CardHeader";
import React from "react";

const PlatformSettings = ({title, subtitle1, subtitle2, subtitle3, subtitle4, subtitle5, subtitle6, subtitle7}) => {
    // Chakra color mode
    const textColor = useColorModeValue("gray.700", "white");
    const maincolor = useColorModeValue("maincolor", "maincolor");
    const searchIconColor = useColorModeValue("gray.700", "gray.200");
    const inputBg = useColorModeValue("white", "gray.800");
    return (
        <Card p='16px'>
            <CardHeader p='12px 5px' mb='12px'>
                <Text fontSize='lg' color={textColor} fontWeight='bold'>
                    {title}
                </Text>
            </CardHeader>
            <CardBody px='5px'>
                <Flex direction='column'>
                    <Text fontSize='sm' color='gray.500' fontWeight='600' mb='20px'>
                        {subtitle1}
                    </Text>
                    <Flex align='center' mb='20px'>
                        <InputGroup
                            bg={inputBg}
                            borderRadius="15px"
                            w="300px"
                            _focus={{
                                borderColor: {maincolor},
                            }}
                            _active={{
                                borderColor: {maincolor},
                            }}
                        >
                            <Input
                                fontSize="xs"
                                py="11px"
                                borderRadius="inherit"
                            />
                        </InputGroup>
                    </Flex>
                    <Text
                        fontSize='sm'
                        color='gray.500'
                        fontWeight='600'
                        m='6px 0px 20px 0px'>
                        {subtitle2}
                    </Text>
                    <Flex align='center' mb='20px'>
                        <InputGroup
                            bg={inputBg}
                            borderRadius="15px"
                            w="300px"
                            _focus={{
                                borderColor: {maincolor},
                            }}
                            _active={{
                                borderColor: {maincolor},
                            }}
                        >
                            <Input
                                fontSize="xs"
                                py="11px"
                                borderRadius="inherit"
                            />
                        </InputGroup>
                    </Flex>
                    <Text
                        fontSize='sm'
                        color='gray.500'
                        fontWeight='600'
                        m='6px 0px 20px 0px'>
                        {subtitle3}
                    </Text>
                    <Flex align='center' mb='20px'>
                        <InputGroup
                            bg={inputBg}
                            borderRadius="15px"
                            w="300px"
                            _focus={{
                                borderColor: {maincolor},
                            }}
                            _active={{
                                borderColor: {maincolor},
                            }}
                        >
                            <Input
                                fontSize="xs"
                                py="11px"
                                borderRadius="inherit"
                            />
                        </InputGroup>
                    </Flex>
                    <Text
                        fontSize='sm'
                        color='gray.500'
                        fontWeight='600'
                        m='6px 0px 20px 0px'>
                        {subtitle4}
                    </Text>
                    <Flex align='center' mb='20px'>
                        <InputGroup
                            bg={inputBg}
                            borderRadius="15px"
                            w="300px"
                            h="200px"
                            _focus={{
                                borderColor: {maincolor},
                            }}
                            _active={{
                                borderColor: {maincolor},
                            }}
                        >
                            <textarea className="w-100 h-100 fs-6 p-1 border rounded"></textarea>
                        </InputGroup>
                    </Flex>
                    <Text
                        fontSize='sm'
                        color='gray.500'
                        fontWeight='600'
                        m='6px 0px 20px 0px'>
                        {subtitle5}
                    </Text>
                    <Flex align='center' mb='20px'>
                        <InputGroup
                            bg={inputBg}
                            borderRadius="15px"
                            w="300px"
                            _focus={{
                                borderColor: {maincolor},
                            }}
                            _active={{
                                borderColor: {maincolor},
                            }}
                        >
                            <Input
                                fontSize="xs"
                                py="11px"
                                borderRadius="inherit"
                            />
                        </InputGroup>
                    </Flex>
                    <Text
                        fontSize='sm'
                        color='gray.500'
                        fontWeight='600'
                        m='6px 0px 20px 0px'>
                        {subtitle6}
                    </Text>
                    <Flex align='center' mb='20px'>
                        <InputGroup
                            bg={inputBg}
                            borderRadius="15px"
                            w="300px"
                            _focus={{
                                borderColor: {maincolor},
                            }}
                            _active={{
                                borderColor: {maincolor},
                            }}
                        >
                            <Input
                                fontSize="xs"
                                py="11px"
                                borderRadius="inherit"
                            />
                        </InputGroup>
                    </Flex>
                    <Text
                        fontSize='sm'
                        color='gray.500'
                        fontWeight='600'
                        m='6px 0px 20px 0px'>
                        {subtitle7}
                    </Text>
                    <Flex align='center' mb='20px'>
                        <InputGroup
                            bg={inputBg}
                            borderRadius="15px"
                            w="300px"
                            _focus={{
                                borderColor: {maincolor},
                            }}
                            _active={{
                                borderColor: {maincolor},
                            }}
                        >
                            <Input
                                fontSize="xs"
                                py="11px"
                                borderRadius="inherit"
                            />
                        </InputGroup>
                    </Flex>
                    <Button colorscheme="maincolor" variant="outline">
                        Сохранить изменения
                    </Button>

                </Flex>
            </CardBody>
        </Card>
    );
};

export default PlatformSettings;
