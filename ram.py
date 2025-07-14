import psutil

def read_ram():
    mem = psutil.virtual_memory()

    print("💾 RAM Info:")
    print(f"Total RAM     : {mem.total / (1024 ** 3):.2f} GB")
    print(f"Available RAM : {mem.available / (1024 ** 3):.2f} GB")
    print(f"Used RAM      : {mem.used / (1024 ** 3):.2f} GB")
    print(f"Free RAM      : {mem.free / (1024 ** 3):.2f} GB")
    print(f"RAM Usage     : {mem.percent}%")

# Run it
read_ram()
