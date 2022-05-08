import re
from STT import *
from TTS import *
import sys
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # General Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo',"hai"], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love','like','admire', 'code', 'clause'], required_words=['code', 'clause','love'or'admire'or'like'])
    response('You are a CodeClause Client', ['who', 'am','I'], single_response=True,required_words=['who','I'])

    # Longer responses servicess tab of website
    response('I am a CodeClause Chatbot', ['who', 'are','you'], single_response=True,required_words=['who'])
    response('Transform the way your business makes decisions. Explore our services and solutions designed to help you realize the full potential of your data so you can put it to work for you.', ['what', 'in','data','and','analytics','provide'], single_response=True)
    response('Compete better, reduce time to market, and improve customer experience with our Intelligent Automation solutions and services, accelerators, and frameworks.', ['what', 'in','ai','and','automation','provide'], single_response=True)
    response('CodeClause helps enterprises connect and monitor devices, secure and automate operations, and compute and manage data.', ['what', 'in','internet','of','things','iot'], single_response=True)
    response('We successfully deliver the customized software\'s for our clients based on their business requirements and it has really helped them to smooth their execution process and have a proper track of their implementation process within their organization.',['what', 'in','software','development'],single_response=True)
    response('We at CodeClause, being the best web design company, consists of a team of dedicated and passionate people who develop flawless websites to full fill your business requirements.',['what', 'in','web','development'],single_response=True,required_words=['web'])
    response('We strengthen your business with the features of rich native or diverse applications and deliver the best user-friendly experience that makes us one of the best mobile app development company.',['what', 'in','app','development'],single_response=True,required_words=['app'])
    response('We help our clients to stand in front of world by Search Engine Optimization(SEO).',['what', 'in','search','engine','optimization','seo'],single_response=True)
    response('We will deploy the clients software securely on the server and maintenance of it.',['what', 'in','web','hosting','&','maintenance'],single_response=True)
    response('Our Creative Designers Offer Outstanding And Attention-Grabbing Visuals For Brochures, Banners, Flyers, Logos, Business Cards, E-Books, And Many More.',['what', 'in','graphic','design'],single_response=True)
    response('Here at CodeClause we offer services like Data & Analytics,Automation AI,Internet of Things,Software Development,Web Development,App Development,Search Engine Optimization,Web Hosting & Maintenance and Graphic Design', ['what', 'services','you','offer'], single_response=True,required_words=['services','offer' or 'provide'])
    
    #contact page
    response('Contact us at info@codeclause.com',['contact','information','how','should','I','codeclause'],single_response=True,required_words=['contact'])
    
    
    #about us page
    response('At CodeClause, We “Strive with Technology” to provide the most effective and affordable service that fulfills our customer’s needs and budget. We provide customized websites and software solutions that suit customer’s company objectives. We always keep involving our customers in an entire process starting from design through deployment, so that your ideas can be incorporated into our work.',['why','choose','us'],single_response=True)
    response('Be passionate about clients success, Be global and responsible,Treat each person with respect,Unyielding integrity in everything we do',['spirit','of','code','clause'],single_response=True,required_words=['spirit'])
    
    #careers page
    
    
    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    tts(response)
    return response


while True:
    print("You : ",end="")
    ans=get_response(stt())
    if ans=='See you!':
        print('Bot: ' +ans)
        break
    else:
        print('Bot: ' +ans)
    # print('Bot: ' + get_response(input('You: ')))