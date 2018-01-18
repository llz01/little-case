package com.example.demo;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequestMapping(value = "/api")
@RestController
public class api_rest_controller {


    @RequestMapping("/chinese")
    public questions chinese_json() {
        questions chinese = new questions();
        chinese.que_1 = "1、选出下列加点字注音全对的一项：";
        chinese.que_2 = "2、下列各组词语中，有错别字的一组是：";
        chinese.que_3 = "3、苏东坡是唐宋八大家之一吗？";
        chinese.que_4 = "4、我国最早的朝代是秦朝吗？";
        chinese.que_5 = "5、诗“一生痴绝处”的下一句是：";
        return chinese;
    }

    @RequestMapping("/english")
    public questions english_json() {
        questions english = new questions();
        english.que_1 = "1、I just heard ____ bank where Dora works was robbed by____ gunman wearing a mask. （2015重庆3）";
        english.que_2 = "2、Jane's grandmother had wanted to write _____ children’s book for many years, but one thing or another always got in ______ way. （2015浙江2）";
        english.que_3 = "3、Brian is gifted in writing music; he is very likely to be ____ Beethoven. （2015四川5）";
        english.que_4 = "4、_____ more learned a man is,_____ more modest be usually become. （2015陕西14）";
        english.que_5 = "5、There is no need to tell me your answer now. Give it some ______ and then let me know. （2015安徽30）";
        return english;
    }

}
