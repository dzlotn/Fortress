// Common passwords list (subset of the full list for client-side checking)
export const COMMON_WORDS = new Set([
  "123456","password","12345678","qwerty","123456789","12345","1234","111111",
  "1234567","dragon","123123","baseball","abc123","football","monkey","letmein",
  "696969","shadow","master","666666","qwertyuiop","123321","mustang","1234567890",
  "michael","654321","superman","1qaz2wsx","7777777","121212","000000","qazwsx",
  "123qwe","killer","trustno1","jordan","jennifer","zxcvbnm","asdfgh","hunter",
  "buster","soccer","harley","batman","andrew","tigger","sunshine","iloveyou",
  "charlie","robert","thomas","hockey","ranger","daniel","starwars","george",
  "computer","michelle","jessica","pepper","1111","555555","11111111","131313",
  "freedom","777777","pass","maggie","159753","aaaaaa","ginger","princess",
  "joshua","cheese","amanda","summer","love","ashley","6969","nicole","chelsea",
  "matthew","access","yankees","987654321","dallas","austin","thunder","taylor",
  "matrix","william","corvette","hello","martin","heather","secret","merlin",
  "diamond","hammer","silver","222222","88888888","anthony","justin","test",
  "bailey","patrick","internet","scooter","orange","11111","golfer","cookie",
  "richard","samantha","guitar","jackson","whatever","mickey","chicken","sparky",
  "snoopy","maverick","phoenix","camaro","peanut","morgan","welcome","falcon",
  "cowboy","ferrari","samsung","smokey","steelers","joseph","mercedes","dakota",
  "arsenal","eagles","melissa","boomer","spider","nascar","monster","tigers",
  "yellow","123123123","gateway","marina","diablo","bulldog","qwer1234","compaq",
  "purple","hardcore","banana","junior","hannah","123654","porsche","lakers",
  "iceman","money","cowboys","987654","london","tennis","999999","coffee","scooby",
  "0000","miller","boston","fuckoff","brandon","yamaha","chester","mother","forever"
]);

export interface PasswordEntry {
  id: string;
  program: string;
  username: string;
  password: string;
}

export interface GenerationLog {
  message: string;
  type: 'info' | 'success' | 'warning' | 'error';
}

// Find a random prime number between min and max (ported from Python primeNumGen)
export function findRandomPrime(min = 10, max = 100): number {
  while (true) {
    const num = Math.floor(Math.random() * (max - min + 1)) + min;
    let isPrime = true;
    for (let j = 2; j <= Math.floor(num / 2); j++) {
      if (num % j === 0) { isPrime = false; break; }
    }
    if (isPrime) return num;
  }
}

// Check for duplicate consecutive chars and ASCII-adjacent chars (ported from pwdCheckCons)
function checkConsecutiveChars(pwd: string): boolean {
  for (let i = 0; i < pwd.length - 1; i++) {
    if (pwd[i] === pwd[i + 1]) return false;
    if (Math.abs(pwd.charCodeAt(i) - pwd.charCodeAt(i + 1)) === 1) return false;
  }
  return true;
}

// Check keyboard proximity (ported from pwdCheckKeyboard)
function checkKeyboardProximity(pwd: string): boolean {
  const keyboardRows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"];
  const keyboardColLeft: Record<string, string> = {
    "1":"1qaz","2":"2wsx","3":"3edc","4":"4rfv","5":"5tgb",
    "6":"6yhn","7":"7ujm","8":"8ik","9":"9ol","0":"0p",
  };
  const keyboardColRight: Record<string, string> = {
    "1":"pl","2":"0okm","3":"9ijn","4":"8uhb","5":"7ygv",
    "6":"6tfc","7":"5rdx","8":"4esz","9":"3wa","0":"2q",
  };

  for (let i = 0; i < pwd.length - 1; i++) {
    const a = pwd[i].toLowerCase();
    const b = pwd[i + 1].toLowerCase();
    for (const row of keyboardRows) {
      if (row.includes(a) && row.includes(b) && Math.abs(row.indexOf(a) - row.indexOf(b)) === 1) return false;
    }
    for (const row of Object.values(keyboardColLeft)) {
      if (row.includes(a) && row.includes(b) && Math.abs(row.indexOf(a) - row.indexOf(b)) === 1) return false;
    }
    for (const row of Object.values(keyboardColRight)) {
      if (row.includes(a) && row.includes(b) && Math.abs(row.indexOf(a) - row.indexOf(b)) === 1) return false;
    }
  }
  return true;
}

