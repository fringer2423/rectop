import {
    REVIEW_SETTINGS_CREATE_REQUEST,
    REVIEW_SETTINGS_CREATE_SUCCESS,
    REVIEW_SETTINGS_CREATE_FAIL,
    REVIEW_SETTINGS_DELETE_REQUEST,
    REVIEW_SETTINGS_DELETE_SUCCESS,
    REVIEW_SETTINGS_DELETE_FAIL,
    REVIEW_SETTINGS_READ_REQUEST,
    REVIEW_SETTINGS_READ_SUCCESS,
    REVIEW_SETTINGS_READ_FAIL,
    REVIEW_SETTINGS_READ_RESET,
    REVIEW_SETTINGS_UPDATE_REQUEST,
    REVIEW_SETTINGS_UPDATE_SUCCESS,
    REVIEW_SETTINGS_UPDATE_FAIL,
    REVIEW_SETTINGS_UPDATE_RESET,
} from "../constants/reviewSettingsConstants";

export const reviewSettingsCreateReducer = (state = {}, action) => {
    switch (action.type) {
        case REVIEW_SETTINGS_CREATE_REQUEST:
            return {loading: true};

        case REVIEW_SETTINGS_CREATE_SUCCESS:
            return {loading: false, reviewSettings: action.payload};

        case REVIEW_SETTINGS_CREATE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const reviewSettingsDeleteReducer = (state = {}, action) => {
    switch (action.type) {
        case REVIEW_SETTINGS_DELETE_REQUEST:
            return {loading: true};

        case REVIEW_SETTINGS_DELETE_SUCCESS:
            return {loading: false, success: true};

        case REVIEW_SETTINGS_DELETE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const reviewSettingsDetailsReducer = (state = {reviewSettings: {}}, action) => {
    switch (action.type) {
        case REVIEW_SETTINGS_READ_REQUEST:
            return {loading: true};

        case REVIEW_SETTINGS_READ_SUCCESS:
            return {loading: false, reviewSettings: action.payload};

        case REVIEW_SETTINGS_READ_FAIL:
            return {loading: false, error: action.payload};

        case REVIEW_SETTINGS_READ_RESET:
            return {reviewSettings: {}};

        default:
            return state;
    }
};

export const reviewSettingsUpdateReducer = (state = {reviewSettings: {}}, action) => {
    switch (action.type) {
        case REVIEW_SETTINGS_UPDATE_REQUEST:
            return {loading: true};

        case REVIEW_SETTINGS_UPDATE_SUCCESS:
            return {loading: false, success: true};

        case REVIEW_SETTINGS_UPDATE_FAIL:
            return {loading: false, error: action.payload};
        
        case REVIEW_SETTINGS_UPDATE_RESET:
            return {reviewSettings: {}};

        default:
            return state;
    }
};
