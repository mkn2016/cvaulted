import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Dashboard from '../views/Dashboard.vue'
import Users from '../views/Users.vue'
import Roles from '../views/Roles.vue'
import Accounts from '../views/Accounts.vue'
import PublicLayout from '../layouts/PublicLayout.vue'
import BaseLayout from '../layouts/BaseLayout.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Login',
    component: Login,
    meta: {
      layout: PublicLayout
    }
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
    meta: {
      layout: PublicLayout
    }
  },
  {
    path: "/secure",
    name: "BaseLayout",
    component: BaseLayout,
    children: [
      {
        path: 'dashboard',
        name: 'Dashboard',
        component: Dashboard,
      },
      {
        path: 'users',
        name: 'users',
        component: Users,
      },
      {
        path: 'roles',
        name: 'Roles',
        component: Roles,
      },
      {
        path: 'accounts',
        name: 'Accounts',
        component: Accounts,
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
