<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/3/28
  Time: 19:58
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
    try {
        String usr=new String(request.getParameter("username").getBytes("ISO-8859-1"),"UTF-8");
        String psw=new String(request.getParameter("psw").getBytes("ISO-8859-1"),"UTF-8");
        if (usr.length()>20||usr.length()<=2){
            response.sendRedirect("error.jsp?error=username");
        }
        if (psw.length()>20||psw.length()<=5){
            response.sendRedirect("error.jsp?error=password");
        }
        if (usr.equals("Koko")&&psw.equals("23333333")){
            response.sendRedirect("list.jsp?user=Koko");
        }
        if (usr.equals("root")&&psw.equals("123456")){
            response.sendRedirect("list.jsp?user=Koko");
        }
            else{
                %>
    <script>
        alert("账号或密码错误，登录失败!");
    </script>
    <%
            out.println(usr+"|"+psw);
        }
    }catch (Exception e){
%>
<div style="text-align: center">
    <form onsubmit="test(this)">
                用户登录<br>
                用户名:<input type="text" name="username"><br>
                密码：<input type="password" name="psw"><br>
        <input type="submit" value="登录">
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

    function validate_psw(field, msg) {
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

    function test(form) {
        with(form)
        {
            if (validate_username(username,"请检查用户名")==false)
            {username.focus();return false}
            if (validate_psw(psw,"请检查密码")==false)
            {psw.focus();return false}
        }
    }

</script>

</body>
</html>
