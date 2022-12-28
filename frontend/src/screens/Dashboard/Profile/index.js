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
import Conversations from "./components/Conversations";
import Header from "./components/Header";
import PlatformSettings from "./components/PlatformSettings";
import ProfileInformation from "./components/ProfileInformation";
import Projects from "./components/Projects";
import {getUserDetails} from "../../../actions/userActions.js"

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

    const userLogin = useSelector(state => state.userLogin);
    const {userInfo} = userLogin;

    const userDetails = useSelector(state => state.userDetails);
    const {user} = userDetails;

    return (
        <Flex direction='column'>
            <Header
                backgroundHeader={ProfileBgImage}
                backgroundProfile={bgProfile}
                avatarImage={avatar4}
                name={user.first_name + " " + user.last_name}
                email={userInfo.username}
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
            <Grid templateColumns={{sm: "1fr", xl: "repeat(3, 1fr)"}} gap='22px'>
                <PlatformSettings
                    title={"Platform Settings"}
                    subtitle1={"ACCOUNT"}
                    subtitle2={"APPLICATION"}
                />
                <ProfileInformation
                    title={"Информация о профиле"}
                    description={
                        "Hi, I’m Esthera Jackson, Decisions: If you can’t decide, the answer is no. If two equally difficult paths, choose the one more painful in the short term (pain avoidance is creating an illusion of equality)."
                    }
                    name={user.first_name + " " + user.last_name}
                    email={userInfo.username}

                />
                <Conversations title={"Conversations"}/>
            </Grid>
            <Projects title={"Projects"} description={"Architects design houses"}/>
        </Flex>
    );
}

export default Profile;
