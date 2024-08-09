
<template>

    <div class="alimento">
        <h3 class="nomeAlimento">{{ alimentoObj.nome }}</h3>
        <p>Kcal: {{ parseFloat(alimentoObj.energia).toFixed(0) }}</p>
        <p>Proteínas: {{ parseFloat(alimentoObj.proteina).toFixed(0) }}</p>
        <p>Carboidratos: {{ parseFloat(alimentoObj.carboidrato).toFixed(0) }}</p>

        <p style="cursor:pointer" @click="invertDetails()"> {{ showDetalhes ? "Esconder detalhes" : "Mostrar detalhes" }} </p>

        <div v-if="showDetalhes">
            <DetalhesAlimento :alimentoDetalhe="alimentoObj"/>
        </div>

    </div>

</template>

<script>

import DetalhesAlimento from './DetalhesAlimento.vue'
import {ref} from 'vue'

export default {
    name: 'Alimento',
    components: {DetalhesAlimento},
    props: {
        alimentoObj: {
            type: Object,
        },
        mostrarDetalhes: {
            type: Boolean,
            default: false,
        }
    },
    setup(props) {
        const showDetalhesLet = ref(props.mostrarDetalhes)
        let showDetalhes = ref(showDetalhesLet.value)

        const invertDetails = () => {
            showDetalhes.value = !showDetalhes.value
        }

        return {showDetalhes, invertDetails}
    }
}

</script>
