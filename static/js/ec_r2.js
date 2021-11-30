var ec_right2 = echarts.init(document.getElementById('r2'), "dark");
// var dom = document.getElementById("container");
// var myChart = echarts.init(dom);
var app = {};



// var option;
var ec_right2_option


const gaugeData = [
  {
    value: 20,
    name: 'Wait',
    title: {
      offsetCenter: ['-40%', '80%']
    },
    detail: {
      offsetCenter: ['-40%', '95%']
    }
  },
  {
    value: 40,
    name: 'Busy',
    title: {
      offsetCenter: ['0%', '80%']
    },
    detail: {
      offsetCenter: ['0%', '95%']
    }
  },
  {
    value: 60,
    name: 'Health',
    title: {
      offsetCenter: ['40%', '80%']
    },
    detail: {
      offsetCenter: ['40%', '95%']
    }
  }
];
ec_right2_option = {
  //标题样式
	title: {
		text: "LoadAverage",
		textStyle: {
			// color: 'white',
		},
		left: 'left',
	},
  series: [
    {
      type: 'gauge',
      anchor: {
        show: true,
        showAbove: true,
        size: 18,
        itemStyle: {
          color: '#FAC858'
        }
      },
      pointer: {
        icon: 'path://M2.9,0.7L2.9,0.7c1.4,0,2.6,1.2,2.6,2.6v115c0,1.4-1.2,2.6-2.6,2.6l0,0c-1.4,0-2.6-1.2-2.6-2.6V3.3C0.3,1.9,1.4,0.7,2.9,0.7z',
        width: 8,
        length: '80%',
        offsetCenter: [0, '8%']
      },
      progress: {
        show: true,
        overlap: true,
        roundCap: true
      },
      axisLine: {
        roundCap: true
      },
      data: gaugeData,
      title: {
        fontSize: 14
      },
      detail: {
        width: 40,
        height: 14,
        fontSize: 14,
        color: '#fff',
        backgroundColor: 'auto',
        borderRadius: 3,
        formatter: '{value}%'
      }
    }
  ]
};
setInterval(function () {
   gaugeData[0].value = +(Math.random() * 100).toFixed(2);
   gaugeData[1].value = +(Math.random() * 100).toFixed(2);
   gaugeData[2].value = +(Math.random() * 100).toFixed(2);
//  console.log(gaugeData)
  ec_right2.setOption({
    series: [
      {
        data: gaugeData
        
      }
    ]
  });
}, 2000);

if (ec_right2_option && typeof ec_right2_option === 'object') {
    // myChart.setOption(option);
    ec_right2.setOption(ec_right2_option)
}
ec_right2.setOption(ec_right2_option)