
/**
 * @typedef {Object} LoginCredential
 * @property {string} username - The user's username or email
 * @property {string} password - The user's password
 */

export default class LoginCredential {
  /**
   * @param {string} username
   * @param {string} password
   */
  constructor(username, password) {
    if (!username || !password) {
      throw new Error('Username and password are required')
    }
    this.username = username
    this.password = password
  }

  /**
   * Returns a plain object for sending via API
   */
  toJSON() {
    return {
      username: this.username,
      password: this.password
    }
  }
}
