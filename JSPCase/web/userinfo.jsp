<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/4/6
  Time: 20:35
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<div style="text-align: center;">
<%
    String msg = new String(request.getParameter("msg").getBytes("ISO-8859-1"), "UTF-8");
    out.println("username:"+msg+"<br><h1>Welcome</h1>");
%>
</div>
</body>
</html>
