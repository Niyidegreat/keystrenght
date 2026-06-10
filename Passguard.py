#!/usr/bin/env python3

import os
import json
import csv
import math
import re
import base64
import hashlib
import logging
import secrets
import string
import requests

from datetime import datetime
from cryptography.fernet import Fernet

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from pyfiglet import Figlet


# =========================
# CONFIG
# =========================

APP_NAME = "PassGuard Pro"
VERSION = "SOC Edition 1.0"

REPORT_DIR = "reports"
LOG_DIR = "logs"
VAULT_DIR = "vault"

console = Console()

os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(VAULT_DIR, exist_ok=True)


# =========================
# LOGGING
# =========================

logging.basicConfig(
    filename=f"{LOG_DIR}/passguard.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# =========================
# COMMON PASSWORDS (MIN SET)
# =========================

COMMON_PASSWORDS = {
    "123456", "password", "123456789", "qwerty",
    "admin", "welcome", "password123", "123123"
}


# =========================
# BANNER
# =========================

def banner():
    fig = Figlet(font="slant")
    console.print(f"[cyan]{fig.renderText(APP_NAME)}[/cyan]")
    console.print(Panel.fit(f"{VERSION}\nSOC-Level Password Security Toolkit"))


# =========================
# ENTROPY
# =========================

def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"[0-9]", password): charset += 10
    if re.search(r"[^\\w]", password): charset += 32

    if charset == 0:
        return 0

    return len(password) * math.log2(charset)


# =========================
# PATTERN DETECTION
# =========================

def detect_patterns(password):
    issues = []

    if re.search(r"(.)\1\1", password):
        issues.append("Repeated characters detected")

    if re.search(r"123|234|345|456|567|678|789", password):
        issues.append("Sequential numbers detected")

    patterns = ["qwerty", "asdf", "zxcv", "password"]
    for p in patterns:
        if p in password.lower():
            issues.append(f"Common pattern: {p}")

    if re.search(r"\d{2}/\d{2}/\d{2,4}", password):
        issues.append("Date pattern detected")

    return issues


# =========================
# REPORTING
# =========================

def save_report(data):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    json_path = f"{REPORT_DIR}/report_{ts}.json"
    csv_path = f"{REPORT_DIR}/report_{ts}.csv"

    with open(json_path, "w") as f:
        json.dump(data, f, indent=4)

    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        for k, v in data.items():
            writer.writerow([k, v])

    console.print(f"[green]Reports saved:[/green] {json_path}, {csv_path}")


# =========================
# PASSWORD ANALYSIS ENGINE
# =========================

def password_strength():
    password = Prompt.ask("Enter password")

    score = 0
    issues = []

    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
    else:
        issues.append("Too short")

    if re.search(r"[A-Z]", password): score += 10
    if re.search(r"[a-z]", password): score += 10
    if re.search(r"[0-9]", password): score += 10
    if re.search(r"[^\\w]", password): score += 15

    entropy = calculate_entropy(password)

    if entropy > 80:
        score += 25
    elif entropy < 50:
        issues.append("Low entropy")

    if password.lower() in COMMON_PASSWORDS:
        score -= 30
        issues.append("Common password detected")

    patterns = detect_patterns(password)
    score -= len(patterns) * 5
    issues.extend(patterns)

    score = max(0, min(100, score))

    if score >= 80:
        rating = "STRONG"
    elif score >= 50:
        rating = "MODERATE"
    else:
        rating = "WEAK"

    console.print("\n[bold cyan]Security Report[/bold cyan]")
    console.print(f"Score: {score}/100")
    console.print(f"Rating: {rating}")
    console.print(f"Entropy: {entropy:.2f}")

    if issues:
        console.print("\n[red]Issues:[/red]")
        for i in issues:
            console.print(f"- {i}")

    save_report({
        "password_score": score,
        "rating": rating,
        "entropy": entropy,
        "issues": issues
    })

    logging.info("Password analyzed")


# =========================
# ENTROPY ONLY
# =========================

def entropy_calculator():
    p = Prompt.ask("Enter password")
    e = calculate_entropy(p)
    console.print(f"Entropy: {e:.2f}")


# =========================
# PATTERN VIEWER
# =========================

