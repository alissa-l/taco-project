
<template>

    <h1> {{ nome }} </h1>
    <AlimentoComponent v-for="aliment in alimentos" :alimentoObj="aliment"></AlimentoComponent>

</template>

<script>

import { Alimento } from '@/classes/alimento';
import AlimentoComponent from './AlimentoComponent.vue';

export default {
    name: 'Categoria',
    props: {
        nome: {
            type: String,
            required: true,
        },
        alimentos: {
            type: Array,
            default: () => [],
            validator: (value) => {
                return value.every((item) => item instanceof Alimento);
            },
        }
    },
    mounted() {
        console.log(this.alimentos);
    }
}

</script>
