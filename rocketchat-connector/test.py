from __init__ import  rocket_connector
import time
messenger = rocket_connector()
messenger.find_username("neme")

messenger.send_message("text")

messenger.change_status("away")

messenger.logout()

