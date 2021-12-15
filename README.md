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
- [find user](#find-user)
- [Send Messages](#sending-messages)

Here an Example on how to find user
```python
>>> from alright import WhatsApp
>>> messenger = WhatsApp()
>>> messenger.find_by_username('saved-name or number or group')
```
