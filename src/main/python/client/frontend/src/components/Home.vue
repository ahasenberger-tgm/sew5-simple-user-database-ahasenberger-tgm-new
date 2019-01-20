<template>
  <div>
    <p>Home</p>
    <!--<p>Users: {{usersjson}}</p>-->
    <input v-model="deleteuserid" name="deleteuserid" id="deleteuserid" placeholder="UserID to delete">
    <button @click="deleteUser">Delete Users</button>
    <br>
    <br>
    <input v-model="usernameeingabe" name="usernameeingabe" placeholder="Insert a new Username">
    <input v-model="emaileingabe" name="emaileingabe" placeholder="Insert a new email address">
    <button @click="addUser">Add a new User</button>
    <br>
    <br>
    <table id="UserTable" align="center">
      <thead>
        <tr>
          <th>ID</th>
          <th>username</th>
          <th>email</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in usersjson">
          <td>{{row.id}}</td>
          <td>{{row.username}}</td>
          <td>{{row.email}}</td>
        </tr>
      </tbody>
    </table>
    <br>
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
      deleteuserid: 0,
      usersjson: {},
      usernameeingabe: '',
      emaileingabe: ''
    }
  },
  methods: {
    deleteUser () {
      const delpath = 'http://localhost:5000/userdelete?userid=' + this.deleteuserid + '&username=&email='
      axios.get(delpath)
    },

    getUsers () {
      const path = 'http://127.0.0.1:5000/userget'
      axios.get(path)
        .then(response => {
          // this.wert = response.data
          this.usersjson = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },

    addUser () {
      const addpath = 'http://localhost:5000/useradd?username=' + this.usernameeingabe + '&email=' + this.emaileingabe
      axios.get(addpath)
      setTimeout(function () {}, 1000)
      window.location.reload(true)
    }
  },
  created () {
    this.getUsers()
  }
}
</script>
