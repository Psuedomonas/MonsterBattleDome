#!/usr/bin/python3.8
#filename: MenuOptions.py
'''
By Nicholas Zehm
2021-3-23
Menu Options
filename: MenuOptions.py
version 0.1
for GUI.py version 0.1
'''

import monster
import tkinter


'''
### Classes ###
'''
class AddToPen:
    self.health = 10
    self.stamina = 10
    self.exp = 0
    self.lvl = 0
    
    def __init__():
        top = Toplevel(root)
        top.title('Lets Make a monster!')
        
        lbl_name = Label(text='Name:').pack()
        entry_name = Entry().pack()
        
        btn_check = Button(text='Submit', command = addSubmit).pack()
        
        lbl_stats = Label(text='').pack()
        
        btn_saveToPen = Button(text='Save monster to pen', state = DISABLED, command = saveToPen).pack()
        
        btn_cancel = Button(text='Cancel', command = __del__).pack()


    def addSubmit():
        try:
            name = entry_name.get()
        except:
            lbl_stats.config(text = "Name assignment failed, clear name or try a different one")
        
        if name in pen:
            lbl_stats.config(text = "Name already in pen")
        
        else:
            lbl_stats.config(text = "{0} is level {1}, has {2} health, {3} stamina, and {4} experience".format(name, self.lvl, health, stamina, exp))
            btn_saveToPen.config(state = NORMAL)

    
    def saveToPen():      
        monster = Monster(health, stamina, exp, lvl)
        
        pen[name]

        del monster
        
        stats = {name, self.health, self.stamina, self.exp, self.lvl}
        return stats

        
    def __del__():
        destroy.top()
  
    
class DMAddToPen:
    def __init__():
        self.m_health = 0
        self.health = 0
        self.stamina = 0
        self.m_stamina = 0
        self.exp = 0
        self.level = 0
        
        top = Toplevel(root)
        top.title('Dome Master: Make a monster')
        
        lbl_name = Label(text='Name:').pack()
        entry_name = Entry().pack()
        
        lbl_m_health = Label(text='Maximum health:').pack()
        entry_m_health = Entry().pack()
        
        lbl_health = Label(text="Current Health:").pack()
        entry_health = Entry().pack()
        
        lbl_m_stamina = Label(text="Maximum stamina").pack()
        entry_m_stamina = Entry().pack()
        
        lbl_stamina = Label(text="Stamina").pack()
        entry_stamina = Entry().pack()
        
        lbl_exp = Label(text="Experience").pack()
        entry_exp = Entry().pack()
        
        lbl_level = Label(text="Level").pack()
        entry_level = Entry().pack()
        
        btn_check = Button(text='Submit', command=addSubmit).pack()
        
        lbl_stats = Label(text='').pack()
        
        btn_saveToPen = Button(text='Save monster to pen', state=DISABLED, command=saveToPen).pack()    

    
    def addSubmit():
        if name in pen:
            lbl_stats.config(text = "Name already in pen")
        
        else:
            lbl_stats.config(text = "{0} is level {1}, has {2} health, {3} stamina, and {4} experience".format(name, lvl, health, stamina, exp))
            btn_saveToPen.config(state = NORMAL)

    
    def saveToPen():      
        monster = Monster(health, stamina, exp, lvl)
        
        pen[name]
        
        del monster

        stats = {name, self.health, self.stamina, self.exp, self.lvl}
        return stats
        
    def __del__():
        destroy.top()


class KillMonster:
    def __init__():
        top = Toplevel(root)
        top.title('Slaughterhouse')


    def __del__():
        destroy.top()
        
