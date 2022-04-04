# [rocketchat-connector](#)
# what is the rocketchat-connector
Library to connect Python to rocket chat 

This library was built in conjunction with the Selenium Library


### Installation

We need to have rocketchat-connector installed on our machine to start using which can either be done directly from **GitHub**

#### installing directly

You first need to clone or download the repo to your local directory and then move into the project directory as shown in the example and then run the below command; 

```bash
git clone https://github.com/sepehrmizani/rocketchat-connector
cd rocketchat-connector
```

### Setting up Selenium

Underneath rocketchat-connector is **Selenium** which is one does all the automation work by directly controlling the browser, so you need to have a selenium driver on your machine for **rocketchat-connector** to work. But luckily rocketchat-connector uses [webdrive-manager](https://pypi.org/project/webdriver-manager/), which does this automatically. You just need to install a browser. By default rocketchat-connector uses [Google Chrome](https://www.google.com/chrome/).

## What you can do with rocketchat-connector?
- [Login ](#Login)
- [find user](#find-user)
- [Send Messages](#sending-messages)
- [change status](#change-status)
- [Logout ](#Logout )


To log in, you must log in to the chat rocket the first time it enters Google, so that from now on the chat rocket can be opened without the need to log in.
 

In the next version, you can login to the code in RocketChat and you do not need to log in to RocketChat manually.

###

Here an Example on how to find user

You can also find groups this way

```python
>>> from rocketchat-connector import rocket_connector
>>> messenger = rocket_connector()
>>> messenger.find_by_username('name or group name')
```


Here an Example on how to send messages

```python
>>> from rocketchat-connector import rocket_connector
>>> messenger = rocket_connector()
>>> messenger.find_user('2557xxxxxz')
>>> messages = ['Morning my love', 'I wish you a good night!']
>>> for message in messages:  
        messenger.send_message(message) 
 ```
        
```python
>>> from rocketchat-connector import rocket_connector
>>> messenger = rocket_connector()
>>> messenger.find_user('2557xxxxxz')
>>> messenger.send_message("message") 
```

Here an Example on how to change-status
```python
>>> from rocketchat-connector import rocket_connector
>>> messenger = rocket_connector()
>>> messenger.change_status("status")
```

Here an Example on how to logout
```python
>>> from rocketchat-connector import rocket_connector
>>> messenger = rocket_connector()
>>> messenger.logout()
```
