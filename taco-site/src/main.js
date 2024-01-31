
import { createApp } from 'vue'
import AlimentoComponent from './components/AlimentoComponent.vue'
import CategoriaComponent from './components/CategoriaComponent.vue'

import App from './App.vue'
import './assets/tailwind.css'

const app = createApp(App)
app.component('AlimentoComponent', AlimentoComponent)
app.component('CategoriaComponent', CategoriaComponent)
const mountedApp = app.mount('#app')
