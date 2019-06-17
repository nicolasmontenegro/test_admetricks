<template>
  <canvas id="chart-dollar" width="400" height="200"></canvas>
</template>

<script>
  import Chart from 'chart.js';

  export default {
    name: 'ChartDollar',
    props: ["dollar_list", "filter_dates"],
    data(){
      return{
        chart: null
      }
    },
    watch: {  
      dollar_list(){this.update_data();}
    },
    mounted(){
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
                  unit: 'day',
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
      update_data(){
        this.chart.data.labels = this.dollar_list.map((entry) => (entry.value_at));
        this.chart.data.datasets.forEach((dataset) => {
            dataset.data = this.dollar_list.map((entry) => (parseFloat(entry[dataset.yAxisID])));
        }, this);
        this.chart.update();
      }
    }
  }
</script>