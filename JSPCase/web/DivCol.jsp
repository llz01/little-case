<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/4/6
  Time: 19:40
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" pageEncoding="UTF-8" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<div style="text-align: center;">
    <%
        for(int i=1;i<9;i++){
            for(int n=1;n<9;n++){
                out.println(i+"X"+n+"="+i*n);
            }
            out.println("<br>");
        }
    %>
</div>
</body>
</html>
