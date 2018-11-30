<template>
  <div>
    <p>Home</p>
    <p>Users: {{wert}}</p>
    <input v-model="deleteuserid" name="deleteuserid" placeholder="UserID to delete">
    <button @click="deleteUser">Delete Users</button>
    <br>
    <button @click="getUsers">Get Data</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      wert: 'kein Wert',
      deleteuserid: 0
    }
  },
  methods: {
    deleteUser () {
      const delpath = 'http://localhost:5000/userdelete/?userid=' + this.deleteuserid + '&username=&email='
      axios.get(delpath)
    },

    getUsers () {
      const path = 'http://127.0.0.1:5000/userget'
      axios.get(path)
        .then(response => {
          this.wert = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getUsers()
  }
}
</script>
