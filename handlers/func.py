from ctypes import resize
from xml.sax.handler import feature_validation
from config import * 
from aiogram import Bot, types
from aiogram.types import ContentType,InputFile
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import os
import pyttsx3
import time
from create_bot import *
import torch
import soundfile as sf
from gtts import gTTS
from pydub import AudioSegment
from pydub import effects



class StateFune(StatesGroup):
	CutZ = State()
	SpeedZ = State()
	NormZ = State()
	TonZ = State()


async def command_start(message : types.Message):
	try:
		your_name = message.from_user.username
		await bot.send_message(message.from_user.id, f"Привет, @{your_name}! Я бот ConventorX 🦾" + "\n" + "Я умею переносить твои сообщения в голос 📃 ==> 🔊" + "\n" + "Отправь мне любое сообщение!💬" + "\n" + f"Контакты☎️: {support_name}")
		await message.delete()
	except:
		await message.reply("❗Ошибка. Попробуй еще раз❗")



async def voice_send(message : types.Message):
		global engine 
		global slovo
		global device
		global local_file
		global model
		global sample_rate
		device = torch.device('cpu')
		torch.set_num_threads(4)
		local_file = 'model.pt'
		model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
		model.to(device)
		sample_rate = 48000
		engine = pyttsx3.init()
		slovo = str(message.text).lower()
		print(slovo)
		if slovo != 'редактировать🛠️' and slovo != 'оставить❌':
			kb_inline = InlineKeyboardMarkup(inline_keyboard=[
			[
				InlineKeyboardButton(
					text = 'Elena💻(Windows 10)',
					callback_data ='Elena'
				)

			],
					[
				InlineKeyboardButton(
					text = 'Irina💻(Windows 10)',
					callback_data ='Irina'
				)

			],		[
				InlineKeyboardButton(
					text = 'Aidar♂️',
					callback_data ='Aidar'
				)

			],
					[
				InlineKeyboardButton(
					text = 'Baya♀️',
					callback_data ='Baya'
				)

			],		[
				InlineKeyboardButton(
					text = 'Kseniya♀️',
					callback_data ='Kseniya'
				)

			],		[
				InlineKeyboardButton(
					text = 'Xenia♀️',
					callback_data ='Xenia'
				)

			],		[
				InlineKeyboardButton(
					text = 'Eugene♂️',
					callback_data ='Eugene'
				)

			],	[
				InlineKeyboardButton(
					text = 'Translator👾(Google gTTS)',
					callback_data ='Translator'
				)

			]


			])
			
			await message.answer("Выбери кто будет озвучивать твой текст🗣️:", reply_markup=kb_inline)


async def voice_elena(call:CallbackQuery):
		try:
			engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ru-RU_Elena_11.0")
			engine.save_to_file(slovo, 'convert.wav')
			print(f'logs:{slovo} speaker: elena')
			engine.runAndWait()
			msg = await call.message.answer("[➕] Сейчас сделаю")
			time.sleep(3)
			await msg.delete()
			
			kb = [
        	[types.KeyboardButton(text="Редактировать🛠️")],
        	[types.KeyboardButton(text="Оставить❌")]
    				]
			keyboard = types.ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
			await call.message.reply_voice(open('convert.wav', 'rb'),reply_markup=keyboard)
			
			
		except:
			await msg.delete()
			await call.message.answer("Ошибка:Недопустимые символы или значения❗")

async def voice_irina(call:CallbackQuery):
		try:
			engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0")
			engine.save_to_file(slovo, 'convert.wav')
			print(f'logs:{slovo} speaker: irina')
			engine.runAndWait()
			msg = await call.message.answer("[➕] Сейчас сделаю")
			time.sleep(3)
			await msg.delete()
			kb = [
        	[types.KeyboardButton(text="Редактировать🛠️")],
        	[types.KeyboardButton(text="Оставить❌")]
    				]
			keyboard = types.ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
			await call.message.reply_voice(open('convert.wav', 'rb'),reply_markup=keyboard)
		except:
			
			await msg.delete()
			await call.message.answer("Ошибка:Недопустимые символы или значения❗")

async def voice_aidar(call:CallbackQuery):
			try:
				print(f'logs:{slovo} speaker: aidar')
				msg = await call.message.answer("[➕] Сейчас сделаю")
				
				if not os.path.isfile(local_file):
					torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',local_file)  
				
				speaker='aidar'

				audio_paths = model.save_wav(text=slovo,
								speaker=speaker,
								sample_rate=sample_rate)

				data, samplerate = sf.read('test.wav')
				sf.write('convert.wav', data, samplerate)
				await msg.delete()
				kb = [
        	[types.KeyboardButton(text="Редактировать🛠️")],
        	[types.KeyboardButton(text="Оставить❌")]
    				]
				keyboard = types.ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
				await call.message.reply_voice((open('convert.wav', 'rb')), reply_markup=keyboard)
				os.remove('test.wav')
			except:
				await msg.delete()
				await call.message.answer("Ошибка:Недопустимые символы или значения❗")
