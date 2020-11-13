#Пример общения с ботом


import telebot
import parser
import requests
from bs4 import BeautifulSoup


URL = 'https://iptvcat.com/'
news = []
new_news = []
findlinks = []
links = []

#datalist = open('datalist.txt','w')
#datalist.write("1")
#datalist.close


#response = requests.get(URL)
#b = response.text

#soup = BeautifulSoup(b, 'lxml')
#bc = soup.head.text

#news = soup.findAll('span', class_='channel_name')

#for i in range(len(news)):
#   if news[i].find('span', class_='channel_name') is not None:
   #     new_news.append(news[i].text)


#for i in range(len(news)):
 #   print(news[i].text)


#main variables
    
 #Токен нашего бота выдает Bot_father
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, я iptv streams hub bot. Введи название канала и я найду доступные потоки или напиши /help, что бы узнать что я еще умею. ')

helpik = [
    'Текущая версия: 1.1',
    'Вот что я умею на данный момент:',
    'Поиск канала по названию',
    'Дальше больше, оставайся со мной. ',
    'Если у вас есть вопросы, задай их в чате поддержки: @iptvstreamshub_support'
]


@bot.message_handler(commands=['info','help','помощь','инструкция'])
def start_handler(message):
    for i in range(len(helpik)):
        bot.send_message(message.chat.id,str(helpik[i]))
    


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    
    if text == 'привет':
        bot.send_message(message.chat.id, 'Привет, я iptv streams hub bot. Введи название канала и я найду доступные потоки или напиши /help, что бы узнать что я еще умею. ')

    elif text == "как дела?":
        bot.send_message(chat_id, 'Хорошо. Тружусь. Ищу потоки нужных пользователю каналов. Введи название канала и я найду доступные для него ссылки')

    else:
        response = requests.get(URL + str('/s/')+ str(text))
        y = response.text
        soup = BeautifulSoup(y, 'lxml')

        findlinks = soup.findAll('span', class_='label label-flat border-info text-info-600 get_vlc')
        uy = str(findlinks)

        if uy.find(':iptvcat.com') > 1:
            print(text)
            #datalist = open('datalist.txt','r')
            #k = (datalist.read())
            #kt = int(k) 
            #kk = 1
            #kkk = str(kt + kk) 
            #datalist.close
            #datalist = open('datalist.txt','w')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
            #datalist.write(kkk)
            #datalist.close
            
            h = []

            for i in range(len(findlinks)):
                ss = str(findlinks[i])
                start = ss.find("http:")
                endd = ss.find(":iptvcat.com")
            
                if endd < 1:
                    endd = len(ss)
                h.append(ss[start:endd])
                link = str(ss[start:endd])
        
        
            for i in range(len(h)):
                if h[i] != "":
                    bot.send_message(chat_id, str(h[i]))
                #f = str(h[i])
                #fayl.writewritelines("#EXTINF:-1,")
                #fayl.writewritelines(f)

            bot.send_message(chat_id, 'Всего найденно ссылок: ' + str(len(h)))
        else:
             bot.send_message(chat_id, "Упс! Ничего не удалось найти. Возможно я еще молод и глуп, а возможно вы написали название канала неверно. Пожалуйста проверте правильность или введите название другово канала. Введи /info и узнай обо мне больше.")

        #bot.send_document(chat_id, fayl)

print("Бот запущен")
bot.polling()