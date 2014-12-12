<%@ page language="java" contentType="text/html; charset=US-ASCII"
    pageEncoding="US-ASCII"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>   
<%@ taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql" %> 
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%-- set data source --%>
<sql:setDataSource
    driver="com.mysql.jdbc.Driver"
    url="jdbc:mysql://csproject.calstatela.edu/gamedev"
    user="gamedev"
    password="3tb=PChh"/>
<%-- query --%>
<c:if test="${empty param.register}">
<sql:query var="record">
select count(*) from users_website where username = '${param.uname}' and password = '${param.pwd}' 
</sql:query>
<c:if test="${ empty param.uname or empty param.pwd}">
      <c:redirect url="${header.referer }" >
              <c:param name="errMsg" value="Please Enter UserName and Password" />
              <c:param name="Msg" value=""/>
      </c:redirect>
       
    </c:if>
<c:if test="${not empty param.uname and not empty param.pwd}">

<c:forEach items = "${record.rowsByIndex }" var="row">
<c:choose>
<c:when test="${row[0] gt 0}">
			<c:set scope="session"
                   var="loginUser"
                   value="${param.uname}"/>
            <c:redirect url="${header.referer }">
            		<c:param name="errMsg" value="" />
            		<c:param name="Msg" value="" />
            </c:redirect>
</c:when>
<c:otherwise>
            <c:redirect url="${header.referer }" >
              <c:param name="errMsg" value="Username/password does not match" />
              <c:param name="Msg" value=""/>
            </c:redirect>
 </c:otherwise>
 </c:choose>

</c:forEach>
</c:if>
</c:if>
<c:if test="${not empty param.register}">
<c:catch var="catchException">
<sql:update>
insert into users_website (username , password) values (?, ?)
<sql:param value = "${param.uname}"/>
<sql:param value = "${param.pwd}"/>
</sql:update>
</c:catch>
<c:if test="${catchException!=null }">
   <c:redirect url="${header.referer }" >
  		<c:param name="errMsg" value="Username already exists "/>
  		<c:param name="Msg" value=""/>
	</c:redirect>
</c:if>
<c:if test="${catchException==null }">
<c:redirect url="${header.referer }" >
<c:param name="errMsg" value=""/>
<c:param name="Msg" value="Registered Successfully! Please Login. "/>
</c:redirect>
</c:if>
</c:if>



<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>

</body>
</html>