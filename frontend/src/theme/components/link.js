export const linkStyles = {
    components: {
        Link: {
            // 3. We can add a new visual variant
            decoration: "none",
            baseStyle: {
                hover: {
                    textDecoration: "none",
                },
                _focus: {
                    boxShadow: "none",
                },
            },
        },
    },
};
