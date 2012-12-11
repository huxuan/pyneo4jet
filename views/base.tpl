<html>
<link rel="stylesheet" href="/views/style.css" />
<head>
    <title>{{get('title', '') and '%s | ' % title }}pyneo4jet</title>
</head>
<body>
    %include nav username=get('username')
    %include tweet_form username=get('username')
    %include
</body>
</html>
