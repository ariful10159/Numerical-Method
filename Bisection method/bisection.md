# Bisection Method — সমীকরণের মূল (root) খোঁজার সহজ পদ্ধতি (বাংলায়)

এই নোটে Bisection পদ্ধতির সংজ্ঞা, কাজের ধরণ, ধাপে ধাপে অ্যালগরিদম, একটি উদাহরণ, সুবিধা ও অসুবিধা এবং অধ্যয়নের টিপস দেয়া আছে।

## 1. Bisection Method কি?
- Bisection হল একটি bracket-based numerical পদ্ধতি যা continuous ফাংশনের জন্য একটি interval [a, b] যেখানে f(a) এবং f(b) ভিন্ন সাইন (sign) হয় — অর্থাৎ f(a)*f(b) < 0 — ধরে সেই interval-এ root (একটি শূন্য) আছে বলে নিশ্চিত হয়।
- পদ্ধতির মূল ধারণা: interval কে ধারাবাহিকভাবে দু ভাগ করে root-এর পাশে থাকা অংশটি বেছে নেওয়া যাতে interval ধীরে ধীরে সংকুচিত হয়ে শূন্যবিন্দুতে পৌছে যায়।

## 2. কেন Bisection ব্যবহার করব?
- নির্ভরযোগ্যতা: যদি শুরুতে [a,b] তে sign change থাকে, তাহলে পদ্ধতিটি নিশ্চিতভাবে একটি root খুঁজে পাবে (converges)।
- সহজতা: সূত্র সহজ ও implementation তে ভুল হওয়ার সুযোগ কম।
- যখন আপনি জানেন যে একটি root আছে (sign change) কিন্তু derivative বা অন্যান্য তথ্য নেই, তখন Bisection ভাল।

## 3. অ্যালগরিদম (ধাপে ধাপে)
1. নির্বাচন করুন একটি interval [a, b] যেখানে f(a)*f(b) < 0।
2. মাঝবিন্দু n = (a + b)/2 নির্ণয় করুন।
3. যদি f(n) == 0 (বা |f(n)| < tol) তবে n হল root।
4. অন্যথায়, যদি f(a)*f(n) < 0 তাহলে বাম অংশে root আছে — b = n; না হলে a = n।
5. ধাপ 2-4 পুনরাবৃত্তি করুন যতক্ষণ না interval দৈর্ঘ্য বা |f(n)| নির্ধারিত tolerance-এর মধ্যে এসে যায়।

## 4. উদাহরণ (হাতেকলমে)
ধরা যাক f(x) = x^3 - x - 2। আমরা দেখব একটি root আছে কিনা: f(1) = -2, f(2) = 4 → sign change আছে → [1,2]

- n1 = (1+2)/2 = 1.5 → f(1.5) = 1.5^3 - 1.5 - 2 = -0.125 → sign(f(1))*sign(f(1.5)) = (+)(-) ??? (উত্তর দেখুন)
- এখানে f(1) = -2 (negative), f(1.5) = -0.125 (negative) → sign same → interval becomes [1.5, 2]
- n2 = (1.5 + 2)/2 = 1.75 → f(1.75) ≈ 1.6094 (positive) → now sign change between 1.5 (negative) and 1.75 (positive) → interval becomes [1.5, 1.75]
- এভাবে চালালে শীঘ্রই root ~ 1.52138 পাওয়া যাবে।

## 5. সুবিধা ও অসুবিধা
- সুবিধা:
	- নির্ভরযোগ্য ও সহজ; convergence গ্যারান্টied (monotonic shrinking of interval) যদি sign change থাকে।
	- derivative প্রয়োজন নেই।
- অসুবিধা:
	- convergence ধীর (linear convergence) — তুলনায় Newton বা secant পদ্ধতির থেকে ধীর।
	- multiple roots বা sign-changing behaviour complicate করতে পারে (যদি f(a) বা f(b) == 0 বা function oscillatory হয়)।

## 6. অধ্যয়ন টিপস
- প্রথমে হাতে 2-3 ধাপ নিজে করে দেখুন যেন interval shrink কিভাবে হচ্ছে বোঝা যায়।
- টলারেন্স দুইভাবে পরীক্ষা করুন: interval width (b-a) < tol এবং |f(mid)| < tol — সাধারণত interval width দিয়ে কেটে দেবেন।
- যদি দ্রুত ফলপ্রসূ পদ্ধতি চান এবং derivative পাওয়া যায়, Newton method প্রাধান্য দিন; কিন্তু Newton ব্যর্থ হতে পারে যদি initial guess খারাপ হয় — তখন bisection নিরাপদ ব্যাকআপ।



