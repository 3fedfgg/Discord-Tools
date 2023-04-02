import requests
import time
from colorama import init, Fore, Style
import art

title = art.text2art("Discord Tools")
print(title)

options = ["Discord Counter Thing", "Webhook Spammer", "Delete DM"]

for i, option in enumerate(options):
    print(f"{i+1}. {option}")

print("\nMade by Bmh")

choice = input("\nEnter an option number: ")

if choice == "1":
    print("\nRunning Discord Counter Thing...")
    time.sleep(1)

    mode = input("Do you want to send a message to a server or a DM? (s/d): ")
    auth_token = input("Enter your authorization token: ")

    # Set up the request headers and message data
    auth = {
       'authorization': auth_token
    }
    msg = {
        'content': ''
    }

    if mode == 's':
        # Ask for server ID and channel ID, then send messages to it
        server_id = input("Enter the server ID: ")
        channel_id = input("Enter the channel ID: ")
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

        # sending messages with numbers from 1 to 1000000
        for i in range(1, 1000001):
            msg['content'] = str(i)
            requests.post(url, headers=auth, data=msg)

            if i % 5 == 0:
                print("Rate Limit Bypass :)")
                time.sleep(5) # pause for 5 seconds after every 5 messages

            time.sleep(1) # delay for 1 second between messages

    elif mode == 'd':
        # Ask for recipient ID, create a DM channel, and send messages to it
        recipient_id = input("Enter the recipient's ID: ")
        url = "https://discord.com/api/v9/users/@me/channels"
        data = {"recipient_id": recipient_id}
        r = requests.post(url, headers=auth, json=data)
        if r.status_code != 200:
            print(f"Error creating DM channel: {r.status_code}")
            exit()

        channel_id = r.json()['id']
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

        # sending messages with numbers from 1 to 1000000
        for i in range(1, 1000001):
            msg['content'] = str(i)
            requests.post(url, headers=auth, data=msg)

            if i % 5 == 0:
                print("Rate Limit Bypass :)")
                time.sleep(5) # pause for 5 seconds after every 5 messages

            time.sleep(1) # delay for 1 second between messages

    else:
        print("Invalid mode selected. Please enter 's' or 'd' as the mode.")
        
elif choice == "2":
    print("\nRunning Webhook Spammer...")
    time.sleep(1)
    
    webhook_url = input("Enter the Discord webhook URL: ")
    message = input("Enter the message to send: ")
    
    # Set up the request headers and message data
    headers = {
        'Content-type': 'application/json'
    }
    data = {
        'content': message
    }

    # Send the message repeatedly
    while True:
        response = requests.post(webhook_url, headers=headers, json=data)
        if response.status_code == 204:
            print("Message sent successfully.")

elif choice == "3":
    print("\nRunning Delete DM...")
    time.sleep(1)
 
import requests
import time

auth_token = input("Enter your Discord auth token: ")
headers = {
    'Authorization': auth_token
}

# Ask the user if they want to delete messages from all DMs or just one DM
while True:
    option = input("Enter 'all' to delete messages from all DMs or 'one' to delete messages from one DM: ")
    
    if option.lower() == "all":
        print("\nNote: If a user has blocked you, you will get an error and the messages won't be deleted.")
        # Fetch the user's DM channels
        url = 'https://discord.com/api/v9/users/@me/channels'
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Error fetching DM channels: {response.status_code}")
            exit()

        channels = response.json()

        # Iterate through the channels and delete all messages
        for channel in channels:
            if channel['type'] == 1:
                # Fetch the messages in the channel
                url = f"https://discord.com/api/v9/channels/{channel['id']}/messages"
                response = requests.get(url, headers=headers)

                if response.status_code != 200:
                    print(f"Error fetching messages: {response.status_code}")
                    continue

                messages = response.json()

                # Delete each message in the channel
                for message in messages:
                    url = f"https://discord.com/api/v9/channels/{channel['id']}/messages/{message['id']}"
                    response = requests.delete(url, headers=headers)

                    if response.status_code != 204:
                        print(f"Error deleting message {message['id']}: {response.status_code}")
                    else:
                        time.sleep(1)  # Add 1-second delay

        print("All DMs deleted successfully.")
        break
        
    elif option.lower() == "one":
        user_id = input("Enter the user ID to delete DMs from: ")
        print("\nNote: If the user has blocked you, you will get an error and the messages won't be deleted.")
        # Fetch the user's DM channel with the specified recipient
        url = f'https://discord.com/api/v9/users/@me/channels'
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error fetching DM channels: {response.status_code}")
            exit()

        channels = response.json()
        dm_channel = None
        for channel in channels:
            if channel['type'] == 1 and channel['recipients'][0]['id'] == user_id:
                dm_channel = channel
                break

        if dm_channel is None:
            print(f"No DM channel found with recipient ID {user_id}.")
            continue

        # Fetch the messages in the channel
        url = f"https://discord.com/api/v9/channels/{dm_channel['id']}/messages"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Error fetching messages: {response.status_code}")
            continue

        messages = response.json()

        # Delete each message in the channel
        for message in messages:
            url = f"https://discord.com/api/v9/channels/{dm_channel['id']}/messages/{message['id']}"
            response = requests.delete(url, headers=headers)

            if response.status_code != 204:
                print(f"Error deleting message {message['id']}: {response.status_code}")
            else:
                time.sleep(1)  # Add 1-second delay