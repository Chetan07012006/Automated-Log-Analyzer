import random
import datetime

# PART 1: THE GENERATOR

def generate_simulation_log(filename, num_tests=500):
    print(f"--- 1. Running Regression Suite (Simulating {num_tests} tests) ---")
    
    test_names = ["ALU_Int_Add", "ALU_Float_Div", "Cache_L1_Hit", "Cache_L2_Miss", 
                  "PCIe_Data_Transfer", "DDR_Memory_Read", "DDR_Memory_Write"]

    possible_errors = [
        "ERROR: Timing Violation at 45ns",
        "ERROR: Data Mismatch (Expected: 0x1, Got: 0x0)",
        "FATAL: Watchdog Timer Expired",
        "ERROR: Bus Protocol Violation"
    ]

    with open(filename, "w") as f:
        # Header with timestamp
        f.write(f"REGRESSION START TIME: {datetime.datetime.now()}\n")
        f.write("="*40 + "\n")

        for i in range(1, num_tests + 1):
            test = random.choice(test_names)
            
            # Logic: 90% chance PASS, 10% chance FAIL (Real world scenario)
            if random.random() > 0.10:
                f.write(f"TEST_{i:03d} : {test} ...... STATUS: PASS\n")
            else:
                error_msg = random.choice(possible_errors)
                f.write(f"TEST_{i:03d} : {test} ...... STATUS: FAIL | {error_msg}\n")
        
        f.write("="*40 + "\n")
        f.write("REGRESSION COMPLETE\n")
    
    print(f"Done! Log file '{filename}' generated with random errors.\n")


# PART 2: THE PARSER 
def analyze_log_file(filename):
    print(f"--- 2. Analyzing Logs (Automation Tool) ---")
    
    stats = {"PASS": 0, "FAIL": 0}
    failed_tests = []

    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                
                # Check keywords
                if "STATUS: PASS" in line:
                    stats["PASS"] += 1
                elif "STATUS: FAIL" in line:
                    stats["FAIL"] += 1
                    failed_tests.append(line)
        
        # --- REPORT GENERATION ---
        print("\n" + "="*30)
        print("   AUTOMATED TRIAGE REPORT   ")
        print("="*30)
        print(f"Total Tests Run : {stats['PASS'] + stats['FAIL']}")
        print(f"Passed          : {stats['PASS']}")
        print(f"Failed          : {stats['FAIL']}")
        print("-" * 30)
        
        if stats['FAIL'] > 0:
            print(f"[ATTENTION] Found {stats['FAIL']} Failures. Listing details:\n")
            for fail in failed_tests:
                parts = fail.split("|")
                test_info = parts[0].strip()
                error_info = parts[1].strip() if len(parts) > 1 else "Unknown Error"
                print(f" -> {test_info}")
                print(f"    Reason: {error_info}")
        else:
            print("Great! All tests passed.")

    except FileNotFoundError:
        print(f"Error: File {filename} not found!")


if __name__ == "__main__":
    log_file = "amd_regression_log.txt"
    generate_simulation_log(log_file)
    analyze_log_file(log_file)