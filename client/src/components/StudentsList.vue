<template>
<div></div>
  <ul>
    <li v-for="student in students" :style="{color}"> {{ student.name }} </li>
  </ul>

</template>

<script>
export default {
  name: "StudentsList",
  props: {
    color: String
  },
  data() {
    return {
      students: []
    }
  },
  async beforeMount() {
    const response = await fetch('/api/v1/lms/student/')

    if (response.status === 200) {
      const results = await response.json()
      this.students = results.results

    }
  }

}
</script>

<style scoped>
</style>