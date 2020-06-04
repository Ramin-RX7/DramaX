import urllib,re

def bing_all_grabber(s):

    lista = []
    page = 1
    while page <= 101:
        try:
            bing = "http://www.bing.com/search?q=ip%3A" + \
                s + "+&count=50&first=" + str(page)
            openbing = urllib.request.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            for i in range(len(findwebs)):
                allnoclean = findwebs[i]
                findall1 = re.findall('http://(.*?)/', allnoclean)
                for idx, item in enumerate(findall1):
                    if 'www' not in item:
                        findall1[idx] = 'http://www.' + item + '/'
                    else:
                        findall1[idx] = 'http://' + item + '/'
                lista.extend(findall1)

            page += 50
        except:
        #except urllib.error.URLError:
            pass

    final = unique(lista)
    return final

def check_wordpress(sites):
    wp = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + 'wp-login.php').getcode() == 200:
                wp.append(site)
        except:
            pass

    return wp

def check_wpstorethemeremotefileupload(sites):
    wpstorethemeremotefileupload = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-content/themes/WPStore/upload/index.php').getcode() == 200:
                wpstorethemeremotefileupload.append(site)
        except:
            pass

    return wpstorethemeremotefileupload

def check_wpcontactcreativeform(sites):
    wpcontactcreativeform = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-content/plugins/sexy-contact-form/includes/fileupload/index.php').getcode() == 200:
                wpcontactcreativeform.append(site)
        except:
            pass

    return wpcontactcreativeform

def check_wplazyseoplugin(sites):
    wplazyseoplugin = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-content/plugins/lazy-seo/lazyseo.php').getcode() == 200:
                wplazyseoplugin.append(site)
        except:
            pass

    return wplazyseoplugin

def check_wpeasyupload(sites):
    wpeasyupload = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-content/plugins/easy-comment-uploads/upload-form.php').getcode() == 200:
                wpeasyupload.append(site)
        except:
            pass

    return wpeasyupload

def check_wpsymposium(sites):
    wpsymposium = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-symposium/server/file_upload_form.php').getcode() == 200:
                wpsycmium.append(site)
        except:
            pass

    return wpsymposium

def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]











'''
def wpminiscanner():
    ip = input('Enter IP: ')
    sites = bing_all_grabber(str(ip))
    print('1')
    wordpress = check_wordpress(sites)
    print('2')
    wpstorethemeremotefileupload = check_wpstorethemeremotefileupload(sites)
    print('3')
    wpcontactcreativeform = check_wpcontactcreativeform(sites)
    print('4')
    wplazyseoplugin = check_wplazyseoplugin(sites)
    print('5')
    wpeasyupload = check_wpeasyupload(sites)
    print('6')
    wpsymposium = check_wpsymposium(sites)
    for ss in wordpress:
        print (ss)
    print ('[*] Found, ', len(wordpress), ' wordpress sites.')
    print ('-' * 30 + '\n')
    for ss in wpstorethemeremotefileupload:
        print (ss)
    print ('[*] Found, ', len(
        wpstorethemeremotefileupload), ' wp_storethemeremotefileupload exploit.')
    print ('-' * 30 + '\n')
    for ss in wpcontactcreativeform:
        print (ss)
    print ('[*] Found, ', len(wpcontactcreativeform), ' wp_contactcreativeform exploit.')
    print ('-' * 30 + '\n')
    for ss in wplazyseoplugin:
        print (ss)
    print ('[*] Found, ', len(wplazyseoplugin), ' wp_lazyseoplugin exploit.')
    print ('-' * 30 + '\n')
    for ss in wpeasyupload:
        print (ss)
    print ('[*] Found, ', len(wpeasyupload), ' wp_easyupload exploit.')
    print ('-' * 30 + '\n')
    for ss in wpsymposium:
        print (ss)

    print('[*] Found, ', len(wpsymposium), ' wp_sympsiup exploit.')

    print('\n')
'''
#wpminiscanner()