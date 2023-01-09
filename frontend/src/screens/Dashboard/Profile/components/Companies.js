// Chakra imports
import {Avatar, Button, Flex, Text, useColorModeValue} from "@chakra-ui/react";
// Assets
import picCompany from "../../../../assets/svg/globe.svg";

// Custom components
import Card from "../../../../components/components/Card/Card";
import CardBody from "../../../../components/components/Card/CardBody";
import CardHeader from "../../../../components/components/Card/CardHeader";
import React, {useState} from "react";

import {useDispatch} from "react-redux";

import {Modal, InputGroup, Form, CloseButton} from "react-bootstrap";

import {createCompany, updateCompany, deleteCompany} from "../../../../actions/companyActions";

const Conversations = ({title, companyInfo}) => {
    // Chakra color mode
    const textColor = useColorModeValue("gray.700", "white");

    const dispatch = useDispatch();

    const [showCreate, setShowCreate] = useState(false);
    const [showEdit, setShowEdit] = useState(false);
    const [showWarning, setShowWarning] = useState(false);

    const [nameCreate, setNameCreate] = useState("");
    const [nameEdit, setNameEdit] = useState("");

    const [warning, setWarning] = useState("");

    const handleCompanyButton = () => {
        if (companyInfo === null) {
            setShowCreate(true);
        } else {
            setShowEdit(true);
        }
    };

    const handleCreate = () => {
        if (nameCreate !== "") {
            setWarning("");
            dispatch(createCompany(nameCreate));
            setShowCreate(false);
        } else {
            setWarning("Заполните пожалуйста название компании");
        }
    };

    const handleEdit = () => {
        if (nameEdit !== "") {
            setWarning("");
            dispatch(updateCompany(nameEdit, companyInfo.id));
            setShowEdit(false);
        } else {
            setWarning("Заполните пожалуйста название компании");
        }
    };

    const handleWarningDelete = () => {
        setShowWarning(true);
    };

    const handleDeleteCompany = () => {
        dispatch(deleteCompany(companyInfo.id));
        console.log(companyInfo);
        setShowWarning(false);
    };

    return (
        <>
            <Modal show={showCreate} onHide={() => setShowCreate(false)}>
                <Modal.Header closeButton>
                    <Modal.Title>Создать компанию</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Form.Label htmlFor="basic-url">
                        Введите название своей компании
                    </Form.Label>
                    <InputGroup className="mb-3">
                        <Form.Control
                            id="basic-url"
                            aria-describedby="basic-addon3"
                            value={nameCreate}
                            onChange={(e) => setNameCreate(e.target.value)}
                            placeholder="Название"
                        />
                    </InputGroup>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="outline" onClick={handleCreate}>
                        Создать
                    </Button>
                    {warning}
                </Modal.Footer>
            </Modal>
            <Modal show={showEdit} onHide={() => setShowEdit(false)}>
                <Modal.Header closeButton>
                    <Modal.Title>Изменить компанию</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Form.Label htmlFor="basic-url">
                        Введите название своей компании
                    </Form.Label>
                    <InputGroup className="mb-3">
                        <Form.Control
                            id="basic-url"
                            aria-describedby="basic-addon3"
                            placeholder="Название"
                            value={nameEdit}
                            onChange={(e) => setNameEdit(e.target.value)}
                        />
                    </InputGroup>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="outline" onClick={handleEdit}>
                        Сохранить
                    </Button>
                    {warning}
                </Modal.Footer>
            </Modal>
            <Modal
                size="lg"
                aria-labelledby="contained-modal-title-vcenter"
                centered
                show={showWarning}
                onHide={() => setShowWarning(false)}
            >
                <Modal.Header closeButton>
                </Modal.Header>
                <Modal.Body>
                    Вы действительно хотите удалить компанию?
                </Modal.Body>
                <Modal.Footer>
                    <Button colorScheme="red" onClick={handleDeleteCompany}>Удалить</Button>
                </Modal.Footer>
            </Modal>
            <Card p="16px">
                <CardHeader p="12px 5px" mb="12px">
                    <Text fontSize="lg" color={textColor} fontWeight="bold">
                        {title}
                    </Text>
                </CardHeader>
                <CardBody px="5px">
                    <Flex direction="column" w="100%">
                        {(companyInfo)  && (
                            <Flex justifyContent="space-between" mb="21px">
                                <Flex align="center">
                                    <Avatar
                                        src={picCompany}
                                        w="50px"
                                        h="50px"
                                        borderRadius="15px"
                                        me="10px"
                                    />
                                    <Flex direction="column">
                                        <Text
                                            fontSize="sm"
                                            color={textColor}
                                            fontWeight="bold"
                                        >
                                            Компания
                                        </Text>
                                        <Text
                                            fontSize="xs"
                                            color="gray.500"
                                            fontWeight="400"
                                        >
                                            {companyInfo.name}
                                        </Text>
                                    </Flex>
                                </Flex>
                                <Flex align="center" mx="10px">
                                    <CloseButton
                                        onClick={handleWarningDelete}
                                    />
                                </Flex>
                            </Flex>
                        )}
                        <Button variant="outline" onClick={handleCompanyButton}>
                            {companyInfo
                                ? "Редактировать"
                                : "Добавить компанию"}
                        </Button>
                    </Flex>
                </CardBody>
            </Card>
        </>
    );
};

export default Conversations;
