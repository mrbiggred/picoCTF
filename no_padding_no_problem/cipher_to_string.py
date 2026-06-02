# Converts the decrypted long from the oracle to a string.  
# Copy the long from the oracle into the msg_long and run the script.

from Crypto.Util.number import long_to_bytes, bytes_to_long

msg_long = 424989173022284116915948047437221254270678170627990120377863759056072717562795964312386693033362856505871000276162854341764296211127

m = long_to_bytes(msg_long)
print(m.decode("utf-8", errors="replace"))
