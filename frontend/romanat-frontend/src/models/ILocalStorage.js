import LoginData from './LoginData' // your JS version of ILgoinData

/**
 * @typedef {Object} ILocalStorage
 * @property {LoginData|null} logged_in_user - Currently logged-in user data
 */

/** 
 * Initial reactive localStorage object
 * @type {ILocalStorage} 
 */
const localStore = {
  logged_in_user: null
}

export default localStore