// Check against common words list (ported from checkCommonWords2)
export function checkCommonWords(pwd: string): boolean {
  const lower = pwd.toLowerCase();
  for (const word of COMMON_WORDS) {
    if (lower.includes(word)) return false;
  }
  return true;
}

// Validate password meets all constraints
function validatePassword(pwd: string): boolean {
  return checkConsecutiveChars(pwd) && checkKeyboardProximity(pwd) && checkCommonWords(pwd);
}

// Generate a password of given length (ported from pwdCreation)
export function generatePassword(num: number): string {
  const letters = "abcdefghijklmnopqrstuvwxyz";
  const digits = "1234567890";
  while (true) {
    const pwd: string[] = [];
    let prevType: number | null = null;
    let consecutiveCount = 0;
    for (let i = 0; i < num; i++) {
      let placed = false;
      while (!placed) {
        const caseType = Math.floor(Math.random() * 3);
        if (caseType === 0 && (prevType !== 0 || consecutiveCount < 3)) {
          pwd.push(digits[Math.floor(Math.random() * 10)]);
          consecutiveCount = prevType === 0 ? consecutiveCount + 1 : 1;
          prevType = 0; placed = true;
        } else if (caseType === 1 && (prevType !== 1 || consecutiveCount < 3)) {
          pwd.push(letters[Math.floor(Math.random() * 26)]);
          consecutiveCount = prevType === 1 ? consecutiveCount + 1 : 1;
          prevType = 1; placed = true;
        } else if (caseType === 2 && (prevType !== 2 || consecutiveCount < 3)) {
          pwd.push(letters[Math.floor(Math.random() * 26)].toUpperCase());
          consecutiveCount = prevType === 2 ? consecutiveCount + 1 : 1;
          prevType = 2; placed = true;
        }
      }
    }
    const pwdStr = pwd.join('');
    if (validatePassword(pwdStr)) return pwdStr;
  }
}

// Helper for length score (ported from f and s functions in Python)
function f(x: number): number {
  return Math.round(Math.abs(Math.sqrt(x + 0.3 * Math.log(x + 0.01)) - 0.308) * 100) / 100;
}

function lengthScore(x: number): number {
  if (x === 150) return 10;
  return Math.round((f(x) - 2.96) * (125 / 113) * 100000) / 100000;
}

// Character distribution score (ported from charDistScore, counts digits/upper/lower)
function charDistributionScore(pwd: string): number {
  if (pwd.length === 0) return 0;
  let digits = 0, upper = 0, lower = 0;
  for (const ch of pwd) {
    if (ch >= '0' && ch <= '9') digits++;
    else if (ch >= 'A' && ch <= 'Z') upper++;
    else if (ch >= 'a' && ch <= 'z') lower++;
  }
  const threshold = pwd.length / 3;
  const diffs = Math.abs(threshold - digits) + Math.abs(threshold - upper) + Math.abs(threshold - lower);
  const totalQuant = (diffs / pwd.length) * 100;
  return Math.max(0, Math.round((100 - totalQuant) * 1000) / 1000);
}

// Calculate password entropy (ported from calculatePasswordEntropy)
export function calculateEntropy(pwd: string): { entropy: number; guessTime: number } {
  if (!pwd) return { entropy: 0, guessTime: 0 };
  let charPool = 0;
  let hasLower = false, hasUpper = false, hasDigit = false;
  for (const ch of pwd) {
    if (ch >= 'a' && ch <= 'z') hasLower = true;
    else if (ch >= 'A' && ch <= 'Z') hasUpper = true;
    else if (ch >= '0' && ch <= '9') hasDigit = true;
  }
  if (hasLower) charPool += 26;
  if (hasUpper) charPool += 26;
  if (hasDigit) charPool += 9; // Python uses 9, not 10
  if (charPool === 0) return { entropy: 0, guessTime: 0 };
  const entropy = Math.log2(charPool) * pwd.length;
  const guessTime = Math.pow(2, Math.min(entropy, 1023)); // cap to avoid Infinity
  return { entropy: Math.round(entropy * 100) / 100, guessTime };
}

export interface PasswordScore {
  total: number;
  lengthVal: number;
  commonWordsVal: number;
  charDistVal: number;
  charDistRaw: number;
  entropy: number;
  guessTime: number;
  isCommon: boolean;
  digitCount: number;
  upperCount: number;
  lowerCount: number;
}

