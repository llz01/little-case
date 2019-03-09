<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/4/6
  Time: 20:01
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
        try{
            String num=new String(request.getParameter("number").getBytes("ISO-8859-1"),"UTF-8");
            float number = new Float(num).parseFloat(num);
            out.println(number+"的平方是："+number*number+"<br>");
            out.println(number+"的立方是："+number*number*number);
        }
        catch (Exception e){
            out.println("Something Wrong!");
        }
    %>
</div>
</body>
</html>