async def voice_baya(call:CallbackQuery):
			try:
				print(f'logs:{slovo} speaker: baya')
				msg = await call.message.answer("[➕] Сейчас сделаю")
				
				if not os.path.isfile(local_file):
					torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',local_file)  
				
				speaker='baya'

				audio_paths = model.save_wav(text=slovo,
								speaker=speaker,
								sample_rate=sample_rate)

				data, samplerate = sf.read('test.wav')
				sf.write('convert.wav', data, samplerate)
				await msg.delete()
				kb = [
        	[types.KeyboardButton(text="Редактировать🛠️")],
        	[types.KeyboardButton(text="Оставить❌")]
    				]
				keyboard = types.ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
				await call.message.reply_voice((open('convert.wav', 'rb')),reply_markup=keyboard)
				os.remove('test.wav')
			except:
				await msg.delete()
				await call.message.answer("Ошибка:Недопустимые символы или значения❗")
async def voice_kseniya(call:CallbackQuery):
			try:
				print(f'logs:{slovo} speaker: kseniya')
				msg = await call.message.answer("[➕] Сейчас сделаю")
				
				if not os.path.isfile(local_file):
					torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',local_file)  
				
				speaker='kseniya'

				audio_paths = model.save_wav(text=slovo,
								speaker=speaker,
								sample_rate=sample_rate)

				data, samplerate = sf.read('test.wav')
				sf.write('convert.wav', data, samplerate)
				await msg.delete()
				kb = [
        	[types.KeyboardButton(text="Редактировать🛠️")],
        	[types.KeyboardButton(text="Оставить❌")]
    				]
				keyboard = types.ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
				await call.message.reply_voice((open('convert.wav', 'rb')),reply_markup=keyboard)
				os.remove('test.wav')
			except:
				await msg.delete()
				await call.message.answer("Ошибка:Недопустимые символы или значения❗")
async def voice_xenia(call:CallbackQuery):
			try:
				print(f'logs:{slovo} speaker: xenia')
				msg = await call.message.answer("[➕] Сейчас сделаю")
				
				if not os.path.isfile(local_file):
					torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',local_file)  
				
				speaker='xenia'

				audio_paths = model.save_wav(text=slovo,
								speaker=speaker,
								sample_rate=sample_rate)

				data, samplerate = sf.read('test.wav')
				sf.write('convert.wav', data, samplerate)
				await msg.delete()
				kb = [
        	[types.KeyboardButton(text="Редактировать🛠️")],
        	[types.KeyboardButton(text="Оставить❌")]
    				]
				keyboard = types.ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
				await call.message.reply_voice((open('convert.wav', 'rb')),reply_markup=keyboard)
				os.remove('test.wav')
			except:
				await msg.delete()
				await call.message.answer("Ошибка:Недопустимые символы или значения❗")
async def voice_eugene(call:CallbackQuery):
			try:
				print(f'logs:{slovo} speaker: eugene')
				msg = await call.message.answer("[➕] Сейчас сделаю")
				
				if not os.path.isfile(local_file):
					torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',local_file)  
				
				speaker='eugene'

				audio_paths = model.save_wav(text=slovo,
								speaker=speaker,
								sample_rate=sample_rate)

				data, samplerate = sf.read('test.wav')
				sf.write('convert.wav', data, samplerate)
				await msg.delete()
				kb = [
        	[types.KeyboardButton(text="Редактировать🛠️")],
        	[types.KeyboardButton(text="Оставить❌")]
    				]
				keyboard = types.ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
				await call.message.reply_voice((open('convert.wav', 'rb')),reply_markup=keyboard)
				os.remove('test.wav')
			except:
				await msg.delete()
				await call.message.answer("Ошибка:Недопустимые символы или значения❗")
		
async def voice_translator(call:CallbackQuery):	
		try:
			print(f'logs:{slovo} speaker: translator')
			msg = await call.message.answer("[➕] Сейчас сделаю")
			s = gTTS(text=slovo,lang='ru',slow=False)
			s.save('convert.wav')
			time.sleep(3)
			await msg.delete()
			await call.message.reply_voice((open('convert.wav', 'rb')))
			os.remove('convert.wav')

		except:
			await msg.delete()
			await call.message.answer("Ошибка:Недопустимые символы или значения❗")
		
		
async def finish(message : types.Message):
	await message.delete()
	os.remove('convert.wav')
	msg = await message.answer(f"Ok",reply_markup=types.ReplyKeyboardRemove())
	await msg.delete()
	

async def perf(message : types.Message):
	
	await bot.send_message(message.from_user.id, f"<b>Обрезка аудио</b>"+"\n\
						"+"Введи начала и конец записи в секундах."+"\n\
						"+"Пример: 1:30 - 2:30 , надо ввести 90:150 ",reply_markup=types.ReplyKeyboardRemove(),parse_mode="HTML")
	await StateFune.CutZ.set()
