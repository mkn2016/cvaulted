import { createApp} from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import moment from "moment"
import './css/index.css'

axios.defaults.baseURL = "http://localhost:8004/api/v1/"
axios.defaults.withCredentials = true

const app =  createApp(App)

app.config.globalProperties.$moment = moment
app.use(store)
app.use(router)
app.mount("#app")
