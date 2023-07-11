import { createRouter, createWebHistory } from 'vue-router'
import SearchResult from '../components/SearchResult.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/search',
      name: 'search',
      component: SearchResult
    },
  ]
})

export default router
