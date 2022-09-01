<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from "./components/common/NavBar.vue";
import {onMounted} from "vue";
import {useUserStore} from "./stores/user";

const userStore = useUserStore()
onMounted(
    async () => {
      await userStore.fetchUser()
    }
)

</script>

<template>
  <header>
    <NavBar />
  </header>

  <RouterView />
</template>

<style scoped>
</style>
