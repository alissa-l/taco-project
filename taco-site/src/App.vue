<template>

  <div class="flex flex-row flex-nowrap items-center justify-center">

    <!-- Seta pra voltar -->
    <span class="justify-self-start cursor-pointer" v-if="mostrarAlimentos" @click="invertExibicao()">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6 ">
        <path fill-rule="evenodd"
          d="M7.72 12.53a.75.75 0 0 1 0-1.06l7.5-7.5a.75.75 0 1 1 1.06 1.06L9.31 12l6.97 6.97a.75.75 0 1 1-1.06 1.06l-7.5-7.5Z"
          clip-rule="evenodd" />
      </svg>

    </span>

    <!-- Titulo -->
    <h1 class="justify-self-center">Tabela Taco</h1>

  </div>

  <!-- Container com categorias -->
  <section class="md:container columns-3 object-center pb-5">
    <div style="cursor: pointer;" v-if="mostrarCategorias" v-on:click="showCategoria(categoria)" class="row"
      v-for="categoria in categorias">
      <h2 class="nomeAlimento">{{ categoria }}</h2>
    </div>
  </section>

  <!-- Componente da categoria se estiver selecionada -->
  <section v-if="mostrarAlimentos">
    <CategoriaComponent :nome="categoriaSelecionada" :alimentos="alimentosPorCategoria[categoriaSelecionada]">
    </CategoriaComponent>
  </section>
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