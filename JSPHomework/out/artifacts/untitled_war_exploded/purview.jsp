<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/4/10
  Time: 9:03
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

            String user = new String(request.getParameter("user").getBytes("ISO-8859-1"), "UTF-8");
            session.setAttribute("user", user);
            if (user.equals("Koko")) {
                session.setAttribute("permission", "1");
            } else {
                session.setAttribute("permission", "0");
            }
        }
        catch (Exception e){
            session.setAttribute("permission", "2");
        }
            String psm = (String) session.getAttribute("permission");
    %>
</body>
</html>
