import {
    createStore,
    combineReducers,
    applyMiddleware
} from 'redux'
import thunk from 'redux-thunk'
import {
    composeWithDevTools
} from 'redux-devtools-extension'


import {
    userLoginReducer,
    userRegisterReducer,
    userDetailsReducer,
    userUpdateReducer,
    userVerifyReducer,
    userLoginCheckReducer,
    userVerifyLoginReducer
} from './reducers/userReducers'

import {rateInfoDataReducer} from './reducers/rateInfoReducers'


const reducer = combineReducers({
    userLogin: userLoginReducer,
    userRegister: userRegisterReducer,
    userDetails: userDetailsReducer,
    userUpdate: userUpdateReducer,
    userVerify: userVerifyReducer,
    userLoginCheck: userLoginCheckReducer,
    userVerifyLogin: userVerifyLoginReducer,

    rateInfoData: rateInfoDataReducer,
})


const userInfoFromStorage = localStorage.getItem('userInfo') ?
    JSON.parse(localStorage.getItem('userInfo')) : null

const isLoggedInFromStorage = localStorage.getItem('isLoggedIn') ? localStorage.getItem('isLoggedIn') : undefined;

const initialState = {
    userLogin: {
        userInfo: userInfoFromStorage
    },
    userVerifyLogin: {
        isLoggedIn: isLoggedInFromStorage
    }
}

const middleware = [thunk]

const store = createStore(reducer, initialState,
    composeWithDevTools(applyMiddleware(...middleware)))

export default store
