# 🔐 KeyStrength

> Intelligent Password Strength Analyzer for Better Cybersecurity

KeyStrength is a Python-based password security assessment platform developed to analyze password strength beyond traditional complexity checks.

The system evaluates passwords using a multi-layered security assessment approach that combines complexity validation, pattern recognition, common password detection, personal information analysis, and intelligent security recommendations.

Unlike traditional password checkers that focus only on character requirements, KeyStrength identifies real-world weaknesses that attackers commonly exploit during credential attacks, including predictable naming conventions, birth years, common password structures, and low-entropy patterns.

The project was developed as a practical cybersecurity initiative to demonstrate secure software development, authentication security principles, password risk assessment, and user-focused defensive security controls.

Business Problem

Compromised credentials remain one of the most common initial attack vectors used in:

Account Takeovers (ATO)
Credential Stuffing Attacks
Brute Force Attacks
Password Spraying Campaigns
Social Engineering Operations
Unauthorized Access Incidents

Despite increased security awareness, many users continue to create passwords based on:

Personal names
Birth years
Keyboard patterns
Common dictionary words
Predictable substitutions

These weaknesses significantly reduce password entropy and increase the likelihood of compromise.

KeyStrength was designed to identify and mitigate these risks before passwords are used in production environments.

Core Security Features
Password Strength Analysis

Performs comprehensive password evaluation based on:

Length
Character diversity
Entropy estimation
Pattern analysis
Predictability assessment
Common Password Detection and Rejection

Identifies passwords frequently found in:

Public breach datasets
Credential dumps
Dictionary attack wordlists

Examples:

password123
admin123
qwerty123
12345678
Personal Information Pattern Detection

Detects password components derived from:

Names
Nicknames
Common identity patterns

This helps reduce vulnerability to targeted password-guessing attacks.

Birthday and Year Detection

Identifies:

Birth years
Date patterns
Predictable numerical sequences

Attackers frequently leverage these patterns during account compromise attempts.

Password Complexity Validation

Validates compliance with password security best practices by analyzing:

Uppercase characters
Lowercase characters
Numbers
Special characters
Minimum length requirements
Intelligent Security Recommendations

Provides contextual recommendations based on identified weaknesses.

Examples include:

Increase entropy
Avoid predictable words
Eliminate personal information
Increase password length
Use passphrases
Strong Password Suggestions

Generates stronger password alternatives aligned with modern password security standards.

Real-Time Security Assessment

Provides immediate password evaluation and security feedback as users type.

Password Visibility Toggle

Enhances usability while maintaining secure password handling practices.

Modern User-Friendly Interface

Clean and intuitive interface focused on accessibility, simplicity, and user education.

Cybersecurity Awareness Support

Educates users on secure password creation practices and promotes stronger security habits.

---

# 🖼️ Application Demostration and Preview

## Main Interface

