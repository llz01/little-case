package com.test.bean;

import java.util.ArrayList;
import com.mysql.jdbc.*;


public class userData {
    private String name;
    private String password;
    private String sex;
    private String age;
    private ArrayList<String> hobbies;

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setPassword(String psw) {
        this.password = psw;
    }

    public String getPassword() {
        return password;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public String getAge() {
        return age;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getSex() {
        return sex;
    }

    public void setHobbies(String hobby) {
        this.hobbies.add(hobby);
    }

    public ArrayList<String> getHobbies() {
        return hobbies;
    }
}
