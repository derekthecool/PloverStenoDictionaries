"""

Add
Apply
Assert
Backup
BackupToAAD
Block
Checkpoint
Clear
Close
Compare
Complete
Compress
Confirm
Connect
Convert
ConvertFrom
ConvertTo
Copy
Debug
Delete
Disable
Disconnect
Dismount
Edit
Enable
Enter
Exit
Expand
Export
Find
Flush
ForEach
Format
Get
Grant
Group
Hide
Import
Initialize
Install
Invoke
Join
Lock
Measure
Merge
Mount
Move
New
Open
Optimize
Out
Pop
Protect
Publish
Push
Read
Receive
Register
Remove
Rename
Repair
Reset
Resize
Resolve
Restart
Restore
Resume
Revoke
Save
Select
Send
Set
Show
Sort
Split
Start
Stop
Suspend
Switch
Sync
Tee
Test
Trace
Unblock
Undo
Uninstall
Unlock
Unprotect
Unregister
Update
Use
Wait
Where
Win
Write
"""

import random
import datetime

# Length of the longest supported key (number of strokes).
LONGEST_KEY = 1

# Lookup function: return the translation for <key> (a tuple of strokes)
# or raise KeyError if no translation is available/possible.


def lookup(key):
    assert len(key) <= LONGEST_KEY

    chord = key[0]

    if len(key) != 1:
        raise KeyError

    if chord == "STR":
        return f"{datetime.datetime.now()}"
    if chord == "STK":
        phrases = ["hello", "bye"]
        return random.choice(phrases)


# Optional: return an array of stroke tuples that would translate back
# to <text> (an empty array if not possible).


def reverse_lookup(text):
    return []
