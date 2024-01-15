
<template>

    <img src="assets/" alt="">
    <h2 class="nomeAlimento">{{ alimento }}</h2>

</template>

<script>


export default {
    name: 'Alimento',
    props: {
        categoria: {
            type: String,
        }
    },
    data() {
        return this.alimentoObj;
    }
}

</script>
