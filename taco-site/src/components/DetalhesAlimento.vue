<template>
    <section>
        <p>Kcal: {{ parseFloat(alimentoDetalhe.energia).toFixed(0) }}</p>
        <p>Proteínas: {{ parseFloat(alimentoDetalhe.proteina).toFixed(0) }}</p>
        <p>Carboidratos: {{ parseFloat(alimentoDetalhe.carboidrato).toFixed(0) }}</p>
        <p>Fibra Alimentar: {{ parseFloat(alimentoDetalhe.alimentar).toFixed(0) }}</p>
        <p>Ácido Graxo Saturado: {{ parseFloat(alimentoDetalhe.agSaturado).toFixed(0) }}</p>
        <p>Ácido Graxo Monoinsaturado: {{ parseFloat(alimentoDetalhe.agMonoinsaturado).toFixed(0) }}</p>
        <p>Ácido Graxo Poliinsaturado: {{ parseFloat(alimentoDetalhe.agPoliinsaturado).toFixed(0) }}</p>
        <p>Colesterol: {{ parseFloat(alimentoDetalhe.colesterol).toFixed(0) }}</p>
        <p>Cálcio: {{ parseFloat(alimentoDetalhe.calcio).toFixed(0) }}</p>
        <p>Magnésio: {{ parseFloat(alimentoDetalhe.magnesio).toFixed(0) }}</p>
        <p>Manganês: {{ parseFloat(alimentoDetalhe.manganes).toFixed(0) }}</p>
        <p>Fósforo: {{ parseFloat(alimentoDetalhe.fosforo).toFixed(0) }}</p>
        <p>Ferro: {{ parseFloat(alimentoDetalhe.ferro).toFixed(0) }}</p>
        <p>Sódio: {{ parseFloat(alimentoDetalhe.sodio).toFixed(0) }}</p>
        <p>Potássio: {{ parseFloat(alimentoDetalhe.potassio).toFixed(0) }}</p>
        <p>Cobre: {{ parseFloat(alimentoDetalhe.cobre).toFixed(0) }}</p>
        <p>Zinco: {{ parseFloat(alimentoDetalhe.zinco).toFixed(0) }}</p>
        <p>Retinol: {{ parseFloat(alimentoDetalhe.retinol).toFixed(0) }}</p>
        <p>RE: {{ parseFloat(alimentoDetalhe.re).toFixed(0) }}</p>
        <p>Tiamina: {{ parseFloat(alimentoDetalhe.tiamina).toFixed(0) }}</p>
        <p>Riboflavina: {{ parseFloat(alimentoDetalhe.riboflavina).toFixed(0) }}</p>
        <p>Piridoxina: {{ parseFloat(alimentoDetalhe.piridoxina).toFixed(0) }}</p>
        <p>Niacina: {{ parseFloat(alimentoDetalhe.niacina).toFixed(0) }}</p>
        <p>Vitamina C: {{ parseFloat(alimentoDetalhe.vitaminac).toFixed(0) }}</p>
        <p>Vitamina E: {{ parseFloat(alimentoDetalhe.vitaminaE).toFixed(0) }}</p>
    </section>  
</template>

<script>

import { Modal } from 'flowbite';
import { Alimento } from '@/classes/alimento';

export default {
    name: 'alimentoDetalhe',
    props: {
        alimentoDetalhe: {
            type: Object,
        },
        specifics: {
            type: Array,
            default: () => [],
        }
    },
    setup(props) {
        return {props}
    }
}

</script>
