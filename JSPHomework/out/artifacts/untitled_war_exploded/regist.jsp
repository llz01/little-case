<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/3/28
  Time: 19:59
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
<%
    try{
        String usr=new String(request.getParameter("username").getBytes("ISO-8859-1"),"UTF-8");
        String psw1=new String(request.getParameter("password1").getBytes("ISO-8859-1"),"UTF-8");
        String psw2=new String(request.getParameter("password2").getBytes("ISO-8859-1"),"UTF-8");
        if (usr.length()>20||usr.length()<=2){
            response.sendRedirect("error.jsp?error=username");
        }
        if (psw1.length()>20||psw1.length()<=5||!psw1.equals(psw2)){
            response.sendRedirect("error.jsp?error=password");
        }
        %>
<script>
    alert("注册成功！")
</script>
    <%
    }
    catch (Exception e){
%>

<div style="margin-top: 10%;margin-left: 40%">
    <form onsubmit="test(this)" method="post">
        <table border="1">
            <tr>
                <th>项目</th>
                <th>内容</th>
            </tr>
            <tr>
                <td>用户名</td>
                <td><input name="username"></td>
            </tr>
            <tr>
                <td>密码</td>
                <td><input type="password" name="password1" id="psw1"></td>
            </tr>
            <tr>
                <td>确认密码</td>
                <td><input type="password" name="password2" id="psw2"></td>
            </tr>
            <tr>
                <td>手机号</td>
                <td><input type="text" name="phoneNumber"></td>
            </tr>
            <tr>
                <td>邮箱地址</td>
                <td><input type="email" name="email"></td>
            </tr>
            <tr>
                <td>个人简介</td>
                <td><input type="text" name="introduction" height="44px"></td>
            </tr>
            <tr>
                <td><button>提交注册</button></td>
            </tr>
        </table>
    </form>
</div>
<%
    }
%>
<script>

    function validate_username(field, msg) {
        with(field)
        {
            if(value==null||value.length>20 || value.length<=2) {
                alert(msg);
                return false;
            }else {
                return true;
            }
        }
    }

    function validate_psw1(field, msg) {
        with(field)
        {
            if(value==null||value.length>20 || value.length<=5) {
                alert(msg);
                return false;
            }else {
                return true;
            }
        }
    }

    function validate_psw2(field, msg) {
        with(field)
        {
            var psw1 = document.getElementById('psw1').value;
            var psw2 = document.getElementById('psw2').value;
            if(value==null||value.length>20 || value.length<=5) {
                alert(msg);
                return false;
            }
            else if(psw1 != psw2){
                alert('密码不一致，请重新输入！');
                return false;
            } else {
                return true;
            }
        }
    }

    function test(form) {
        with(form)
        {
            if (validate_username(username,"请检查用户名")==false)
            {username.focus();return false}
            if (validate_psw1(password1,"请检查密码")==false)
            {password1.focus();return false}
            if (validate_psw2(password2,"确认密码有误")==false)
            {password2.focus();return false}
        }
    }

</script>
</body>
</html>