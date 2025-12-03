<template>
  <div class="w-full h-full">
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js'

export default {
  name: 'OccupancyChart',
  props: {
    data: Object
  },
  mounted() {
    this.renderChart()
  },
  methods: {
    renderChart() {
      Chart.register(...registerables)
      
      const ctx = this.$refs.chartCanvas.getContext('2d')
      new Chart(ctx, {
        type: 'line',
        data: this.data,
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: false
            }
          },
          scales: {
            y: {
              beginAtZero: true,
              max: 100,
              ticks: {
                callback: function(value) {
                  return value + '%'
                }
              }
            }
          }
        }
      })
    }
  }
}
</script>