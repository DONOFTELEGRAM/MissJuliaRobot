# MADE BY @MissAlexa_Robot
# He has wasted a lot of time of his life to make this so please give proper credits to him 😭

from telethon import *
from telethon.tl import *
from alexa.events import register
from pymongo import MongoClient
from alexa import MONGO_DB_URI
from alexa.events import register
from alexa import tbot


client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client['test']
approved_users = db.approve
dbb = client['poll']
poll_id = dbb.pollid

#------ THANKS TO LONAMI ------#
async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (await tbot(functions.channels.GetParticipantRequest(chat, user))).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator)
        )
    elif isinstance(chat, types.InputPeerChat):
        ui = await tbot.get_peer_id(user)
        ps = (await tbot(functions.messages.GetFullChatRequest(chat.chat_id))) \
            .full_chat.participants.participants
        return isinstance(
            next((p for p in ps if p.user_id == ui), None),
            (types.ChatParticipantAdmin, types.ChatParticipantCreator)
        )
    else:
        return None

# syntax : /poll 12345 | am i cool? | False False False yes no
# syntax : /poll 12345 | am i cool? | True@1 False False yes no
@register(pattern="^/poll (.*)")
async def _(event):
    approved_userss = approved_users.find({})
    for ch in approved_userss: 
        iid = ch['id']
        userss = ch['user']
    if event.is_group:
     if (await is_register_admin(event.input_chat, event.message.sender_id)):
       pass
     elif event.chat_id == iid and event.from_id == userss:  
       pass
     else:
       return
    try: 
      quew= event.pattern_match.group(1)
    except Exception:
       await event.reply("Where is the question ?")
       return
    if "|" in quew:
         secrets, quess, options = quew.split("|")
    secret = secrets.strip()
    
    if not secret:
        await event.reply("I need a poll id of 5 digits to make a poll")
        return

    try:
      secret = int(secret)
    except ValueError:
      await event.reply("Poll id should contain only numbers")
      return

    count=0
    while(int(secret)>0):
      count=count+1
      secret=int(secret)//10

    if count != 5:
        await event.reply("Poll id should be an integer of 5 digits")
        return
  
    allpoll = poll_id.find({})
    for c in allpoll:
      if event.from_id == c['user'] and secret == c['pollid']:
          await event.reply("Please give another poll id, this id is already used")
          return
      poll_id.insert_one({'user':event.from_id,'pollid':secret})
    
    ques = quess.strip()
    option = options.strip()
    quiz = option.split(' ')[1-1] 
    if "True" in quiz:
       quizy = True
       if "@" in quiz:
          one, two = quiz.split("@")
          rightone = two.strip()
       else:
          await event.reply("You need to select the right answer with question number like True@1, True@3 etc..")
          return          

       quizoptionss = []
       try: 
         ab = option.split(' ')[4-1] 
         cd = option.split(' ')[5-1] 
         quizoptionss.append(types.PollAnswer(ab, b'1'))
         quizoptionss.append(types.PollAnswer(cd, b'2'))
       except Exception:
         await event.reply("At least need two options to create a poll")
         return
       try:
         ef = option.split(' ')[6-1] 
         quizoptionss.append(types.PollAnswer(ef, b'3'))
       except Exception:
         ef = None        
       try:
         gh = option.split(' ')[7-1] 
         quizoptionss.append(types.PollAnswer(gh, b'4'))
       except Exception:
         gh = None  
       try:
         ij = option.split(' ')[8-1] 
         quizoptionss.append(types.PollAnswer(ij, b'5'))
       except Exception:
         ij = None
       try:
         kl = option.split(' ')[9-1] 
         quizoptionss.append(types.PollAnswer(kl, b'6'))
       except Exception:
         kl = None
       try:
         mn = option.split(' ')[10-1] 
         quizoptionss.append(types.PollAnswer(mn, b'7'))
       except Exception:
         mn = None        
       try:
         op = option.split(' ')[11-1] 
         quizoptionss.append(types.PollAnswer(op, b'8'))
       except Exception:
         op = None   
       try:
         qr = option.split(' ')[12-1] 
         quizoptionss.append(types.PollAnswer(qr, b'9'))
       except Exception:
         qr= None   
       try:
         st = option.split(' ')[13-1] 
         quizoptionss.append(types.PollAnswer(st, b'10'))
       except Exception:
         st = None   
         
    elif "False" in quiz:
       quizy = False
    else:
       await event.reply("Wrong arguments provided !")
       return
       
    pvote = option.split(' ')[2-1] 
    if "True" in pvote:
       pvoty = True
    elif "False" in pvote:
       pvoty = False
    else:
       await event.reply("Wrong arguments provided !")
       return
    mchoice = option.split(' ')[3-1] 
    if "True" in mchoice:
       mchoicee = True
    elif "False" in mchoice:
       mchoicee = False
    else:
       await event.reply("Wrong arguments provided !")
       return
    optionss = []
    try: 
      ab = option.split(' ')[4-1] 
      cd = option.split(' ')[5-1] 
      optionss.append(types.PollAnswer(ab, b'1'))
      optionss.append(types.PollAnswer(cd, b'2'))
    except Exception:
      await event.reply("At least need two options to create a poll")
      return
    try:
      ef = option.split(' ')[6-1] 
      optionss.append(types.PollAnswer(ef, b'3'))
    except Exception:
      ef = None     
    try:
      gh = option.split(' ')[7-1] 
      optionss.append(types.PollAnswer(gh, b'4'))
    except Exception:
      gh = None  
    try:
      ij = option.split(' ')[8-1] 
      optionss.append(types.PollAnswer(ij, b'5'))
    except Exception:
      ij = None
    try:
      kl = option.split(' ')[9-1] 
      optionss.append(types.PollAnswer(kl, b'6'))
    except Exception:
      kl = None
    try:
      mn = option.split(' ')[10-1] 
      optionss.append(types.PollAnswer(mn, b'7'))
    except Exception:
      mn = None     
    try:
      op = option.split(' ')[11-1] 
      optionss.append(types.PollAnswer(op, b'8'))
    except Exception:
      op = None   
    try:
      qr = option.split(' ')[12-1] 
      optionss.append(types.PollAnswer(qr, b'9'))
    except Exception:
      qr= None   
    try:
      st = option.split(' ')[13-1] 
      optionss.append(types.PollAnswer(st, b'10'))
    except Exception:
      st = None   
  
    if pvoty==False and quizy==False and mchoicee==False:      
     await tbot.send_file(event.chat_id, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=optionss,
        quiz=False)))

      
    if pvoty==True and quizy==False and mchoicee==True:      
     await tbot.send_file(event.chat_id, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=optionss,
        quiz=False,
        multiple_choice=True, 
        public_voters=True)))


    if pvoty==False and quizy==False and mchoicee==True:      
     await tbot.send_file(event.chat_id, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=optionss,
        quiz=False,
        multiple_choice=True, 
        public_voters=False)))
   
 
    if pvoty== True and quizy==False and mchoicee==False:      
     await tbot.send_file(event.chat_id, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=optionss,
        quiz=False,
        multiple_choice=False, 
        public_voters=True)))
            

    if pvoty==False and quizy==True and mchoicee==False:
     await tbot.send_file(event.chat_id, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=quizoptionss,
        quiz=True
    ),
    correct_answers=[f"{rightone}"]))
    
    if pvoty==True and quizy==True and mchoicee==False:
     await tbot.send_file(event.chat_id, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=quizoptionss,
        quiz=True,
        public_voters=True
    ),
    correct_answers=[f"{rightone}"]))
    
    if pvoty==True and quizy==True and mchoicee==True:
       await event.reply("You can't use multiple voting with quiz mode")
       return
    if pvoty==False and quizy==True and mchoicee==True:
       await event.reply("You can't use multiple voting with quiz mode")
       return


