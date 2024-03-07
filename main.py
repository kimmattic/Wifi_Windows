import subprocess

print(f"\n")
print(f"Your wifi and password on Windows\n ")

wifi = (
    subprocess.check_output(["netsh", "wlan", "show", "profiles"])
    .decode("utf-8")
    .split("\n")
)
d = [i.split(":")[1][1:-1] for i in wifi if "All" in i]
for i in d:
    results = (
        subprocess
        .check_output(["netsh", "wlan", "show", "profile", i, "key=clear"])
        .decode("utf-8")
        .split("\n")
    )
    re = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print("{:<30}|  {:<}".format(i, re[0]))
    except IndexError:
        print("{:<30}|  {:<}".format(i, ""))
