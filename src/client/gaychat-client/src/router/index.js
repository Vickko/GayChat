import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView'
import LoginView from '../views/LoginView'
import IndexView from '../views/IndexView'
import LoginBox from '@/components/LoginBox'
import ForgetPasswd from '@/components/ForgetPasswd'
import SignUp from '@/components/SignUp'
import ChatView from '../views/test_ChatView'
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
    children: [
      {
        path: '/chat',
        name: 'chat',
        component: ChatView,
        children: [{ path: '/chatbox', name: 'chatbox', component: ChatBox }]
      }
    ]
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
