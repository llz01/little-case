package com.phoenix.test;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@javax.servlet.annotation.WebServlet(name = "FirstServlet")
public class FirstServlet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest request, javax.servlet.http.HttpServletResponse response) throws ServletException, IOException {
        String userName = request.getParameter("userName");
        userName = "Hello" + userName;
        request.setAttribute("userName", userName);
        request.getRequestDispatcher("/Success.jsp").forward(request, response);
    }

    @Override
    protected void doGet(javax.servlet.http.HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doPost(request, response);
    }
}
