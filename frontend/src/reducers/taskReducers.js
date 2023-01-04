import {
    TASK_READ_FAIL,
    TASK_READ_REQUEST,
    TASK_READ_SUCCESS
} from '../constants/taskConstants';

export const taskReadReducer = (state = {}, action) => {
    switch (action.type) {
        case TASK_READ_REQUEST:
            return {loading: true};

        case TASK_READ_SUCCESS:
            return {loading: false, taskInfo: action.payload};

        case TASK_READ_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};
