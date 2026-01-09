from src.question_3 import gender_survival_time

def run_tests(csv_path):

    print("Running tests...\n")

    # Test 1 – check if file exists and has required columns
    try:
        print("Test: Checking file validity")
        gender_survival_time(csv_path)
        print("Test passed: File is valid and columns exist.\n")
    except FileNotFoundError:
        print("Test failed: File not found.")
    except KeyError as e:
        print(f"Test failed: Missing required column - {e}")
    except Exception as e:
        print(f"Test failed: {e}")


if __name__ == "__main__":
    try:
        run_tests("BrainTumor.csv")

    finally:
        print("All tests finished.")
