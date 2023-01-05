import axios from "axios";

import {
    TASK_READ_REQUEST,
    TASK_READ_SUCCESS,
    TASK_READ_FAIL,
} from "../constants/taskConstants";

export const taskData = (taskId) => async (dispatch, getState) => {
    try {
        dispatch({
            type: TASK_READ_REQUEST,
        });

        const {
            userLogin: {userInfo},
        } = getState();

        const config = {
            headers: {
                "Content-type": "application/json",
                Authorization: `Bearer ${userInfo.token}`,
            },
        };

        await axios
            .get(`/api/task/read/`, {task_id: taskId}, config)
            .then((res) => {
                dispatch({
                    type: TASK_READ_SUCCESS,
                    payload: res.data,
                });
            });
    } catch (e) {
        switch (e) {
            case 400:
                dispatch({
                    type: TASK_READ_FAIL,
                    payload: "Ошибка при обработке запроса",
                });
                break;
            case 401:
                dispatch({
                    type: TASK_READ_FAIL,
                    payload: "Пустой или неправильный токен",
                });
                break;
            case 404: 
            dispatch({
                type: TASK_READ_FAIL,
                payload: "Task не найден",
            });
            break;
        
            default:
                dispatch({
                    type: TASK_READ_FAIL,
                    payload: "Произошла ошибка при запросе " + e,
                });
                break;
        }
    }
};
