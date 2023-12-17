from ctypes import resize
from xml.sax.handler import feature_validation
from config import TOKEN
from aiogram import Bot, types
from aiogram.types import ContentType,InputFile
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import pyttsx3
import time
from create_bot import *
import torch
import soundfile as sf


class StateF(StatesGroup):
	nazGolos = State()

async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, "Привет! Я бот ConventorX.\n\
			 Я умею переносить твои сообщение в голос 📃 ==> 🔊 \n\
			 Отправь мне любое сообщение!\n\
			 \n\
			 Контакты: @r00ty0u")
		await message.delete()
	except:
		await message.reply("❗Ошибка. Попробуй еще раз❗")



async def voice_send(message : types.Message):
		global slovo
		slovo = str(message.text)
		kb = [
        [
            types.KeyboardButton(text="Elena"),
            types.KeyboardButton(text="Irina"),
	    	types.KeyboardButton(text="Aidar"),
		    types.KeyboardButton(text="Baya"),
		    types.KeyboardButton(text="Ksenia"),
		    types.KeyboardButton(text="Xenia"),
		    types.KeyboardButton(text="Eugene"),
		    types.KeyboardButton(text="Random"),
		    

        ],
   		 ]
		keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=False,
        input_field_placeholder="Голос"
		)
		await message.answer("Выбери кто будет озвучивать твой текст", reply_markup=keyboard)
		await StateF.nazGolos.set()


async def voice_dev(message : types.Message,state: FSMContext):
		await state.update_data(
            {
                    'item': message.text
            }
        	)
		duration = str(message.text)
		
		
		
		# if duration.lower() != 'aidar' and duration.lower() != 'baya' and duration.lower() != 'ksenia' and duration.lower() != 'xenia' and duration.lower() != 'eugene' and duration.lower() != 'random':   
		if duration == 'Elena' or duration == 'Irina':
			engine = pyttsx3.init()
			if duration == 'Elena': 
				engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ru-RU_Elena_11.0")
			elif duration == 'Irina':
				engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0")

			engine.save_to_file(slovo, 'convert.ogg')
			print(slovo)
			engine.runAndWait()
			markup = types.ReplyKeyboardRemove()
			msg = await bot.send_message(message.from_user.id, "[➕] Сейчас сделаю",reply_markup=markup)

			time.sleep(5)
			await msg.delete()
			await bot.send_voice(message.from_user.id,(open('convert.ogg', 'rb')))
			os.remove('convert.ogg')
			await state.finish()
			

		elif duration.lower() == 'aidar' or duration.lower() == 'baya' or duration.lower() == 'ksenia' or duration.lower() == 'xenia' or duration.lower() == 'eugene' or duration.lower() == 'random':   
			print(slovo)
			markup = types.ReplyKeyboardRemove()
			msg = await bot.send_message(message.from_user.id, "[➕] Сейчас сделаю",reply_markup=markup)
			device = torch.device('cpu')
			torch.set_num_threads(4)
			local_file = 'model.pt'
			if not os.path.isfile(local_file):
				torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',local_file)  
			model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
			model.to(device)
			sample_rate = 48000
			speaker=duration.lower()

			audio_paths = model.save_wav(text=slovo,
                             speaker=speaker,
                             sample_rate=sample_rate)

			data, samplerate = sf.read('test.wav')
			sf.write('convert.ogg', data, samplerate)
			await msg.delete()
			await bot.send_voice(message.from_user.id,(open('convert.ogg', 'rb')))
			os.remove('test.wav')
			os.remove('convert.ogg')
			await state.finish()


def funct(dp : Dispatcher):
	dp.register_message_handler(command_start,commands=['start'])
	dp.register_message_handler(voice_send)
	dp.register_message_handler(voice_dev,state=StateF.nazGolos)




		# # if duration.lower() != 'aidar' and duration.lower() != 'baya' and duration.lower() != 'ksenia' and duration.lower() != 'xenia' and duration.lower() != 'eugene' and duration.lower() != 'random':   
		# if duration == 'Elena' or duration == 'Irina':
		# 	engine = pyttsx3.init()
		# 	if duration == 'Elena': 
		# 		engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ru-RU_Elena_11.0")
		# 	elif duration == 'Irina':
		# 		engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0")

		# 	engine.save_to_file(slovo, 'convert.ogg')
		# 	print(slovo)
		# 	engine.runAndWait()
		# 	markup = types.ReplyKeyboardRemove()
		# 	msg = await bot.send_message(call.message.from_user.id, "[➕] Сейчас сделаю",reply_markup=markup)

		# 	time.sleep(5)
		# 	await msg.delete()
		# 	await bot.send_voice(call.message.from_user.id,(open('convert.ogg', 'rb')))
		# 	os.remove('convert.ogg')

			

		# elif duration.lower() == 'aidar' or duration.lower() == 'baya' or duration.lower() == 'ksenia' or duration.lower() == 'xenia' or duration.lower() == 'eugene' or duration.lower() == 'random':   
		# 	print(slovo)
		# 	msg = await bot.send_message(call.message.from_user.id, "[➕] Сейчас сделаю")
			
		# 	if not os.path.isfile(local_file):
		# 		torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',local_file)  
			
		# 	speaker=duration.lower()

		# 	audio_paths = model.save_wav(text=slovo,
        #                      speaker=speaker,
        #                      sample_rate=sample_rate)

		# 	data, samplerate = sf.read('test.wav')
		# 	sf.write('convert.ogg', data, samplerate)
		# 	await msg.delete()
		# 	await bot.send_voice(call.message.from_user.id,(open('convert.ogg', 'rb')))
		# 	os.remove('test.wav')
		# 	os.remove('convert.ogg')













	