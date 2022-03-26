from ProcessLoopFor import ProcessLoop

def main():
    processLoop = ProcessLoop(range(1000,100000000,1))
    processLoop.run()

main()