import { createRouter, createWebHashHistory } from 'vue-router'

import Resume from '@/views/Resume.vue'

const routes = [
  {
    path: '/',
    redirect:'/home'
  },
  {
    path: '/home',
    name: 'home',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/home.vue')
  },
  //添加新的路由
  {
    path: '/CV',
    name: 'CV',
    component: Resume
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
