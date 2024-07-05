from speedtest import Speedtest
wifi = Speedtest()

print("Getting Download speed....")
download = wifi.download()
print(f"Download: {download /1024/1024:.2f} mbps")

print("Getting Upload speed....")
upload = wifi.upload()
print(f"Upload: {upload /1024/1024:.2f} mbps")
