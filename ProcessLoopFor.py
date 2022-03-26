from process import Process

class ProcessLoop(Process):
    
    def process(self):
        list_process = []
        for number in self.case:
            list_process.append(number)
            list_process.pop()
            self.count_entrance += 1