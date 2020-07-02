#!python
print("Content-Type: text/html")
print()
import cgi, os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width" initial-scale="1">
  <link rel="stylesheet" href="login.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js">

  </script>
  <script>
$(document).ready(function(){
  $(".signup-farm").hide();
  $(".signup").css("background","none");
  $(".signup").click(function(){
    $(".login-farm").hide();
    $(".signup-farm").show();
    $(".login").css("background","none");
    $(".signup").css("background","#fff");
  })
  $(".login").click(function(){
    $(".login-farm").show();
    $(".signup-farm").hide();
    $(".login").css("background","#fff");
    $(".signup").css("background","none");
  })
  $(".btn").click(function(){
    $(".input").val("");
  })
});
</script>
</head>
<body>
  <div class="container">
    <div class="login">로그인</div>
    <div class="signup">회원가입</div>

    <div class="login-farm">
      <input type="text" placeholder="이메일 주소" class="input"><br>
      <input type="password" placeholder="비밀번호" class="input"><br>
      <div class="btn">확인</div>
      <span><a href="#">아이디 혹은 비밀번호를 잃어버리셨나요?</a></span>
    </div>
    <form action="customers.py" method="post">
        <div class="signup-farm">
          <input type="text" name="title" placeholder="성함" class="input"><br>
          <input type="text" name="description" placeholder="이메일 주소" class="input"><br>
          <input type="password" name="userpassword" placeholder="비밀번호" class="input"><br>
          <input type="text" name="usernumber" placeholder="사업자 번호" class="input"><br>
          <input type="submit" class="btn">
        </div>
    </form>
  </div>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr))
