function getTableName() {
    var TableName = $("#id1").val();//从界面某个标签的id获取你要的值
    var DBType = $("#Id2").val();
    if (TableName == "" || TableName == null) {
        alert("没有数据");
    } else {
        $.ajax({
            type: "POST",//用POST传递数据，GET也可以
            url: "/DbColTypeConfig/getDBType",//我用的是MVC，这样可以直接触发对应的Controle
            data: {
                "TableName": TableName,//把要传递的数据组成Jason类型，向后台传递，直接在形参中接收即可
                "DBType": DBType
            },
            dataType: "json",//定义的是返回数据的格式，直接写json就对了，写text的话还要用JSON.pare()再转换一次
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