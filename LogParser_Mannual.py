# log_parser.py
import re

def parse_simulation_logs(log_file_path):
    # Variables to track stats
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    failure_details = []

    print("--- Starting Log Analysis ---")

    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                # Simulating reading a massive log file
                if "TEST_START" in line:
                    total_tests += 1
                
                if "PASS" in line.upper():
                    passed_tests += 1
                elif "FAIL" in line.upper() or "ERROR" in line.upper():
                    failed_tests += 1
                    # Store the specific error line for debugging later
                    failure_details.append(line.strip())

        # Generating Summary Report
        print(f"\nTotal Tests Run: {total_tests}")
        print(f"Passed: {passed_tests}")
        print(f"Failed: {failed_tests}")
        
        if failed_tests > 0:
            print("\n[CRITICAL] Failure Summary:")
            for error in failure_details:
                print(f" -> {error}")
            print("\nAction: Please triage the failed tests.")
        else:
            print("\nAll tests passed successfully!")

    except FileNotFoundError:
        print("Error: Log file not found.")

# Dummy file creation for testing purposes
with open("sim_log.txt", "w") as f:
    f.write("TEST_START: ALU_ADD_OP\nRESULT: PASS\n")
    f.write("TEST_START: ALU_SUB_OP\nRESULT: PASS\n")
    f.write("TEST_START: ALU_DIV_OP\nERROR: Division by zero exception at time 40ns\n")
    f.write("TEST_START: MEM_WRITE\nRESULT: PASS\n")

# Run the parser
parse_simulation_logs("sim_log.txt")