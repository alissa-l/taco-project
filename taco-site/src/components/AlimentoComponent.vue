
<template>

    <div class="alimento">
        <h3 class="nomeAlimento">{{ alimentoObj.nome }}</h3>
        <p>Kcal: {{ parseFloat(alimentoObj.energia).toFixed(0) }}</p>
        <p>Proteínas: {{ parseFloat(alimentoObj.proteina).toFixed(0) }}</p>
        <p>Carboidratos: {{ parseFloat(alimentoObj.carboidrato).toFixed(0) }}</p>

        <p style="cursor:pointer" @click="showDetalhesModal(alimentoObj.nome)"> {{ showDetalhes ? "Esconder detalhes" : "Mostrar detalhes" }} </p>

        <vs-modal :ref=alimentoObj.nome v-model="showDetalhes" :title="'Detalhes de ' + alimentoObj.nome">
            <section v-if=showDetalhes>
                <DetalhesAlimento :alimentoDetalhe=alimentoObj></DetalhesAlimento>
            </section>
        </vs-modal>
    </div>

</template>

<script>

import DetalhesAlimento from './DetalhesAlimento.vue'
import {ref} from 'vue'
import VsModal from '@vuesimple/vs-modal';

export default {
    name: 'Alimento',
    components: {VsModal, DetalhesAlimento},
    props: {
        alimentoObj: {
            type: Object,
        },
    },
    data() {
        return {
            showDetalhes: false,
        }
    },
    methods: {
        showDetalhesModal(nome) {
            this.$refs[nome].open();
            this.showDetalhes = true;
        }
    },
}

</script>
