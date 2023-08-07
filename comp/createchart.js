function newChart(id,labeldata,labelname,chartdata) {
    const ctx = document.getElementById(id).getContext('2d');
    const chart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labeldata,
        datasets: [{
          label: labelname,
          data: chartdata
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        },
        plugins: {
        tooltip: {
          callbacks: {
            title: function(context) {
              var index = context[0].dataIndex;
              var reversedIndex = context[0].dataset.data.length - 1 - index;//indexを逆順にしてグラフ描画のreverseに対応させる
              var title = titles[reversedIndex];
              return title;
            }
          }
        }
      }
      }
    });
    return chart;
  }