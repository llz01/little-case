<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/4/11
  Time: 9:40
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
        String brand=new String(request.getParameter("brand").getBytes("ISO-8859-1"),"UTF-8");
        String model=new String(request.getParameter("model").getBytes("ISO-8859-1"),"UTF-8");
        String date=new String(request.getParameter("date").getBytes("ISO-8859-1"),"UTF-8");
        String price=new String(request.getParameter("price").getBytes("ISO-8859-1"),"UTF-8");
        String introduce=new String(request.getParameter("introduce").getBytes("ISO-8859-1"),"UTF-8");

        String driverName="com.mysql.jdbc.Driver";
        String userName="root";
        String userPasswd="123456";
        String dbName="jsp";
        String tableName="product";

        String url="jdbc:mysql://localhost/"+dbName+"?useSSL=false&user="+userName+"&password="+userPasswd;
        Class.forName("com.mysql.jdbc.Driver").newInstance();
        Connection conn=DriverManager.getConnection(url);
        String sql="UPDATE product SET brand=?,model=?,date=?,price=?,introduce=? WHERE id="+id;
        PreparedStatement ps = conn.prepareStatement(sql);
        ps.setString(1, brand);
        ps.setString(2, model);
        ps.setString(3, date);
        ps.setString(4, price);
        ps.setString(5, introduce);
        int row = ps.executeUpdate();

        out.println("Inserted "+row+"data");
        ps.close();
        conn.close();
        response.sendRedirect("mobileInfo.jsp");
    } catch (Exception error){
        out.println(error);
    }
%>
</body>
</html>
