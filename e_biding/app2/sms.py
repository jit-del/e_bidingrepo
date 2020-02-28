
def sendSMS(contactno,message):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+contactno
    headers = {
        'authorization': "q4F3dxa5Zw12tpHJ6Lb8gvMBc7hGIurTRlVXWfiSEzsDjeCPKQJoQnW9Tj8v654ke03fLzEAiZuCIO7r",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    s1 = response.text
    return s1