import axios from "axios";

import {
    COMPANY_CREATE_FAIL,
    COMPANY_CREATE_REQUEST,
    COMPANY_CREATE_SUCCESS,
    COMPANY_DELETE_FAIL,
    COMPANY_DELETE_REQUEST,
    COMPANY_DELETE_SUCCESS,
    COMPANY_READ_FAIL,
    COMPANY_READ_REQUEST,
    COMPANY_READ_RESET,
    COMPANY_READ_SUCCESS,
    COMPANY_UPDATE_FAIL,
    COMPANY_UPDATE_REQUEST,
    COMPANY_UPDATE_RESET,
    COMPANY_UPDATE_SUCCESS,
} from "../constants/companyConstants";

export const createCompany = (companyName) => async (dispatch, getState) => {
    try {
        dispatch({
            type: COMPANY_CREATE_REQUEST,
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

        const {data} = await axios.post(
            `/api/company/create/`,
            {name: companyName},
            config
        );

        dispatch({
            type: COMPANY_CREATE_SUCCESS,
            payload: data,
        });
    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: COMPANY_CREATE_FAIL,
                    payload: "Ошибка при создании",
                });
                break;

            default:
                dispatch({
                    type: COMPANY_CREATE_FAIL,
                    payload: "Произошла ошибка: " + error,
                });
                break;
        }
    }
};

export const readCompany = (companyID) => async (dispatch, getState) => {
    try {
        dispatch({
            type: COMPANY_READ_REQUEST,
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

        const {data} = await axios.get(`/api/company/read/${companyID}`, config);

        dispatch({
            type: COMPANY_READ_SUCCESS,
            payload: data,
        });
    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: COMPANY_READ_FAIL,
                    payload: "Ошибка при запросе",
                });
                break;

            case 403:
                dispatch({
                    type: COMPANY_READ_FAIL,
                    payload: "Ошибка доступа",
                });
                break;

            case 404:
                dispatch({
                    type: COMPANY_READ_FAIL,
                    payload: "Компания не найдена",
                });
                break;

            default:
                dispatch({
                    type: COMPANY_READ_FAIL,
                    payload: "Произошла ошибка: " + error,
                });
                break;
        }
    }
};

export const updateCompany =
    (companyName, companyID) => async (dispatch, getState) => {
        try {
            dispatch({
                type: COMPANY_UPDATE_REQUEST,
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

            const {data} = await axios.put(
                `/api/company/update/${companyID}`,
                {name: companyName},
                config
            );

            dispatch({
                type: COMPANY_UPDATE_SUCCESS,
                payload: data,
            });
        } catch (error) {
            switch (error.response.status) {
                case 400:
                    dispatch({
                        type: COMPANY_UPDATE_FAIL,
                        payload: "Ошибка при запросе",
                    });
                    break;

                case 403:
                    dispatch({
                        type: COMPANY_UPDATE_FAIL,
                        payload: "Ошибка доступа",
                    });
                    break;

                case 404:
                    dispatch({
                        type: COMPANY_UPDATE_FAIL,
                        payload: "Компания не найдена",
                    });
                    break;

                default:
                    dispatch({
                        type: COMPANY_UPDATE_FAIL,
                        payload: "Произошла ошибка: " + error,
                    });
                    break;
            }
        }
    };

export const deleteCompany = (companyID) => async (dispatch, getState) => {
    try {
        dispatch({
            type: COMPANY_DELETE_REQUEST,
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

        const {data} = await axios.delete(
            `/api/company/delete/${companyID}`,
            config
        );

        dispatch({
            type: COMPANY_DELETE_SUCCESS,
        });

        dispatch({
            type: COMPANY_READ_RESET,
        });

        dispatch({
            type: COMPANY_UPDATE_RESET,
        });
    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: COMPANY_DELETE_FAIL,
                    payload: "Ошибка при запросе",
                });
                break;

            case 403:
                dispatch({
                    type: COMPANY_DELETE_FAIL,
                    payload: "Ошибка доступа",
                });
                break;

            case 404:
                dispatch({
                    type: COMPANY_DELETE_FAIL,
                    payload: "Компания не найдена",
                });
                break;

            default:
                dispatch({
                    type: COMPANY_DELETE_FAIL,
                    payload: "Произошла ошибка: " + error,
                });
                break;
        }
    }
};
