<template>


  <div class="container">

    <div class="row" v-for="chunk in alimentosChunked">



      <div class="col" v-for="alimento in chunk">

        <AlimentoComponent :alimentoObj="alimento" >
        </AlimentoComponent>

      </div>
    
    </div>


  </div>

  
</template>

<script>

//Se precisar dividir os repos
//import tacoData from "./taco_data/taco2011.json";
import tacoData from "../../data/taco2011.json";
import { Alimento } from "./classes/alimento.js";

export default {
    name: 'App',
    data() {
        return {
          categorias: [],
          alimentos: [],
          alimentosChunked: [],
          unidades: [],
        }
    },
    beforeMount() {
      this.getData();
    },
    methods: {
        getData() {


          let categorias = tacoData['Categorias'];
          let myData = tacoData['Data'];
          let unidades = tacoData['NutrientesUnidades'];

          for (let i = 0; i < categorias.length; i++) {
            let alimentosCategoria = myData[categorias[i]];

            for (let j = 0; j < alimentosCategoria.length; j++) {
              let alimento = Object.assign(new Alimento, alimentosCategoria[j]);
              this.alimentos.push(alimento);
            }
          }

          for (let i = 0; i < unidades.length; i++) {
            let unidade = unidades[i];
            this.unidades.push(unidade);
          }

          this.dataChunk(this.alimentos, 3);
          
        },
        dataChunk(array, size) {
          let chunkedArray = [];
          for (let i = 0; i < array.length; i += size) {
            chunkedArray.push(array.slice(i, i + size));
          }
          this.alimentosChunked = chunkedArray;
        }
    },    
}

</script>