<div align="center">

# 🐍 Discord.py Beginner Examples

### A small collection of slash-command examples to help beginners understand how a Discord bot works.

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Library-discord.py-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="discord.py">
  <img src="https://img.shields.io/badge/Level-Beginner-2EA44F?style=for-the-badge" alt="Beginner level">
  <img src="https://img.shields.io/badge/Commands-Slash%20Commands-8A2BE2?style=for-the-badge" alt="Slash commands">
</p>

<p>
  <a href="#-about"><img src="https://img.shields.io/badge/About-5865F2?style=for-the-badge" alt="About"></a>
  <a href="#-examples-included"><img src="https://img.shields.io/badge/Examples-2EA44F?style=for-the-badge" alt="Examples"></a>
  <a href="#-setup"><img src="https://img.shields.io/badge/Setup-orange?style=for-the-badge" alt="Setup"></a>
  <a href="#-important-notes"><img src="https://img.shields.io/badge/Notes-red?style=for-the-badge" alt="Notes"></a>
</p>

</div>

---

## 📌 About

This repository contains a simple `discord.py` script demonstrating several common bot features: basic slash commands, role management, and reading a member's recent messages in the current channel.

> **Learning project:** This code is intended to give beginners an idea of how things work in `discord.py`. It is an introductory example, not a complete or production-ready moderation bot. Read the code, experiment with it in a test server, and check the official documentation as you learn.

## ✨ Examples Included

| Command | What it demonstrates |
|---|---|
| `/hello` | Sends an ephemeral greeting to the person who invoked the command. |
| `/say arg` | Accepts a string argument and repeats it in a response. |
| `/addrole member role` | Checks whether the invoking user has Manage Roles permission, then attempts to add a role. |
| `/remove_role member role` | Demonstrates removing a role and handling errors. |
| `/messagehistory member limit` | Checks Read Message History permission, then searches recent messages in the current channel for a selected member. |

### 🧩 Other concepts in the script

- **Slash-command registration:** `bot.tree.sync()` syncs application commands when the bot starts.
- **Command parameters:** Uses Discord types such as `discord.Member` and `discord.Role` to provide Discord-aware options.
- **Permissions:** Shows a basic permission check before role assignment and message-history access.
- **Error handling:** Demonstrates `discord.Forbidden` handling and general exception reporting.
- **Message timestamps:** Formats message creation times using `datetime.strftime()`.
- **Asynchronous history iteration:** Uses `async for` to read messages from channel history.

## 🛠️ Setup

### 1. Install Python

Install a supported Python version, then check that Python and pip are available:

```bash
python --version
python -m pip --version
```

### 2. Install discord.py

```bash
python -m pip install -U discord.py
```

### 3. Create a Discord application and bot

1. Open the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create an application and add a bot.
3. Copy the bot token.
4. Invite the bot to a test server with the required permissions and application-command support.

### 4. Add your token

Replace the placeholder in the script:

```python
token = "add your token here"
```

Make sure the bottom of your Python file starts the bot, for example:

```python
bot.run(token)
```

**Security tip:** Never publish your real bot token in a public repository. If it is exposed, reset it in the Developer Portal. For projects beyond a quick local example, load it from an environment variable instead.

### 5. Run the bot

Save the script as `bot.py`, then run:

```bash
python bot.py
```

After the bot starts and the slash commands sync, try the commands in your test server. Command registration can take a little time to appear.

## 🔐 Permissions and Discord settings

Depending on the commands you use, the bot needs suitable server and channel permissions:

- **Manage Roles** to add or remove roles.
- **View Channels**, **Read Message History**, and access to the relevant channel to inspect message history.
- The bot's highest role must be above any role it is expected to assign or remove.
- Enable the relevant bot intents in the Developer Portal if your wider project needs them. This example initializes `discord.Intents.all()`, which requests all intents; only enable privileged intents that you actually need.

The invoking user's permissions and the bot's own permissions are different. Both may need to be checked for a reliable implementation.

## ⚠️ Important Notes

This is a beginner example, so there are some limitations worth understanding:

- The `/remove_role` command uses `@commands.has_permissions` on an application command. Prefix-command checks do not automatically behave like application-command permission checks in every context; for slash commands, use the appropriate `app_commands` checks or check permissions inside the function.
- The `/messagehistory` command searches only the **current channel**, not every channel in the server.
- The `limit` parameter should be constrained to a sensible positive range. Very large values may make the command slow or impractical.
- Discord limits interaction response lengths. Returning `output[:1900]` helps keep the response under the usual message limit, but it can cut off a record mid-line and does not split long histories into multiple messages.
- Message content may contain Markdown or backticks, which can interfere with the code-block formatting used by the history command.
- The script imports `json` but does not currently use it.
- Error handling and permission checks are intentionally simple and should be improved before using a bot in a public server.

## 🧠 What Beginners Can Learn

1. How to define application commands with `@bot.tree.command`.
2. How to receive and respond to a `discord.Interaction`.
3. How typed parameters can represent members and roles.
4. How to perform basic permission checks.
5. How to use `await` for asynchronous Discord operations.
6. How to iterate through channel history and format timestamps.
7. Why permissions, input validation, and error handling matter.

## 📚 Useful Resources

- [discord.py documentation](https://discordpy.readthedocs.io/en/stable/)
- [discord.py API reference](https://discordpy.readthedocs.io/en/stable/api.html)
- [Discord Developer Portal](https://discord.com/developers/applications)
- [Discord Developer Documentation](https://discord.com/developers/docs)

---

<div align="center">

**Made for learning and experimentation.**

⭐ Try the examples in a private test server and build on them as you learn!

</div>
