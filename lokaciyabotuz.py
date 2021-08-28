import telebot 
 
from telebot import types
 
from geopy.geocoders import Nominatim 
 
get_number = types.ReplyKeyboardMarkup(resize_keyboard=True) 
get_number.add(types.KeyboardButton('Локацияны жибериү✅',request_location=True)) 
 
bot = telebot.TeleBot("1859117618:AAHYFw0Iv_-mhFDgLkH_ZLrg51yRteSw6HM") 
 
@bot.message_handler(commands=['start']) 
def welcome(message): 
    bot.send_message(message.chat.id,'Ассалаума Алейкум!\nЖайласқан орныңыз ҳаққында билмекши болсаңыз, "Локацияны жибериү✅" түймесин басың!',reply_markup=get_number) 
    bot.register_next_step_handler(message,get_number_function) 
 
def get_number_function(message): 
    if message.location is None: 
        bot.send_message(message.chat.id, "Илтимас, түймени басың!",reply_markup=get_number) 
        bot.register_next_step_handler(message,get_number_function) 
    else: 
        geolocator = Nominatim(user_agent="geoapiExercises")  
        location = geolocator.geocode(str(message.location.latitude)+","+str(message.location.longitude))  
        bot.send_message(message.chat.id, f"🗺Сиздиң жайласқан орныңыз ҳаққында мағлыумат: {location}") 
 
bot.polling()