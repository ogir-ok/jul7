<template>
<form @submit="loginUser">
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="data.email">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
    {{error.email}}
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" v-model="data.password">\
    {{error.password}}
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>

</template>

<script>
export default {
  name: "LoginForm",
  data(){
    return {
      data: {
        email: '',
        password: ''
      },
      error: {
      }
    }
  },
  methods: {
    async loginUser(e) {
      e.preventDefault()
      e.stopPropagation()

      console.log(this.data)

      const resp = await fetch('/api/v1/auth/token/',
      {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(this.data)
          }
      )

      if (resp.status === 400) {
        this.error = await resp.json()
        return
      } else {
        const data =  await resp.json()
        localStorage.setItem('userToken', data.access)
      }



    }
  }
}
</script>

<style scoped>

</style>