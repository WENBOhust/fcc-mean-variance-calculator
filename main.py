from mean_var_std import calculate

try:
    result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print("✅ Test passed!")
    for key, value in result.items():
        print(f"{key}: {value}")
except Exception as e:
    print("❌ Error:", e)
Add test script
