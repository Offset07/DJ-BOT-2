from highrise import *
from highrise.models import *
import asyncio
from asyncio import Task

emote_list : list[tuple[str, str]] = [('Rest', 'sit-idle-cute'), ('Zombie', 'idle_zombie'), ('Relaxed', 'idle_layingdown2'), ('Attentive', 'idle_layingdown'), ('Sleepy', 'idle-sleep'), ('Pouty Face', 'idle-sad'), ('Posh', 'idle-posh'), ('Sleepy', 'idle-loop-tired'), ('Tap Loop', 'idle-loop-tapdance'), ('Sit', 'idle-loop-sitfloor'), ('Shy', 'idle-loop-shy'), ('Bummed', 'idle-loop-sad'), ("Chillin'", 'idle-loop-happy'), ('Annoyed', 'idle-loop-annoyed'), ('Aerobics', 'idle-loop-aerobics'), ('Ponder', 'idle-lookup'), ('Hero Pose', 'idle-hero'), ('Relaxing', 'idle-floorsleeping2'), ('Cozy Nap', 'idle-floorsleeping'), ('Enthused', 'idle-enthusiastic'), ('Boogie Swing', 'idle-dance-swinging'), ('Feel The Beat', 'idle-dance-headbobbing'), ('Irritated', 'idle-angry'), ('Yes', 'emote-yes'), ('I Believe I Can Fly', 'emote-wings'), ('The Wave', 'emote-wave'), ('Tired', 'emote-tired'), ('Think', 'emote-think'), ('Theatrical', 'emote-theatrical'), ('Tap Dance', 'emote-tapdance'), ('Super Run', 'emote-superrun'), ('Super Punch', 'emote-superpunch'), ('Sumo Fight', 'emote-sumo'), ('Thumb Suck', 'emote-suckthumb'), ('Splits Drop', 'emote-splitsdrop'), ('Snowball Fight!', 'emote-snowball'), ('Snow Angel', 'emote-snowangel'), ('Shy', 'emote-shy'), ('Secret Handshake', 'emote-secrethandshake'), ('Sad', 'emote-sad'), ('Rope Pull', 'emote-ropepull'), ('Roll', 'emote-roll'), ('ROFL!', 'emote-rofl'), ('Robot', 'emote-robot'), ('Rainbow', 'emote-rainbow'), ('Proposing', 'emote-proposing'), ('Peekaboo!', 'emote-peekaboo'), ('Peace', 'emote-peace'), ('Panic', 'emote-panic'), ('No', 'emote-no'), ('Ninja Run', 'emote-ninjarun'), ('Night Fever', 'emote-nightfever'), ('Monster Fail', 'emote-monster_fail'), ('Model', 'emote-model'), ('Flirty Wave', 'emote-lust'), ('Level Up!', 'emote-levelup'), ('Amused', 'emote-laughing2'), ('Laugh', 'emote-laughing'), ('Kiss', 'emote-kiss'), ('Super Kick', 'emote-kicking'), ('Jump', 'emote-jumpb'), ('Judo Chop', 'emote-judochop'), ('Imaginary Jetpack', 'emote-jetpack'), ('Hug Yourself', 'emote-hugyourself'), ('Sweating', 'emote-hot'), ('Hero Entrance', 'emote-hero'), ('Hello', 'emote-hello'), ('Headball', 'emote-headball'), ('Harlem Shake', 'emote-harlemshake'), ('Happy', 'emote-happy'), ('Handstand', 'emote-handstand'), ('Greedy Emote', 'emote-greedy'), ('Graceful', 'emote-graceful'), ('Moonwalk', 'emote-gordonshuffle'), ('Ghost Float', 'emote-ghost-idle'), ('Gangnam Style', 'emote-gangnam'), ('Frolic ', 'emote-frollicking'), ('Faint', 'emote-fainting'), ('Clumsy', 'emote-fail2'), ('Fall', 'emote-fail1'), ('Face Palm', 'emote-exasperatedb'), ('Exasperated', 'emote-exasperated'), ('Elbow Bump', 'emote-elbowbump'), ('Disco', 'emote-disco'), ('Blast Off', 'emote-disappear'), ('Faint Drop', 'emote-deathdrop'), ('Collapse', 'emote-death2'), ('Revival', 'emote-death'), ('Dab', 'emote-dab'), ('Curtsy', 'emote-curtsy'), ('Confusion', 'emote-confused'), ('Cold', 'emote-cold'), ('Charging', 'emote-charging'), ('Bunny Hop', 'emote-bunnyhop'), ('Bow', 'emote-bow'), ('Boo', 'emote-boo'), ('Home Run!', 'emote-baseball'), ('Falling Apart', 'emote-apart'), ('Thumbs Up', 'emoji-thumbsup'), ('Point', 'emoji-there'), ('Sneeze', 'emoji-sneeze'), ('Smirk', 'emoji-smirking'), ('Sick', 'emoji-sick'), ('Gasp', 'emoji-scared'), ('Punch', 'emoji-punch'), ('Pray', 'emoji-pray'), ('Stinky', 'emoji-poop'), ('Naughty', 'emoji-naughty'), ('Mind Blown', 'emoji-mind-blown'), ('Lying', 'emoji-lying'), ('Levitate', 'emoji-halo'), ('Fireball Lunge', 'emoji-hadoken'), ('Give Up', 'emoji-give-up'), ('Tummy Ache', 'emoji-gagging'), ('Flex', 'emoji-flex'), ('Stunned', 'emoji-dizzy'), ('Cursing Emote', 'emoji-cursing'), ('Sob', 'emoji-crying'), ('Clap', 'emoji-clapping'), ('Raise The Roof', 'emoji-celebrate'), ('Arrogance', 'emoji-arrogance'), ('Angry', 'emoji-angry'), ('Vogue Hands', 'dance-voguehands'), ('Savage Dance', 'dance-tiktok8'), ("Don't Start Now", 'dance-tiktok2'), ('Yoga Flow', 'dance-spiritual'), ('Smoothwalk', 'dance-smoothwalk'), ('Ring on It', 'dance-singleladies'), ("Let's Go Shopping", 'dance-shoppingcart'), ('Russian Dance', 'dance-russian'), ('Robotic', 'dance-robotic'), ("Penny's Dance", 'dance-pennywise'), ('Orange Juice Dance', 'dance-orangejustice'), ('Rock Out', 'dance-metal'), ('Karate', 'dance-martial-artist'), ('Macarena', 'dance-macarena'), ('Hands in the Air', 'dance-handsup'), ('Floss', 'dance-floss'), ('Duck Walk', 'dance-duckwalk'), ('Breakdance', 'dance-breakdance'), ('K-Pop Dance', 'dance-blackpink'), ('Push Ups', 'dance-aerobics')]

