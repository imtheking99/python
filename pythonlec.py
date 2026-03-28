name = "Alice"
score = 98.5


# — Method 1: % operator (OLD, avoid) —
msg1 = "Hello %s, you scored %.1f" % (name, score)


# — Method 2: .format() (OK but verbose) —
msg2 = "Hello {}, you scored {:.1f}".format(name, score)


# — Method 3: f-strings (BEST – use this!) —
msg3 = f"Hello {name}, you scored {score:.1f}"


# f-strings support expressions directly
x, y = 10, 3

print(f"{x} ÷ {y} = {x/y:.2f}")  # 10 ÷ 3 = 3.33
print(f"{name.upper()} has {len(name)} chars")


# Debug shortcut (Python 3.8+)
value = 42

print(f"{value=}")  # value=42