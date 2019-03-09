import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login'
import ManageTeacher from '@/components/ManageTeacher'
import ManageComputerRoom from '@/components/ManageComputerRoom'
import ManageCourse from '../components/ManageCourse'
import App from '../App'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'App',
      component: App,
    }/*,
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/manage-teacher',
      name: 'ManageTeacher',
      component: ManageTeacher
    },
    {
      path: '/manage-computer-room',
      name: 'ManageComputerRoom',
      component: ManageComputerRoom
    },
    {
      path: '/manage-course',
      name: 'ManageCourse',
      component: ManageCourse
    }*/
  ]
})
