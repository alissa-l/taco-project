<template>
  <h1>oi</h1>
  
  <button @click="getData()">AAAAAAA</button>
  
</template>

<script>

//Se precisar dividir os repos
//import tacoData from "./taco_data/taco2011.json";
import tacoData from "../../data/taco2011.json";



export default {
    name: 'App',
    data() {
        return {
            data1: [],
            message: 'Hello World!'
        }
    },
    methods: {
        getData() {
          let myDataArr = Array.from(tacoData['Data']);

          

          console.log(myDataArr)

          

        }
    },    
}

</script>