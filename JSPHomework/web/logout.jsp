<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/4/10
  Time: 8:46
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
    <%
        session.removeAttribute("user");
        out.println("已注销!");
        response.sendRedirect("list.jsp");
    %>
</body>
</html>