async def loop(self: BaseBot, user: User, message: str) -> None:
    # Defining the loop_emote method locally so it cann't be accessed from the command handler.
    async def loop_emote(self: BaseBot, user: User, emote_name: str) -> None:
        emote_id = "loop"
        for emote in emote_list:
            if emote[0].lower() == emote_name.lower():
                emote_id = emote[1]
                break
        if emote_id == "dance-blackpink":
            await self.highrise.chat("Invalid emote")
            return
        user_position = None
        user_in_room = False
        room_users = (await self.highrise.get_room_users()).content
        for room_user, position in room_users:
            if room_user.id == user.id:
                user_position = position
                start_position = position
                user_in_room = True
                break
        if user_position == None:
            await self.highrise.chat("User not found")
            return
        await self.highrise.chat(f"@{user.username} is looping {emote_name}")
        while start_position == user_position:
            try:
                await self.highrise.send_emote(emote_id, user.id)
            except:
                await self.highrise.chat(f"Sorry, @{user.username}, this emote isn't free or you don't own it.")
                return
            await asyncio.sleep(10)
            room_users = (await self.highrise.get_room_users()).content
            user_in_room = False
            for room_user, position in room_users:
                if room_user.id == user.id:
                    user_position = position
                    user_in_room = True
                    break
            if user_in_room == False:
                break
    try:
        splited_message = message.split(" ")
        # The emote name is every string after the first one
        emote_name = " ".join(splited_message[1:])
    except:
        await self.highrise.chat("Invalid command format. Please use '/loop <emote name>.")
        return
    else:   
        taskgroup = self.highrise.tg
        task_list : list[Task] = list(taskgroup._tasks)
        for task in task_list:
            if task.get_name() == user.username:
                # Removes the task from the task group
                task.cancel()

        room_users = (await self.highrise.get_room_users()).content
        user_list  = []
        for room_user, pos in room_users:
            user_list.append(room_user.username)

        taskgroup.create_task(coro=loop_emote(self, user, emote_name))
        task_list : list[Task] = list(taskgroup._tasks)
        for task in task_list:
            if task.get_coro().__name__ == "loop_emote" and not (task.get_name() in user_list):
                task.set_name(user.username)

async def stop_loop(self: BaseBot, user: User, message: str) -> None:
        taskgroup = self.highrise.tg
        task_list : list[Task] = list(taskgroup._tasks)
        for task in task_list:
            print(task.get_name())
            if task.get_name() == user.username:
                task.cancel()
                await self.highrise.chat(f"Stopping your emote loop, {user.username}!")
                return
        await self.highrise.chat(f"You're not looping any emotes, {user.username}")
        return