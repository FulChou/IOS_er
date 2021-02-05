package com.fulchou.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@Controller
public class AjaxController {
 
  @RequestMapping("/ajax1")
  public void ajax1(String name , HttpServletResponse response) throws IOException {
    if ("admin".equals(name)){
      response.getWriter().print("true");
     }else{
      response.getWriter().print("false");
     }
   }

}
