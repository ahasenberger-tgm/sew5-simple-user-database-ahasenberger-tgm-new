<template>
  <div>
    <p>Home</p>
    <p>Random Data: {{wert}}</p>
    <button @click="getRandom">Get Data</button>
  </div>
</template>

<script>
  import axios from 'axios'

export default {
 data () {
   return {
     wert: "kein Wert"
   }
 },
methods: {
  getRandomInt (min, max) {
    min = Math.ceil(min)
    max = Math.floor(max)
    return Math.floor(Math.random() * (max - min + 1)) + min
  },
  getRandom () {
    //this.randomNumber = this.getRandomInt(1, 100)
    this.wert = this.getDataFromBackend()
  },

  getDataFromBackend(){
    const path = 'https://microgreengamification.herokuapp.com/erfolg';
    axios.get(path)
      .then(response => {
        this.wert = response.data.name
      })
      .catch(error => {
        console.log(error)
      });
  }
  },
  created () {
   this.getRandom()
  }
}
</script>
