import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => {
    return { user: null }
  },

  actions: {
    logOut() {
      this.user = null
    },
    async logIn(data) {
      this.user = {
        'user': 'admin@admin.com'
      }
    }
  },
})