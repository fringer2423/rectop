import {
    TELEBOT_CREATE_REQUEST,
    TELEBOT_CREATE_SUCCESS,
    TELEBOT_CREATE_FAIL,
    TELEBOT_DELETE_REQUEST,
    TELEBOT_DELETE_SUCCESS,
    TELEBOT_DELETE_FAIL,
    TELEBOT_READ_REQUEST,
    TELEBOT_READ_SUCCESS,
    TELEBOT_READ_FAIL,
    TELEBOT_UPDATE_REQUEST,
    TELEBOT_UPDATE_SUCCESS,
    TELEBOT_UPDATE_FAIL,
    TELEBOT_UPDATE_RESET,
} from "../constants/telebotConstants";

export const telebotCreateReducer = (state = {}, action) => {
    switch (action.type) {
        case TELEBOT_CREATE_REQUEST:
            return {loading: true};

        case TELEBOT_CREATE_SUCCESS:
            return {loading: false, telebot: action.payload};

        case TELEBOT_CREATE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const telebotDeleteReducer = (state = {}, action) => {
    switch (action.type) {
        case TELEBOT_DELETE_REQUEST:
            return {loading: true};

        case TELEBOT_DELETE_SUCCESS:
            return {loading: false, success: true};

        case TELEBOT_DELETE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const telebotDetailsReducer = (state = {}, action) => {
    switch (action.type) {
        case TELEBOT_READ_REQUEST:
            return {loading: true};

        case TELEBOT_READ_SUCCESS:
            return {loading: false, telebot: action.payload};

        case TELEBOT_READ_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const telebotUpdateReducer = (state = {}, action) => {
    switch (action.type) {
        case TELEBOT_UPDATE_REQUEST:
            return {loading: true};

        case TELEBOT_UPDATE_SUCCESS:
            return {loading: false, success: true};

        case TELEBOT_UPDATE_FAIL:
            return {loading: false, error: action.payload};
        
        case TELEBOT_UPDATE_RESET:
            return {telebot: {}};

        default:
            return state;
    }
};
