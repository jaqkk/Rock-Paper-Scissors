def main():
    import tkinter as tk
    from tkinter import simpledialog
    from time import sleep
    import random
    import sys

    ROOT = tk.Tk()
    ROOT.geometry("500x500")

    #allowed character list and initializing counts
    rps = ["r", "p", "s" , "R", "P", "S" , " ", "q", "None"]

    tie_count= 0
    win_count=0
    lose_count=0

    font1 =("Times",30,"normal")

    c = True

    #Rock Paper Scissors runtime loop, first input asks for r p s (with random and quit options as well)
    while c == True:
        l1 = tk.Label(ROOT,font=font1,text="W/T/L:"+str(win_count)+" "+str(tie_count)+" "+str(lose_count) )
        l1.grid(row=0,column=0,padx=10,pady=20)

        e1 = tk.Entry(ROOT,   width=20,bg='yellow') # added one Entry box
        e1.grid(row=1,column=2) 
        
        userchoice = simpledialog.askstring(title="Rock Paper Scissors!",
                                  prompt="Rock (r), paper (p), scissors (s)! --- random (Space)  quit (q):")
        #print(userchoice)

        if userchoice == "q" or userchoice == None:
            break

        if userchoice not in rps:
            print("Error! Only letters r, p, s allowed")

        elif len(userchoice) > 1:
            print("Error! Only 1 character max allowed")

        if userchoice == " ":
            userchoice = rps[random.randint(0, 2)]

        

        UC = str(userchoice).lower()
        cpu = rps[random.randint(0, 2)]

        #matchups
        

        if UC == cpu:
            tie_count+=1
            print("Tie!")
            print("Your input was:", UC)
            print("Computer choice was:", cpu)
            continue

        elif UC == "r" and cpu == "s" or UC == "s" and cpu == "p" or UC== "p" and cpu == "r":
            win_count+=1
            print("Winner!")
            print("Your input was:", UC)
            print("Computer choice was:", cpu)
            continue

        elif UC == "r" and cpu == "p" or UC == "s" and cpu == "r" or UC== "p" and cpu == "s":
            lose_count+=1
            print("Loser!")
            print("Your input was:", UC)
            print("Computer choice was:", cpu)
            continue
            
        #continue/quit
        #cont = simpledialog.askstring(title="Rock Paper Scissors!",
                                  #prompt="Rock (x), paper (p), scissors (s)! --- random (Space)  quit (q):  ")
        #if cont == "q":
            #c = False
        #
    print("\n Wins:" , win_count, "\n Loses:" , lose_count, "\n Ties:" , tie_count)
    sleep(5)
    sys.exit()
    ROOT.mainloop()

if __name__ == "__main__":
    main()