The main dashboard provides a simple and intuitive experience, allowing users to enter a password, analyze its strength, and receive recommendations instantly.
![Main Interface](https://github.com/Niyidegreat/keystrenght/blob/719d9cdab64d7cc0b2d854274d39401a037847b4/main-interface.png)

---

## Strong Password Analysis

Example of a password that satisfies all security requirements including length, uppercase letters, lowercase letters, numbers, and special characters.

**Security Status:** Strong

![Strong Password](https://github.com/Niyidegreat/keystrenght/blob/719d9cdab64d7cc0b2d854274d39401a037847b4/strong.png)

---

## Strong Password with Possible Year/Birthday Detection

Example of a password that meets all security requirements but contains a possible birth year or predictable personal information pattern.

**Security Status:** Strong

**Additional Notice:** Password may contain a year or birthday-related pattern. Users are encouraged to make the password less predictable.

![Strong Password With Year Detection](https://github.com/Niyidegreat/keystrenght/blob/719d9cdab64d7cc0b2d854274d39401a037847b4/strong-year.png)

---

## Moderate Password Analysis

Example of a password that meets some security requirements but could be improved for stronger security.

**Security Status:** Moderate

**Recommendations:**

* Increase password length
* Add more special characters
* Use less predictable character combinations

![Moderate Password](https://github.com/Niyidegreat/keystrenght/blob/719d9cdab64d7cc0b2d854274d39401a037847b4/Moderate.png)

---

## Weak Password Analysis

Example of a password that lacks sufficient complexity and does not meet recommended password security standards.

**Security Status:** Weak

**Recommendations:**

* Add uppercase letters
* Add lowercase letters
* Include numbers
* Include special symbols
* Use at least 8 characters

![Weak Password]([screenshots/weak.png](https://github.com/Niyidegreat/keystrenght/blob/719d9cdab64d7cc0b2d854274d39401a037847b4/weak.png))

---

## Common Password Detection (Rejected)

Example of a password identified as a commonly used password.

**Security Status:** Rejected

**Result:**

The password is common and should not be used.

KeyStrength immediately warns the user and recommends creating a more unique password.

![Common Password Detection](https://github.com/Niyidegreat/keystrenght/blob/719d9cdab64d7cc0b2d854274d39401a037847b4/weak-common.png)

---

# 🔍 How KeyStrength Works

KeyStrength evaluates passwords using cybersecurity best practices and industry-standard password requirements.

The tool checks for:

* Password length
* Uppercase letters
* Lowercase letters
* Numbers
* Special symbols
* Common passwords
* Predictable personal information
* Password complexity

---

# 📊 Password Evaluation Criteria

| Requirement             | Status      |
| ----------------------- | ----------- |
| Minimum 8 Characters    | Required    |
| Uppercase Letter        | Required    |
| Lowercase Letter        | Required    |
| Number                  | Required    |
| Special Character       | Required    |
| Common Password Check   | Required    |
| Name Detection          | Alerted     |
| Birthday/Year Detection | Alerted     |

---

# 🚦 Password Strength Levels

| Score           | Rating   |
| --------------- | -------- |
| 0 – 2           | Weak     |
| 3 – 4           | Moderate |
| 5               | Strong   |
| Common Password | Rejected |

---

# 💡 Example Results

## Example 1

### Input

```text
password123
```

### Output

```text
❌ WEAK

The password is common.

Recommendation:
Choose a unique password that combines uppercase letters,
lowercase letters, numbers, and symbols.
```

---

## Example 2

### Input

```text
John@2000
```

### Output

```text
Strength: Strong

Warning:
Password contains a possible name and birth year.

Suggested Alternative:
John@Drive#2000
```

---

## Example 3

### Input

```text
john
```

### Output

```text
Strength: Weak

Recommendations:

• Use at least 8 characters
• Add uppercase letters
• Add numbers
• Add special characters
```

---

# 🛠️ Installation

## Clone the Repository

```bash
https://github.com/Niyidegreat/keystrenght.git
```

## Navigate to Project Directory

```bash
cd KeyStrength
```

## Install Required Dependencies

```bash
pip install customtkinter
```

## Run the Application

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
   ├── main-interface.png
   ├── moderate.png
   ├── strong.png
   ├── strong-year.png
   ├── weak.png
   └── weak-common.png


---

# 🔒 Security Notice

KeyStrength performs all password analysis locally on the user's machine.

* No passwords are stored.
* No passwords are transmitted.
* No passwords are uploaded to external servers.
* No user information is collected.

All analysis is performed offline for privacy and security.

---

## Technical Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Application Logic |
| Tkinter | Graphical User Interface |
| Regular Expressions (Regex) | Pattern Detection |
| Git | Version Control |
| GitHub | Repository Management |
| Object-Oriented Programming (OOP) | Application Architecture |
# Future Improvements

Planned enhancements for future versions include:

* Password Entropy Calculation
* Password Breach Detection
* Secure Password Generator
* Password History Analysis
* Export Security Reports as PDF
* Dark and Light Themes
* Password Strength Graphs
* Multi-Language Support
* AI-Powered Password Recommendations
* Have I Been Pwned Integration

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve KeyStrength:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a pull request

---

# ⭐ Support

If you found this project useful:

* Star the repository
* Share it with others
* Report bugs and issues
* Suggest new features

---

# 👨‍💻 Author

### Adeniyi Ojedele (Niyi De Great)

Cybersecurity Analyst | UI/UX Designer | Cybersecurity + AI Enthusiast | Founder of Neotherion

Email: ojedeleadeniyi1@gmail.com

Passionate about cybersecurity, secure systems, digital safety, and building tools that make technology safer and easier to use.

---

## 🔐 Strong Passwords Are the First Line of Defense in Cybersecurity.
