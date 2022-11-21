from bflogoreplacer import replace_logo

with open("proximo.mcm") as f:
    f.write(replace_logo("default.mcm", "logo.png"))