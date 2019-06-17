<template>
  <div class="row">
    <div class="col-md-6">
      <b-input-group size="sm" prepend="Desde">
        <datepicker :language="es" v-model="filter_dates.start" @input="change_event"></datepicker>
      </b-input-group>
    </div>
    <div class="col-md-6">
      <b-input-group size="sm" prepend="Hasta">
        <datepicker :language="es" v-model="filter_dates.end" @input="change_event"></datepicker>
      </b-input-group>
    </div>
  </div>
</template>

<script>
  import Datepicker from 'vuejs-datepicker';
  import {en, es} from 'vuejs-datepicker/dist/locale'

  export default {
    name: 'ChartFilter',
    components: {
      Datepicker
    },
    props: ["filter_dates"],
    data () {
      return {
        en: en,
        es: es
      }
    },
    methods:{
      change_event(e){
        this.$bus.$emit('change-chart');
      }
    }
  }
</script>