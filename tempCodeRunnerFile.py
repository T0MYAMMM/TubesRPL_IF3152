hs = leaf.winfo_screenheight()
    x = (ws/2) - (width/2)
    y = (hs/2) - (height/2)
    leaf.geometry("%dx%d+%d+%d" % (width, height, x, y))