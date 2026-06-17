# 🔐 KeyStrength

**Owner:** Adeniyi Ojedele (Niyi De Great)

KeyStrength is a modern cybersecurity-focused password strength analysis tool built with Python. It helps users evaluate the security of their passwords, detect weak patterns, identify common passwords, and receive actionable recommendations for creating stronger credentials.

Unlike traditional password checkers, KeyStrength not only scores password strength but also identifies predictable elements such as names, birth years, and commonly used passwords while providing intelligent suggestions to improve security.

---

# 📌 Features

* Password Strength Analysis
* Common Password Detection
* Name Pattern Detection
* Birthday/Year Detection
* Password Complexity Validation
* Intelligent Recommendations
* Strong Password Suggestions
* Security Score Rating
* Password Visibility Toggle
* Modern User Interface
* Cybersecurity Awareness Support

---

# 🖼️ Screenshots

## Main Application Interface

Add a screenshot showing the application's home screen.

```text
screenshots/main-interface.png
```

**What to capture:**

* Application window
* Password input field
* Analyze button
* Password visibility toggle
* Overall UI design

![Main Interface](screenshots/main-interface.png)

---

## Password Analysis Example

Add a screenshot showing a password being analyzed.

```text
screenshots/password-analysis.png
```

**What to capture:**

* User-entered password
* Analysis result
* Security score
* Recommendations section

![Password Analysis](screenshots/strong-year.png)

---

## Common Password Detection

Add a screenshot demonstrating password rejection.

```text
screenshots/common-password-detection.png
```

**Example Input:**

```text
password123
```

**Expected Result:**

```text
The password is common.
Password Rejected.
```

![Common Password Detection](screenshots/weak-common.png)

---

## Name and Birthday Detection

Add a screenshot showing personal information detection.

```text
screenshots/name-birthday-detection.png
```

**Example Input:**

```text
John@2000
```

**Expected Result:**

```text
Password contains possible birthday.
```

![Name and Birthday Detection](screenshots/weak-year.png)

---

## Password Recommendation System

Add a screenshot showing generated recommendations.

```text
screenshots/weak.png
```

**What to capture:**

* Missing password requirements
* Suggested improvements
* Generated secure password examples

![Recommendations](screenshots/weak.png)

---

# 🚀 How It Works

KeyStrength evaluates passwords using cybersecurity best practices.

The tool checks:

✅ Minimum length

✅ Uppercase letters

✅ Lowercase letters

✅ Numbers

✅ Special characters

✅ Common password databases

✅ Predictable personal information

---

# 🔍 Password Evaluation Criteria

| Requirement           | Status      |
| --------------------- | ----------- |
| Minimum 8 Characters  | Required    |
| Uppercase Letter      | Required    |
| Lowercase Letter      | Required    |
| Number                | Required    |
| Special Symbol        | Required    |
| Common Password Check | Required    |
| Name Detection        | Recommended |
| Birthday Detection    | Recommended |

---

# 📊 Password Strength Levels

| Score | Rating   |
| ----- | -------- |
| 0 – 2 | Weak     |
| 3 – 4 | Moderate |
| 5    | Strong   |

---

# Example Analysis

## Example 1

**Password**

```text
password123
```

**Result**

```text
❌ Rejected

The password is common.
Please choose a more unique password.
```

---

## Example 2

**Password**

```text
John@2000
```

**Result**

```text
Strength: Strong

Password contains possible name and birthday.

Suggested Alternative:
John@Drive#2000
```

---

## Example 3

**Password**

```text
john
```

**Result**

```text
Weak Password

Recommendations:

• Add uppercase letters
• Add numbers
• Add special characters
• Use at least 8 characters
```

---

# 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/keystrength.git
```

Move into the project directory:

```bash
cd keystrength
```

Install dependencies:

```bash
pip install customtkinter
```

Run the application:

```bash
python keystrength.py
```

---

# 📂 Project Structure

```text
KeyStrength/
│
├── keystrength.py
├── common_passwords.txt
├── README.md
│
├── screenshots/
│   ├── main-interface.png
│   ├── moderate.png
│   ├── weak-common.png
│   ├── weak-year.png
│   └── weak.png
│
└── assets/
    └── logo.png
```

---

# 🎯 Future Improvements

* Password Entropy Calculation
* Password Breach Detection
* Have I Been Pwned Integration
* Secure Password Generator
* Password History Analysis
* PDF Security Reports
* AI-Based Password Suggestions
* Light/Dark Theme Switching
* Multi-Language Support

---

# 🔐 Security Notice

KeyStrength performs all password analysis locally on the user's machine.

No passwords are stored, transmitted, or shared with external servers.

---

# 👨‍💻 Author

**Adeniyi Ojedele (Niyi De Great)**
ojedeleadeniyi1@gmail.com

Cybersecurity Enthusiast • UI/UX Designer • Builder

---

# ⭐ Support

If you found this project useful:

* Star the repository
* Share it with others
* Contribute improvements
* Report issues

---

**Strong passwords are the first line of defense in cybersecurity.**
