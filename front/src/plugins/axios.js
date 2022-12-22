import axios from 'axios'
// import router from './router'
// import store from './store'
// import Promise from 'es6-promise'

const host = window.location.hostname

const kapaAPI = axios.create({
  baseURL: 'http://' + host + ':8000/api/',
  // timeout: 100000,
  headers: {
    'Content-type': 'application/json; charset=UTF-8'
  }
})

// const setBearer = function () {
//   const localToken = localStorage.getItem('token')
//   if (localToken) {
//     hubAPI.defaults.headers.common.Authorization = `Bearer ${localToken}`
//   }
//   return hubAPI
// }

// export { hubAPI, setBearer }
export { kapaAPI }
