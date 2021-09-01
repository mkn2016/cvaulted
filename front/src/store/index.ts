import { createStore } from 'vuex'
import router from '../router'
import axios from 'axios'

export default createStore({
  state: {
    token: "",
    user: {},
    authenticated: false,
    users: [],
    accounts: [],
    statistics: {},
    roles: []
  },
  mutations: {
    setUsers: (state, payload) => {
      state.users = payload
    },
    setRoles: (state, payload) => {
      state.roles = payload
    },
    setStatistics: (state, payload) => {
      state.statistics = payload
    },
    setAccounts: (state, payload) => {
      state.accounts = payload
    },
    setToken: (state, token) => {
      state.token = token
      if (token && state.token) {
        state.authenticated = true
      } else {
        state.authenticated = false
      }
    },
    reset: (state) => {
      state.token = ""
      state.user = {}
      state.authenticated = false
    },
    setUser: (state, payload) => {
      state.user = payload
    },
  },
  actions: {
    setToken({commit}, payload) {
      commit("setToken", payload)
    },
    setUser({commit}, payload) {
      commit("setUser", payload)
    },
    setUsers({commit}, payload) {
      commit("setUsers", payload)
    },
    setAccounts({commit}, payload) {
      commit("setAccounts", payload)
    },
    async register({commit}, payload) {
      console.log(payload)

      await axios.post(
        "auth/register",
        payload

      ).then(response => {
        console.log(response.data)
      }).catch(error => {
        if (error.response) {
          console.log(error.response)
        } else if (error.request) {
          console.log(error.request);
          console.log(error.request.message);
        } else {
          console.log('Error', error.message);
        }
      })
    },
    async fetchRoles({commit}) {
      const sessionToken = sessionStorage.getItem("token")

      await axios.get(
        "roles/",
          {
              headers: {
              "Authorization": "Bearer " + sessionToken,
              },
              withCredentials: true
          }
      ).then(response => {
        commit("setRoles", response.data["data"])
      }).catch(error => {
        console.log(error.message)
      })
    },
    async fetchUsers({commit}) {
      const sessionToken = sessionStorage.getItem("token")

      await axios.get(
        "users/",
          {
              headers: {
              "Authorization": "Bearer " + sessionToken,
              },
              withCredentials: true
          }
      ).then(response => {
        commit("setUsers", response.data["data"])
      }).catch(error => {
        console.log(error.message)
      })
    },
    async fetchAccounts({commit}) {
      const sessionToken = sessionStorage.getItem("token")

      await axios.get(
        "users/accounts",
          {
              headers: {
              "Authorization": "Bearer " + sessionToken,
              },
              withCredentials: true
          }
      ).then(response => {
        commit("setAccounts", response.data["data"])
      }).catch(error => {
        console.log(error.message)
      })
    },
    async fetchStatistics({commit}) {
      const sessionToken = sessionStorage.getItem("token")

      await axios.get(
        "statistics/",
          {
              headers: {
              "Authorization": "Bearer " + sessionToken,
              },
              withCredentials: true
          }
      ).then(response => {
        commit("setStatistics", response.data["data"])
      }).catch(error => {
        console.log(error.message)
      })
    },
    async logout({commit}) {
      await axios.post(
        "auth/logout"
      ).then(_=> {
        commit("reset")
        sessionStorage.removeItem("token")
        router.push("/")
      })
    }
  },
  modules: {
  }
})
