
<template>

    <h2 class="nomeAlimento">{{ alimentoObj.nome }}</h2>
    <p>Kcal: {{ parseFloat(energia).toFixed(0) }}</p>
    <p>Proteínas: {{ parseFloat(proteina).toFixed(0) }}</p>
    <p>Carboidratos: {{ parseFloat(carboidrato).toFixed(0) }}</p>

</template>

<script>


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
