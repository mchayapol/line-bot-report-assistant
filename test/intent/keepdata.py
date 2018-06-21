# Registration intent

class keepdata():
    def __init__(self):
        self.intent_complete = False
        self.STATE_IDLE = 0
        self.ASK_REPORT = 1000
        self.ASK_PHOTO = 400
        self.DONE = 9999
        self.var_report = ''
        self.var_photo = None

        self.current_state = self.STATE_IDLE

    def handle(self, message):
        if  self.current_state == self.ASK_REPORT:
           
            self.var_report = message
            #self.current_state = self.ASK_PHOTO
            #return "Your Photo"
        #elif self.current_state == self.ASK_PHOTO:
            #self.var_photo = message
            self.current_state = self.DONE
            return "end"
        

        if message == 'end':
           
            self.intent_complete = True
            return "save"
        elif message == 'result':
            self.current_state = self.ASK_REPORT
            return "start"
        elif message == 'next':
            self.current_state = self.ASK_REPORT
            return "start"
    
    def endIntent(self):
        return self.current_state == self.DONE

    def getCurrentState(self):
        return self.current_state
    
    def getData(self):
        return{
             
            'report':self.var_report,
            'photo':self.var_photo

        }


if __name__ == "__main__":
    rego = keepdata()

    while not rego.endIntent():
        s = input()
        o = rego.handle(s)
        print(o)

