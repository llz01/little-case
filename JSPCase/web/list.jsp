<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/3/28
  Time: 19:55
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h4 style="text-align: center">我的留言板</h4>
<div style="margin-top: 10%;margin-left: 40%">
    <%
        if(session.getAttribute("user")!=null){
    %>
    <p><a href="#"><%=session.getAttribute("user")%></a><b>|</b><a href="logout.jsp">注销</a></p>
    <%    }
        else {
    %>
    <p><a href="login.jsp">登录</a><b>|</b><a href="regist.html">注册</a></p>
    <%
        }
    %>
    <%@include file="purview.jsp"%>
    <%
        if (psm.equals("1")){
    %>
    <table border="1">
        <tr>
            <th></th>
            <th>标题</th>
            <th>发布时间</th>
            <th>发布人</th>
        </tr>
        <tr>
            <td>1</td>
            <td><a href="Detail.html">留言2</a></td>
            <td>2017/2/28</td>
            <td>张三</td>
        </tr>
        <tr>
            <td>2</td>
            <td><a href="javascript:void(0)">留言3</a></td>
            <td>2017/2/25</td>
            <td>张三</td>
        </tr>
        <tr>
            <td>3</td>
            <td><a href="javascript:void(0)">留言4</a></td>
            <td>2017/2/24</td>
            <td>李四</td>
        </tr>
        <tr>
            <td>4</td>
            <td><a href="javascript:void(0)">留言5</a></td>
            <td>2017/2/24</td>
            <td>李四</td>
        </tr>
    </table>
<%
    }
    else if (psm.equals("0")){
%>
    <table border="1">
        <tr>
            <th></th>
            <th>标题</th>
            <th>发布时间</th>
            <th>发布人</th>
            <th>管理</th>
        </tr>
        <tr>
            <td>1</td>
            <td><a href="Detail.html">留言2</a></td>
            <td>2017/2/28</td>
            <td>张三</td>
            <td>删除</td>
        </tr>
        <tr>
            <td>2</td>
            <td><a href="javascript:void(0)">留言3</a></td>
            <td>2017/2/25</td>
            <td>张三</td>
            <td>删除</td>
        </tr>
        <tr>
            <td>3</td>
            <td><a href="javascript:void(0)">留言4</a></td>
            <td>2017/2/24</td>
            <td>李四</td>
            <td>删除</td>
        </tr>
        <tr>
            <td>4</td>
            <td><a href="javascript:void(0)">留言5</a></td>
            <td>2017/2/24</td>
            <td>李四</td>
            <td>删除</td>
        </tr>
    </table>
<%
    }
%>
    <form onsubmit="return test(this)" method="post" action="publish.jsp">
        标题：<input type="text" name="title"><br>
        内容：<input type="text" name="msg"><br>
        <input type="submit">
    </form>
</div>
<script>

    function validate_title(field, msg) {
        with(field)
        {
            if(value==null||value.length>50 || value.length<=2) {
                alert(msg);
                return false;
            }else {
                return true;
            }
        }
    }

    function validate_msg(field, msg) {
        with(field)
        {
            if(value==null||value.length>500 || value.length<=5) {
                alert(msg);
                return false;
            }else {
                return true;
            }
        }
    }

    function test(form) {
        with(form)
        {
            if (validate_title(title,"请检查标题")==false)
            {title.focus();return false}
            if (validate_msg(msg,"请检查内容")==false)
            {msg.focus();return false}
        }
    }

</script>
</body>
</html>
