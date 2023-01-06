import {createStore, combineReducers, applyMiddleware} from "redux";
import thunk from "redux-thunk";
import {composeWithDevTools} from "redux-devtools-extension";

import {
    userLoginReducer,
    userRegisterReducer,
    userDetailsReducer,
    userUpdateReducer,
    userVerifyReducer,
    userLoginCheckReducer,
    userVerifyLoginReducer,
} from "./reducers/userReducers";

import {rateInfoDataReducer} from "./reducers/rateInfoReducers";

import {taskReadReducer} from "./reducers/taskReducers";

import {
    rateAddReducer,
    rateChangeReducer,
    rateReadReducer,
} from "./reducers/rateReducers";

import {
    QRAllReducer,
    QRCreateReducer,
    QRGetOneReducer,
} from "./reducers/QRCodeRedusers";

import {
    companyCreateReducer,
    companyDeleteReducer,
    companyDetailsReducer,
    companyUpdateReducer,
} from "./reducers/companyReducers";

import {
    answerCreateReducer,
    answerDeleteReducer,
    answerDetailsReducer,
    answerUpdateReducer,
} from "./reducers/answerReducers";

import {
    branchCreateReducer,
    branchAllReducer,
    branchGetOneReducer,
    branchUpdateReducer,
} from "./reducers/branchReducers";

import {
    connectCreateReducer,
    connectDeleteReducer,
    connectAllReducer,
    connectGetOneReducer,
    connectUpdateReducer,
} from "./reducers/connectReducers";

import {
    telebotCreateReducer,
    telebotDeleteReducer,
    telebotDetailsReducer,
    telebotUpdateReducer,
} from "./reducers/telebotReducers";

import {
    reviewCreateReducer,
    reviewDeleteReducer,
    reviewAllReducer,
    reviewGetOneReducer,
    reviewListReducer,
    reviewUpdateReducer,
} from "./reducers/reviewReducers";

import {
    reviewSettingsCreateReducer,
    reviewSettingsDeleteReducer,
    reviewSettingsDetailsReducer,
    reviewSettingsUpdateReducer,
} from "./reducers/reviewSettingsReducers";

const reducer = combineReducers({
    userLogin: userLoginReducer,
    userRegister: userRegisterReducer,
    userDetails: userDetailsReducer,
    userUpdate: userUpdateReducer,
    userVerify: userVerifyReducer,
    userLoginCheck: userLoginCheckReducer,
    userVerifyLogin: userVerifyLoginReducer,

    rateInfoData: rateInfoDataReducer,

    rateAdd: rateAddReducer,
    rateChange: rateChangeReducer,
    rateRead: rateReadReducer,

    QRCreate: QRCreateReducer,
    QRAll: QRAllReducer,
    QRGetOne: QRGetOneReducer,

    taskRead: taskReadReducer,

    companyCreate: companyCreateReducer,
    companyDelete: companyDeleteReducer,
    companyDetails: companyDetailsReducer,
    companyUpdate: companyUpdateReducer,

    branchAll: branchAllReducer,
    branchCreate: branchCreateReducer,
    branchGetOne: branchGetOneReducer,
    branchUpdate: branchUpdateReducer,

    answerCreate: answerCreateReducer,
    answerDelete: answerDeleteReducer,
    answerDetails: answerDetailsReducer,
    answerUpdate: answerUpdateReducer,

    connectCreate: connectCreateReducer,
    connectAll: connectAllReducer,
    connectDelete: connectDeleteReducer,
    connectGetOne: connectGetOneReducer,
    connectUpdate: connectUpdateReducer,

    telebotCreate: telebotCreateReducer,
    telebotDetails: telebotDetailsReducer,
    telebotDelete: telebotDeleteReducer,
    telebotUpdate: telebotUpdateReducer,

    reviewCreate: reviewCreateReducer,
    reviewAll: reviewAllReducer,
    reviewDelete: reviewDeleteReducer,
    reviewGetOne: reviewGetOneReducer,
    reviewList: reviewListReducer,
    reviewUpdate: reviewUpdateReducer,

    reviewSettingsCreate: reviewSettingsCreateReducer,
    reviewSettingsDelete: reviewSettingsDeleteReducer,
    reviewSettingsDetails: reviewSettingsDetailsReducer,
    reviewSettingsUpdate: reviewSettingsUpdateReducer,
});

const userInfoFromStorage = localStorage.getItem("userInfo")
    ? JSON.parse(localStorage.getItem("userInfo"))
    : null;

const isLoggedInFromStorage = localStorage.getItem("isLoggedIn")
    ? localStorage.getItem("isLoggedIn")
    : undefined;

const companyFromStorage = localStorage.getItem("isLoggedIn")
    ? JSON.parse(localStorage.getItem("company"))
    : null;

const initialState = {
    userLogin: {
        userInfo: userInfoFromStorage,
    },
    userVerifyLogin: {
        isLoggedIn: isLoggedInFromStorage,
    },

    companyDetails: {
        company: companyFromStorage,
    },
};

const middleware = [thunk];

const store = createStore(
    reducer,
    initialState,
    composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
