boardArr = ["X","X","X",4,5,6,7,8,9]
def aboutToWinCheck():
    aboutToWin = ""
    if boardArr[0:3]==["O","O"]:
        if boardArr[0:3]==["O","O"]:
            aboutToWin = True
        
    
    elif boardArr[3:6]==["O","O"]:
        if boardArr[3:6]==["O","O"]:
            aboutToWin = True
        
    
    elif boardArr[6:9]==["O","O"]:
        if boardArr[6:9]==["O","O"]:
            aboutToWin = True
        

    elif boardArr[0:7:3]==["O","O"]:
        if boardArr[0:7:3]==["O","O"]:
            aboutToWin = True
        

    elif boardArr[1:8:3]==["O","O"]:
        if boardArr[1:8:3]==["O","O"]:
            aboutToWin = True
        

    elif boardArr[2:9:3]==["O","O"]:
        if boardArr[2:9:3]==["O","O"]:
            aboutToWin = True
        

    elif boardArr[0:9:4]==["O","O"]:
        if boardArr[0:9:4]==["O","O"]:
            aboutToWin = True
        
    
    elif boardArr[2:7:2]==["O","O",7] or boardArr[2:7:2]==["O",5,"O"] or boardArr[2:7:2]==[3,"O","O"]:
        if boardArr[2:7:2]==["O","O"]:
            aboutToWin = True

    else:
        aboutToWin = False
        
winCheck()