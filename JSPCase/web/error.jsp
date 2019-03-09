<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/3/28
  Time: 19:59
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>404 Not Found</title>
</head>
<body>
<div style="text-align: center">
<h3 style="text-align: center">
    There are some errors about the <font color="red"><%= request.getParameter("error")%></font>
</h3>
</div>
</body>
</html>
