<template>
  
  <div class="container">
    <span v-if="mostrarAlimentos" @click="invertExibicao()">
      <svg style="width: 2em; height: 2em;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8"/>
    </svg>  </span>


    <div style="cursor: pointer;" v-if="mostrarCategorias" v-on:click="showCategoria(categoria)" class="row" v-for="categoria in categorias">
        <h2 class="nomeAlimento">{{ categoria }}</h2>
    </div>


    <section v-if="mostrarAlimentos">
      <CategoriaComponent :nome="categoriaSelecionada" :alimentos="alimentosPorCategoria[categoriaSelecionada]"></CategoriaComponent>
    </section>

    
  </div>

</template>

<script>

//Se precisar dividir os repos
import tacoData from "./assets/data/taco2011.json";
import { Alimento } from "./classes/alimento.js";
import CategoriaComponent from "./components/CategoriaComponent.vue";

export default {
    name: 'App',
    data() {
        return {
          categorias: [],
          alimentosPorCategoria: {},
          unidades: [],
          mostrarCategorias: true,
          categoriaSelecionada: [],
          mostrarAlimentos: false,
        }
    },
    beforeMount() {
      this.getData();
    },
    methods: {
        getData() {


          this.categorias = tacoData['Categorias'];
          
          let myData = tacoData['Data'];
          let unidades = tacoData['NutrientesUnidades'];

          for (let i = 0; i < this.categorias.length; i++) {
            this.alimentosPorCategoria[this.categorias[i]] = [];
            let alimentosCategoria = myData[this.categorias[i]];
            let j = 0;
            for (let alimento in alimentosCategoria) {
              let alimentoObj = Object.assign(new Alimento, alimentosCategoria[alimento]);
              this.alimentosPorCategoria[this.categorias[i]].push(alimentoObj);
              j++;
            }
          }

          for (let i = 0; i < unidades.length; i++) {
            let unidade = unidades[i];
            this.unidades.push(unidade);
          }          
        },
        showCategoria(categoria) {
          console.log(this.categorias)
          console.log(this.alimentosPorCategoria[categoria])
          console.log(categoria)
          this.categoriaSelecionada = categoria;
          this.mostrarCategorias = false;
          this.mostrarAlimentos = true;
        },

        invertExibicao() {
          this.mostrarCategorias = !this.mostrarCategorias;
          this.mostrarAlimentos = !this.mostrarAlimentos;
        }
    },    
}

</script>