<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/4/6
  Time: 20:24
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<%
    try {
        String usr = new String(request.getParameter("username").getBytes("ISO-8859-1"), "UTF-8");
        String psw = new String(request.getParameter("psw").getBytes("ISO-8859-1"), "UTF-8");
        if (usr.equals("Koko") && psw.equals("23333333")) {
            response.sendRedirect("userinfo.jsp?msg="+usr);
        } else {
            response.sendRedirect("login.html");
        }
    }
    catch (Exception e){
            out.println("Something Wrong!");
        }
%>
</body>
</html>
