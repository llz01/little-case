$.get("/api/chinese", do_something);
function do_something(data, status) {
    //console.log(data);
    //console.log(data["_que_1"]);
    $("ol").append("<p>"+data["_que_1"]+"</p>");
    $("ol").append("<p>"+data["_que_2"]+"</p>");
    $("ol").append("<p>"+data["_que_3"]+"</p>");
    $("ol").append("<p>"+data["_que_4"]+"</p>");
    $("ol").append("<p>"+data["_que_5"]+"</p>");
    $("p").eq(0).after("<div class='btn-group'>"+
        "<a href='javascript:void(0)' type='button' onclick=\"change(this)\" class=\"btn btn-default btn-sm\">A．吮吸(shǔn)    涎皮（yán）    敕造（chì）   百无聊赖(lài)</a>" +
        "<a href='javascript:void(0)' type='button' onclick=\"change(this)\" class=\"btn btn-default btn-sm\">B．讪讪(shàn)    庠序（xiáng）   俨然(yǎn)     少不更事(jīng)</a>"+
        "<a href='javascript:void(0)' type='button' onclick=\"score(this)\" class=\"btn btn-default btn-sm\">C．折本（shé）   干瘪（biě)     谬种(miù)     沸反盈天(fèi)</a>"+
        "<a href='javascript:void(0)' type='button' onclick=\"change(this)\" class=\"btn btn-default btn-sm\">D．蹙缩（cù）    驯熟(xùn)      两靥（yàn）     鸡豚狗彘（zhì）</a>"+
        "</div>")
    $("p").eq(1).after("<div class='btn-group'>"+
        "<a href='javascript:void(0)' type='button' onclick=\"change(this)\" class=\"btn btn-default btn-sm\">A．寒暄   执着  踌躇   众说纷纭 </a>" +
        "<a href='javascript:void(0)' type='button' onclick=\"score(this)\" class=\"btn btn-default btn-sm\">B． 慰藉   隽永   朦胧   眼花瞭乱 </a>"+
        "<a href='javascript:void(0)' type='button' onclick=\"change(this)\" class=\"btn btn-default btn-sm\">C．鞭笞   赋予  萦绕   出神入化</a>"+
        "<a href='javascript:void(0)' type='button' onclick=\"change(this)\" class=\"btn btn-default btn-sm\">D． 窟窿   穹隆   缥缈   叹为观止</a>"+
        "</div>")
    $("p").eq(2).after("<div class='btn-group'>"+
        "<a href='javascript:void(0)' type='button' onclick=\"score(this)\" class=\"btn btn-default btn-sm\">是</a>" +
        "<a href='javascript:void(0)' type='button' onclick=\"change(this)\" class=\"btn btn-default btn-sm\">否</a>"+
        "</div>")
    $("p").eq(3).after("<div class='btn-group'>"+
        "<a href='javascript:void(0)' type='button' onclick=\"change(this)\" class=\"btn btn-default btn-sm\">是</a>" +
        "<a href='javascript:void(0)' type='button' onclick=\"score(this)\" class=\"btn btn-default btn-sm\">否</a>"+
        "</div>")
    $("p").eq(4).after("<form name='form1'>" +
        "<input type=\"text\" name=\"five\" id='form1'>" +
        "<a  id='shi' onclick=\"over(this)\" class=\"btn btn-default btn-sm\">确定</a>"+
        "</form>")
}

var count = 0;
function score(id) {
    id.className = 'btn btn-info btn-sm';
    count += 20;
    console.log(count);
}

function change(id) {
    id.className = 'btn btn-info btn-sm';
    console.log(count);
}

function over(id) {
    id.className = 'btn btn-info btn-sm';
    ccc();
}

function ccc() {
    var form = document.getElementById('form1');
    var content = form.value;
    console.log(content);
    if(content == "无梦到徽州") {
        count += 20;
    }
    alert("您本次得分为:"+count.toString());
    count = 0;
}



