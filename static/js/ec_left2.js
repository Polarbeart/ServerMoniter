var ec_left2 = echarts.init(document.getElementById('l2'), "dark");
var ec_left2_Option = {
	tooltip: {
		trigger: 'axis',
		//指示器
		axisPointer: {
			type: 'line',
			lineStyle: {
				color: '#7171C6'
			}
		},
	},
//	legend: {
//		data: ['内存使用量'],
//		left: "middle"
//	},
	//标题样式
	title: {
		text: "MemeoryInfo",
		textStyle: {
			color: 'white',
		},
		left: 'left'
	},
	//图形位置
	grid: {
		left: '4%',
		right: '6%',
		bottom: '4%',
		top: 50,
		containLabel: true
	},
	xAxis: [{
		type: 'category',
		//x轴坐标点开始与结束点位置都不在最边缘
		// boundaryGap : true,
        boundaryGap: false,
		data: []
	}],
	yAxis: [{
		type: 'value',
		max: 100,
		//y轴字体设置

		//y轴线设置显示
		axisLine: {
			show: true
		},
//		axisLabel: {
//			show: true,
//			color: 'white',
//			fontSize: 12,
//			formatter: function(value) {
//				if (value >= 1000) {
//					value = value / 1000 + 'k';
//				}
//				return value;
//			}
//		},
		//与x轴平行的线样式
		splitLine: {
			show: true,
			lineStyle: {
				color: '#17273B',
				width: 1,
				type: 'solid',
			}
		}
	}],
	series: [{
		name: "内存使用量",
		type: 'line',
		smooth: true,
		data: [],
		areaStyle: {}
	}]
};

ec_left2.setOption(ec_left2_Option)
