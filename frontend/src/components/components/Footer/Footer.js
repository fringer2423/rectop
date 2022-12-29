/*eslint-disable*/
import React from "react";
import {Flex, Link, List, ListItem, Text} from "@chakra-ui/react";
import PropTypes from "prop-types";

export default function Footer(props) {
    // const linkmaincolor = useColorModeValue("maincolor", "red.200");=
    return (
        <Flex
            flexDirection={{
                base: "column",
                xl: "row",
            }}
            alignItems={{
                base: "center",
                xl: "start",
            }}
            justifyContent="space-between"
            px="30px"
            pb="20px"
        >
            <Text
                color="gray.400"
                textAlign={{
                    base: "center",
                    xl: "start",
                }}
                mb={{base: "20px", xl: "0px"}}
            >
                &copy; {1900 + new Date().getYear()},{" "}
                <Text as="span">
                    Made with ❤️ by
                </Text>
                <Link
                    // color={linkmaincolor}
                    color="maincolor"
                    href="https://www.creative-tim.com"
                    target="_blank"
                >

                    Creative Tim
                </Link>
                &
                <Link
                    // color={linkmaincolor}
                    color="maincolor"
                    href="https://www.simmmple.com"
                    target="_blank"
                >
                    Simple
                </Link>
                for a better web
            </Text>
            <List display="flex">
                <ListItem
                    me={{
                        base: "20px",
                        md: "44px",
                    }}
                >
                    <Link color="gray.400" href="https://www.creative-tim.com">
                        Creative Tim
                    </Link>
                </ListItem>
                <ListItem
                    me={{
                        base: "20px",
                        md: "44px",
                    }}
                >
                    <Link color="gray.400" href="https://www.simmmple.com">
                        Simple
                    </Link>
                </ListItem>
                <ListItem
                    me={{
                        base: "20px",
                        md: "44px",
                    }}
                >
                    <Link
                        color="gray.400"
                        href="#blog"

                    >
                        Blog
                    </Link>
                </ListItem>
                <ListItem>
                    <Link
                        color="gray.400"
                        href="#license"

                    >
                        License
                    </Link>
                </ListItem>
            </List>
        </Flex>
    );
}
