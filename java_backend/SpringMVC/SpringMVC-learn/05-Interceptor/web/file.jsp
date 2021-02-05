<%--
  Created by IntelliJ IDEA.
  User: vincent
  Date: 2021/2/4
  Time: 10:43 下午
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>

<hr>

<body>
<form action="/upload" enctype="multipart/form-data" method="post">
    <input type="file" name="file"/>
    <input type="submit" value="upload">
</form>

</body>
</html>
