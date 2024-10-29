![cover](blum.png)
# Blum Enhanced By @TheTeamAlexa

AUTO CLAIM FOR BLUM / @blum THE SCRIPT IS ORIGINALLY BELONG TO CUCUMBER

[![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/TheTeamAlexa)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/TheTeamAlexa)

# Table of Contents
- [Blum Enhanced By @TheTeamAlexa](#blumalexa)
- [Warning](#warning)
- [Tutorial Video](#tutorial-video)
- [Available Features](#available-features)
- [How to Use](#how-to-use)
  - [Command Line Options / Arguments](#command-line-options--arguments)
  - [Termux](#termux)
- [Viewing Reports](#viewing-reports)
- [Thank You](#thank-you)

# Tutorial Video

Clik On **[Tutorial Video](https://youtu.be/T4n9E1ySFMY?si=7Sn-KzdhfJg1PMum)** to wtch full video how we can use this on termux.

# Warning

All risks are borne by the user never try to use on main account 😕 

# Available Features

- [x] Automatic Claim Every 8 Hours
- [x] Automatic Daily Check-In (Login)
- [x] Automatic Claim of Referral Results
- [x] Proxy Support
- [x] Automatic Task Completion
- [x] Automatic Game Play after Claiming
- [x] Multi-process support
- [x] Random User-Agent
- [x] Total balance report of all accounts
- [x] Waiting time before starting the program

# How to Use

## Command Line Options / Arguments

This script/program supports several argument parameters that can be used. Here's an explanation of the arguments:

`--data` / `-D`: Used when you have a different filename for storing account data. By default, the filename used by this script/program to store account data is `data.txt`. For example, if you have a file named `query.txt` as the file storing account data, just run `bot.py` with the `--data` / `-D` argument. Example: `python bot.py --data query.txt`

## Termux

1. Make sure your device has Python and Git installed.

    Recommendation: Use Python version 3.8+ (3.8 or newer)
   
    Install Python
   ```shell
   pkg install python3
   ```
   Then use all of these command at once
   ```shell
   pkg update && pkg upgrade -y
pkg install python rust git -y
pkg install nano
git clone https://github.com/TheTeamAlexa/Blum.git
cd Blum
pip install -r requirements.txt
nano data.txt
   ```
2. Edit the `data.txt` file, enter your query data into the `data.txt` file. One line for 1 account, if you want to add a 2nd account, fill it in on a new line.

6. Run the program/script.
   ```
   python Blum.py
   ```

# Viewing Reports

To view a report of the total balance of all accounts you can run a file called `report.py`


## How to get query ID through tgWebAppData (query_id / user_id)

1. Login telegram via portable or web version
2. Launch the bot
3. Press `F12` on the keyboard 
4. Open console
5. Сopy this code in Console for getting tgWebAppData (user= / query=):

```javascript
copy(Telegram.WebApp.initData)
```

6. you will get data that looks like this

```
query_id=AA....
user=%7B%22id%....
```
7. add it to `data.txt` file or create it if you dont have one


You can add more and run the accounts in turn by entering a query id in new line like this:
```txt
query_id=xxxxxxxxx-Rxxxxujhash=cxxx
query_id=xxxxxxxxx-Rxxxxujhash=cxxxx
```


# Error Table

| Error                 | Description                                                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Wrong format | This is because the query ID you have pasted has a extra Space so close your bot and try again and take a look during the editing of ``` nana data.txt ```           |

# Thank You
