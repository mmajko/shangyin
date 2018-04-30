from shangyin.interface import display, rfid
import shangyin.storage as storage
import time

# Connect database and RFID reader
db = storage.connect()
db_cur = db.cursor()
reader = rfid.init()

# Init database if needed
if storage.need_setup(db_cur):
    storage.setup(db_cur)

# Init LCD display
disp = display.Display(None)

disp.set(0, 'shangyin v0.1 T')
disp.set(1, 'Hello! The machine is ready for some work. Tap your card now.')

db.close()

while True:
    # Wait for user's card
    cuid = rfid.wait_for_card(reader)

    # Check if it's a valid card
    if not cuid == None:
        disp.set(1, 'Card: {}'.format(cuid))

    # Log a coffee for this card
    storage.log_coffee_to_uid(db_cur, cuid)

    # Update the display
    disp.update()
    time.sleep(2)

    # Back to standby display
    disp.set(1, 'Hello! The machine is ready for some work. Tap your card now.')
    disp.update()