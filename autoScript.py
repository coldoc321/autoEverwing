import time, os, sys
import PIL, signal
from contextlib import contextmanager

def get_pixel_colour(i_x, i_y):
    import PIL.Image # python-imaging
    import PIL.ImageStat # python-imaging
    import Xlib.display # python-xlib
    o_x_root = Xlib.display.Display().screen().root
    o_x_image = o_x_root.get_image(i_x, i_y, 1, 1, Xlib.X.ZPixmap, 0xffffffff)
    o_pil_image_rgb = PIL.Image.frombytes("RGB", (1, 1), o_x_image.data, "raw", "BGRX")
    lf_colour = PIL.ImageStat.Stat(o_pil_image_rgb).mean
    return tuple(map(int, lf_colour))

def raise_timeout(signum, frame):
    raise TimeoutError

@contextmanager
def timeout(time):
    # Register a function to raise a TimeoutError on the signal.
    signal.signal(signal.SIGALRM, raise_timeout)
    # Schedule the signal to be sent after ``time``.
    signal.alarm(time)

    try:
        yield
    except TimeoutError:
        os.system('cnee --replay -f refresh.xnr --time 0.1')
        pass
    finally:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        # Unregister the signal so it won't be triggered
        # if the timeout is not reached.

startSec=2.5
print('start in {} seconds ...'.format(startSec))

print('you can specify [shard time] to do shard getting.')
print('you can specify [plan A(default) B].')
time.sleep(startSec)
shard=False
plan='A'
if len(sys.argv) > 1:
    try:
        shardTime=int(sys.argv[1])
        shard=True
    except:
        plan=sys.argv[1]
if shard:
    for i in range(shardTime):
        os.system('cnee --replay -f shardStart.xnr --time 0.1')
        while True:
            os.system('cnee --replay -f shardClick.xnr --time 0.01')
            if get_pixel_colour(1099, 878) == (88, 211, 0):
                break
else:
    while True:
        if plan == 'B':
            if get_pixel_colour(1229, 233) == (185, 32, 31):
                os.system('cnee --replay -f closeEventB.xnr --time 0.1')
            if get_pixel_colour(1200, 318) == (189, 34, 33):
                os.system('cnee --replay -f closeEventB2.xnr --time 0.1')
            if get_pixel_colour(1203, 318) == (181, 30, 29):
                os.system('cnee --replay -f closeEventB3.xnr --time 0.1')
            if get_pixel_colour(1218, 237) == (191, 35, 34):
                os.system('cnee --replay -f closeEventB4.xnr --time 0.1')
        elif plan == 'A':
            while True:
                time.sleep(1.5)
                if get_pixel_colour(1230, 233) == (185, 33, 32):
                    os.system('cnee --replay -f closeEventA.xnr --time 0.1')
                    time.sleep(2)
                    continue
                if get_pixel_colour(1223, 231) == (180, 30, 29):
                    os.system('cnee --replay -f closeEventA2.xnr --time 0.1')
                    time.sleep(2)
                    continue
                if get_pixel_colour(1215, 318) == (183, 31, 30):
                    os.system('cnee --replay -f closeEventA3.xnr --time 0.1')
                    time.sleep(2)
                    continue
                break
            if get_pixel_colour(1066, 982) == (3, 187, 246):
                os.system('cnee --replay -f closeEventA.xnr --time 0.1')
        if get_pixel_colour(1214, 316) == (183, 32, 31):
            os.system('cnee --replay -f closeAdd.xnr --time 0.1')
            time.sleep(0.3)
        if get_pixel_colour(1214, 233) == (186, 33, 32):
            os.system('cnee --replay -f closeAdd2.xnr --time 0.1')
            time.sleep(0.3)
        if get_pixel_colour(1231, 231) == (184, 32, 31):
            os.system('cnee --replay -f closeAdd3.xnr --time 0.1')
            time.sleep(0.3)
        if plan == 'B':
            os.system('cnee --replay -f startB.xnr --time 0.1')
        elif plan == 'A':
            os.system('cnee --replay -f startA.xnr --time 0.1')
        with timeout(180):
            while True:
                if plan == 'B' and get_pixel_colour(1195, 257) == (180, 30, 29):
                    os.system('cnee --replay -f closeContinueB.xnr --time 0.1')
                    break
                elif plan == 'A' and get_pixel_colour(1210, 256) == (186, 33, 32):
                    os.system('cnee --replay -f closeContinueA.xnr --time 0.1')
                    break
                time.sleep(0.3)
            while True:
                if plan == 'B' and get_pixel_colour(1055, 988) == (2, 174, 229):
                    os.system('cnee --replay -f closeBragB.xnr --time 0.1')
                    break
                elif plan == 'A' and  get_pixel_colour(1066, 982) == (3, 187, 246):
                    os.system('cnee --replay -f closeBragA.xnr --time 0.1')
                    break
                time.sleep(0.3)




# print (get_pixel_colour(1210, 256))
#
# print('you can specify [shard time] to do shard getting.')
# time.sleep(startSec)
# shard=False
# if len(sys.argv) > 1:
#     shardTime=int(sys.argv[1])
#     shard=True
# if shard:
#     for i in range(shardTime):
#         os.system('cnee --replay -f shard.xnr --time 1')
# else:
#     while True:
#         os.system('cnee --replay -f events1.xnr --time 1')
#
#         time.sleep(130.2)
#
#         os.system('cnee --replay -f events2.xnr --time 1')
