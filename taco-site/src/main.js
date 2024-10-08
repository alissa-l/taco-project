import './assets/global.css'

import { createApp } from 'vue'
import AlimentoComponent from './components/AlimentoComponent.vue'
import CategoriaComponent from './components/CategoriaComponent.vue'
import DetalhesAlimento from './components/DetalhesAlimento.vue'

import App from './App.vue'

const app = createApp(App)
app.component('AlimentoComponent', AlimentoComponent)
app.component('CategoriaComponent', CategoriaComponent)

const mountedApp = app.mount('#app')
