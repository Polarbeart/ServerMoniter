var ec_right1 = echarts.init(document.getElementById('r1'),"dark");
var ec_right1_option = {
	//标题样式
	title : {
	    text : "RealTimeIO",
	    textStyle : {
	        color : 'white',
	    },
	    left : 'left'
	},
	  color: ['#3398DB'],
	    tooltip: {
	        trigger: 'axis',
	        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
	            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
	        }
	    },
    xAxis: {
        type: 'category',
        data: []
    },
    yAxis: {
        type: 'value',
        //与x轴平行的线样式
		splitLine: {
			show: true,
			lineStyle: {
				color: '#17273B',
				width: 1,
				type: 'solid',
			}
		}
    },
    legend: {
		data: ['realTimeSent','realTimeRcvd'],
		left: "middle"
	},
   	series: [{
		name: "realTimeSent",
		type: 'line',
		smooth: true,
		data: []//[260, 406, 529]
	}, {
		name: "realTimeRcvd",
		type: 'line',
		smooth: true,
		data: []//[54, 37, 3935]
	}]
};
ec_right1.setOption(ec_right1_option)