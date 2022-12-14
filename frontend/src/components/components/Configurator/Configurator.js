// Chakra Imports
import {
    Box,
    Button,
    Drawer,
    DrawerBody,
    DrawerCloseButton,
    DrawerContent,
    DrawerHeader,
    Flex,
    Icon,
    Link,
    Switch,
    Text,
    useColorMode,
    useColorModeValue,
} from "@chakra-ui/react";
import GitHubButton from "react-github-btn";
import {Separator} from "../Separator/Separator";
import PropTypes from "prop-types";
import React, {useState} from "react";
import {FaTwitter, FaFacebook} from "react-icons/fa";

export default function Configurator(props) {
    const {secondary, isOpen, onClose, fixed, ...rest} = props;
    const [switched, setSwitched] = useState(props.isChecked);

    const {colorMode, toggleColorMode} = useColorMode();
    // Chakra Color Mode
    let fixedDisplay = "flex";
    if (props.secondary) {
        fixedDisplay = "none";
    }

    let bgButton = useColorModeValue(
        "linear-gradient(81.62deg, #313860 2.25%, #151928 79.87%)",
        "white"
    );
    let colorButton = useColorModeValue("white", "gray.700");
    const secondaryButtonBg = useColorModeValue("white", "transparent");
    const secondaryButtonBorder = useColorModeValue("gray.700", "white");
    const secondaryButtonColor = useColorModeValue("gray.700", "white");
    const settingsRef = React.useRef();
    return (
        <>
            <Drawer
                isOpen={props.isOpen}
                onClose={props.onClose}
                placement={document.documentElement.dir === "rtl" ? "left" : "right"}
                finalFocusRef={settingsRef}
                blockScrollOnMount={false}
            >
                <DrawerContent>
                    <DrawerHeader pt="24px" px="24px">
                        <DrawerCloseButton/>
                        <Text fontSize="xl" fontWeight="bold" mt="16px">
                            Настройки
                        </Text>
                        <Text fontSize="md" mb="16px">
                            Настройте тему своего личного кабинета
                        </Text>
                        <Separator/>
                    </DrawerHeader>
                    <DrawerBody w="340px" ps="24px" pe="40px">
                        <Flex flexDirection="column">
                            <Box>
                                <Text fontSize="md" fontWeight="600">
                                    Выберите тип навигационной панели
                                </Text>
                                <Text fontSize="sm" mb="16px">
                                    Выберите из двух вариантов
                                </Text>
                                <Flex>
                                    <Button
                                        w="50%"
                                        p="8px 32px"
                                        me="8px"
                                        colorscheme="maincolor"
                                        borderColor="maincolor"
                                        color="maincolor"
                                        variant="outline"
                                        fontSize="xs"
                                        onClick={props.onTransparent}
                                    >
                                        Прозрачная
                                    </Button>
                                    <Button
                                        type="submit"
                                        bg="maincolor"
                                        w="50%"
                                        p="8px 32px"
                                        mb={5}
                                        color="white"
                                        fontSize="xs"
                                        onClick={props.onOpaque}
                                    >
                                        Непрозрачная
                                    </Button>
                                </Flex>
                            </Box>
                            <Box
                                display={fixedDisplay}
                                justifyContent="space-between "
                                mb="16px"
                            >
                                <Text fontSize="md" fontWeight="600" mb="4px">
                                    Navbar Fixed
                                </Text>
                                <Switch
                                    colorscheme="maincolor"
                                    isChecked={switched}
                                    onChange={(event) => {
                                        if (switched === true) {
                                            props.onSwitch(false);
                                            setSwitched(false);
                                        } else {
                                            props.onSwitch(true);
                                            setSwitched(true);
                                        }
                                    }}
                                />
                            </Box>
                            <Flex
                                justifyContent="space-between"
                                alignItems="center"
                                mb="24px"
                            >
                                <Text fontSize="md" fontWeight="600" mb="4px">
                                    Тема: светлая/темная
                                </Text>
                                <Button onClick={toggleColorMode}>
                                    Тема {colorMode === "light" ? "Темная" : "Светлая"}
                                </Button>
                            </Flex>

                            <Separator/>
                        </Flex>
                    </DrawerBody>
                </DrawerContent>
            </Drawer>
        </>
    );
}
Configurator.propTypes = {
    secondary: PropTypes.bool,
    isOpen: PropTypes.bool,
    onClose: PropTypes.func,
    fixed: PropTypes.bool,
};
