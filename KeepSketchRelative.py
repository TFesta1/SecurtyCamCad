import pyperclip

mainLen = 35.69  #the MM length we want to keep it relative to

otherLen = 35.8 #Some other length

calc = otherLen / mainLen

# 12.5x = 17.42

# 17.42/12.5 = 1.3936

# 12.5*1.3936 = 17.42
msg = f"<<PivotBracketPan_Master>>.Constraints.ArcDistAtCenter * {round(calc,3)}" #Put this on some other length to keep it the same, until the mainlength changes
print(f"{mainLen} * {calc} = {otherLen}")
pyperclip.copy(msg)

print(f"Copied to clipboard: {msg}")


# Note, this still has a lot of wire closed issues if you have a mirrored sketch with Z,S (Symmetry tool in sketcher) but we can maybe just scale it instead
# Actually we can't scale the sketch as we need the 4.9mm depth...


