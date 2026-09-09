import json
from pathlib import Path

from src.services.extractor import extract_resume


BASE_DIR = Path(__file__).resolve().parents[1]

DATASET_PATH = BASE_DIR / "evals" / "dataset.json"


def load_dataset():
    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def evaluate_case(case):

    print(f"\nRunning: {case['id']}")

    result, latency = extract_resume(
        case["input"]
    )

    expected = case["expected"]

    role_correct = (
        result.primary_role
        == expected["primary_role"]
    )

    experience_correct = (
        result.experience_level
        == expected["experience_level"]
    )

    years_correct = (
        result.years_experience
        == expected["years_experience"]
    )

    return {
        "id": case["id"],
        "expected": expected,
        "actual": {
            "primary_role": result.primary_role,
            "experience_level": result.experience_level,
            "years_experience": result.years_experience,
        },
        "scores": {
            "role_correct": role_correct,
            "experience_correct": experience_correct,
            "years_correct": years_correct,
        },
        "latency_seconds": round(latency, 2),
    }


def main():

    dataset = load_dataset()

    results = []

    for case in dataset:
        try:
            result = evaluate_case(case)
            results.append(result)

        except Exception as error:

            print(
                f"Failed {case['id']}: {error}"
            )

    # -----------------------------
    # Individual Results
    # -----------------------------

    print("\n========== EVALUATION RESULTS ==========\n")

    for result in results:

        print(f"Case: {result['id']}")

        print(
            "Role:",
            result["scores"]["role_correct"],
        )

        print(
            "Experience:",
            result["scores"]["experience_correct"],
        )

        print(
            "Years:",
            result["scores"]["years_correct"],
        )

        print(
            "Latency:",
            result["latency_seconds"],
        )

        print()

    # -----------------------------
    # Aggregate Metrics
    # -----------------------------

    total_cases = len(results)

    if total_cases == 0:
        print("No successful evaluation cases.")
        return

    role_correct_count = sum(
        result["scores"]["role_correct"]
        for result in results
    )

    experience_correct_count = sum(
        result["scores"]["experience_correct"]
        for result in results
    )

    years_correct_count = sum(
        result["scores"]["years_correct"]
        for result in results
    )

    total_latency = sum(
        result["latency_seconds"]
        for result in results
    )

    # Accuracy for each field

    role_accuracy = (
        role_correct_count / total_cases
    ) * 100

    experience_accuracy = (
        experience_correct_count / total_cases
    ) * 100

    years_accuracy = (
        years_correct_count / total_cases
    ) * 100

    # Overall field-level accuracy

    total_correct_fields = (
        role_correct_count
        + experience_correct_count
        + years_correct_count
    )

    total_fields = total_cases * 3

    overall_accuracy = (
        total_correct_fields / total_fields
    ) * 100

    average_latency = (
        total_latency / total_cases
    )

    # -----------------------------
    # Print Summary
    # -----------------------------

    print("\n========== EVALUATION SUMMARY ==========\n")

    print(f"Total Cases: {total_cases}")

    print(
        f"Role Accuracy: "
        f"{role_accuracy:.2f}%"
    )

    print(
        f"Experience Accuracy: "
        f"{experience_accuracy:.2f}%"
    )

    print(
        f"Years Accuracy: "
        f"{years_accuracy:.2f}%"
    )

    print(
        f"Overall Field Accuracy: "
        f"{overall_accuracy:.2f}%"
    )

    print(
        f"Average Latency: "
        f"{average_latency:.2f}s"
    )

    print("\n========================================")

    
    
if __name__ == "__main__":
    main()