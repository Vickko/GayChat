import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import IndexView from '../views/IndexView.vue'
import LoginBox from '@/components/LoginBox'
import ForgetPasswd from '@/components/ForgetPasswd'
import SignUp from '@/components/SignUp'
import ChatBox from '@/components/ChatBox'

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
    path: '/loginView',
    name: 'login',
    component: LoginView,
    redirect: '/login',
    children: [
      { path: '/login', component: LoginBox },
      { path: '/forgetPasswd', component: ForgetPasswd },
      { path: '/signUp', component: SignUp }
    ]
  },
  {
    path: '/index',
    name: 'index',
    component: IndexView,
    children: [{ path: '/chat', component: ChatBox }]
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
