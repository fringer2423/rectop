import {
    BRANCH_CREATE_REQUEST,
    BRANCH_CREATE_SUCCESS,
    BRANCH_CREATE_FAIL,
    BRANCH_ALL_REQUEST,
    BRANCH_ALL_SUCCESS,
    BRANCH_ALL_FAIL,
    BRANCH_GET_ONE_REQUEST,
    BRANCH_GET_ONE_SUCCESS,
    BRANCH_GET_ONE_FAIL,
    BRANCH_UPDATE_REQUEST,
    BRANCH_UPDATE_SUCCESS,
    BRANCH_UPDATE_FAIL,
    BRANCH_UPDATE_RESET
} from "../constants/branchConstants";

export const branchCreateReducer = (state = {}, action) => {
    switch (action.type) {
        case BRANCH_CREATE_REQUEST:
            return {loading: true};

        case BRANCH_CREATE_SUCCESS:
            return {loading: false, branch: action.payload};

        case BRANCH_CREATE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const branchAllReducer = (state = {}, action) => {
    switch (action.type) {
        case BRANCH_ALL_REQUEST:
            return {loading: true};

        case BRANCH_ALL_SUCCESS:
            return {loading: false, branches: action.payload};

        case BRANCH_ALL_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const branchGetOneReducer = (state = {}, action) => {
    switch (action.type) {
        case BRANCH_GET_ONE_REQUEST:
            return {loading: true};

        case BRANCH_GET_ONE_SUCCESS:
            return {loading: false, branch: action.payload};

        case BRANCH_GET_ONE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const branchUpdateReducer = (state = {}, action) => {
    switch (action.type) {
        case BRANCH_UPDATE_REQUEST:
            return {loading: true};

        case BRANCH_UPDATE_SUCCESS:
            return {loading: false, success: true};

        case BRANCH_UPDATE_FAIL:
            return {loading: false, error: action.payload};

        case BRANCH_UPDATE_RESET:
            return {branch: {}};

        default:
            return state;
    }
};