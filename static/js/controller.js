function gettime() {
	$.ajax({
		url: "/time",
		timeout: 10000, //超时时间设置为10秒；
		success: function(data) {
			$("#tim").html(data)
		},
		error: function(xhr, type, errorThrown) {

		}
	});
}

function get_c1_data() {
	$.ajax({
		url: "/c1",
		success: function(data) {
			$(".num h1").eq(0).text(data.confirm);
			$(".num h1").eq(1).text(data.suspect);
			$(".num h1").eq(2).text(data.heal);
			$(".num h1").eq(3).text(data.dead);
		},
		error: function(xhr, type, errorThrown) {

		}
	})
}
function get_c2_data2222() {
    $.ajax({
        url:"/c2",
        success: function(data) {
			if (data == null || data == '') {
                    alert("请联系\n管理员维护数据");
                } else {
                    //清空table中的html
                    $("#tabletext").html("");
                    window.obj = data;
                    var arr = Object.keys(data);
                    // var vallue =Object.va(data);
                    var objs = JSON.stringify(data);

                    // console.log(objs);
                    console.log(arr[0])       

                    var str = "";//把数据组装起来
                    for(var i = 0;i<Number(arr.length);i++){
                        str1 = "<tr>" +
                        //data.dataInfo[i]
                            "<td>"+data.process+ "</td>" +
                            "<td>"+data.memory+ "</td>" +
                            "<td>"+data.state+ "</td>" +
                            "<td>"+data.create+ "</td>" +
                            "<td>"+12345+ "</td>" +
//                            "<td>"+data.data[i].user_id + "</td>" +
//                            "<td>"+data.data[i].user_id + "</td>" +
                            "</tr>";
                        $("#tabletext").append(str1);

                    }
                }
		},
		error: function(xhr, type, errorThrown) {

		}
    })
}

function get_l1_data() {
    $.ajax({
        url:"/l1",
        success: function(data) {
			ec_left1_Option.xAxis[0].data=data.time
            ec_left1_Option.series[0].data=data.percent
//            ec_left1_Option.series[1].data=data.suspect
//            ec_left1_Option.series[2].data=data.heal
//            ec_left1_Option.series[3].data=data.dead
            ec_left1.setOption(ec_left1_Option)
		},
		error: function(xhr, type, errorThrown) {

		}
    })
}

function get_l2_data() {
    $.ajax({
        url:"/l2",
        success: function(data) {
			ec_left2_Option.xAxis[0].data=data.time
            ec_left2_Option.series[0].data=data.percent
//            ec_left2_Option.series[1].data=data.suspect_add
            ec_left2.setOption(ec_left2_Option)
		},
		error: function(xhr, type, errorThrown) {

		}
    })
}

function get_r1_data() {
    $.ajax({
        url: "/r1",
        success: function (data) {
            ec_right1_option.xAxis.data=data.time;
            ec_right1_option.series[0].data=data.realTimeSent;
            ec_right1_option.series[1].data=data.realTimeRcvd;

            ec_right1.setOption(ec_right1_option);
        }
    })
}


function get_r2_data() {
             // 0: {value: 94.89, name: 'Good', title: {…}, detail: {…}}
            // 1: {value: 46.38, name: 'Better', title: {…}, detail: {…}}
            // 2: {value: 55.38, name: 'Perfect', title: {…}, detail: {…}}
    $.ajax({
        url: "/r2",
        success: function (data) {
            window.obj = data
            console.log(window.obj)
//            gaugeData[0].value = data.value1;
//            gaugeData[1].value = data.value2;
//            gaugeData[2].value = data.value3;
            // gaugeData[2].value = +(Math.random() * 100).toFixed(2);
            // ec_right2_option.series[0].data=data.kws;
//             ec_right2_option.series[0].data={value: 94.89, name: 'Good',title: {…}, detail: {…}};
//             ec_right2_option.series[2].data={value: 94.89, name: 'Good',title: {…}, detail: {…}};
//             ec_right2_option.series[1].data={value: 94.89, name: 'Good',title: {…}, detail: {…}};
            // ec_right2_option.series[1].data=23;
            // ec_right2_option.series[2].data=23;
            ec_right2_option.series
   
            ec_right2.setOption(ec_right2_option);
        }
    })
}

function get_list_data() {
    $.ajax({
        url: "/list",
        success: function (data){
            var myselect=document.getElementById("selector");
            var list_value = data.select2;
//            console.log(list_value)
//            // var index = myselect.selectedIndex;// selectedIndex是所选中的项的index
//            var index = myselect.selectedIndex
//            myselect.options[index].value;
//            console.log(myselect.options[index].value)

//            window.obj = data;
//            console.log(window.obj)
        }
    })
}
// 刷新下拉列表
// function getlist_value(){
//     $.ajax({
//         url: "/",
//         success: function(data){
//             $(".select_value").eq(0).text(data.confirm);
// //			$(".num h1").eq(1).text(data.suspect);
// //			$(".num h1").eq(2).text(data.heal);
// //			$(".num h1").eq(3).text(data.dead);
//         },
//     })
// }


//刷新表格
function getTableName() {
    var TableName = $("#id1").val();//从界面某个标签的id获取你要的值
    var DBType = $("#Id2").val();
    if (TableName == "" || TableName == null) {
        alert("没有数据");
    } else {
        $.ajax({
//            type: "POST",//用POST传递数据，GET也可以
            url: "/getTableName",//我用的是MVC，这样可以直接触发对应的Controle
//            data: {
//                "TableName": TableName,//把要传递的数据组成Jason类型，向后台传递，直接在形参中接收即可
//                "DBType": DBType
//            },
//            dataType: "json",//定义的是返回数据的格式，直接写json就对了，写text的话还要用JSON.pare()再转换一次
            success: function (data) {
                if (data == null || data == '') {
                    alert("请联系\n管理员维护数据");
                    
                } else {

                    var str = "";//把数据组装起来
                    for (var i = 0; i < data.dataInfo.length; i++) {
                        str += "<tr><td>" + data.dataInfo[i].tableName +
                            "</td><td>" + data.dataInfo[i].colName +
                            "</td><td>" + data.dataInfo[i].dbType +
                            "</td><td>" + data.dataInfo[i].colId +
                            "</td><td>" + data.dataInfo[i].defaultValue +
                            "</td><td>" + data.dataInfo[i].colType +
                            "</td><td>" + data.dataInfo[i].colLength +
                            "</td><td>" + data.dataInfo[i].ver +
                            "</td><td>" + data.dataInfo[i].isEnable + "</td></tr>";
                    }
                    $("#tableText").html(str);//把拼好的样式填到指定的位置，一个Ajax的表格刷新功能就完成了
                }
            }
        });
    }
};

// gettime()
get_c1_data()
// get_c2_data()
get_l1_data()
get_l2_data()
get_r1_data()
get_r2_data()
get_list_data()
//getTableName()
//
// setInterval(gettime,1000)
setInterval(get_c1_data,1000)
setInterval(get_list_data,1000)
//setInterval(get_c2_data,10000*10)
setInterval(get_l1_data,1000)
setInterval(get_l2_data,1000)
setInterval(get_r1_data,1000)
setInterval(get_r2_data,1000)
