Title: Shell tips
Date: 2014-05-02 22:41
Author: ihommmani
Status: draft
Summary: How you can increase shell script quality with few tips 


Shell language is at disadvantage compared to other languages such as Java, C/C++ and others. 
Unlike those, we usually do not learn it on classes (unless we aim becoming a system administrator).
Most of us learned learn it on his/her own. It is true for me but also for most of the people I met. 
As software developpers we focused on object programming and functionnal programming but hardly on pure scripting languages.  
And shell is one of them.   
Why ? Because we wrongly think it as a burden, something useless used by a bunch of hackers.
Rather learning it we prefer to google the task we want and copy/paste the all thing. 
The result could be a poor written script if lucky, or a weapon of mass destruction in the hands of beginners (no parameters checking, security leaks...and the feared rm -rf *).   
I recently focused on the langage because as a GNU/Linux user I needed to make some repetitive tasks. 
I don't know if it's the fact of becoming older but the truth is I hate repeating myself when I can obviously automate the task.  
And we all use script in this way for that matter. 
What is your bashrc, if not a script allowing you to initialize many things you would have to repeat without it (environement variables, aliases, ) ?

I will use this article as a reminder, and to share some tips we can use to greatly improve shell script readability, maintanability and security.

## Expansion operators

## Arguments

## Know the until loop
In general we use while loop to wait for an event to happen. 
But semanticaly, until is more fited to do so.

## Here scripts
When I needed to write a script, I usualy start an editor and begin to write the script done.
No matter the size of the script. In reality we can gain time by not starting any editor and taking advantage of the here script.
Suppose, your script is 8 or ten lines long like this one. 
Here script is also your friend to output some text. 
You surely know the well known echo command.
And you surely have seen the following lines:
echo "##########################"
echo "###### HELLO WORLD #######"
echo "##########################"

It 's a lot of echo there.
Now consider this piece of code:

cat << EOF
##################
####HELLO WORLD###
##################
EOF

I don't know for you but I prefer the second version. Much more...DRY


## Special variable
Any shell script can access the following variables:
$@
$? ...

## Special files
/dev/null
/dev/tty

## Use test
Did you know that [...] is an alias for *test* ?
The command test allow you to, as it sounds, test a condition.
Instead of writting: 
if [ toto = titi ]
    then 
        echo titi
fi

Do instead: test toto = titi

## Why to suround variables with brackets when working with conditions ?
Because bad things happen if the variable is not initialized.

'
'
Surounding the variable allow to protect us from this and at least contains a null string.
So, even tough this is clearly not an obligation, it 

## Manipulate the files descriptor
I mean do it. It's a nice feature. 
You want to hush your script up ? Easy.
Just redirect the Stdout and Stderr to the /dev/null

## You don't understand the & sign in stream redirection ?
The well known make > results > 2>&1
We always forget where the sign goes and uber all what does it stands for.
Luckily the problems are solvable at the same time.
When you see redirect the STDERR wherever file descriptor 1 is.
So to blackout you script, do the following at the beginning:

## Should I use echo for debugging ? Answer: No!
The shell allow you to trace the call it has been through.
Using echo to debug is simply a waste of time when you have sh -x.
To much information ? Do it like a surgeon.
Surround the piece of code you want to debug with set -x...set +x (Yeah I know, the convention sucks: - to enable and + to disable) 

## Use getopts...for small utilities.
In my opinion, if your script exceeds 20~30 line you should add the option handling, (at least for the --help)
Getopts 


## understand the shif command for option handling
You don't have to manipulate option through $3, $4 or higher. 
Stick with the brave $1 and $2. Above, it's a mess. For the other guy who will read you. 
(Don't forget that the other guy, it's you in two month)

## Master the power of pipelining


Shell language is at disadvantage compared to other languages.
It is viewed as a scripting langage (and it's true) only useful for system administration task.
At school I haven't seen anybody learning shell. Even as a scripting language shell is seen less.
The consequence can be seen in the quality of shell script.
Before learning it on my own, I usually googled the question "How to..." and then copy/paste/adapt.
The overal script is more like a bunch of nonsens hard to read and understand. 
More important, we usually don't see any security concern nor stability concern.
I coded in shell this way for quite a time, until I read an article and a book showing me how powerfull the language is, 
and haw readable script can be.

I can't sum up all I've learned in just one article. Instead, I will, as the previous article did, give some tips to 
, if not master, at least produce better scripts.
You will 

## Variables manipulation

## Arguments

## Now the until loop
In general we use while loop to wait for an event to happen. 
But semanticaly, until is more fited to do so.

## Here scripts
When I needed to write a script, I usualy start an editor and begin to write the script done.
No matter the size of the script. In reality we can gain time by not starting any editor and taking advantage of the here script.
Suppose, your script is 8 or ten lines long like this one. 
Here script is also your friend to output some text. 
You surely know the well known echo command.
And you surely have seen the following lines:
echo "##########################"
echo "###### HELLO WORLD #######"
echo "##########################"

It 's a lot of echo there.
Now consider this piece of code:

cat << EOF
##################
####HELLO WORLD###
##################
EOF

I don't know for you but I prefer the second version. Much more...DRY


## Special variable
Any shell script can access the following variables:
$@
$? ...

## Special files
/dev/null
/dev/tty

## Use test
Did you know that [...] is an alias for *test* ?
The command test allow you to, as it sounds, test a condition.
Instead of writting: 
if [ toto = titi ]
    then 
        echo titi
fi

Do instead: test toto = titi

## Why to suround variables with brackets when working with conditions ?
Because bad things happen if the variable is not initialized.

'
'
Surounding the variable allow to protect us from this and at least contains a null string.
So, even tough this is clearly not an obligation, it 

## Manipulate the files descriptor
I mean do it. It's a nice feature. 
You want to hush your script up ? Easy.
Just redirect the Stdout and Stderr to the /dev/null

## You don't understand the & sign in stream redirection ?
The well known make > results > 2>&1
We always forget where the sign goes and uber all what does it stands for.
Luckily the problems are solvable at the same time.
When you see redirect the STDERR wherever file descriptor 1 is.
So to blackout you script, do the following at the beginning:

## Should I use echo for debugging ? Answer: No!
The shell allow you to trace the call it has been through.
Using echo to debug is simply a waste of time when you have sh -x.
To much information ? Do it like a surgeon.
Surround the piece of code you want to debug with set -x...set +x (Yeah I know, the convention sucks: - to enable and + to disable) 

## Use getopts...for small utilities.
In my opinion, if your script exceeds 20~30 line you should add the option handling, (at least for the --help)
Getopts 


## understand the shif command for option handling
You don't have to manipulate option through $3, $4 or higher. 
Stick with the brave $1 and $2. Above, it's a mess. For the other guy who will read you. 
(Don't forget that the other guy, it's you in two month)

## Master the power of pipelining


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

## Change the shell behavior at the runtime whit the eval statement 

## Subshell|codeblock

