import tweepy, datetime, time
import random as r

def t_update():
    h = datetime.datetime.now().hour
    m = datetime.datetime.now().minute
    s = datetime.datetime.now().second
    return h, m, s

def sleep_t(hour, minute=0, second=0, passed=False):
    (h, m, s) = t_update()
    #print(h)
    #print(passed == True)
    sl = 0
    if s < second:
        sl += second - s
    elif s > second:
        sl += 60 - s + second
        m+=1

    if m < minute:
        sl += (minute - m)*60
    elif m > minute:
        sl += (60 - m + minute)*60
        h+=1

    if h == hour:
        if passed:
            passed = False
    elif h < hour:
        sl += ( hour - h )*60*60
        if passed == True:
            passed = False
    elif h > hour:
        sl += (24 - h + hour)*60*60


    return sl, passed

def sleep_w(dow, hour, minute=0, second=0):
    ( sl, passed ) = sleep_t(hour, minute, second, True)
    days = 0
    today = datetime.date.today().isoweekday()
    if passed:
        today += 1
    if today < dow:
        days = dow - today
    elif today > dow:
        days = (7 - today) + dow

    sl += days*24*60*60

    return sl

def load_tw(tw_list, f_name="doc/tweet.txt"):
    f = open(f_name, "r")
    for line in f:
        tw_list.append(line[:len(line)-1])
    f.close()
    return

def load_pic(pic, f_name="doc/pic.txt"):
    f = open(f_name, "r")
    tmp = f.readline()
    while tmp:
        pic.append(tmp[:len(tmp)-1])
        tmp = f.readline()
        pic.append(tmp[:len(tmp)-1])
        tmp = f.readline()
    f.close()
    return

def get_api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    
    # Construct the API instance
    return tweepy.API(auth)

'''#######################################################'''
def specific_time_tweet(api, tw, pic, hour, minute=0, second=0, rand=0):
    f = open("doc/used.txt", "a")

    sl = sleep_t(hour, minute, second)[0]
    #print(sl)
    time.sleep(sl)
    while len(tw) > 0:
        if rand == 0:
            n = 0
        elif rand == 1:
            n = r.randint(0, len(tw)-1)
        if tw[n] == "pic":
            if rand == 0:
                i = 0
            elif rand == 1:
                i = r.randint(0, ( len(pic) / 2 ) - 1)
            api.update_with_media("pic/" + pic[i*2], status = pic[i*2+1])
            #print("picture/" + pic[i*2])
            #print(pic[i*2 + 1])
            del tw[n]
            f.write(pic[i*2] + "\n")
            del pic[i*2]
            f.write(pic[i*2] + "\n")
            del pic[i*2]
        else:
            api.update_status(status = tw[n])
            #print(tw[n])
            f.write(tw[n] + "\n")
            del tw[n]
        f.write("\n")

        # print remaining
        rem = open("doc/tweet.txt", "w")
        for e in tw:
            rem.write(e+"\n")
        rem.close()

        rem_p = open("doc/pic.txt", "w")
        for e in pic:
            rem_p.write(e+"\n")
        rem_p.close()

        time.sleep(24*60*60)

    f.close()
    return

def specific_day_tweet(api, tw, pic, day, hour, minute=0, second=0, rand=0):
    f = open("doc/used.txt", "a")

    sl = sleep_w(day, hour, minute, second)
    #print(sl)
    time.sleep(sl)

    while len(tw) > 0:
        if rand == 0:
            n = 0
        elif rand == 1:
            n = r.randint(0, len(tw)-1)

        if tw[n] == "pic":
            if rand == 0:
                i = 0
            elif rand == 1:
                i = r.randint(0, ( len(pic) / 2 ) - 1)

            api.update_with_media("pic/" + pic[i*2], status = pic[i*2+1])
            #print("picture/" + pic[i*2])
            #print(pic[i*2 + 1])
            del tw[n]
            f.write(pic[i*2] + "\n")
            del pic[i*2]
            f.write(pic[i*2] + "\n")
            del pic[i*2]
        else:
            api.update_status(status = tw[n])
            #print(tw[n])
            f.write(tw[n] + "\n")
            del tw[n]
        f.write("\n")

        # print remaining
        rem = open("doc/tweet.txt", "w")
        for e in tw:
            rem.write(e+"\n")
        rem.close()

        rem_p = open("doc/pic.txt", "w")
        for e in pic:
            rem_p.write(e+"\n")
        rem_p.close()

        time.sleep(7*24*60*60)

    f.close()
    return
