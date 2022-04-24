from contextlib import nullcontext
from nanoleafapi import Nanoleaf 
from nanoleafapi import NanoleafDigitalTwin
from nanoleafapi import RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, BLUE, PINK, PURPLE, WHITE
import pandas as pd
import numpy as np
from io import StringIO as io
class JarvisNanoleaf:
    def activateNanoleaf():
        nl = Nanoleaf("192.168.1.239")
        #print("Hello, I am JARVIS")
        #nl.set_color((RED))
        digital_twin = NanoleafDigitalTwin(nl)
        panel_ids=nl.get_ids()
        #print(panel_ids[0])
        panelone = ""
        i=-1
        NanQuestion = input("Certainly Sir, would you like me to open a preset or are you making a new design?")    
        if NanQuestion == ("custom"):
            while i < 16:
                i+=1
                PQ1 = input("Panel Color?")
                if PQ1 == ("red"):
                    PQ1.lower()
                    panelone = (255, 0, 0)
                    digital_twin.set_color(panel_ids[i], (panelone))
                    digital_twin.sync()
                elif PQ1 == ("orange"):
                    panelone = ORANGE
                    digital_twin.set_color(panel_ids[i], (panelone))
                    digital_twin.sync()
                elif PQ1 == ("yellow"):
                    panelone = YELLOW
                    digital_twin.set_color(panel_ids[i], (panelone))
                    digital_twin.sync()
                elif PQ1 == ("green"):
                    panelone = GREEN
                    digital_twin.set_color(panel_ids[i], (panelone))
                    digital_twin.sync()
                elif PQ1 == ("blue"):
                    panelone = BLUE
                    digital_twin.set_color(panel_ids[i], (panelone))
                    digital_twin.sync()
                elif PQ1 == ("pink"):
                    panelone = PINK
                    digital_twin.set_color(panel_ids[i], (panelone))
                    digital_twin.sync()
                elif PQ1 == ("purple"):
                    panelone = PURPLE
                    digital_twin.set_color(panel_ids[i], (panelone))
                    digital_twin.sync()
                elif PQ1 == ("white"):
                    panelone = WHITE
                    digital_twin.set_color(panel_ids[i], (panelone))
                    digital_twin.sync()
            savequestion = input("Would you like to save this preset?")
            if savequestion == ("yes"):
                namequestion = input("Yes Sir, what would you like to name this preset?")
                presets = pd.DataFrame([[digital_twin.get_color(panel_ids[0])],[digital_twin.get_color(panel_ids[1])],[digital_twin.get_color(panel_ids[2])],[digital_twin.get_color(panel_ids[3])],[digital_twin.get_color(panel_ids[4])],[digital_twin.get_color(panel_ids[5])],[digital_twin.get_color(panel_ids[6])],[digital_twin.get_color(panel_ids[7])],[digital_twin.get_color(panel_ids[8])],[digital_twin.get_color(panel_ids[9])],[digital_twin.get_color(panel_ids[10])],[digital_twin.get_color(panel_ids[11])],[digital_twin.get_color(panel_ids[12])],[digital_twin.get_color(panel_ids[13])],[digital_twin.get_color(panel_ids[14])],[digital_twin.get_color(panel_ids[15])],[digital_twin.get_color(panel_ids[16])]])
                numpy_array = presets.to_numpy()
                #numpy_array.replace(',','', regex=True, inplace=True)
                newpreset = np.savetxt(namequestion + ".txt", numpy_array, fmt = "%s")
                print(namequestion)
            elif savequestion == ("no"):
                exit()

        if NanQuestion == ("preset"):
            WO = input("Of course sir, which preset would you like me to bring up today?")
            #with open(WO + ".txt") as selectfile:
            #selectfile = open(WO + ".txt",'r')
            RES = ("Great choice sir!")
            selectfile = open(WO + ".txt", "r")
            content = selectfile.read()
            content_list = content.splitlines()
            selectfile.close()
            #print(content_list[0])
            n=-1
            while n < 16:
                n+=1
                firstpanel = content_list[n]
                panelone = (0, 255, 0)
                #print(content_list[n])
                #newple = tuple(map(str, content_list[n].splitlines()))
                #print(content_list[n])
                bad_chars = ['(', ')', ',']
                split_string = content_list[n].split(":", 2)   
                substring = split_string[0] 
                for i in bad_chars :
                    substring = substring.replace(i, '')
                res = tuple(map(int, substring.split(' ')))    
                print(res)
                #nl.set_color(content_list[n])
                digital_twin.set_color(panel_ids[n], (res))
                #digital_twin.set_color(panel_ids[1], (content_list[1]))
                digital_twin.sync()
            exit()