def pattern_detector():
    p = Prompt.ask("Enter password")
    issues = detect_patterns(p)

    if not issues:
        console.print("[green]No issues found[/green]")
    else:
        for i in issues:
            console.print(f"- {i}")


# =========================
# PASSWORD GENERATOR
# =========================

def password_generator():
    length = int(Prompt.ask("Length", default="16"))

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(chars) for _ in range(length))

    console.print(f"\nGenerated Password:\n{password}")

    logging.info("Password generated")


# =========================
# HASHING
# =========================

def hash_generator():
    text = Prompt.ask("Enter text")

    console.print("\nHashes:")
    console.print(f"MD5: {hashlib.md5(text.encode()).hexdigest()}")
    console.print(f"SHA1: {hashlib.sha1(text.encode()).hexdigest()}")
    console.print(f"SHA256: {hashlib.sha256(text.encode()).hexdigest()}")
    console.print(f"SHA512: {hashlib.sha512(text.encode()).hexdigest()}")


def hash_identifier():
    h = Prompt.ask("Enter hash")

    l = len(h)

    if l == 32:
        console.print("MD5")
    elif l == 40:
        console.print("SHA1")
    elif l == 64:
        console.print("SHA256")
    elif l == 128:
        console.print("SHA512")
    else:
        console.print("Unknown")


# =========================
# BREACH CHECKER (HIBP)
# =========================

def breach_checker():
    password = Prompt.ask("Enter password")

    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    r = requests.get(url)

    for line in r.text.splitlines():
        h, count = line.split(":")
        if h == suffix:
            console.print(f"[RED]BREACHED {count} times[/RED]")
            return

    console.print("[GREEN]Not found in breaches[/GREEN]")


# =========================
# VAULT (ENCRYPTED)
# =========================

VAULT_FILE = f"{VAULT_DIR}/vault.dat"


def get_cipher(master):
    key = hashlib.sha256(master.encode()).digest()
    return Fernet(base64.urlsafe_b64encode(key))


def load_vault(master):
    cipher = get_cipher(master)

    if not os.path.exists(VAULT_FILE):
        return [], cipher

    try:
        data = open(VAULT_FILE, "rb").read()
        decrypted = cipher.decrypt(data).decode()
        return json.loads(decrypted), cipher
    except:
        console.print("[red]Invalid master password[/red]")
        return None, None


def save_vault(vault, cipher):
    data = json.dumps(vault).encode()
    encrypted = cipher.encrypt(data)

    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted)


def password_vault():
    master = Prompt.ask("Master password", password=True)

    vault, cipher = load_vault(master)
    if vault is None:
        return

    while True:
        console.print("\n1 Add\n2 View\n3 Delete\n0 Exit")
        c = Prompt.ask("Choice")

        if c == "1":
            vault.append({
                "site": Prompt.ask("Site"),
                "user": Prompt.ask("User"),
                "pass": Prompt.ask("Pass", password=True)
            })
            save_vault(vault, cipher)

        elif c == "2":
            for i, v in enumerate(vault):
                console.print(i, v)

        elif c == "3":
            i = int(Prompt.ask("Index"))
            vault.pop(i)
            save_vault(vault, cipher)

        elif c == "0":
            break


# =========================
# MENU
# =========================

def menu():
    table = Table(title="PassGuard Pro SOC Edition")

    table.add_row("1", "Password Analysis")
    table.add_row("2", "Entropy Check")
    table.add_row("3", "Pattern Detection")
    table.add_row("4", "Generator")
    table.add_row("5", "Hash Generator")
    table.add_row("6", "Hash Identifier")
    table.add_row("7", "Breach Checker")
    table.add_row("8", "Vault")
    table.add_row("0", "Exit")

    console.print(table)


def main():
    banner()

    while True:
        menu()
        c = Prompt.ask("Select")

        if c == "1":
            password_strength()
        elif c == "2":
            entropy_calculator()
        elif c == "3":
            pattern_detector()
        elif c == "4":
            password_generator()
        elif c == "5":
            hash_generator()
        elif c == "6":
            hash_identifier()
        elif c == "7":
            breach_checker()
        elif c == "8":
            password_vault()
        elif c == "0":
            break


if __name__ == "__main__":
    main()