@register(pattern="^/stoppoll (.*)")
async def stop(event):
   secret = event.pattern_match.group(1)
   approved_userss = approved_users.find({})
   for ch in approved_userss: 
        iid = ch['id']
        userss = ch['user']
   if event.is_group:
     if (await is_register_admin(event.input_chat, event.message.sender_id)):
       pass
     elif event.chat_id == iid and event.from_id == userss:  
       pass
     else:
       return

   try:
      secret = int(secret)
   except ValueError:
      await event.reply("Poll id should contain only numbers")
      return

   count=0
   while(int(secret)>0):
      count=count+1
      secret=int(secret)//10

   if count != 5:
        await event.reply("Poll id should be an integer of 5 digits")
        return

   if not event.reply_to_msg_id:
     await event.reply("Please reply to a poll to stop it")
     return
   else:
    try:
     msg = await event.get_reply_message()
     print(msg.from_id)
     if not str(msg.from_id) == "PeerUser(user_id=1199522861)":
       await event.reply("I can't do this operation on this poll.\nProbably it's not created by me")     
       return
     if msg.poll:     
      allpoll = poll_id.find({})
      for c in allpoll:
         if not event.from_id == c['user'] and secret == c['pollid']:
            await event.reply("Oops, either you haven't created this poll or you have given wrong poll id")
            return
         poll_id.delete_one({'user':event.from_id,'pollid':secret})     
         pollid = msg.poll.poll.id 
         await msg.edit(file=types.InputMediaPoll(
          poll=types.Poll(
             id=pollid,
             question="",
             answers =[],
             closed=True)))
         await event.reply("Successfully stopped the poll")
     else:
        await event.reply("This isn't a poll")
    except Exception:
       await event.reply("I can't do this operation on this poll.\nProbably it's already closed")     
       return
