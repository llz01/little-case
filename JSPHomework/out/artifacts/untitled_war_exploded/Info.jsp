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
<center>
    <form action="showInfo.jsp" method="post">
        姓名：<input type="text" name="name"><br>
        密码：<input type="password" name="password"><br>
        性别：<input type="radio" name="sex" value="Male">男
              <input type="radio" name="sex" value="Female">女<br>
        <label>年龄：</label>
        <select name="age">
            <option value="11~20 years">11~20 岁</option>
            <option value="20~30 years">20~30 岁</option>
        </select><br>
        <label>兴趣：</label><input type="checkbox" name="hobbies" value="看书">看书
              <input type="checkbox" name="hobbies" value="足球">足球
              <input type="checkbox" name="hobbies" value="音乐">音乐<br>
        <input type="submit" value="提交">
    </form>
</center>
</body>
</html>
