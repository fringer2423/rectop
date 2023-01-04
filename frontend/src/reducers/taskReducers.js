import {
    TASK_READ_FAIL,
    TASK_READ_REQUEST,
    TASK_READ_SUCCESS
} from '../constants/taskConstants';

export const taskReadReducer = (state = {}, action) => {
    switch (action.type) {
        case RATE_INFO_DATA_REQUEST:
            return {loading: true};

        case RATE_INFO_DATA_SUCCESS:
            return {loading: false, taskInfo: action.payload};

        case RATE_INFO_DATA_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};
