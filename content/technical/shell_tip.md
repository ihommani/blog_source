Title: Shell tips
Date: 2014-05-02 22:41
Author: ihommmani
Status: draft
Summary: Various tips 


Sometimes i need to automate tasks through shell script. 
To make the thing clearer for the person who use it I usually put some echo "What ever"
For small text it's oK 
But when you've got to write more text, instead of calling many times echo, 
we can do that this way:

cat << EOF
Hello there, i'm writting something
sooooooooooooooooooooooooooooooo lonnnnnnnnnnnnnnnnnnnnng
to show some improvement in scripting speed. 

EOF

