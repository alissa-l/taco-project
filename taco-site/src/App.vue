<template>

  <div class="container">
    <div v-if="showCategorias" class="row" v-for="categoria in categoriasMap">
      <div class="col" v-for="categoria in chunk">
        <CategoriaComponent :categoria="categoria" >
        </CategoriaComponent>
      </div>
    </div>
  </div>

  <!-- <div class="container">
    <div v-if="showAlimentos" class="row" v-for="chunk in alimentosChunked">
      <div class="col" v-for="alimento in chunk">
        <AlimentoComponent :alimentoObj="alimento" >
        </AlimentoComponent>
      </div>
    </div>
  </div> -->

</template>

<script>

//Se precisar dividir os repos
import tacoData from "./assets/data/taco2011.json";
import { Alimento } from "./classes/alimento.js";
import { categoriasMap } from "./classes/categoriasMap.js";

export default {
    name: 'App',
    data() {
        return {
          data: JSON.parse(JSON.stringify(tacoData)),
          categorias: [],
          alimentosPorCategoria: {},
          alimentosChunked: [],
          nutrientesUnidades: {},
          showAlimentos: false,
          showCategorias: true,
          categoriasMap: categoriasMap,
        }
    },
    beforeMount() {
      this.getAlimentos();
    },
    methods: {
        getAlimentos() {

          this.data.Categorias.forEach(element => {
            this.categorias.push(element);
          });

          for (let nutriente in this.data.NutrientesUnidades) {
            this.nutrientesUnidades[nutriente] = this.data.NutrientesUnidades[nutriente];
          }

          for (let categoria in this.data.Alimentos) {

            this.alimentosPorCategoria[categoria] = [];

            for (let alimentoKey in this.data.Alimentos[categoria]) {
              let alimento = Object.assign(new Alimento(), this.data.Alimentos[categoria][alimentoKey]);
              this.alimentosPorCategoria[categoria].push(alimento)
            }
            
          }
          
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