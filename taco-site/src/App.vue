<template>
  <div class="container">
    <div style="cursor: pointer;" v-if="showCategorias" v-on:click="showCategoria(categoria)" class="row" v-for="categoria in categorias">
        <h2 class="nomeAlimento">{{ categoria }}</h2>
    </div>
  </div>

  <div v-if="showAlimentos">
    <CategoriaComponent :nome="categoriaSelecionada" :alimentos="alimentosByCategoria[categoriaSelecionada]"></CategoriaComponent>
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
          alimentosByCategoria: {},
          unidades: [],
          showCategorias: true,
          showAlimentos: false,
          categoriaSelecionada: [],
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
            this.alimentosByCategoria[this.categorias[i]] = [];
            let alimentosCategoria = myData[this.categorias[i]];
            let j = 0;
            for (let alimento in alimentosCategoria) {
              let alimentoObj = Object.assign(new Alimento, alimentosCategoria[alimento]);
              this.alimentosByCategoria[this.categorias[i]].push(alimentoObj);
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
          console.log(this.alimentosByCategoria[categoria])
          console.log(categoria)
          this.categoriaSelecionada = categoria;
          this.showCategorias = false;
          this.showAlimentos = true;
        }
    },    
}

</script>