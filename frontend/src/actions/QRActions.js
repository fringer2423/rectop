import axios from "axios";

import {
    QR_CREATE_REQUEST,
    QR_CREATE_SUCCESS,
    QR_CREATE_FAIL,
    QR_ALL_REQUEST,
    QR_ALL_FAIL,
    QR_ALL_SUCCESS,
    QR_GET_ONE_FAIL,
    QR_GET_ONE_REQUEST,
    QR_GET_ONE_SUCCESS,
} from "../constants/QRCodeConstants";


export const qrCodeCreate = (branchID) => async(dispatch, getState) => {
    try {
        dispatch({
            type: QR_CREATE_REQUEST,
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
            `/api/qrcode/create/`,
            {type: branchID},
            config,
        )

        dispatch({
            type: QR_CREATE_SUCCESS,
            payload: data,
        });


    } catch (error) {

        switch (error) {
            case 400:
                dispatch({
                    type: QR_CREATE_FAIL,
                    payload: 'Ошибка при создании',
                })
                break;
            case 401:
                dispatch({
                    type: QR_CREATE_FAIL,
                    payload: 'Пустой или неправильный токен',
                })
                break;
            case 403:
                dispatch({
                    type: QR_CREATE_FAIL,
                    payload: 'Ошибка доступа',
                })
                break;

            case 404:
                dispatch({
                    type: QR_CREATE_FAIL,
                    payload: 'Филиал не найден',
                })
                break;

            case 406:
                dispatch({
                    type: QR_CREATE_FAIL,
                    payload: 'У вас уже есть код на данный филиал',
                })
                break;
            default:
                dispatch({
                    type: QR_CREATE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                })
                break;
        }
        
    }
}

export const getAllCodes = () => async (dispatch) => {
    try {
        dispatch({
            type: QR_ALL_REQUEST,
        });

        const config = {
            headers: {
                "Content-type": "application/json",
            },
        };

        const {data} = await axios.get(
            `/api/qrcode/read/all`,
            config,
        );

        dispatch({
            type: QR_ALL_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error) {
            case 400:
                dispatch({
                    type: QR_ALL_FAIL,
                    payload: 'Ошибка при запросе',
                })
                break;

            case 404:
                dispatch({
                    type: QR_ALL_FAIL,
                    payload: 'Коды не найдены',
                })
                break;

            default:
                dispatch({
                    type: QR_ALL_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                })
                break;
        }
    }
} 

export const getOneCode = (codeID) => async (dispatch) => {
    try {
        dispatch({
            type: QR_GET_ONE_REQUEST,
        });

        const config = {
            headers: {
                "Content-type": "application/json",
            },
        };

        const {data} = await axios.get(
            `/api/qrcode/read/${codeID}`,
            config,
        );

        dispatch({
            type: QR_GET_ONE_SUCCESS,
            payload: data,
        });


    } catch (error) {
        switch (error) {
            case 400:
                dispatch({
                    type: QR_GET_ONE_FAIL,
                    payload: 'Ошибка при запросе',
                })
                break;

            case 403:
                dispatch({
                    type: QR_GET_ONE_FAIL,
                    payload: 'Ошибка доступа',
                })
                break;

            case 404:
                dispatch({
                    type: QR_GET_ONE_FAIL,
                    payload: 'Код не найден',
                })
                break;

            default:
                dispatch({
                    type: QR_GET_ONE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                })
                break;
        }
    }
}
