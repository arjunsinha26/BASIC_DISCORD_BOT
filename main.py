from discord.ext import commands
from discord import app_commands
import discord
from datetime import datetime
import json


token = "add your token here"


bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} is ready")
    try:
        synced = await bot.tree.sync()
        #print(f"Synced {len(synced)} commands")
        for i in synced:
            print(i)
        print("These are active commands!")
    except Exception as e:
        print(e)


@bot.tree.command(name="hello", description="Example 1") #Example 1
async def hello(interaction:discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command", ephemeral=True)



@bot.tree.command(name = "say",description="Example 2")   #Example 2
@app_commands.describe(arg = "Whatever argument you wanna pass")
async def say(interaction:discord.Interaction,arg : str):
    await interaction.response.send_message(f"{interaction.user.name} said: `{arg}`")


@bot.tree.command(name="addrole",description="add role to someone") #Add Role
async def addrole_slash(interaction: discord.Interaction, member:discord.Member, role:discord.Role):
    if not interaction.user.guild_permissions.manage_roles:
        return await interaction.response.send_message("No permission", ephemeral=True)
    try:
        await member.add_roles(role)
        await interaction.response.send_message(f"Added {role.name} to {member.mention}")
    except discord.Forbidden:
        await interaction.response.send_message("Bot lacks permission", ephemeral=True)


@bot.tree.command(name = "remove_role", description="removing role from a user")
@commands.has_permissions(manage_roles=True)
async def removerole(interaction:discord.Interaction,member:discord.Member,role:discord.Role):
    try:
        await member.remove_roles(role)
        await interaction.response.send_message(f"Removed {role.name} from {member.mention}")
    except discord.Forbidden:
        await interaction.response.send_message("I don't have permission to remove this role")
    except Exception as e:
        await interaction.response.send_message(f"Error: -[{e}]")

@bot.tree.command(name="messagehistory",description="History of a member's messages")
async def message_history(interaction:discord.Interaction,member:discord.Member,limit:int):
    if not interaction.user.guild_permissions.read_message_history:
        await interaction.response.send_message("No permission.",ephemeral=True)
        return
    channel = interaction.channel
    records = []
    async for msg in channel.history(limit=limit):
        if msg.author == member:
            content = msg.content if msg.content else "[No Text]"
            timestamp = msg.created_at.strftime("%Y-%m-%d %H:%M:%S")

            records.append(f"```[{timestamp}]{member}:{content}```")

    if not records:
        await interaction.response.send_message(f"No messages found from {member.id}",ephemeral=True)
        return
    records.reverse()
    output = "\n".join(records)
    await interaction.response.send_message(output[:1900])
