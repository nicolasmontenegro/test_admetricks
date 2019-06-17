<template>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <h1>Variante de divisa</h1>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <ChartFilter :filter_dates="filter_dates"></ChartFilter>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <ChartDollar :dollar_list="dollar_list" :filter_dates="filter_dates"></ChartDollar>
      </div>
    </div>
  </div>
</template>

<script>
import Logo from '~/components/Logo.vue';
import ChartDollar from '~/components/ChartDollar.vue';
import ChartFilter from '~/components/ChartFilter.vue';

export default {
  components: {
    Logo,
    ChartDollar,
    ChartFilter
  },
  data(){
    return{
      dollar_list: [],
      filter_dates:{
        start: new Date(new Date().setDate(new Date().getDate()-10)),
        end: new Date(Date.now())
      }
    }
  },
  watch: {  
    filter_dates(){
      this.fetch_data();
    }
  },
  mounted(){
    this.fetch_data();
    this.$bus.$on('change-chart', (e) => {this.fetch_data()})
  },
  methods:{
    fetch_data(){
      fetch(`http://127.0.0.1:8000/dollar/?format=json&date_start=${this.filter_dates.start.toISOString().slice(0,10)}&date_end=${this.filter_dates.end.toISOString().slice(0,10)}`)
        .then(response => (response.json()))
        .then(result => (this.dollar_list = result));
    }
  }

}
</script>