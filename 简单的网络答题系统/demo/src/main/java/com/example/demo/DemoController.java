package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class DemoController {

    @RequestMapping(value="/chinese", produces="text/plain;charset=UTF-8")
    public String chinese(ModelMap map) {
        map.addAttribute("subject", "语文");
        map.addAttribute("subject_js", "chinese_script.js");
        return "ch_examination";
    }

    @RequestMapping(value="/english", produces="text/plain;charset=UTF-8")
    public String english(ModelMap map) {
        map.addAttribute("subject", "English");
        return "en_examination";
    }
}
