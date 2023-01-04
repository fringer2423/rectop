import {
    CONNECT_CREATE_REQUEST,
    CONNECT_CREATE_SUCCESS,
    CONNECT_CREATE_FAIL,
    CONNECT_DELETE_REQUEST,
    CONNECT_DELETE_SUCCESS,
    CONNECT_DELETE_FAIL,
    CONNECT_ALL_REQUEST,
    CONNECT_ALL_SUCCESS,
    CONNECT_ALL_FAIL,
    CONNECT_GET_ONE_REQUEST,
    CONNECT_GET_ONE_SUCCESS,
    CONNECT_GET_ONE_FAIL,
    CONNECT_UPDATE_REQUEST,
    CONNECT_UPDATE_SUCCESS,
    CONNECT_UPDATE_FAIL,
    CONNECT_UPDATE_RESET,
} from "../constants/connectConstants";


export const connectCreateReducer = (state = {}, action) => {
    switch (action.type) {
        case CONNECT_CREATE_REQUEST:
            return {loading: true};

        case CONNECT_CREATE_SUCCESS:
            return {loading: false, connect: action.payload};

        case CONNECT_CREATE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const connectDeleteReducer = (state = {}, action) => {
    switch (action.type) {
        case CONNECT_DELETE_REQUEST:
            return {loading: true};

        case CONNECT_DELETE_SUCCESS:
            return {loading: false, success: true};

        case CONNECT_DELETE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const connectAllReducer = (state = {}, action) => {
    switch (action.type) {
        case CONNECT_ALL_REQUEST:
            return {loading: true};

        case CONNECT_ALL_SUCCESS:
            return {loading: false, connects: action.payload};

        case CONNECT_ALL_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const connectGetOneReducer = (state = {}, action) => {
    switch (action.type) {
        case CONNECT_GET_ONE_REQUEST:
            return {loading: true};

        case CONNECT_GET_ONE_SUCCESS:
            return {loading: false, connects: action.payload};

        case CONNECT_GET_ONE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const connectUpdateReducer = (state = {}, action) => {
    switch (action.type) {
        case CONNECT_UPDATE_REQUEST:
            return {loading: true};

        case CONNECT_UPDATE_SUCCESS:
            return {loading: false, success: true};

        case CONNECT_UPDATE_FAIL:
            return {loading: false, error: action.payload};
        
        case CONNECT_UPDATE_RESET:
            return {connect: {}};

        default:
            return state;
    }
};

