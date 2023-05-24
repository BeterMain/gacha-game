import random
import os

class GachaGame():
    def __init__(self):

        # Character pools

        self.ssrCharacters = [] # 3 SSR
        self.srCharacters = [] # 3 SR
        self.RareCharacters = [] # 3 R
        self.LRCharacters = [] # 3 LR

        path = 'Gacha Game/Characters/'
        # list files in img directory
        files = os.listdir(path)

        for file in files:
            # make sure file is an image
            if file.endswith(( '.png')) and file.startswith('ssr_'):
                self.ssrCharacters.append(path + file)
            elif file.endswith(( '.png')) and file.startswith('sr_'):
                self.srCharacters.append(path + file)
            elif file.endswith(('.png')) and file.startswith('r_'):
                self.RareCharacters.append(path + file)
            elif file.endswith(('.png')) and file.startswith('lr_'):
                self.LRCharacters.append(path + file)

        # Player Characters
        self.userCharacters =[]

    def SingleSummon(self):
        # Single Summon
        # Setting rates
        SSRmaxIndex = len(self.ssrCharacters) -1
        SRmaxIndex = len(self.srCharacters) -1
        RmaxIndex = len(self.RareCharacters) -1
        LrMaxIndex = len(self.LRCharacters) -1
        LrRandomIndex = random.randint(0, LrMaxIndex)
        SSrRandomIndex = random.randint(0, SSRmaxIndex)
        SrRandomIndex = random.randint(0, SRmaxIndex)
        RareRandomIndex = random.randint(0, RmaxIndex)
        SummonRates = random.randint(1,100)

        if SummonRates >= 99:
            self.userCharacters.append(str(self.LRCharacters[LrRandomIndex]))
            return(self.LRCharacters[LrRandomIndex])
            
        elif SummonRates > 95:
            self.userCharacters.append(str(self.ssrCharacters[SSrRandomIndex]))
            return(self.ssrCharacters[SSrRandomIndex])
            
        elif SummonRates > 79:
            self.userCharacters.append(str(self.srCharacters[SrRandomIndex]))
            return(self.srCharacters[SrRandomIndex])
            
        else :
            self.userCharacters.append(str(self.RareCharacters[RareRandomIndex]))
            return(self.RareCharacters[RareRandomIndex])
            

    def MultiSummon(self):
        # Multi Summon
        # Setting rates
        SSRmaxIndex = len(self.ssrCharacters) -1
        SRmaxIndex = len(self.srCharacters) -1
        RmaxIndex = len(self.RareCharacters) -1
        LrMaxIndex = len(self.LRCharacters) -1
        LrRandomIndex = random.randint(0, LrMaxIndex)
        SSrRandomIndex = random.randint(0, SSRmaxIndex)
        SrRandomIndex = random.randint(0, SRmaxIndex)
        RareRandomIndex = random.randint(0, RmaxIndex)

        MultiSummonRates = random.randint(1,100)
        if MultiSummonRates >= 98:
            self.userCharacters.append(str(self.LRCharacters[LrRandomIndex]))
            return(self.LRCharacters[LrRandomIndex])
            
        elif MultiSummonRates > 90:
            self.userCharacters.append(str(self.ssrCharacters[SSrRandomIndex]))
            return(self.ssrCharacters[SSrRandomIndex])
            
        elif MultiSummonRates > 79:
            self.userCharacters.append(str(self.srCharacters[SrRandomIndex]))
            return(self.srCharacters[SrRandomIndex])
            
        else :
            self.userCharacters.append(str(self.RareCharacters[RareRandomIndex]))
            return(self.RareCharacters[RareRandomIndex])
                

    def ShowCharacters(self):
    # Show Characters
        self.userCharacters.sort(reverse = True)
        if len(self.userCharacters) > 0:
            for i in range(len(self.userCharacters)):
                return(self.userCharacters[i])
                
        else:
            return("No Characters in inventory")