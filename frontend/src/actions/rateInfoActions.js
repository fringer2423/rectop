import axios from "axios";

import {
    RATE_INFO_DATA_REQUEST,
    RATE_INFO_DATA_SUCCESS,
    RATE_INFO_DATA_FAIL,
} from "../constants/rateInfoConstants";

export const dataRate = () => async (dispatch) => {
    try {
        dispatch({
            type: RATE_INFO_DATA_REQUEST,
        });

        const config = {
            headers: {
                "Content-type": "application/json",
            },
        };

        await axios.get(`/api/rate_info/read/`, config).then((response) => {
            dispatch({
                type: RATE_INFO_DATA_SUCCESS,
                payload: response.data,
            });
            // console.log(response.data, " response.data");
            localStorage.setItem("rateInfo ", JSON.stringify(response.data));
        });
    } catch (e) {
        switch (e.response.status) {
            case 404:
                dispatch({
                    type: RATE_INFO_DATA_FAIL,
                    payload: "Нет информации о тарифах",
                });
                break;
            default:
                dispatch({
                    type: RATE_INFO_DATA_FAIL,
                    payload: "Произошла ошибка при запросе цены о тарифах " + e,
                });
        }
    }
};
