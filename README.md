# 📧 Mail — Custom Email Protocol

A custom email system built on raw TCP sockets with a self-designed text protocol inspired by SMTP. No libraries, no frameworks — just pure socket programming from the ground up.

---

## 📁 Project Structure

```
mail/
├── server.py      # TCP server — receives and stores emails
├── clientS.py     # TCP client — connects and sends emails
├── app.py         # Tkinter GUI — user interface
└── emails.txt     # Email storage (auto-created)
```

---

## 🔌 How It Works

The system uses a custom text protocol over TCP. When sending an email the client sends a sequence of commands the server parses line by line:

```
EX: sender@example.com        → From
USQUE: receiver@example.com   → To
NUNTIUS: Hello, this is a message.  → Message body
TERMINUS                       → End of email
```

> Latin naming: `EX` = from, `USQUE` = to/until, `NUNTIUS` = message, `TERMINUS` = end

Once `TERMINUS` is received the server writes the email to `emails.txt` and sends back a confirmation.

---

## 🚀 Getting Started

### Requirements

- Python 3.x
- No external dependencies

### 1. Configure the IP

In both `server.py` and `clientS.py`, set `dominus` to your local IP address:

```python
dominus = "192.168.1.177"  # replace with your IP
ostium = 8475              # port
```

### 2. Start the server

```bash
python server.py
```

You should see:
```
Wolf Tears Email is running on Host:192.168.1.177:Port:8475
```

### 3. Run the GUI

```bash
python app.py
```

Fill in your email address, the recipient, and your message — then click **Send**.

---

## 🖥️ GUI

The Tkinter GUI (`app.py`) provides three fields:

| Field | Description |
|-------|-------------|
| Your Oratio | Your email / sender address |
| To Oratio | Recipient address |
| Message | The message body |

Click **Send** to deliver. Fields clear automatically after sending.

---

## 📨 Email Storage

Emails are saved to `emails.txt` in the server's working directory in this format:

```
From: sender@example.com
To: receiver@example.com
Message: Hello, this is a message.
---
```

---

## 🛠️ Tech Stack

- **Python** — All logic
- **socket** — Raw TCP server and client
- **tkinter** — Desktop GUI
- **Custom protocol** — Text-based, inspired by SMTP

---

## 📌 Known Issues

- `connectionAlive` / `connection_alive` variable name mismatch — the loop may not exit cleanly after receiving `TERMINUS`
- Server is single-threaded — can only handle one client at a time
- No authentication or encryption
- Messages that exceed 1024 bytes may be split across multiple `recv()` calls and misparse

---

## 🔮 Planned Features

- [ ] Multi-client support with threading
- [ ] Inbox view per recipient
- [ ] Simple login system
- [ ] Message framing to handle large messages
- [ ] Encryption

---

## 👤 Author

**Quidon Roethof** — [github.com/Darklord1234938](https://github.com/Darklord1234938)
