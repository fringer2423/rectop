// Chakra imports
import {Flex, Grid, useColorModeValue} from "@chakra-ui/react";
import avatar4 from "../../../assets/img/avatars/avatar4.png";
import ProfileBgImage from "../../../assets/img/ProfileBackground.png";
import React, {useEffect} from "react";
import {FaCube, FaPenFancy} from "react-icons/fa";
import {
    useSelector,
    useDispatch
} from "react-redux";
import {IoDocumentsSharp} from "react-icons/io5";
import Companies from "./components/Companies";
import Header from "./components/Header";
import PlatformSettings from "./components/PlatformSettings";
import ProfileInformation from "./components/ProfileInformation";
import {getUserDetails} from "../../../actions/userActions.js";

function Profile() {
    // Chakra color mode
    const textColor = useColorModeValue("gray.700", "white");
    const bgProfile = useColorModeValue(
        "hsla(0,0%,100%,.8)",
        "linear-gradient(112.83deg, rgba(255, 255, 255, 0.21) 0%, rgba(255, 255, 255, 0) 110.84%)"
    );

    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getUserDetails());
    }, [])

    const companyDetails = useSelector(state => state.companyDetails);
    const {company} = companyDetails;
    

    const userDetails = useSelector(state => state.userDetails);
    const {user, error} = userDetails;

    return (
        <Flex direction='column'>
            <Header
                backgroundHeader={ProfileBgImage}
                backgroundProfile={bgProfile}
                avatarImage={avatar4}
                name={user.first_name + " " + user.last_name}
                email={user.email}
                tabs={[
                    {
                        name: "OVERVIEW",
                        icon: <FaCube w='100%' h='100%'/>,
                    },
                    {
                        name: "TEAMS",
                        icon: <IoDocumentsSharp w='100%' h='100%'/>,
                    },
                    {
                        name: "PROJECTS",
                        icon: <FaPenFancy w='100%' h='100%'/>,
                    },
                ]}
            />
            <Grid templateColumns={{sm: "1fr", md: "repeat(2, 1fr)", xl: "repeat(3, 1fr)"}} gap='22px'>
                <ProfileInformation
                    title={"???????????????????? ?? ??????????????"}
                    description={
                        user.description
                    }
                    mobile={user.phone_number}
                    rate={user.rate}
                    job={user.job_title}
                    name={user.first_name + " " + user.last_name}
                    email={user.email}
                    error={error}

                />
                <Companies title={"????????????????"} companyInfo={company}/>
                <PlatformSettings
                    title={"?????????????????? ?????????????? ????????????????"}
                    subtitle1={"???????? ??????*"}
                    subtitle2={"???????? ??????????????*"}
                    subtitle3={"?????????? ???????????? ?????? ?????????????????? ????????????*"}
                    subtitle4={"?????????? ????????????????"}
                    subtitle5={"?????? ?????????? ????????????????"}
                    subtitle6={"???????? ??????????????????"}
                    subtitle7={"Email"}
                />
            </Grid>

        </Flex>
    );
}

// <Projects title={"????????????????"} description={"???????????????? ???????? ????????????????"}/>

export default Profile;
