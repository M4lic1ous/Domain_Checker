# 🌐 Domain Scanner Pro

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![DNS](https://img.shields.io/badge/DNS-Google%208.8.8.8-orange.svg)](https://developers.google.com/speed/public-dns)

## 🔍 Ultimate Domain TLD Checker

A powerful, lightning-fast domain availability scanner that checks thousands of TLDs (Top-Level Domains) simultaneously. Built for cybersecurity researchers, domain investors, and penetration testers.

---

## ✨ Features

- 🚀 **High-Speed Scanning** - Multi-threaded DNS resolution
- 🎨 **Beautiful UI** - Neon-colored real-time progress display
- 📊 **Detailed Statistics** - Success rate, total checked, found domains
- 🌍 **Extensive TLD Support** - 500+ TLDs including `.com`, `.org`, `.io`, `.tech`, `.app` and more
- 🔄 **Live Progress** - Real-time updates with progress bar
- 📱 **Comprehensive Results** - IP resolution for found domains
- 🛡️ **Google DNS** - Uses 8.8.8.8 and 1.1.1.1 for accurate results

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/domain-scanner-pro.git

# Navigate to the directory
cd domain-scanner-pro

# Install dependencies
pip install dnspython
```

---

## 🚀 Usage

```bash
python domain_scanner.py
```

### Example Output:

```
🔍 Starting domain testing for: google
✅ google.com  ➜  142.250.185.46
✅ google.org  ➜  142.250.185.46
❌ google.xyz  ➜  Not found
✅ google.io   ➜  142.250.185.46
```

---

## 📊 TLD Categories

| Category | Examples |
|----------|----------|
| Generic | .com, .org, .net, .biz, .info |
| New gTLDs | .app, .tech, .cloud, .online, .shop |
| Country | .us, .uk, .de, .fr, .jp, .cn |
| Special | .io, .ai, .co, .fm, .tv |

---

## 🎯 Use Cases

- 🔐 **Cybersecurity Research** - Domain enumeration
- 💼 **Domain Investors** - Find valuable domains
- 🛡️ **Penetration Testing** - Subdomain discovery
- 📈 **Market Research** - Check domain availability
- 🏢 **Brand Protection** - Monitor trademark infringements

---

## 🛠️ Technical Details

- **DNS Resolver**: Google Public DNS (8.8.8.8, 1.1.1.1)
- **Timeout**: 2 seconds per query
- **TLD Count**: 500+ Top-Level Domains
- **Language**: Python 3.6+
- **Dependencies**: dnspython

---

## 📝 Example Search

```bash
# Search for "cyber" domain
Enter domain name (without extension): cyber

# Results will show:
✅ cyber.com    ➜  192.168.1.1
✅ cyber.tech   ➜  192.168.1.2
❌ cyber.xyz    ➜  Not found
✅ cyber.ai     ➜  192.168.1.3
```

---

## 🔧 Customization

You can easily customize the TLD list by modifying the `TLDS` array in the script:

```python
TLDS = [
    "com", "org", "net",  # Add your TLDs here
    # ... existing TLDs
]
```

---

## ⚡ Performance Tips

- Run with stable internet connection
- Use on systems with good DNS cache
- Recommended for moderate TLD checks (500+)
- For large-scale scanning, consider using asynchronous DNS

---

## 🌟 Credits

**Created by Malicious**

- 🎭 **Team**: Dark Justice Team
- 📱 **Telegram**: [M4lic1ous](https://t.me/M4lic1ous)
- 💻 **GitHub**: [M4lic1ous](https://github.com/M4lic1ous)

---

## 📞 Contact

- **Telegram**: [@M4lic1ous]
- **Dark Justice Team**

---

## ⭐ Show Your Support

If you find this tool useful, consider:

- ⭐ Starring the repository
- 🐛 Reporting issues
- 💡 Suggesting features
- 🔄 Sharing with others

---

**Made with ❤️ by Malicious | Dark Justice Team**
Tg : @M4lic1ous
