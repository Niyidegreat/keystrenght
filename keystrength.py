import customtkinter as ctk
import re
import random
import string
from tkinter import messagebox

# ==================================
# KEYSTRENGTH
# Owner: Adeniyi Ojedele (Niyi De Great)
# ==================================

COMMON_PASSWORDS = [
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "admin",
    "welcome",
    "abc123",
    "football",
    "letmein",
    "iloveyou"
]

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class KeyStrength:

    def __init__(self, root):

        self.root = root
        self.root.title("KeyStrength v1.0")
        self.root.geometry("850x650")

        title = ctk.CTkLabel(
            root,
            text="🔐 KeyStrength",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=15)

        subtitle = ctk.CTkLabel(
            root,
            text="Advanced Password Strength Analyzer",
            font=("Arial", 14)
        )
        subtitle.pack()

        self.password_entry = ctk.CTkEntry(
            root,
            width=500,
            height=45,
            show="*",
            placeholder_text="Enter Password"
        )
        self.password_entry.pack(pady=20)

        self.show_var = ctk.BooleanVar()

        show_check = ctk.CTkCheckBox(
            root,
            text="Show Password",
            variable=self.show_var,
            command=self.toggle_password
        )
        show_check.pack()

        analyze_btn = ctk.CTkButton(
            root,
            text="Analyze Password",
            command=self.analyze
        )
        analyze_btn.pack(pady=20)

        self.score_label = ctk.CTkLabel(
            root,
            text="",
            font=("Arial", 18, "bold")
        )
        self.score_label.pack()

        self.result_box = ctk.CTkTextbox(
            root,
            width=700,
            height=250
        )
        self.result_box.pack(pady=15)

    def toggle_password(self):

        if self.show_var.get():
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")

    def generate_suggestion(self, password):

        symbols = "!@#$%^&*"

        return (
            password +
            random.choice(symbols) +
            ''.join(random.choice(string.ascii_letters)
                    for _ in range(4))
        )

    def analyze(self):

        password = self.password_entry.get()

        self.result_box.delete("1.0", "end")

        if not password:
            messagebox.showerror(
                "Error",
                "Please enter a password."
            )
            return

        lower = re.search(r"[a-z]", password)
        upper = re.search(r"[A-Z]", password)
        digit = re.search(r"\d", password)
        symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

        score = 0
        recommendations = []

        if len(password) >= 8:
            score += 1
        else:
            recommendations.append(
                "Use at least 8 characters."
            )

        if lower:
            score += 1
        else:
            recommendations.append(
                "Add lowercase letters."
            )

        if upper:
            score += 1
        else:
            recommendations.append(
                "Add uppercase letters."
            )

        if digit:
            score += 1
        else:
            recommendations.append(
                "Add numbers."
            )

        if symbol:
            score += 1
        else:
            recommendations.append(
                "Add special symbols."
            )

        # Common password detection

        if password.lower() in COMMON_PASSWORDS:

            self.score_label.configure(
                text="❌ REJECTED",
                text_color="red"
            )

            self.result_box.insert(
                "end",
                "The password is common.\n\n"
            )

            self.result_box.insert(
                "end",
                "Use a unique password.\n\n"
            )

            self.result_box.insert(
                "end",
                "Example:\n"
                "My$ecure2026!Pass"
            )

            return

        # Detect birthdays

        birthday_pattern = re.search(
            r"(19\d{2}|20\d{2})",
            password
        )

        # Detect possible names

        name_pattern = re.search(
            r"^[A-Za-z]+",
            password
        )

        if birthday_pattern and name_pattern:

            recommendations.append(
                "Password contains possible "
                "name and birthday."
            )

            stronger = (
                password[:4] +
                "@Drive#" +
                password[4:]
            )

            self.result_box.insert(
                "end",
                f"Suggested Stronger Version:\n"
                f"{stronger}\n\n"
            )

        if score <= 2:
            strength = "Weak"
            color = "red"

        elif score <= 4:
            strength = "Moderate"
            color = "orange"

        else:
            strength = "Strong"
            color = "green"

        self.score_label.configure(
            text=f"{strength} ({score}/5)",
            text_color=color
        )

        self.result_box.insert(
            "end",
            f"Password Strength: {strength}\n\n"
        )

        if recommendations:

            self.result_box.insert(
                "end",
                "Recommendations:\n"
            )

            for item in recommendations:
                self.result_box.insert(
                    "end",
                    f"• {item}\n"
                )

        else:

            self.result_box.insert(
                "end",
                "Excellent password.\n"
            )

        self.result_box.insert(
            "end",
            "\nSuggested Password:\n"
        )

        self.result_box.insert(
            "end",
            self.generate_suggestion(password)
        )


root = ctk.CTk()
app = KeyStrength(root)
root.mainloop()