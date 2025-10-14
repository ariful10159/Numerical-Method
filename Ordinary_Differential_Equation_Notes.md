
# 📘 Ordinary Differential Equation (ODE) — Full Notes

## 🔹 Definition

An **Ordinary Differential Equation (ODE)** is a differential equation that involves a function of **one independent variable** and its **derivatives**.

> **বাংলায় সংজ্ঞা:**  
> এমন সমীকরণ যেখানে একটি চলক অনুযায়ী কোনো ফাংশনের ডেরিভেটিভ বা পরিবর্তনের হার (rate of change) নির্ণয় করা হয়, সেটাকেই Ordinary Differential Equation বলে।

---

## 🔹 Examples

### 🧩 First Order ODE:
\[
\frac{dy}{dx} = 3x^2 + 2y
\]
এখানে \( y \) হলো dependent variable এবং \( x \) হলো independent variable।

### 🧩 Second Order ODE:
\[
\frac{d^2y}{dx^2} + 3\frac{dy}{dx} + 2y = 0
\]

---

## 🔹 Types of ODE

| Type | Example | Description |
|------|----------|-------------|
| **Linear ODE** | \( \frac{dy}{dx} + P(x)y = Q(x) \) | y এবং এর ডেরিভেটিভের ঘাত ১ |
| **Non-linear ODE** | \( \frac{dy}{dx} = y^2 + x \) | y বা তার ডেরিভেটিভের ঘাত ১-এর বেশি |
| **Homogeneous ODE** | \( \frac{dy}{dx} + 2y = 0 \) | সব টার্মে y এবং এর ডেরিভেটিভ আছে |
| **Non-homogeneous ODE** | \( \frac{dy}{dx} + 2y = e^x \) | এমন টার্ম আছে যা y-এর উপর নির্ভরশীল নয় |

---

## 🔹 Real-Life Applications

### 🚗 1. Motion of an Object (Newton’s 2nd Law)
\[
m \frac{d^2x}{dt^2} = F(x,t)
\]
This is a **2nd order ODE** that describes motion under force.

### 🌡️ 2. Heat Transfer (Newton’s Law of Cooling)
\[
\frac{dT}{dt} = -k(T - T_{env})
\]

### 👥 3. Population Growth
\[
\frac{dP}{dt} = kP \quad \Rightarrow \quad P = P_0 e^{kt}
\]

---

## 🔹 Key Terms

| Term | Meaning |
|------|----------|
| **Ordinary** | Only one independent variable |
| **Differential** | Contains derivatives |
| **Equation** | Expressed in equality form |

---

## 🔹 Quick Summary Table

| Concept | Explanation |
|----------|--------------|
| Independent Variable | Usually x or t |
| Dependent Variable | Function like y(x) |
| Derivative | Rate of change (dy/dx) |
| Order of ODE | Highest derivative present |
| Degree of ODE | Power of highest derivative |

---

## 🔹 Example Problem

**Given:** \( \frac{dy}{dx} = 2x \)  
**Integrate both sides:**  
\[
y = \int 2x \, dx = x^2 + C
\]  
✅ **Solution:** \( y = x^2 + C \)

---

## 🔹 Summary

- ODEs describe how a quantity changes with respect to another variable.  
- Used in physics, biology, economics, and engineering.  
- Solving methods include **Euler’s**, **Picard’s**, **Runge–Kutta**, **Milne’s**, etc.

---

## 🧠 Mnemonic

> “Ordinary → One variable → One rate of change.”

---

### ✍️ Next Topics to Learn

- Euler’s Method  
- Picard’s Method  
- Runge-Kutta Method  
- Milne’s Method  
- Taylor Series Method  

---

**Author:** Ariful Islam  
**Course:** Numerical Methods  
**Topic:** Ordinary Differential Equation (ODE)  
**Language:** English + Bangla (Mixed for understanding)
