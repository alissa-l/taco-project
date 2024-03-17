
<template>

    <div class="alimento" @click="mostrarDetalhes=!mostrarDetalhes">
        <h2 class="nomeAlimento">{{ alimentoObj.nome }}</h2>
        <p>Kcal: {{ parseFloat(alimentoObj.energia).toFixed(0) }}</p>
        <p>Proteínas: {{ parseFloat(alimentoObj.proteina).toFixed(0) }}</p>
        <p>Carboidratos: {{ parseFloat(alimentoObj.carboidrato).toFixed(0) }}</p>


        <section v-if="mostrarDetalhes" class="alimento-infos-extras">
            <p>Fibra Alimentar: {{ parseFloat(alimentoObj.alimentar).toFixed(0) }}</p>
            <p>Ácido Graxo Saturado: {{ parseFloat(alimentoObj.agSaturado).toFixed(0) }}</p>
            <p>Ácido Graxo Monoinsaturado: {{ parseFloat(alimentoObj.agMonoinsaturado).toFixed(0) }}</p>
            <p>Ácido Graxo Poliinsaturado: {{ parseFloat(alimentoObj.agPoliinsaturado).toFixed(0) }}</p>
            <p>Colesterol: {{ parseFloat(alimentoObj.colesterol).toFixed(0) }}</p>
            <p>Cálcio: {{ parseFloat(alimentoObj.calcio).toFixed(0) }}</p>
            <p>Magnésio: {{ parseFloat(alimentoObj.magnesio).toFixed(0) }}</p>
            <p>Manganês: {{ parseFloat(alimentoObj.manganes).toFixed(0) }}</p>
            <p>Fósforo: {{ parseFloat(alimentoObj.fosforo).toFixed(0) }}</p>
            <p>Ferro: {{ parseFloat(alimentoObj.ferro).toFixed(0) }}</p>
            <p>Sódio: {{ parseFloat(alimentoObj.sodio).toFixed(0) }}</p>
            <p>Potássio: {{ parseFloat(alimentoObj.potassio).toFixed(0) }}</p>
            <p>Cobre: {{ parseFloat(alimentoObj.cobre).toFixed(0) }}</p>
            <p>Zinco: {{ parseFloat(alimentoObj.zinco).toFixed(0) }}</p>
            <p>Retinol: {{ parseFloat(alimentoObj.retinol).toFixed(0) }}</p>
            <p>RE: {{ parseFloat(alimentoObj.re).toFixed(0) }}</p>
            <p>Tiamina: {{ parseFloat(alimentoObj.tiamina).toFixed(0) }}</p>
            <p>Riboflavina: {{ parseFloat(alimentoObj.riboflavina).toFixed(0) }}</p>
            <p>Piridoxina: {{ parseFloat(alimentoObj.piridoxina).toFixed(0) }}</p>
            <p>Niacina: {{ parseFloat(alimentoObj.niacina).toFixed(0) }}</p>
            <p>Vitamina C: {{ parseFloat(alimentoObj.vitaminac).toFixed(0) }}</p>
            <p>Vitamina E: {{ parseFloat(alimentoObj.vitaminaE).toFixed(0) }}</p>
        </section>
    </div>

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
        return {
            alimentoObj: this.alimentoObj,
            mostrarDetalhes: false,

        }
    }
}

</script>
