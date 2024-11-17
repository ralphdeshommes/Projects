from elements import *
from tkinter import *

element = [hydrogen,helium,lithium,beryllium,boron,carbon,nitrogen,oxygen,fluorine,sodium,magnesium,aluminium,silicon,phosphorus,sulfur,chlorine,argon]





compounds = {
    "water": [hydrogen,hydrogen, oxygen],
    "triflourine" : [fluorine, fluorine, fluorine],
    "ammonia" : [fluorine, fluorine, fluorine],
    "carbon dioxide" : [carbon, oxygen, oxygen]
}

def element_count(compound_name):
    check = []
    details = ""
    compound = compounds[compound_name]
    for element in compound:
        if element not in check:
            details += f"({compound.count(element)} {element.name})" + "\n"
            check.append(element)
    return(details)
# want to count the amount of elements inside of the compound

def compound_element_details(compound_name):
    if compound_name not in compounds:
        return()
    details = ""
    compound = compounds[compound_name]
    details += (f"Compound {compound_name} elemental makeup:") + "\n"
    details += element_count(compound_name)
    check = []
    for element in compound:     
        if element.name not in check:
            details += (f"{element.name}({element.symbol})\natomic number: {element.atomic_number}\natomic mass: {element.atomic_mass}\n")
            check.append(element.name)
    details += mol_conversion(compound_name)
    return(details)

            
def mol_conversion(compound_name):
    details = ""
    compound = compounds[compound_name]
    total = 1
    for element in compound:
        total += element.atomic_mass
    
    details += (f"the total mass : {compound_name} {total:.2f}")
    return(details)





def main():
    def compound_detail_entry():
        if (f"{entry.get()}") not in compounds:
            label_blank_name.config(font="1",text="Not in the list please try again")
            detail_label.config(text="")
        else: 
            label_blank_name.config(text=f"{entry.get().upper()}")
            detail_label.config(text=f"{compound_element_details(entry.get())}")
        
       
    
    def element_detail_entry():
        element_button.config(text=f"{(entry.get()).capitalize()}")


    window = Tk()
    window.geometry("300x300")
    window.title("Compound/Element details")
    label = Label(window,text="Enter Element or compound")
    label.pack()
    entry = Entry(window)
    entry.pack()
    testing = entry.get()
    print(testing)
    frame = Frame(window)
    frame.pack()
    element_button = Button(frame, text="Element",command=element_detail_entry)
    element_button.pack(side=LEFT)
    compound_button = Button(frame, text="Compound", command= compound_detail_entry)
    compound_button.pack(side=RIGHT)
    label_blank_name = Label(window,font="80")
    label_blank_name.pack()
    detail_label = Label(window)
    detail_label.pack()
    
      

    


   

    window.mainloop()



main()
    
