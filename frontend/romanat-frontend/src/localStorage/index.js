import { reactive, watch } from "vue"
import dlv from "dlv"

export const store = reactive({ logged_in_user: null })

export const save = async (key, value) => {
  localStorage.setItem(key, JSON.stringify(value))
  store[key] = value
}


export const set = (key, update) => {
  store[key] = { ...(store[key] || {}), ...update }
}

export const unSet = (key) => {
  store[key] = null
}

export const remove = (key) => {
  return new Promise((resolve) => {
    localStorage.removeItem(key)
    unSet(key)
    resolve()
  })
}

export const get = (path) => dlv(store, path)

export const load = (key) => {
  return new Promise((resolve) => {
    try {
      const value = JSON.parse(localStorage.getItem(key))
      if (value) set(key, value)
      resolve(get(key))
    } catch {
      resolve(get(key))
    }
  })
}

export const authorize = (key, callback) => {
  watch(
    () => store[key],
    (keyValue) => callback(keyValue)
  )
}
