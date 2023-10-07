# password-manager-cli
## Introduction

In the current scenario, we need different accounts to access even the most basic of internet services and these accounts pile up very quickly. Usually we are able to remember a few passwords of your key accounts like Facebook, Google, Apple, etc. but what about all the other services we signed up for?  
  
What people usually do is either produce a strong password and reuse it on all the sites or services they sign up for, which is not at all ideal as it makes hacking your account a lot easier as a security breach in one of your accounts will compromise all the other accounts. Another most common password strategy is people using different but very easy passwords for different accounts, this can help avoid security breach of all the accounts at once but it also opens the horizon for someone easily guessing your password.

Sometimes people store their passwords in the form of a document or in some notes app which is also not advisable as if someone gets access to your physical device or there is a ransomware attack on your device then the attacker basically has your entire life in their possession.

None of the above mentioned approaches is ideal nor the combination of the two.

Now then ever we have a pressing need of having strong and distinct passwords for our various accounts, and to put it simply that's very difficult.

Nowadays we see many companies building password management systems but only a handful of them are good and most of them are paid or have paywalls to access even the basic features, which is highly frustrating for the end user. Mostly these password managers are cloud based, that is all the data you have shared is uploaded to the company’s servers so if god forbid there is an attack on their company’s servers then all your passwords may get compromised. This was the account of the companies which are considered to be industry standard.

To resolve these problems we came up with the idea of making a password management system which auto generates strong passwords for you and stores it behind your master password. The passwords are encrypted and stored locally on your device, so no one can see your valuable passwords, even if there is a data breach from your end.

## Aim
To make our users’ life easier by maintain a database of encrypted passwords of all the websites a user wants to store

## Idea Source
1. The difficulty in remembering a lot of different passwords
2. Not having a secure place to store passwords
3. Help people be more vigilant from phishing attacks
4. Having a password manager on you local device as nowadays everything is moving to the cloud and some people may not be comfortable with the privacy risks it may have

## Plan for implementation

- Having your passwords stored safely is such a way that you can easily access them.
- Convenient way of storing and accessing passwords
- You only need to remember one password (that is the master password)
- It can also auto generate strong passwords for you.
- Users can add specific short names and nicknames for services for convenient access
- Users and also skip adding URLs or name of utilities and only use short name so that others cannot know which sites password is stored
- Encrypting the passwords stored so if someone gets access to your device they can’t see  your password without knowing your master password
- Having contingency methods to recover passwords
- Easy sign up process so everyone can easily make their account and can have the convenience of using a password manager
- Searching passwords made easy; there will an option of copying the passwords you are searching
- Users can also change passwords and ids stored
- Users can also delete the all the data (that is the passwords and the ids) with just a click of a button
- We have implemented 2 confirmation wizards so that someone doesn’t accidentally delete their data along with the need to re login before deleting or modifying anything

## Sample data & Data Tables

#### Tabular representation of a Sample Data (decrypted)

|USERNAME|NAME|MASTER PASSWORD|FORGOT Q1 ANS|FORGOT Q2 ANS|FORGOT Q3 ANS|PASSWORD FILE|
|---|---|---|---|---|---|---|
|k_tashif|Tashif|Catmeo024@##.|ant|delhi|sleeping|k_tashif.csv|
|alpha10|Riya|nOt_wh0.uTHIK|meowth|bombay|dancing|alpha10.csv|
|moty_n|Rick|Wubb@_Lubba_dub-dub|eating|cat|new york|moty_n.csv|

#### Tabular representation of a Sample Data (encrypted)

|USERNAME|NAME|MASTER PASSWORD|FORGOT Q1 ANS|FORGOT Q2 ANS|FORGOT Q3 ANS|PASSWORD FILE|
|---|---|---|---|---|---|---|
|k_tashif|Tashif|yWpiak680@)).|Wjp|Zahde|ohaalejc|k_tashif.csv|
|alpha10|Riya|jKp_sd6.qPDEG|iakspd|XkiXWu|ZWjYejc|alpha10.csv|
|moty_n|Rick|SqXX@_HqXXW_ZqX-ZqX|aWpejc|YWp|jas ukng|moty_n.csv|

#### Tabular representation {k_tashif.csv}

|SHORTNAME|URL/UTILITY|USER ID|LOCAL PASSWORD|
|---|---|---|---|
|fb|www.facebook.com|randomuser123|yWpsf56ak680@)).|
|insta|www.instagram.com|nouser58|jKp_sd6...ZWjYejc|
||www.replit.com|notauser85|SqXX@_aWpejc_ZqX-Wjp|

  

## Menu Options

![](file:////Users/taf/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image002.jpg)

## Validations and Add on Features

- Auto password generator
- When you search for a password it automatically gets copied to ur clipboard
- All the passwords are encrypted  so even if someone gets hold of the file he can not read it
- You don't lose your data if you forget your master password. (forget password button available)
- Tells you if the password you have entered is weak and suggests a stronger password


