<template>

    <h2 class="text-center"> {{ nome }} </h2>
    <section class="md:container grid grid-cols-3 grid-flow-row">
        <AlimentoComponent class="h-1/5 text-nowrap" v-for="aliment in alimentos" :alimentoObj="aliment" :mostrarDetalhes="false"></AlimentoComponent>
    </section>
    

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
    }
}

</script>
