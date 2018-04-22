<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/4/8
  Time: 19:41
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="com.mysql.jdbc.Driver" %>
<%@ page import="java.sql.*" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<%
    try{
        String id = new String(request.getParameter("id").getBytes("ISO-8859-1"),"UTF-8");
        String driverName="com.mysql.jdbc.Driver";
        String userName="root";
        String userPasswd="123456";
        String dbName="jsp";
        String tableName="product";

        String url="jdbc:mysql://localhost/"+dbName+"?useSSL=false&user="+userName+"&password="+userPasswd;
        Class.forName("com.mysql.jdbc.Driver").newInstance();
        Connection conn=DriverManager.getConnection(url);
        String sql="DELETE from product WHERE id="+id;
        PreparedStatement ps = conn.prepareStatement(sql);
        int row = ps.executeUpdate();

        ps.close();
        conn.close();
        response.sendRedirect("mobileInfo.jsp");
    } catch (Exception error){
        out.println(error);
    }
%>
</body>
</html>
