import re

def multi_replace(string, replacements, ignore_case=False):
    """
    Given a string and a dict, replaces occurrences of the dict keys found in the 
    string, with their corresponding values. The replacements will occur in "one pass", 
    i.e. there should be no clashes.
    :param str string: string to perform replacements on
    :param dict replacements: replacement dictionary {str_to_find: str_to_replace_with}
    :param bool ignore_case: whether to ignore case when looking for matches
    :rtype: str the replaced string
    """
    
    if ignore_case:
        replacements = dict((pair[0].lower(), pair[1]) for pair in sorted(replacements.items()))
    rep_sorted = sorted(replacements, key=lambda s: (len(s), s), reverse=True)

    rep_escaped = [re.escape(replacement) for replacement in rep_sorted]
    pattern = re.compile("|".join(rep_escaped), re.I if ignore_case else 0)

    return pattern.sub(lambda match: replacements[match.group(0).lower() 
                                                  if ignore_case else match.group(0)], string)

urtext = '''
1 کمپنی
فروری سنہ 2013ء میں جارج سینیس، اسکاٹ ایرکسن اور نک ونٹر نے کوڈ کامبیٹ کی بنیاد رکھی۔ ان لوگوں نے اس سے پہلے زبان سکھانے والے ایک اطلاقیہ اسکریٹر کو بھی بنایا تھا۔ سنہ 2014ء میں کوڈ کامبیٹ کو وائے کامبینیٹر کمپنی کی مالی معاونت بھی حاصل ہو گئی۔ کوڈ کامبیٹ کے مطابق اس کی تمام مصنوعات مفت ہیں اور کمپنی کا منصوبہ ہے کہ باصلاحیت کھلاڑیوں کو سافٹ ویئر کمپنیوں کی معلومات فراہم کرکے پیسے کمائے جائیں۔ تاہم اس نے اضافی کھیلوں کے لیے ماہانہ زر تعاون کا نظام بھی متعارف کرایا ہے۔ح1ح
2 مصنوعات
کوڈ کامبیٹ کا کھیل براؤزر میں کھیلا جاتا ہے۔ یہ کھیل اپنے کھیلنے والوں کو جاوا اسکرپٹ اور پائیتھن جیسی پروگرامنگ زبانیں سکھاتا اور ساتھ ہی کمپیوٹر سائنس کے بنیادی اصولوں سے واقف کراتا ہے۔ کھیل کے درجات میں آگے بڑھنے کے لیے کھلاڑیوں کو کوڈ لکھنا لازمی ہے۔ اسے تنہا بھی کھیل سکتے ہیں اور متعدد افراد مل کر بھی ساتھ کھیلتے ہیں۔ اس کھیل میں بنیادی طور پر ثانوی تعلیم کے بچوں کو مخاطب کیا گیا ہے۔ اسے مختلف تجزیہ نگاروں نے پسند اور مثبت اقدام قرار دیا۔ح2ح

جنوری 2014ء میں کوڈ کامبیٹ نے اپنے سافٹ ویئر کو آزاد مصدر کر دیا اور لیول ایڈیٹر بھی جاری کیا تاکہ صارفین بھی کھیل کے معلوماتی مواد میں اضافہ کر سکیں۔ح4ح
'''

extlinks = ['https://www.crunchbase.com/','http://www.cnet.com/', 'https://techcrunch.com/', 'http://www.linuxjournal.com/', 'https://www.pcmag.com/', '[http://codecombat.com/]']

dlinks = {}
for  i,link in enumerate(extlinks):
    i+=1
    dkey = 'ح' + str(i) + 'ح'
    dlinks[dkey] = '<ref>' + link + '</ref>'

print('Now printing Values of Dictionary')

dlen = len(dlinks)
for key,val in dlinks.items():
    print(key,val)

#print(urtext)
lstlnkTuples = list(dlinks.items())
print(lstlnkTuples)

for r in tuple(dlinks.items()):
    urtext = urtext.replace(*r)

print(urtext)


fintext = multi_replace(urtext, dlinks)
#print(fintext)