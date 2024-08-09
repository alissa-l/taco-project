
<template>

    <h2> {{ nome }} </h2>
    <section class="md-container columns-3 ">
        <AlimentoComponent class="m-3" v-for="aliment in alimentos" :alimentoObj="aliment" :mostrarDetalhes="false"></AlimentoComponent>
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
