<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/4/7
  Time: 16:32
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html; charset=UTF-8" %>
<%@ page language="java" %>
<%@ page import="com.mysql.jdbc.Driver" %>
<%@ page import="java.sql.*" %>
<%  //request.setCharacterEncoding("UTF-8");
    try{
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
        String sql="INSERT INTO product(brand,model,date,price,introduce) VALUES('"+brand+"','"+model+"','"+date+"','"+price+"','"+introduce+"')";
        PreparedStatement ps = conn.prepareStatement(sql);
        /*ps.setString(1, brand);
        ps.setString(2, model);
        ps.setString(3, date);
        ps.setString(4, price);
        ps.setString(5, introduce);*/
        int row = ps.executeUpdate(sql);

        out.print("Inserted "+row+"data");
        ps.close();
        conn.close();
    }
    catch (Exception e){
        out.println(e);
%>
        <div style="text-align: center;">
    <form action="mobileAdd.jsp" method="post">
        <input type="text" placeholder="品牌" name="brand">
        <input placeholder="型号" type="text" name="model">
        <input type="text" placeholder="上市日期" name="date">
        <input type="text" placeholder="价格" name="price">
        <input type="text" placeholder="简介" name="introduce">
        <input type="submit" value="提交">
    </form>
</div>
<%}%>
</body>
</html>
