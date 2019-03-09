<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/4/15
  Time: 16:03
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="com.test.bean.userData" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<jsp:useBean id="user" class="com.test.bean.userData">
    <jsp:setProperty name="user" property="*"/>
</jsp:useBean>
<center>
    <b>姓名:</b><jsp:getProperty name="user" property="name"/><br>
    <b>密码:</b><jsp:getProperty name="user" property="password"/><br>
    <b>性别:</b><jsp:getProperty name="user" property="sex"/><br>
    <b>年龄:</b><jsp:getProperty name="user" property="age"/><br>
    <b>兴趣:</b>看书<br>
</center>
</body>
</html>
