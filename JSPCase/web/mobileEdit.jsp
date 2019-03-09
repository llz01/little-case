<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/4/8
  Time: 11:52
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html; charset=UTF-8" %>
<%@ page language="java" %>
<%@ page import="com.mysql.jdbc.Driver" %>
<%@ page import="java.sql.*" %>
<%
    request.setCharacterEncoding("UTF-8");
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

        Statement stmt=conn.createStatement();
        ResultSet rs=stmt.executeQuery("SELECT * from product WHERE id="+id);
%>

    <%
        rs.next();
    %>
<div style="text-align: center;">
    <form action="mobileEdit_post.jsp" method="post">
        <input hidden type="text" value="<%=rs.getString(1)%>" name="id"><br>
        品牌：<input type="text" value="<%=rs.getString(2)%>" name="brand"><br>
        型号：<input type="text" value="<%=rs.getString(3)%>" name="model"><br>
        日期：<input type="text" value="<%=rs.getString(4)%>" name="date"><br>
        价格：<input type="text" value="<%=rs.getString(5)%>" name="price"><br>
        简介：<input type="text" value="<%=rs.getString(6)%>" name="introduce"><br>
        <input type="submit" value="提交">
    </form>
</div>

    <%
        rs.close();
        conn.close();
        stmt.close();
    }
    catch (NullPointerException e){
        out.println(e);
    }
    %>
</body>
</html>
