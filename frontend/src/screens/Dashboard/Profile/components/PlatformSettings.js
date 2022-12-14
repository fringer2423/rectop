// Chakra imports
import {
    Flex,
    Switch,
    Text,
    Input,
    InputGroup,
    useColorModeValue,
    Button,
} from "@chakra-ui/react";
// Custom components
import Card from "../../../../components/components/Card/Card";
import CardBody from "../../../../components/components/Card/CardBody";
import CardHeader from "../../../../components/components/Card/CardHeader";
import React, {useState} from "react";
import {useDispatch, useSelector} from "react-redux";
import {updateUser} from "../../../../actions/userActions";

const PlatformSettings = ({
    title,
    subtitle1,
    subtitle2,
    subtitle3,
    subtitle4,
    subtitle5,
    subtitle6,
    subtitle7,
}) => {
    // Chakra color mode
    const textColor = useColorModeValue("gray.700", "white");
    const maincolor = useColorModeValue("maincolor", "maincolor");
    const searchIconColor = useColorModeValue("gray.700", "gray.200");
    const inputBg = useColorModeValue("white", "gray.800");

    const dispatch = useDispatch();

    const [name, setName] = useState("");
    const [surname, setSurname] = useState("");
    const [password, setPassword] = useState("");
    const [description, setDescription] = useState("");
    const [mobile, setMobile] = useState("");
    const [job, setJob] = useState("");
    const [email, setEmail] = useState("");
    const [necessaryText, setNecessaryText] = useState("");

    const userUpdate = useSelector((state) => state.userUpdate);
    const userDetails = useSelector((state) => state.userDetails);
    const {user, error: detailError} = userDetails;
    const {error} = userUpdate;

    let userUpdateInfo = {
        first_name: name,
        last_name: surname,
        password: password,
        description: description,
        phone_number: mobile,
        job_title: job,
        email: email,
    };

    const handleUpdateProfileInfo = () => {
        if (name !== "" && surname !== "" && password !== "") {
            dispatch(updateUser(userUpdateInfo));
            setNecessaryText("");
        } else {
            setNecessaryText("?????????????????? ???????????????????????? ????????");
        }
    };

    return (
        <Card p="16px">
            {detailError ? (
                <h1>?????????????????? ???????????? ?????? ???????????????? ????????????</h1>
            ) : (
                <CardHeader p="12px 5px" mb="12px">
                    <Flex direction="column">
                        <Text fontSize="lg" color={textColor} fontWeight="bold">
                            {title}
                        </Text>
                        <p className="text-secondary">
                            ???????????????????????? ???????? ???????????????? *
                        </p>
                        {error && (
                            <h5 className="text-danger">
                                ?????????????????? ???????????? ???????????????????? ????????????
                            </h5>
                        )}
                    </Flex>
                </CardHeader>
            )}
            {detailError ? (
                <h1>?????????????????? ???????????? ?????? ???????????????? ????????????</h1>
            ) : (
                <CardBody px="5px">
                    <Flex direction="column">
                        <Text
                            fontSize="sm"
                            color="gray.500"
                            fontWeight="600"
                            mb="20px"
                        >
                            {subtitle1}
                        </Text>
                        <Flex align="center" mb="20px">
                            <InputGroup
                                bg={inputBg}
                                borderRadius="15px"
                                w="250px"
                                _focus={{
                                    borderColor: {maincolor},
                                }}
                                _active={{
                                    borderColor: {maincolor},
                                }}
                            >
                                <Input
                                    value={name}
                                    onChange={(e) => setName(e.target.value)}
                                    fontSize="xs"
                                    py="11px"
                                    borderRadius="inherit"
                                />
                            </InputGroup>
                        </Flex>
                        <Text
                            fontSize="sm"
                            color="gray.500"
                            fontWeight="600"
                            m="6px 0px 20px 0px"
                        >
                            {subtitle2}
                        </Text>
                        <Flex align="center" mb="20px">
                            <InputGroup
                                bg={inputBg}
                                borderRadius="15px"
                                w="250px"
                                _focus={{
                                    borderColor: {maincolor},
                                }}
                                _active={{
                                    borderColor: {maincolor},
                                }}
                            >
                                <Input
                                    value={surname}
                                    onChange={(e) => setSurname(e.target.value)}
                                    fontSize="xs"
                                    py="11px"
                                    borderRadius="inherit"
                                />
                            </InputGroup>
                        </Flex>
                        <Text
                            fontSize="sm"
                            color="gray.500"
                            fontWeight="600"
                            m="6px 0px 20px 0px"
                        >
                            {subtitle3}
                        </Text>
                        <Flex align="center" mb="20px">
                            <InputGroup
                                bg={inputBg}
                                borderRadius="15px"
                                w="250px"
                                _focus={{
                                    borderColor: {maincolor},
                                }}
                                _active={{
                                    borderColor: {maincolor},
                                }}
                            >
                                <Input
                                    type='password'
                                    value={password}
                                    onChange={(e) =>
                                        setPassword(e.target.value)
                                    }
                                    fontSize="xs"
                                    py="11px"
                                    borderRadius="inherit"
                                />
                            </InputGroup>
                        </Flex>
                        <Text
                            fontSize="sm"
                            color="gray.500"
                            fontWeight="600"
                            m="6px 0px 20px 0px"
                        >
                            {subtitle4}
                        </Text>
                        <Flex align="center" mb="20px">
                            <InputGroup
                                bg={inputBg}
                                borderRadius="15px"
                                w="250px"
                                h="200px"
                                _focus={{
                                    borderColor: {maincolor},
                                }}
                                _active={{
                                    borderColor: {maincolor},
                                }}
                            >
                                <textarea
                                    className="form-control w-100 h-100 p-1 border rounded"
                                    value={description}
                                    style={{fontSize: "0.7rem"}}
                                    onChange={(e) =>
                                        setDescription(e.target.value)
                                    }
                                ></textarea>
                            </InputGroup>
                        </Flex>
                        <Text
                            fontSize="sm"
                            color="gray.500"
                            fontWeight="600"
                            m="6px 0px 20px 0px"
                        >
                            {subtitle5}
                        </Text>
                        <Flex align="center" mb="20px">
                            <InputGroup
                                bg={inputBg}
                                borderRadius="15px"
                                w="250px"
                                _focus={{
                                    borderColor: {maincolor},
                                }}
                                _active={{
                                    borderColor: {maincolor},
                                }}
                            >
                                <Input
                                    value={mobile}
                                    onChange={(e) => setMobile(e.target.value)}
                                    fontSize="xs"
                                    py="11px"
                                    borderRadius="inherit"
                                />
                            </InputGroup>
                        </Flex>
                        <Text
                            fontSize="sm"
                            color="gray.500"
                            fontWeight="600"
                            m="6px 0px 20px 0px"
                        >
                            {subtitle6}
                        </Text>
                        <Flex align="center" mb="20px">
                            <InputGroup
                                bg={inputBg}
                                borderRadius="15px"
                                w="250px"
                                _focus={{
                                    borderColor: {maincolor},
                                }}
                                _active={{
                                    borderColor: {maincolor},
                                }}
                            >
                                <Input
                                    value={job}
                                    onChange={(e) => setJob(e.target.value)}
                                    fontSize="xs"
                                    py="11px"
                                    borderRadius="inherit"
                                />
                            </InputGroup>
                        </Flex>
                        <Text
                            fontSize="sm"
                            color="gray.500"
                            fontWeight="600"
                            m="6px 0px 20px 0px"
                        >
                            {subtitle7}
                        </Text>
                        <Flex align="center" mb="20px">
                            <InputGroup
                                bg={inputBg}
                                borderRadius="15px"
                                w="250px"
                                _focus={{
                                    borderColor: {maincolor},
                                }}
                                _active={{
                                    borderColor: {maincolor},
                                }}
                            >
                                <Input
                                    value={email}
                                    onChange={(e) => setEmail(e.target.value)}
                                    fontSize="xs"
                                    py="11px"
                                    borderRadius="inherit"
                                />
                            </InputGroup>
                        </Flex>
                        {necessaryText !== "" && (
                            <p className="text-secondary">{necessaryText}</p>
                        )}
                        <Button
                            colorscheme="maincolor"
                            variant="outline"
                            onClick={handleUpdateProfileInfo}
                        >
                            ?????????????????? ??????????????????
                        </Button>
                    </Flex>
                </CardBody>
            )}
        </Card>
    );
};

export default PlatformSettings;
