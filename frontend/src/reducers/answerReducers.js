import {
    ANSWER_CREATE_REQUEST,
    ANSWER_CREATE_SUCCESS,
    ANSWER_CREATE_FAIL,
    ANSWER_DELETE_REQUEST,
    ANSWER_DELETE_SUCCESS,
    ANSWER_DELETE_FAIL,
    ANSWER_READ_REQUEST,
    ANSWER_READ_SUCCESS,
    ANSWER_READ_FAIL,
    ANSWER_READ_RESET,
    ANSWER_UPDATE_REQUEST,
    ANSWER_UPDATE_SUCCESS,
    ANSWER_UPDATE_FAIL,
    ANSWER_UPDATE_RESET,
} from "../constants/answerConstants";

export const answerCreateReducer = (state = {}, action) => {
    switch (action.type) {
        case ANSWER_CREATE_REQUEST:
            return {loading: true};

        case ANSWER_CREATE_SUCCESS:
            return {loading: false, answer: action.payload};

        case ANSWER_CREATE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const answerDeleteReducer = (state = {}, action) => {
    switch (action.type) {
        case ANSWER_DELETE_REQUEST:
            return {loading: true};

        case ANSWER_DELETE_SUCCESS:
            return {loading: false, success: true};

        case ANSWER_DELETE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const answerDetailsReducer = (state = {answer: {}}, action) => {
    switch (action.type) {
        case ANSWER_READ_REQUEST:
            return {loading: true};

        case ANSWER_READ_SUCCESS:
            return {loading: false, answer: action.payload};

        case ANSWER_READ_FAIL:
            return {loading: false, error: action.payload};

        case ANSWER_READ_RESET:
            return {answer: {}};

        default:
            return state;
    }
};

export const answerUpdateReducer = (state = {answer: {}}, action) => {
    switch (action.type) {
        case ANSWER_UPDATE_REQUEST:
            return {loading: true};

        case ANSWER_UPDATE_SUCCESS:
            return {loading: false, success: true};

        case ANSWER_UPDATE_FAIL:
            return {loading: false, error: action.payload};

        case ANSWER_UPDATE_RESET:
            return {answer: {}};

        default:
            return state;
    }
};
