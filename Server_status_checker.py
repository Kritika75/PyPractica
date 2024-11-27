import socket
import ssl
import smtplib
import pickle
from datetime import datetime

#server details
SERVER = "www.google.com" #replace with server domain or IP
PORT = 443

#alert email details
EMAIL = "my_email@gmail.com"
PASSWORD = "my_password"
RECIPIENT = "recipient@gmail.com"

HISTORY_FILE = "server_history.pkl"

def check_server_status():
    try:
        context = ssl.create_default_context()
        with socket.create_connection((SERVER, PORT), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=SERVER) as sock:
                print(f"[{datetime.now()}] server is up!")
                return True
    except Exception as e:
        print(f"[{datetime.now()}] server id down! Error: {e}")
        return False

def send_email_alert():
    try:
        with smtplib.SMPT("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            subject = "server down alert!"
            body = f"Alert: The server {SERVER} is down as of {datetime.now()}"
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(EMAIL, RECIPIENT, message)
            print("alert email has been sent successfully")
    except Exception as e:
        print(f"Failed to send alert email. Error: {e}")
        
def save_history(status):
    try:
        history = load_history()
        history.append({"status": status, "time": datetime.now()})
        with open(HISTORY_FILE, "wb") as file:
            pickle.dump(history, file)
        print("Server history saved")
    except Exception as e:
        print(f"Failed to dave history. Error: {e}")
        
def load_history():
    try:
        with open(HISTORY_FILE, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
    
if __name__ == "__main__":
    print("server status checker running...\n")
    status = check_server_status()
    save_history(status)
    if not status:
        send_email_alert()