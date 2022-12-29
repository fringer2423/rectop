// Chakra imports
import {
    Avatar,
    Button,
    Flex,
    Text,
    useColorModeValue,
} from "@chakra-ui/react";
// Assets
import picCompany from "../../../../assets/svg/globe.svg";

// Custom components
import Card from "../../../../components/components/Card/Card";
import CardBody from "../../../../components/components/Card/CardBody";
import CardHeader from "../../../../components/components/Card/CardHeader";
import React from "react";

const Conversations = ({title}) => {
    // Chakra color mode
    const textColor = useColorModeValue("gray.700", "white");

    return (
        <Card p='16px'>
            <CardHeader p='12px 5px' mb='12px'>
                <Text fontSize='lg' color={textColor} fontWeight='bold'>
                    {title}
                </Text>
            </CardHeader>
            <CardBody px='5px'>
                <Flex direction='column' w='100%'>
                    <Flex justifyContent='space-between' mb='21px'>
                        <Flex align='center'>
                            <Avatar
                                src={picCompany}
                                w='50px'
                                h='50px'
                                borderRadius='15px'
                                me='10px'
                            />
                            <Flex direction='column'>
                                <Text fontSize='sm' color={textColor} fontWeight='bold'>
                                    Компания
                                </Text>
                                <Text fontSize='xs' color='gray.500' fontWeight='400'>
                                    Билайн
                                </Text>
                            </Flex>
                        </Flex>
                    </Flex>
                    <Button colorscheme="maincolor" variant="outline">
                        Добвить компанию
                    </Button>
                </Flex>
            </CardBody>
        </Card>
    );
};

export default Conversations;
