import numpy as np
import matplotlib.pyplot as plt

# Function
def f(x):
    return x**3 - 4*x - 9

# Bisection Method with step-by-step output
def bisection(f, a, b, tol=1e-5):
    if f(a) * f(b) >= 0:
        print("Error: f(a) and f(b) must have opposite signs!")
        return None
    
    print(f"\n{'Iteration':<12} {'a':<12} {'b':<12} {'mid':<12} {'f(mid)':<12} {'|b-a|':<12}")
    print("-" * 72)
    
    iteration = 0
    while abs(b - a) > tol:
        mid = (a + b) / 2
        f_mid = f(mid)
        
        iteration += 1
        print(f"{iteration:<12} {a:<12.6f} {b:<12.6f} {mid:<12.6f} {f_mid:<12.6f} {abs(b-a):<12.6f}")
        
        if f(a) * f_mid < 0:
            b = mid
        else:
            a = mid
    
    root = (a + b) / 2
    return root

# Main program - User Input
print("=" * 72)
print("BISECTION METHOD - ROOT FINDER")
print("=" * 72)
print("Function: f(x) = x³ - 4x - 9")
print()

try:
    a = float(input("Enter first value (a): "))
    b = float(input("Enter second value (b): "))
    tol = float(input("Enter tolerance (press Enter for default 1e-5): ") or 1e-5)
    
    # Find root
    root = bisection(f, a, b, tol)
    
    if root is not None:
        print("\n" + "=" * 72)
        print(f"✓ Root found: x ≈ {root:.8f}")
        print(f"✓ f({root:.8f}) = {f(root):.2e}")
        print("=" * 72)
        
        # Plot
        x_min, x_max = min(a, b) - 1, max(a, b) + 1
        x = np.linspace(x_min, x_max, 200)
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, f(x), 'b-', linewidth=2, label='f(x) = x³ - 4x - 9')
        plt.axhline(0, color='red', linestyle='--', alpha=0.7, label='y = 0')
        plt.axvline(root, color='green', linestyle='--', alpha=0.7, label=f'Root = {root:.5f}')
        plt.scatter(root, f(root), color='red', s=100, zorder=5, label=f'f({root:.5f}) ≈ 0')
        plt.scatter([a, b], [f(a), f(b)], color='orange', s=80, zorder=4, label='Initial points')
        
        plt.title("Bisection Method - Root Finding", fontsize=14, fontweight='bold')
        plt.xlabel('x', fontsize=12)
        plt.ylabel('f(x)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.legend(fontsize=10)
        plt.tight_layout()
        plt.show()

except ValueError:
    print("Error: Please enter valid numeric values!")
except Exception as e:
    print(f"Error: {e}")