'''
    Generate messages by using from some wishing templates and synonyms list
'''
import random

GLOBAL_SYNONYM_DICT = {
    "good" : ['good','great','marvelous','blissful','positive','superb','nice','wonderful','splendid','cheerful','eventful'],
    "morning" : ['morning','aurora','forenoon','sunup','sunrise'],
    "wish" : ['wish','wishing'],
    "hey" : ['hey','hi','hello','howdy','yo','heya'],
    "afternoon" : ['noon','afternoon','day'],
    "evening" : ['evening','sunset','teatime','sundown'],
    "sweet" : ['sweet','beautiful'],
    "night" : ['bedtime','gloom','nighttime','night']
}

DELIMITERS = [':)',':-)',';-)','.','!','!!','','','']


def genMessage(template_file):
    '''
        Generates a message
        @param  template_file Template file to use for generating message
    '''
    f = open(template_file,'r')
    messages_list = f.readlines()
    f.close()
    word_list = random.choice(messages_list).rstrip('\n').split(' ')
    message = []
    for s in word_list:
        s = s.rstrip(',').rstrip('!').rstrip('!!')
        if s in GLOBAL_SYNONYM_DICT:
            middle_delimeter = ''
            if s == 'hey':
                middle_delimeter = random.choice(['!','!!',','])
            message.append(random.choice(GLOBAL_SYNONYM_DICT[s]) + middle_delimeter)
        else :
            message.append(s)
    message.append(random.choice(DELIMITERS))
    return ' '.join(message)

