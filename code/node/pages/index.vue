<template>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <h1>Variante de divisa</h1>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <canvas id="chart-dollar" width="400" height="200"></canvas>
      </div>
    </div>
  </div>
</template>

<script>
import Logo from '~/components/Logo.vue'
import Chart from 'chart.js';

export default {
  components: {
    Logo
  },
  data(){
    return{
      dollar_list: [],
      chart: null
    }
  },
  mounted(){
    fetch("http://127.0.0.1:8000/dollar/?format=json")
        .then(response => (response.json()))
        .then(result => (this.update_data(result)));


    this.chart = new Chart(
      document.getElementById('chart-dollar'), 
      {
        type: 'line',
        data: {
          labels: [],
          datasets: [
            {
              label: 'Variación',
              yAxisID: "delta",
              fill: false,
              backgroundColor: "#ff5029",
              borderColor: "#ffa28e",

              data: []
            },
            {
              label: 'Valor',
              yAxisID: "value",
              fillColor : "#f5f5f5",
              strokeColor : "#eeeeee",
              pointColor : "#d7d7d7",
              pointStrokeColor : "#fff",
              hidden: true,
              data: []
            },]
        },

        options: {

          responsive: true,
          scales: {
            xAxes: [{
              type: "time",
              time: {
                displayFormats: {
                  day: 'YYYY-MM-DD'
                }
              }
            }],
            yAxes: [{
              id: "delta",
              type: 'linear',
              position: "right",
               ticks: {
                min: -15.0, 
                max: 15.0, 
              }

            }, {
              id: "value",
              type: 'linear',
              position: "left",
            }]
          }

        }
      });
  },
  methods:{
    update_data(dollar_list){
      this.dollar_list = dollar_list;

      this.chart.data.labels = this.dollar_list.map((entry) => (entry.value_at));
      this.chart.data.datasets.forEach((dataset) => {
          dataset.data = this.dollar_list.map((entry) => (parseFloat(entry[dataset.yAxisID])));
      }, this);
      this.chart.update();
    }
  }


}
</script>