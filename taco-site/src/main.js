import './assets/main.css'

import { createApp } from 'vue'
import AlimentoComponent from './components/AlimentoComponent.vue'

import App from './App.vue'

const app = createApp(App)
app.component('AlimentoComponent', AlimentoComponent)
const montedApp = app.mount('#app')
