
<template>

    <h2 class="nomeAlimento">{{ alimento }}</h2>
    <p>Kcal: {{ parseFloat(energia).toFixed(0) }}</p>
    <p>Proteínas: {{ parseFloat(proteina).toFixed(0) }}</p>
    <p>Carboidratos: {{ parseFloat(carboidrato).toFixed(0) }}</p>

</template>

<script>

import { Alimento } from "../classes/alimento.js";

export default {
    name: 'Alimento',
    props: {
        alimentoObj: {
            type: Object,
        }
    },
    data() {
        return this.alimentoObj;
    }
}

</script>
