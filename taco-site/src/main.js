
import { createApp } from 'vue'
import AlimentoComponent from './components/AlimentoComponent.vue'
import CategoriaComponent from './components/CategoriaComponent.vue'
import alimentoModal from './components/AlimentoModal.vue'

import App from './App.vue'
import './assets/tailwind.css'

const app = createApp(App)
app.component('AlimentoComponent', AlimentoComponent)
app.component('CategoriaComponent', CategoriaComponent)
app.component('AlimentoModal', alimentoModal)
const mountedApp = app.mount('#app')
