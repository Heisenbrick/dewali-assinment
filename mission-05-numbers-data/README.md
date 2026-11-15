# Mission 5 — Numbers and data

## 1. Task / objective
The objective of Mission 5 was to master computer data representation. This included performing manual conversions between Decimal (base-10), Binary (base-2), and Hexadecimal (base-16) number systems, verifying calculations programmatically in Python, creating an interactive CLI number converter (`number_converter.py`), and analyzing how text is encoded using ASCII and Unicode (UTF-8).

## 2. Work completed
- Performed step-by-step manual conversions for seven numerical problems with detailed working.
- Verified all manual mathematical results using Python's built-in conversion functions (`bin()`, `hex()`, and `int()`).
- Developed, tested, and documented `mission-05-numbers-data/number_converter.py`.
- Researched ASCII decimal code mappings and answered core questions on character encoding.

## 3. Commands / tools used
- Python Interactive Shell / REPL: Executed mathematical conversions and verified truth values.
- `mission-05-numbers-data/number_converter.py`: Custom interactive conversion script.

## 4. My understanding

### Task 5.1 — Convert Numbers by Hand

#### 1. Convert decimal 13 to binary
- Use successive division by 2, recording remainders:
  - 13 ÷ 2 = 6, remainder **1**
  - 6 ÷ 2 = 3, remainder **0**
  - 3 ÷ 2 = 1, remainder **1**
  - 1 ÷ 2 = 0, remainder **1**
- Reading remainders from bottom to top: **`1101₂`**

#### 2. Convert decimal 25 to binary
- Successive division by 2:
  - 25 ÷ 2 = 12, remainder **1**
  - 12 ÷ 2 = 6, remainder **0**
  - 6 ÷ 2 = 3, remainder **0**
  - 3 ÷ 2 = 1, remainder **1**
  - 1 ÷ 2 = 0, remainder **1**
- Reading remainders from bottom to top: **`11001₂`**

#### 3. Convert binary 1010 to decimal
- Multiply each bit by its positional weight ($2^n$):
  - $(1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)$
  - $= (1 \times 8) + (0 \times 4) + (1 \times 2) + (0 \times 1)$
  - $= 8 + 0 + 2 + 0 = \mathbf{10_{10}}$

#### 4. Convert binary 1101 to decimal
- Positional weights:
  - $(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$
  - $= (1 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1)$
  - $= 8 + 4 + 0 + 1 = \mathbf{13_{10}}$

#### 5. Convert hexadecimal A to decimal
- In hexadecimal, digits 0–9 represent 0–9, and letters A–F represent 10–15:
  - $\text{A}_{16} = \mathbf{10_{10}}$

#### 6. Convert hexadecimal 1F to decimal
- Positional weights in base 16 ($16^1, 16^0$), where $\text{F} = 15$:
  - $(1 \times 16^1) + (15 \times 16^0)$
  - $= 16 + 15 = \mathbf{31_{10}}$

#### 7. Convert binary 1111 to hexadecimal
- Group into 4 bits (nibble) and evaluate:
  - $(1 \times 8) + (1 \times 4) + (1 \times 2) + (1 \times 1) = 15_{10}$
  - In base 16, decimal 15 is represented by: **`F₁₆`**

---

### Task 5.2 — Verify Using Python

| Expression Tested | Python Output | Matches Manual Calculation? |
| :--- | :--- | :---: |
| `bin(13)` | `'0b1101'` | Yes |
| `bin(25)` | `'0b11001'` | Yes |
| `int('1010', 2)` | `10` | Yes |
| `int('1101', 2)` | `13` | Yes |
| `int('A', 16)` | `10` | Yes |
| `int('1F', 16)` | `31` | Yes |
| `hex(0b1111)` | `'0xf'` | Yes |

---

### Task 5.3 — Build a Small Number Converter
The program `number_converter.py` prompts the user for a decimal integer, validates input, and displays formatted binary and hexadecimal equivalents.

**Test Runs:**

| Test Number (Input) | Binary Output | Hexadecimal Output |
| :---: | :--- | :--- |
| **42** | `0b101010` (Raw: `101010`) | `0x2A` (Raw: `2A`) |
| **255** | `0b11111111` (Raw: `11111111`) | `0xFF` (Raw: `FF`) |
| **1024** | `0b10000000000` (Raw: `10000000000`) | `0x400` (Raw: `400`) |

**Explanation of Functions:**
- `bin(x)`: Converts an integer `x` into a binary string prefixed with `'0b'`. It computes the base-2 positional bit representation.
- `hex(x)`: Converts an integer `x` into a lowercase hexadecimal string prefixed with `'0x'`. It computes the base-16 representation, grouping bits into 4-bit nibbles.
- `int(s, base)`: Parses a string representation `s` in the specified numerical `base` back into a standard base-10 integer.

---

### Task 5.4 — How is Text Stored?
- **ASCII Codes**:
  - Uppercase **'A'**: Decimal **65** (Binary: `01000001`)
  - Lowercase **'a'**: Decimal **97** (Binary: `01100001`)
- **Why a computer needs an encoding standard:**
  Computers only store and transmit binary states (0s and 1s). An encoding standard (such as ASCII or Unicode UTF-8) provides a standardized, universal mapping dictionary connecting abstract alphanumeric characters to specific numerical values, ensuring that text authored on one machine renders identically across any computer in the world without corruption.
- **Example of a character not in basic ASCII:**
  The Euro symbol **€** (Unicode `U+20AC`), the Indian Rupee symbol **₹** (Unicode `U+20B9`), or emojis such as **🚀** (Unicode `U+1F680`). Basic ASCII is limited to 7 bits (128 characters), accommodating only standard English letters, digits, and control symbols.

## 5. Difficulties faced
Handling the prefix characters (`0b` and `0x`) returned by Python's native `bin()` and `hex()` functions.

## 6. How I resolved them
Formatted the converter output to display both standard prefixed notation and sliced raw representations (`[2:]`) with uppercase formatting for readability.

## 7. Evidence / files
- Converter script: `mission-05-numbers-data/number_converter.py`
- Mission documentation: `mission-05-numbers-data/README.md`
- Evidence log: `evidence/converter_tests.txt`

## 8. Commit details
- **Commit Message**: `Build number converter and practise data representation`
- **Confirmation**: Script, tests, and documentation staged and committed to branch `main`.
