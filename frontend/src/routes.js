// import
import Dashboard from "./screens/Dashboard/Dashboard";
import Tables from "./screens/Dashboard/Tables";
import Billing from "./screens/Dashboard/Billing";

import Profile from "./screens/Dashboard/Profile";
import LogInPage from "./screens/LogInPage.js";
import RegistrationPage from "./screens/RegistrationPage.js";
import VerificationScreen from "./screens/VerificationScreen.js"

import {
    HomeIcon,
    StatsIcon,
    CreditIcon,
    PersonIcon,
    DocumentIcon,
    RocketIcon,
    SupportIcon,
} from "./components/components/Icons/Icons";

export const dashRoutes = [
    {
        path: "/",
        name: "Dashboard",

        icon: <HomeIcon color="inherit"/>,
        component: Dashboard,
        layout: "/dashboard",
    },
    {
        path: "/tables",
        name: "Tables",

        icon: <StatsIcon color="inherit"/>,
        component: Tables,
        layout: "/dashboard",
    },
    {
        path: "/billing",
        name: "Billing",

        icon: <CreditIcon color="inherit"/>,
        component: Billing,
        layout: "/dashboard",
    },

    {
        path: "/profile",
        name: "Личный кабинет",

        icon: <PersonIcon color="inherit"/>,
        secondaryNavbar: true,
        component: Profile,
        layout: "/dashboard",
    },
    {
        path: "/signin",
        name: "Sign In",

        icon: <DocumentIcon color="inherit"/>,
        component: LogInPage,
        layout: "/auth",
    },
    {
        path: "/signup",
        name: "Sign Up",

        icon: <RocketIcon color="inherit"/>,
        secondaryNavbar: true,
        component: RegistrationPage,
        layout: "/auth",
    },
    {
        path: "/verify/:code",
        name: "Verify email",

        icon: <RocketIcon color="inherit"/>,
        secondaryNavbar: false,
        component: VerificationScreen,
        layout: "/auth",
    },
];
export default dashRoutes;
