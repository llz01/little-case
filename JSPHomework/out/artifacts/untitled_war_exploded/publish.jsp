<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/3/28
  Time: 19:55
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div style="text-align: center">
    <%
        String title=new String(request.getParameter("title").getBytes("ISO-8859-1"),"UTF-8");
        String msg=new String(request.getParameter("msg").getBytes("ISO-8859-1"),"UTF-8");
        if (title.length()<=2||title.length()>50) {
            //out.println("Title is unqualified!");
            response.sendRedirect("error.jsp?error=title");
        }
        else {
            out.println("标题："+title+"<br>");
        }
        if (msg.length()<=5||msg.length()>500) {
            //out.println("The message is unqualified!");
            response.sendRedirect("error.jsp?error=message");
        }
        else {
            out.println("内容："+msg);
        }
    %>
</div>
</body>
</html>
