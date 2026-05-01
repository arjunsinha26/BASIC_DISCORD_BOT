# Discord Slash Command Bot

A multi-purpose Discord bot built using `discord.py` that demonstrates **slash commands**, permission handling, and basic server management utilities.

---

## 🚀 Features

* Slash command support using `app_commands`
* Role management (add/remove roles)
* Channel management (create/delete text & voice channels)
* Webhook management (create/delete)
* Message history tracking
* Permission inspection
* Server structure export (channel listing + backup)

---

## 📦 Requirements

* Python 3.8+
* discord.py

Install dependencies:

```bash
pip install discord.py
```

---

## ⚙️ Setup

1. Create a bot from the Discord Developer Portal
2. Enable **Message Content Intent** and required permissions
3. Copy your bot token
4. Replace in code:

```python
token = "YOUR_TOKEN_HERE"
```

---

## ▶️ Run the Bot

```bash
python your_file_name.py
```

---

## 🧠 Slash Commands Overview

| Command                            | Description                              |
| ---------------------------------- | ---------------------------------------- |
| `/hello`                           | Sends a greeting message                 |
| `/say <text>`                      | Echoes user input                        |
| `/addrole <member> <role>`         | Adds a role to a user                    |
| `/remove_role <member> <role>`     | Removes a role                           |
| `/messagehistory <member> <limit>` | Fetches recent messages                  |
| `/create_text_channel <name>`      | Creates a text channel                   |
| `/create_voice_channel <name>`     | Creates a voice channel                  |
| `/delete_channel <name>`           | Deletes a channel                        |
| `/my_perms`                        | Lists bot permissions                    |
| `/create_webhook <name>`           | Creates a webhook                        |
| `/delete_webhook <name>`           | Deletes webhook(s) by name               |
| `/raw_copy_channels`               | Lists all channels by category           |
| `/backup`                          | Creates a JSON backup of server channels |

---

## 🔐 Permissions Required

Depending on command usage:

* Manage Roles
* Manage Channels
* Manage Webhooks
* Read Message History

The bot also checks its **own permissions** before executing actions.

---

## 📁 Output

### Backup Command

Creates a `.json` file containing:

* Categories
* Channels
* Channel settings (topic, slowmode, bitrate, etc.)

---

## ⚠️ Notes

* Slash commands are synced on startup (`bot.tree.sync()`)
* Some commands are **ephemeral** (visible only to the user)
* Output messages are trimmed to fit Discord limits (~2000 chars)
* Webhook URLs are sensitive — do not expose publicly

---

## 🧾 License

For educational and personal use.
