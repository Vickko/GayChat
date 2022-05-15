import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import LoginBox from '@/components/LoginBox'
import ForgetPasswd from '@/components/ForgetPasswd'
import SignUp from '@/components/SignUp'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    redirect: '/LoginBox',
    children: [
      { path: '/LoginBox', component: LoginBox },
      { path: '/ForgetPasswd', component: ForgetPasswd },
      { path: '/SignUp', component: SignUp }
    ]
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
