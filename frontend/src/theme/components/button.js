export const buttonStyles = {
    components: {
        Button: {
            variants: {
                "no-hover": {
                    hover: {
                        boxShadow: "none",
                    },
                },
                "transparent-with-icon": {
                    bg: "transparent",
                    fontWeight: "bold",
                    borderRadius: "inherit",
                    cursor: "pointer",
                    hover: "none",
                    _active: {
                        bg: "transparent",
                        transform: "none",
                        borderColor: "transparent",
                    },
                    _focus: {
                        boxShadow: "none",
                    },
                    hover: {
                        boxShadow: "none",
                    },
                },
            },
            baseStyle: {
                borderRadius: "15px",
                _focus: {
                    boxShadow: "none",
                },
            },
        },
    },
};
