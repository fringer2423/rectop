import {
    USER_LOGIN_REQUEST,
    USER_LOGIN_SUCCESS,
    USER_LOGIN_FAIL,
    USER_LOGOUT,
    USER_REGISTER_REQUEST,
    USER_REGISTER_SUCCESS,
    USER_REGISTER_FAIL,
    USER_VERIFY_REQUEST,
    USER_VERIFY_SUCCESS,
    USER_VERIFY_FAIL,
    USER_LOGIN_CHECK_REQUEST,
    USER_LOGIN_CHECK_SUCCESS,
    USER_LOGIN_CHECK_FAIL,
    USER_VERIFY_LOGIN_REQUEST,
    USER_VERIFY_LOGIN_SUCCESS,
    USER_VERIFY_LOGIN_FAIL,
    USER_DETAILS_REQUEST,
    USER_DETAILS_SUCCESS,
    USER_DETAILS_FAIL,
    USER_DETAILS_RESET,
    USER_UPDATE_REQUEST,
    USER_UPDATE_SUCCESS,
    USER_UPDATE_FAIL,
    USER_UPDATE_RESET,
} from "../constants/userConstants";

export const userLoginReducer = (state = {}, action) => {
    switch (action.type) {
        case USER_LOGIN_REQUEST:
            return {loading: true};

        case USER_LOGIN_SUCCESS:
            return {loading: false, userInfo: action.payload};

        case USER_LOGIN_FAIL:
            return {loading: false, error: action.payload};

        case USER_LOGOUT:
            return {};

        default:
            return state;
    }
};

export const userRegisterReducer = (state = {}, action) => {
    switch (action.type) {
        case USER_REGISTER_REQUEST:
            return {loading: true};

        case USER_REGISTER_SUCCESS:
            return {loading: false, userInfo: action.payload};

        case USER_REGISTER_FAIL:
            return {loading: false, error: action.payload};

        case USER_LOGOUT:
            return {};

        default:
            return state;
    }
};

export const userVerifyReducer = (state = {}, action) => {
    switch (action.type) {
        case USER_VERIFY_REQUEST:
            return {loading: true};

        case USER_VERIFY_SUCCESS:
            return {loading: false, userInfo: action.payload};

        case USER_VERIFY_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const userVerifyLoginReducer = (state = {}, action) => {
    switch (action.type) {
        case USER_VERIFY_LOGIN_REQUEST:
            return {loading: true};

        case USER_VERIFY_LOGIN_SUCCESS:
            return {loading: false, detail: action.payload, isLoggedIn: true};

        case USER_VERIFY_LOGIN_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const userLoginCheckReducer = (state = {}, action) => {
    switch (action.type) {
        case USER_LOGIN_CHECK_REQUEST:
            return {loading: true};

        case USER_LOGIN_CHECK_SUCCESS:
            return {loading: false, detail: action.payload};

        case USER_LOGIN_CHECK_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const userDetailsReducer = (state = {user: {}}, action) => {
    switch (action.type) {
        case USER_DETAILS_REQUEST:
            return {...state, loading: true};

        case USER_DETAILS_SUCCESS:
            return {loading: false, user: action.payload};

        case USER_DETAILS_FAIL:
            return {loading: false, error: action.payload};

        case USER_DETAILS_RESET:
            return {user: {}};

        default:
            return state;
    }
};

export const userUpdateReducer = (state = {user: {}}, action) => {
    switch (action.type) {
        case USER_UPDATE_REQUEST:
            return {loading: true};

        case USER_UPDATE_SUCCESS:
            return {loading: false, success: true};

        case USER_UPDATE_FAIL:
            return {loading: false, error: action.payload};

        case USER_UPDATE_RESET:
            return {user: {}};

        default:
            return state;
    }
};
