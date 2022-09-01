<template>
  <div>
    <div v-if="userStore.user">
      {{ userStore.getUserName }}

      <a href="#" @click="logOut"> Log out</a>
    </div>
    <div v-else>
      <RouterLink to="login"> Log In </RouterLink>
    </div>
  </div>
</template>

<script>
import {useUserStore} from "../../stores/user";

export default {
  name: "UserBadge",
  setup() {
    const userStore = useUserStore();
    return {
      userStore
    }
  },
  data() {
    return {
      user: this.userStore.user
    }
  },
  methods: {
    logOut() {
      this.userStore.logOut()
    },
    logIn() {
      this.userStore.logIn()
    }
  },
  /*async beforeMount() {
    const token = localStorage.getItem('userToken');
    if (!token) {
      return
    }

    const res = await fetch('/api/v1/auth/current-user/',
        {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        })

    this.user = await res.json()
  }*/
}
</script>

<style scoped>

</style>