import Vue from 'vue'
import Router from 'vue-router'
import index from '@/components/index'
import allNews from '../components/allNews'
import about from '../components/about'
import HuanQiu from '../components/huanqiu'
import Netease from '../components/Netease'
import PaperNews from '../components/PaperNews'
import PeopleDaily from '../components/PeopleDaily'
import Tencent from '../components/Tencent'
import sohu from '../components/sohu'
import digest from '../components/digest'
Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/all',
      name: 'all',
      component: allNews
    },
    {
      path: '/about',
      name: 'about',
      component: about
    },
    {
      path: '/huanqiu',
      name: 'huanqiu',
      component: HuanQiu
    },
    {
      path: '/netease',
      name: 'netease',
      component: Netease
    },
    {
      path: '/papernews',
      name: 'papernews',
      component: PaperNews
    },
    {
      path: '/peopledaily',
      name: 'peopledaily',
      component: PeopleDaily
    },
    {
      path: '/tencent',
      name: 'tencent',
      component: Tencent
    },
    {
      path: '/sohu',
      name: 'sohu',
      component: sohu
    },
    {
      path: '/digest',
      name: 'digest',
      component: digest
    }
  ]
})
