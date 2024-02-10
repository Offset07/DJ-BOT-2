from highrise import BaseBot, Position
from highrise.models import SessionMetadata, User
from highrise import __main__
from highrise.models import Item
from asyncio import run as arun
from highrise.models import AnchorPosition
import random
from highrise.models import GetMessagesRequest
from asyncio import run as arun
import requests
from highrise import BaseBot, __main__
from highrise.models import (AnchorPosition, Item, Position, User,)
from highrise import BaseBot
from collections import UserDict
from highrise.models import SessionMetadata, User
from json import load, dump
from time import time
from math import sqrt
from highrise import BaseBot, User, Position, AnchorPosition

from highrise.models import Position
from highrise.models import SessionMetadata, User, CurrencyItem, Item, AnchorPosition, Reaction, ModerateRoomRequest, Position
import random
import asyncio
from highrise import *
from highrise.models import *
import asyncio
from asyncio import Task

from highrise import *
from highrise.models import *
import asyncio
from asyncio import Task

from highrise import *
from highrise.models import *
import asyncio
from asyncio import Task



class BotDefinition:

  def __init__(self, bot, room_id, api_token):
      self.bot = bot
      self.room_id = room_id
      self.api_token = api_token


class MyBot(BaseBot):
  dancs = [
    "idle-loop-sitfloor", "emote-tired", "emoji-thumbsup", "emoji-angry",
    "dance-macarena", "emote-hello", "dance-weird", "emote-superpose",
    "idle-lookup", "idle-hero", "emote-wings", "emote-laughing", "emote-kiss",
    "emote-wave", "emote-hearteyes", "emote-theatrical", "emote-teleporting",
    "emote-slap", "emote-ropepull", "emote-think", "emote-hot",
    "dance-shoppingcart", "emote-greedy", "emote-frustrated", "emote-float",
    "emote-baseball", "emote-yes", "idle_singing", "idle-floorsleeping",
    "idle-enthusiastic", "emote-confused", "emoji-celebrate", "emote-no",
    "emote-swordfight", "emote-shy", "dance-tiktok2", "emote-model",
    "emote-charging", "emote-snake", "dance-russian", "emote-sad",
    "emote-lust", "emoji-cursing", "emoji-flex", "emoji-gagging",
    "dance-tiktok8", "dance-blackpink", "dance-pennywise", "emote-bow",
    "emote-curtsy", "emote-snowball", "emote-snowangel", "emote-telekinesis",
    "emote-maniac", "emote-energyball", "emote-frog", "emote-cute",
    "dance-tiktok9", "dance-tiktok10", "emote-pose7", "emote-pose8",
    "idle-dance-casual", "emote-pose1", "emote-pose3", "emote-pose5",
    "emote-cutey", "emote-Relaxing", "emote-model", "emote-fashionista",
    "emote-gravity", "emote-zombierun", "emoji-ceilebrate", "emoji-floss",
    "emote-Relaxing ", "emote-punkguitar", "dance-tiktok9", "dance-weird",
    "emote-punkguitar", "idle-uwu"
    "emote-bow", "emote-cursty", "dance-breakdance", "emote-creepycute","emote-headblowup","idle-guitar"
  ]



  def __init__(self):
    super().__init__()
    self.is_dancing = False

  async def on_start(self, session_metadata: SessionMetadata) -> None:
    print("selamün aleyküm")
    self.highrise.tg.create_task(
      self.highrise.teleport(session_metadata.user_id, Position(7, 0, 7, "FrontRight")))

  async def run(self, room_id, token):
      definitions = [BotDefinition(self, room_id, token)]
      await __main__.main(definitions)

  async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
    await self.highrise.send_whisper(user.id, "hoş geldiniz geldiğiniz için bir adet hamburger kazandiniz🍔")
    await self.highrise.send_whisper(user.id, "🍌🍉ooo kimler gelmiş kimlerr")
    await self.highrise.send_whisper(user.id, "hoş geldin kankam♥️")

    await self.highrise.react("heart", user.id)


    try:
        emote_id = random.choice(self.dancs)
        await self.highrise.send_emote(emote_id, user.id)
    except:
        print(f"{emote_id}")

    await self.highrise.send_emote("dance-floss") 


  async def on_chat(self, user: User, message: str) -> None:
    


    if message.startswith("yemek"):
      await self.highrise.chat(f"hamburgerimiz var 🍔 $${user.username} ")





    
    if message.startswith("اك"):
      await self.highrise.chat(f"عندنا تاكو 🌯 $${user.username}")

    if message.startswith("اكل"):
      await self.highrise.chat(f"عندنا نودلز🍜 $${user.username}")

    if message.startswith("اكل"):
      await self.highrise.chat(f"عندنا سوشي 🍣 $${user.username}")

    if message.startswith("اكل") :
      await self.highrise.chat(f"عندنا بيتزا 🥘 $${user.username}")

    if message.startswith("اكل"):
      await self.highrise.chat(f"عندنا فلافل🧆🥙 $${user.username}")

    if message.startswith("اكل"):
      await self.highrise.chat(f"عندنا هوت دوج 🌭 $${user.username}")

    if message.startswith("اكل"):
      await self.highrise.chat(f"عندنا ارز  🍚$${user.username}")

    if message.startswith("اكل"):
      await self.highrise.chat(f"عندنا بوبا🧋 $${user.username}")

    if message.startswith("اكل"):
      await self.highrise.chat(f"تحليه 🍬🍫🍪🍩🍭🧁 $${user.username}")

    if message.startswith("اكل"):
      await self.highrise.chat(f"اكتب اسم الصنف عشان تعرف السعر $${user.username}")

    if message.startswith("همبرغر"):
      await self.highrise.chat(f"$بي 30-  @{user.username}")

    if message.startswith("ماشي همبرغر"):
      await self.highrise.chat(f"اتفضل 🍔 @{user.username}")

    if message.startswith("تاكو"):
      await self.highrise.chat(f"$بي 10     @{user.username}")

    if message.startswith("ماشي تاكو"):
      await self.highrise.chat(f"اتفضل 🌯 @{user.username}")

    if message.startswith("نودلز"):
      await self.highrise.chat(f"$بي 15  @{user.username}")

    if message.startswith("ماشي"):
      await self.highrise.chat(f"اتفضل 🍜 @{user.username}")

    if message.startswith("سوشي"):
      await self.highrise.chat(f"$بي 100  @{user.username}")

    if message.startswith("ماشي سوشي"):
      await self.highrise.chat(f"اتفضل 🍱 @{user.username}")

    if message.startswith("بيتزا"):
      await self.highrise.chat(f"$بي 5  @{user.username}")

    if message.startswith("ماشي بيتزا"):
      await self.highrise.chat(f"اتفضل 🍕 @{user.username}")

    if message.startswith("فلافل"):
      await self.highrise.chat(f"$بي 5  @{user.username}")

    if message.startswith("ماشي فلافل"):
      await self.highrise.chat(f"اتفضل 🥙 @{user.username}")

    if message.startswith("هوت دوج"):
      await self.highrise.chat(f"$بي 15  @{user.username}")

    if message.startswith("ماشي هوت دوج"):
      await self.highrise.chat(f"اتفضل🌭 @{user.username}")

    if message.startswith("ارز"):
      await self.highrise.chat(f"$بي 25  @{user.username}")

    if message.startswith("ماشي ارز"):
      await self.highrise.chat(f"اتفضل 🍚 @{user.username}")

    if message.startswith("بوبا"):
      await self.highrise.chat(f"$بي 50  @{user.username}")

    if message.startswith("ماشي بوبا"):
      await self.highrise.chat(f"اتفضل 🧋 @{user.username}")

    if message.startswith("تحليه"):
      await self.highrise.chat(f"$30 بي   @{user.username}")

    if message.startswith("ماشي تحليه"):
     await self.highrise.chat(f"اتفضل 🍫🍬🍩 @{user.username}")








    dance_emotes = {
      "float": "emote-float",
      "pose1": "dance-tiktok2",
      "pose1": "emote-pose1",
      "shoppingcart": "dance-shoppingcart",
      "russian": "dance-russian",
      "sing": "idle_singing",
      "enthused": "idle-enthusiastic",
      "casual": "idle-dance-casual",
      "sit": "idle-loop-sitfloor",
      "lust": "emote-lust",
      "greedy": "emote-greedy",
      "bow": "emote-bow",
      "crusty": "emote-curtsy",
      "snowball": "emote-snowball",
      "snowangel": "emote-snowangel",
      "confused": "emote-confused",
      "teleporting": "emote-teleporting",
      "sword": "emote-swordfight",
      "energyball": "emote-energyball",
      "tiktok8": "dance-tiktok8",
      "kpop": "dance-blackpink",
      "model": "emote-model",
      "wise": "dance-pennywise",
      "tiktok10": "dance-tiktok10",
      "telekinesis": "emote-telekinesis",
      "hot": "emote-hot",
      "weird": "dance-weird",
      "pose7": "emote-pose7",
      "pose8": "emote-pose8",
      "pose3": "emote-pose3",
      "pose5": "emote-pose5"
    }

    if message.startswith("Loop") and not self.is_dancing:
      dance_number = message.split(" ")[1]
      dance_emote = dance_emotes.get(dance_number)
      if dance_emote:
          self.is_dancing = True
          while self.is_dancing:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote(dance_emote, user.id)
      else:
          await self.highrise.chat("الرقم غير صالح")
    elif message.startswith("stop dance"):
      self.is_dancing = False
      await self.highrise.chat("تم إيقاف الرقص")

    if message.startswith("0"):
      await self.highrise.send_emote("emote-float", user.id)
    if message.startswith("2"):
      await self.highrise.send_emote("dance-tiktok2", user.id)   
    if message.startswith("3"):
      await self.highrise.send_emote("emote-pose1", user.id)
    if message.startswith("4"):
      await self.highrise.send_emote("dance-shoppingcart", user.id)
    if message.startswith("5"):
      await self.highrise.send_emote("dance-russian", user.id)
    if message.startswith("6"):
      await self.highrise.send_emote("idle_singing", user.id)
    if message.startswith("7"):
      await self.highrise.send_emote("idle-enthusiastic", user.id)   
    if message.startswith("8"):
      await self.highrise.send_emote("idle-dance-casual", user.id)   
    if message.startswith("9"):
      await self.highrise.send_emote("idle-loop-sitfloor", user.id)
    if message.startswith("10"):
      await self.highrise.send_emote("emote-lust", user.id)
    if message.startswith("11"):
      await self.highrise.send_emote("emote-greedy", user.id)
    if message.startswith("12"):
      await self.highrise.send_emote("emote-bow", user.id)
    if message.startswith("13"):
      await self.highrise.send_emote("emote-curtsy", user.id)
    if message.startswith("14"):
      await self.highrise.send_emote("emote-snowball", user.id)
    if message.startswith("15"):
      await self.highrise.send_emote("emote-snowangel", user.id)
    if message.startswith("16"):
      await self.highrise.send_emote("emote-confused", user.id)
    if message.startswith("17"):
      await self.highrise.send_emote("emote-teleporting", user.id)
    if message.startswith("18"):
      await self.highrise.send_emote("emote-swordfight", user.id)
    if message.startswith("19"):
      await self.highrise.send_emote("emote-energyball", user.id)
    if message.startswith("20"):
      await self.highrise.send_emote("dance-tiktok8", user.id)
    if message.startswith("21"):
      await self.highrise.send_emote("dance-blackpink", user.id)
    if message.startswith("22"):
      await self.highrise.send_emote("emote-model", user.id)
    if message.startswith("23"):
      await self.highrise.send_emote("dance-pennywise", user.id)
    if message.startswith("24"):
      await self.highrise.send_emote("dance-tiktok10", user.id)
    if message.startswith("25"):
      await self.highrise.send_emote("emote-telekinesis", user.id)
    if message.startswith("26"):
      await self.highrise.send_emote("emote-hot", user.id)
    if message.startswith("27"):
      await self.highrise.send_emote("dance-weird", user.id)
    if message.startswith("28"):
      await self.highrise.send_emote("emote-pose7", user.id)
    if message.startswith("29"):
      await self.highrise.send_emote("emote-pose8", user.id)
    if message.startswith("30"):
      await self.highrise.send_emote("emote-pose3", user.id)
    if message.startswith("31"):
      await self.highrise.send_emote("emote-pose5", user.id)  
    if message.startswith("32"):
      await self.highrise.send_emote("emote-pose5", user.id)  
    if message.startswith("31"):
      await self.highrise.send_emote("emote-pose5", user.id)  
    if message.startswith("31"):
      await self.highrise.send_emote("emote-pose5", user.id)   

    

    if "نزلني" in message or "نزلني" in message:
            try:
                await self.highrise.teleport(f"{user.id}", Position(5, 0, 3))
            except:
                print("error 3")

    if "صعدني" in message or "طلعني" in message:
      try:
          await self.highrise.teleport(f"{user.id}", Position(10, 7, 3))
      except:
          print("error 3")

    if message.startswith("Kick"):
            if user.username == "o.r.d.3.k" "MR.ORDER":
                pass
            else:
                await self.highrise.chat("You do not have permission to use this command.")
                return
            #separete message into parts
            parts = message.split()
            #check if message is valid "kick @username"
            if len(parts) != 2:
                await self.highrise.chat("Invalid kick command format.")
                return
            #checks if there's a @ in the message
            if "@" not in parts[1]:
                username = parts[1]
            else:
                username = parts[1][1:]
            #check if user is in room
            room_users = (await self.highrise.get_room_users()).content
            for room_user, pos in room_users:
                if room_user.username.lower() == username.lower():
                    user_id = room_user.id
                    break
            if "user_id" not in locals():
                await self.highrise.chat("User not found, please specify a valid user and coordinate")
                return
            #kick user
            try:
                await self.highrise.moderate_room(user_id, "kick")
            except Exception as e:
                await self.highrise.chat(f"{e}")
                return
            #send message to chat
            await self.highrise.chat(f"{username} has been kicked from the room.")

    if message.startswith("move"):
            room_dictionary = {"room_1":"<6512abf950df23a28e2fe293>",
                               "room_2":"<651be7abc1be5f769730182c>",}
            if user.username != "TOMY_X" "sucuk.yumurta":
                await self.highrise.chat("You do not have permission to use this command.")
                return
            parts = message.split()
            if len(parts) != 3:
                await self.highrise.chat("Invalid move command format.")
                return
            command, username, room = parts
            if "@" not in username:
                username = username
            else:
                username = username[1:]
            if room not in room_dictionary:
                await self.highrise.chat("Invalid room, please specify a valid room.")
                return
            #check if user is in room
            room_users = (await self.highrise.get_room_users()).content
            for room_user, pos in room_users:
                if room_user.username.lower() == username.lower():
                    user_id = room_user.id
                    break
            if "user_id" not in locals():
                await self.highrise.chat("User not found, please specify a valid user and coordinate")
                return
            #move user
            try:
                await self.highrise.move_user_to_room(user_id, room_dictionary[room])
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")
                return

    if message.startswith("users"):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"There are {len(room_users)} users in the room")

    if message.startswith("wallet"):
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.chat(f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")

    if message.lower().startswith("/voiceremove "):
            try:
                command, username = message.split(" ")
            except:
                await self.highrise.chat("Invalid command, please use /voiceremove <username>")
                return
            #gets room users and check if the user is in the room
            room_users = (await self.highrise.get_room_users()).content
            for room_user, position in room_users:
                if room_user.username.lower() == username.lower():
                    user_id = room_user.id
                    break
            if "user_id" not in locals():
                await self.highrise.chat(f"User '{username}' not found.")
                return

            #checks if the user is already in the voice list
            voice_list = (await self.highrise.get_voice_status()).users
            if user_id not in voice_list:
                await self.highrise.chat(f"User '{username}' is not in the voice list.")
                return

            await self.highrise.remove_user_from_voice(user_id)
            await self.highrise.chat(f"Removed '{username}' from the voice list.")

    if message.lstrip().startswith("add"):
      if user.username.lower() in [ "tomy_x" , "o.r.d.3.k"]:
              response = await self.highrise.get_room_users()
              users = [content[0] for content in response.content]
              usernames = [user.username.lower() for user in users]

              parts = message[1:].split()
              args = parts[1:]

              if len(args) < 2:
                      await self.highrise.send_whisper(user.id, "Use: Command > Name > Place ")
                      return
              elif args[0][0] != "@":
                      await self.highrise.send_whisper(user.id, f" Incorrect format  '@username'.")
                      return
              elif args[0][1:].lower() not in usernames:
                      await self.highrise.send_whisper(user.id, f"{args[0][1:]}Not in the room.")
                      return

              position_name = " ".join(args[1:])
              if position_name == 'VIP2':
                      dest = Position(19, 4.5, 17)

              elif position_name == 'VIP1':
                      dest = Position(16, 11, 9)

              elif position_name == 'DJ':
                      dest = Position(10, 0.5, 1)

              elif position_name == 'HOST':
                      dest = Position(15, 7, 6)  

              elif position_name == 'down':
                      dest = Position(5, 0, 6)  

              else:
                      return await self.highrise.send_whisper(user.id, f"  The site is wrong ")
              user_id = next ((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
              if not user_id:
                      await self.highrise.send_whisper(user.id, f"User {args[0][1:]} unavailable ")
                      return

              await self.highrise.teleport(user_id, dest)
              await self.highrise.send_whisper(user.id, f" move  {args[0][1:]} to ({dest.x}, {dest.y}, {dest.z})")
      else:
              await self.highrise.send_whisper(user.id, " You can't fix this ")
    else:
          pass

    if message.lower().startswith("/equip"):
      await self.highrise.set_outfit(outfit=[
            Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
            Item(type='clothing', amount=1, id='hair_front-n_malenew09', account_bound=False, active_palette=1),
            Item(type='clothing', amount=1, id='eyebrow-n_25', account_bound=False, active_palette=1),
            Item(type='clothing', amount=1, id='mouth-basic2018smugmouth', account_bound=False, active_palette=3),
            Item(type='clothing', amount=1, id='nose-n_basic2018newnose20',),
            Item(type='clothing', amount=1, id='shirt-f_marchingband', account_bound=False, active_palette=-1),
            Item(type='clothing', amount=1, id='pants-n_room12019rippedpantsblack', account_bound=False, active_palette=-1),
            Item(type='clothing',amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
            Item(type='clothing', amount=1, id='eye-n_basic2018woaheyes', account_bound=False, active_palette=7),
            Item(type='clothing', amount=1, id='handbag-n_room22019banana', account_bound=False, active_palette=-1),
            ])

    if "Charging" in message:
      try:
        emote_id = "emote-charging"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Wise" in message:
      try:
        emote_id = "dance-pennywise"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Tiktok2" in message:
      try:
        emote_id = "dance-tiktok2"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Virgalrove" in message:
      try:
        emote_id = "dance-tiktok9"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Weird" in message:
      try:
        emote_id = "dance-weird"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Telekinesis" in message:
      try:
        emote_id = "emote-telekinesis"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Tiktok8" in message:
      try:
        emote_id = "dance-tiktok8"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Maniac" in message:
      try:
        emote_id = "emote-maniac"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Zombie" in message:
      try:
        emote_id = "emote-zombierun"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Relaxing" in message:
      try:
        emote_id = "emote-Relaxing"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Gravity" in message:
      try:
        emote_id = "emote-gravity"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Fashon" in message:
      try:
        emote_id = "emote-fashionista"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Pose7" in message:
      try:
        emote_id = "emote-pose7"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Pink" in message:
      try:
        emote_id = "dance-blackpink"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Kiss" in message:
      try:
        emote_id = "emote-kiss"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Hello" in message:
      try:
        emote_id = "emote-hello"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Tiktok8" in message:
      try:
        emote_id = "dance-tiktok8"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Weird" in message:
      try:
        emote_id = "dance-weird"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "هاي" in message:
      try:
        emote_id = "emote-kiss"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "شكرا" in message:
      try:
        emote_id = "emote-kiss"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "تو" in message:
      try:
        emote_id = "idle-dance-casual"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")


    if "Model" in message:
      try:
        emote_id = "emote-model"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "no" in message:
      try:
        emote_id = "emote-no"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "رقصني" in message:
      try:
        emote_id = random.choice(self.dancs)
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Confused" in message:
      try:
        emote_id = "emote-confused"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")
    if "cute" in message:
      try:
        emote_id = "emote-cute"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")
    if "Curtsy" in message:
      try:
        emote_id = "emote-curtsy"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Tiktok4 " in message:
      try:
        emote_id = "idle-dance-tiktok4"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Uwu" in message:
      try:
        emote_id = "idle-uwu"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "Kpop" in message:
      try:
        emote_id = "dance-blackpink"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Energy ball" in message:
      try:
        emote_id = "emote-energyball"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Float" in message:
      try:
        emote_id = "emote-float"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Frog" in message:
      try:
        emote_id = "emote-frog"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Teleport" in message:
      try:
        emote_id = "emote-teleporting"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Sword" in message:
      try:
        emote_id = "emote-swordfight"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Casual" in message:
      try:
        emote_id = "idle-dance-casual"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Cutey" in message:
      try:
        emote_id = "idle-dance-cutey"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "You got a tip!" in message:
      try:
        emote_id = "dance-tiktok2"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Sing" in message:
      try:
        emote_id = "idle_singing"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Greedy" in message:
      try:
        emote_id = "emote-greedy"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Sweating" in message:
      try:
        emote_id = "emote-hot"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Pose1" in message:
      try:
        emote_id = "emote-superpose"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Russian dance" in message:
      try:
        emote_id = "dance-russian"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Snake" in message:
      try:
        emote_id = "emote-snake"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Lust" in message:
      try:
        emote_id = "emote-lust"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Wise" in message:
      try:
        emote_id = "dance-pennywise"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Bow" in message:
      try:
        emote_id = "emote-bow"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Gagging" in message:
      try:
        emote_id = "emoji-gagging"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Rest" in message:
      try:
        emote_id = "idle-loop-sitfloor"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Enthused" in message:
      try:
        emote_id = "idle-enthusiastic"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Snow ball" in message:
      try:
        emote_id = "emote-snowball"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Snow angel" in message:
      try:
        emote_id = "emote-snowangel"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Flex" in message:
      try:
        emote_id = "emoji-flex"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Laugh" in message:
      try:
        emote_id = "emote-laughing"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Yes" in message:
      try:
        emote_id = "emote-yes"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Guitar" in message:
      try:
        emote_id = "emote-punkguitar"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "ولكم" in message:
      try:
        emote_id = "emote-bow"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    

    if "Sad" in message:
      try:
        emote_id = "emote-sad"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "Shy" in message:
      try:
        emote_id = "emote-shy2"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if message.startswith("sword"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("emote-swordfight", roomUser.id)

    if message.startswith("singing"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("idle_singing", roomUser.id)

    if message.startswith("guitar"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("emote-punkguitar", roomUser.id)

    

    if message.startswith("float"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("emote-float", roomUser.id)

    if message.startswith("snowangel"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("emote-snowangel", roomUser.id)

    if message.startswith("snowball"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("emote-snowball", roomUser.id)

    if message.startswith("teleporting"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("emote-teleporting", roomUser.id)

    if message.startswith("wise"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("dance-pennywise", roomUser.id)

    if message.startswith("fashionista"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("emote-fashionista", roomUser.id)

    if message.startswith("kpop"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("dance-blackpink", roomUser.id)

    if message.startswith("virgal"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("dance-tiktok9", roomUser.id)

    if message.startswith("sit"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("idle-loop-sitfloor", roomUser.id)

    if message.startswith("snake"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("emote-snake", roomUser.id)

    if message.startswith("icecream"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("dance-icecream", roomUser.id)

    if message.startswith("laughing"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("emote-laughing", roomUser.id)


    if message.startswith("shoppingchart"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("dance-shoppingcart", roomUser.id)

    if message.startswith("russian"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("dance-russian", roomUser.id)

    if message.startswith("kiss"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
         await self.highrise.send_emote("emote-kiss", roomUser.id)

    if message.startswith("blush"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("emote-shy2", roomUser.id)

    if message.startswith("enthused"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("idle-enthusiastic", roomUser.id)

    if message.startswith("zombierun"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("emote-zombierun", roomUser.id)

    if message.startswith("frog"):
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("emote-frog", roomUser.id)

    if message.startswith("cüzdan"):
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.chat(f"Bot cüzdanı şunları içerir: {wallet[0].amount} {wallet[0].type}")

    if message.startswith("users"):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"There are {len(room_users)} users in the room")

    if message.lower().startswith("/getoutfit"):
            response = await self.highrise.get_my_outfit()
            for item in response.outfit:
                await self.highrise.chat(item.id)

  async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:
    response = await self.highrise.get_messages(conversation_id)
    if isinstance(response, GetMessagesRequest.GetMessagesResponse):
        message = response.messages[0].content
    print (message)
    if message == "You got a tip!":
        await self.highrise.send_message(conversation_id, "tysm for tip i wish you enjoy in this party🎃")



  async def grant_gold_to_all(self, amount):
          bot_wallet = await self.highrise.get_wallet()
          bot_amount = bot_wallet.content[0].amount
          response = await self.highrise.get_room_users()
          num_users = len(response.content)
          total_gold = amount * num_users
          if bot_amount >= total_gold:
              for content in response.content:
                  user_id = content[0].id
                  await self.highrise.tip_user(user_id, f"gold.{amount}")
          else:
              await self.highrise.chat("herkeze yeterince altın yok")



if __name__ == "__main__":
  room_id = "64e99ff81188da64f8889bfa"
  token = "01b50864d754b0b8522967751d2b34d252b2e8bcc065ef7327b70dfb9d14aaa6"
  arun(MyBot().run(room_id, token))
