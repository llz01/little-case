<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2018/4/8
  Time: 11:38
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html; charset=UTF-8" %>
<%@ page import="com.mysql.jdbc.Driver" %>
<%@ page import="java.sql.*" %>
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

        Statement stmt=conn.createStatement();
        ResultSet rs=stmt.executeQuery("SELECT * from product WHERE id="+id);
%>
<div style="text-align: center;">
    <table border="1">
        <tr>
            <th>品牌</th>
            <th>型号</th>
            <th>生产日期</th>
            <th>售价</th>
            <th>简介</th>
            <th colspan="3">操作</th>
        </tr>
        <%
            while(rs.next()){
                out.println("<tr>");
                out.println("<td>"+rs.getString(2)+"</td>");
                out.println("<td>"+rs.getString(3)+"</td>");
                out.println("<td>"+rs.getString(4)+"</td>");
                out.println("<td>"+rs.getString(5)+"</td>");
                out.println("<td>"+rs.getString(6)+"</td>");
                out.println("<td><a href='mobileDetail.jsp?id="+rs.getString(1)+"'>详细</a></td>");
                out.println("<td><a href='mobileEdit.jsp?id="+rs.getString(1)+"'>编辑</a></td>");
                out.println("<td><a href='delete.jsp?id="+rs.getString(1)+"'>删除</a></td>");
                out.println("</tr>");
            }

            // out.print("Inserted "+row+"data");
            rs.close();
            conn.close();
            stmt.close();
        }
        catch (Exception e){
            out.println(e);
        %>
    </table>
</div>
<%}%>
</body>
</html>
