<%--
  Created by IntelliJ IDEA.
  User: vincent
  Date: 2021/2/4
  Time: 8:47 下午
  To change this template use File | Settings | File Templates.
--%>

<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
   <title>$Title$</title>
    <%--<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>--%>
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script>
  function a1(){
    $.post({
      url:"/ajax1",
      data:{'name':$("#txtName").val()},
      success:function (data,status) {
        alert(data);
        alert(status);
      }
    });
  }
</script>
  </head>
<body>

<%--onblur：失去焦点触发事件--%>
用户名:<input type="text" id="txtName" onblur="a1()"/>

</body>
</html>
