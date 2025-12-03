
/**
 * @typedef {Object} LoginData
 * @property {string} access_token - JWT access token
 * @property {string} refresh_token - JWT refresh token
 * @property {boolean} is_admin - Is the user an admin
 * @property {boolean} requiresReset - Does the user need password reset
 * @property {string} username - User's username
 * @property {string} id - User's unique ID
 */

export default class LoginData {
  /**
   * @param {Object} data
   * @param {string} data.access_token
   * @param {string} data.refresh_token
   * @param {boolean} data.is_admin
   * @param {boolean} data.requiresReset
   * @param {string} data.username
   * @param {string} data.id
   */
  constructor({ access_token, refresh_token, is_admin, requiresReset, username, id }) {
    this.access_token = access_token
    this.refresh_token = refresh_token
    this.is_admin = is_admin
    this.requiresReset = requiresReset
    this.username = username
    this.id = id
  }

  /**
   * Returns plain object for storage or API
   */
  toJSON() {
    return {
      access_token: this.access_token,
      refresh_token: this.refresh_token,
      is_admin: this.is_admin,
      requiresReset: this.requiresReset,
      username: this.username,
      id: this.id
    }
  }
}
