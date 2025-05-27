import sys
from simulator import Simulator

def run_simulator(file_path):
    sim = Simulator()
    try:
        with open(file_path, 'r') as f:
            for line in f:
                sim.execute(line.strip())
                if sim.last_report:
                    print(sim.last_report)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <commands.txt>")
        return
    run_simulator(sys.argv[1])

if __name__ == "__main__":
    main()