async def perf_cut_dev(message : types.Message,state: FSMContext):
	await state.update_data(
            {
                    'item': message.text
            }
        	)
	try:
		duration = message.text
		global StartT 
		global StopT 
		StartT = int(message.text.split(':')[0])*1000
		StopT = int(message.text.split(':')[1])*1000
		print(StartT,StopT)
		song = AudioSegment.from_wav("convert.wav")
		cutS = song[StartT:StopT]
		cutS.export('convert.wav',format='wav')
		kb = [
				[types.KeyboardButton(text="1")]
						]
		keyboard = types.ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
		await bot.send_message(message.from_user.id, f"<b>Изменение скорости</b>"+"\n\
						 "+"Введи значение скорости(больше или равное 1)."+"\n\
							"+"Пример: 1.5 "+"\n\
								"+"(По умолчанию: 1)",reply_markup=keyboard,parse_mode='HTML')
		await StateFune.SpeedZ.set()
	except:
		await message.answer("Ошибка:Недопустимые символы или значения❗")
async def perf_speedup_dev(message : types.Message,state: FSMContext):
		await state.update_data(
            {
                    'item': message.text
            }
        	)
		if float(message.text)>=1:
			duration = float(message.text) + 0.01
			song = AudioSegment.from_wav("convert.wav")
			speedS = song.speedup(duration, 150, 25)
			speedS.export('convert.wav', format="wav")
			kb = [
        	[types.KeyboardButton(text="+")],
        	[types.KeyboardButton(text="-")]
    				]
			keyboard = types.ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
			await bot.send_message(message.from_user.id, f"<b>Нормализация</b>"+"\n\
						  "+"Нормализовать ваше аудио?"+"\n\
							"+"(+ = Да , - = Нет)",reply_markup=keyboard,parse_mode='HTML')
			await StateFune.NormZ.set()

		else:
			await bot.send_message(message.from_user.id, f"Число должно быть больше или равно 1")
async def perf_normz_dev(message : types.Message,state: FSMContext):
		await state.update_data(
            {
                    'item': message.text
            }
        	)
		if message.text == '+':
			song = AudioSegment.from_wav("convert.wav")
			normzS= effects.normalize(song)
			normzS.export('convert.wav',format='wav')
		kb = [
        	[types.KeyboardButton(text="1")]]
		keyboard = types.ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
		await bot.send_message(message.from_user.id, f"<b>Изменение тональности</b>"+"\n\
						 "+"Введите тональность вашего аудио(от -10 до 10)"+"\n\
							"+"(По умолчанию: 1)",reply_markup=keyboard,parse_mode='HTML')
		await StateFune.TonZ.set()
async def perf_ton_dev(message : types.Message,state: FSMContext):
		await state.update_data(
            {
                    'item': message.text
            }
        	)
		duration = float(message.text)/20
		song = AudioSegment.from_wav("convert.wav")
		new_sample_rate = int(song.frame_rate * (2.0 ** duration))
		hipitch_sound = song._spawn(song.raw_data, overrides={'frame_rate': new_sample_rate})
		hipitch_sound = hipitch_sound.set_frame_rate(44100)

		hipitch_sound.export('convert.wav',format='wav')
		await message.answer_voice((open('convert.wav', 'rb')),reply_markup=types.ReplyKeyboardRemove())
		await state.finish()
		os.remove("convert.wav")



	





async def support_author(message : types.Message):
		try:
			your_name = message.from_user.username
			await bot.send_message(message.from_user.id, f"Спасибо за поддержку, @{your_name} 🍵" + "\n" + "\n" + f"{qiwi}")
			await message.delete()
		except:
			await message.reply("❗Ошибка. Попробуй еще раз❗")

		

	


def funct(dp : Dispatcher):
	dp.register_message_handler(command_start,commands=['start'])
	dp.register_message_handler(finish,text='Оставить❌')
	dp.register_message_handler(perf,text='Редактировать🛠️')
	dp.register_message_handler(perf_cut_dev,state=StateFune.CutZ)
	dp.register_message_handler(perf_speedup_dev,state=StateFune.SpeedZ)
	dp.register_message_handler(perf_normz_dev,state=StateFune.NormZ)
	dp.register_message_handler(perf_ton_dev,state=StateFune.TonZ)



	dp.register_message_handler(support_author,commands=['support_author'])
	dp.register_message_handler(voice_send)
	dp.register_callback_query_handler(voice_elena,text="Elena")
	dp.register_callback_query_handler(voice_irina,text="Irina")
	dp.register_callback_query_handler(voice_aidar,text="Aidar")
	dp.register_callback_query_handler(voice_baya,text="Baya")
	dp.register_callback_query_handler(voice_kseniya,text="Kseniya")
	dp.register_callback_query_handler(voice_xenia,text="Xenia")
	dp.register_callback_query_handler(voice_eugene,text="Eugene")
	dp.register_callback_query_handler(voice_translator,text='Translator')

	


	