// Full password scoring (ported from findPWDInfo/checkStrength)
export function scorePassword(pwd: string): PasswordScore {
  if (!pwd) return {
    total: 0, lengthVal: 0, commonWordsVal: 0, charDistVal: 0, charDistRaw: 0,
    entropy: 0, guessTime: 0, isCommon: false, digitCount: 0, upperCount: 0, lowerCount: 0
  };

  const isCommon = !checkCommonWords(pwd);
  const lenVal = lengthScore(pwd.length);
  const commonWS = isCommon ? 0 : 10;
  const charDistRaw = charDistributionScore(pwd);
  const cDS = Math.round(charDistRaw / 10);
  const { entropy, guessTime } = calculateEntropy(pwd);
  const total = Math.max(Math.round((lenVal * 3.3 + commonWS * 3.4 + cDS * 3.4) * 1000) / 1000, 0);

  let digitCount = 0, upperCount = 0, lowerCount = 0;
  for (const ch of pwd) {
    if (ch >= '0' && ch <= '9') digitCount++;
    else if (ch >= 'A' && ch <= 'Z') upperCount++;
    else if (ch >= 'a' && ch <= 'z') lowerCount++;
  }

  return { total, lengthVal: lenVal, commonWordsVal: commonWS, charDistVal: cDS, charDistRaw, entropy, guessTime, isCommon, digitCount, upperCount, lowerCount };
}

// Simple Caesar-based encryption (ported from encryptPassword — NOT truly secure, educational only)
export function encryptPassword(pwd: string, x: number): string {
  return pwd.split('').map((char, i) => {
    const len = pwd.length;
    const divisor = len - i;
    const shift = (divisor === 0 ? 0 : i % divisor) + x;
    let newOrd = char.charCodeAt(0) + shift;
    if (newOrd > 126) newOrd -= 94;
    return String.fromCharCode(newOrd);
  }).join('');
}

export function decryptPassword(pwd: string, x: number): string {
  return pwd.split('').map((char, i) => {
    const len = pwd.length;
    const divisor = len - i;
    const shift = (divisor === 0 ? 0 : i % divisor) + x;
    let newOrd = char.charCodeAt(0) - shift;
    if (newOrd < 32) newOrd += 94;
    return String.fromCharCode(newOrd);
  }).join('');
}

// localStorage persistence
const STORAGE_KEY = 'fortress_vault';

export function savePasswords(entries: PasswordEntry[]): void {
  const encrypted = entries.map(e => ({
    id: e.id,
    program: e.program,
    username: encryptPassword(e.username, 5),
    password: encryptPassword(e.password, 1),
  }));
  localStorage.setItem(STORAGE_KEY, JSON.stringify(encrypted));
}

export function loadPasswords(): PasswordEntry[] {
  try {
    const data = localStorage.getItem(STORAGE_KEY);
    if (!data) return [];
    const encrypted: PasswordEntry[] = JSON.parse(data);
    return encrypted.map(e => ({
      id: e.id,
      program: e.program,
      username: decryptPassword(e.username, 5),
      password: decryptPassword(e.password, 1),
    }));
  } catch { return []; }
}

// Graphical bar (ported from printStrengthGraphically)
export function strengthBar(score: number): string {
  const filled = Math.round(Math.min(score, 100) / 10);
  return '█'.repeat(filled) + '░'.repeat(Math.max(10 - filled, 0));
}

export function strengthLabel(score: number): string {
  if (score < 20) return 'Very Weak';
  if (score < 40) return 'Weak';
  if (score < 60) return 'Moderate';
  if (score < 80) return 'Strong';
  return 'Very Strong';
}

export function strengthColor(score: number): string {
  if (score < 20) return '#ef4444';
  if (score < 40) return '#f97316';
  if (score < 60) return '#eab308';
  if (score < 80) return '#22c55e';
  return '#10b981';
}

export function formatGuessTime(guessTime: number): string {
  if (!isFinite(guessTime) || guessTime > 1e30) return '> 10³⁰ years';
  const seconds = guessTime / 1e9; // assuming 1 billion guesses/sec
  if (seconds < 1) return 'Instant';
  if (seconds < 60) return `${seconds.toFixed(1)} seconds`;
  if (seconds < 3600) return `${(seconds / 60).toFixed(1)} minutes`;
  if (seconds < 86400) return `${(seconds / 3600).toFixed(1)} hours`;
  if (seconds < 31536000) return `${(seconds / 86400).toFixed(1)} days`;
  const years = seconds / 31536000;
  if (years < 1e6) return `${years.toFixed(0)} years`;
  if (years < 1e9) return `${(years / 1e6).toFixed(1)}M years`;
  return `${(years / 1e9).toFixed(1)}B years`;
}
