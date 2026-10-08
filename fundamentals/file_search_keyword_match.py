import os
from common.files import KeywordScanner

def simulate_docs(root_dir):
    """
    Simulate the creation of documentation files in the specified root directory.

    Args:
        root_dir (str): The root directory where the documentation files will be created.

    Returns:
        None
    """
    os.makedirs(root_dir, exist_ok=True)
    sample_data = [
        ("docs/team_notes.md", "Reminder: TODO add onboarding steps.\n"),
        ("docs/legal/privacy_policy.md", "Compliant with GDRPand otherstandards."),
        ("docs/archive/old_notes.txt", "Legacy TODOs clean."),
        ("docs/dev/integratiion_guide.md", "Endpoints... TODO: Validate tokens."),
        ("docs/README.md", "Project README \n")
    ]
    for  path, content in sample_data:
        full_path = os.path.join(root_dir, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)
    print(f"Simulated docs created in '{root_dir}'")

if __name__ == "__main__":
    doc_dir = "project_docs"
    simulate_docs(doc_dir)
    scanner = KeywordScanner(
        root_dir=doc_dir,
        pattern="*.md",
        keywords=["TODO", "GDRP"]
    )

    scanner.scan_with_os_walk()
    scanner.scan_with_pathlib()
    scanner.report_result()