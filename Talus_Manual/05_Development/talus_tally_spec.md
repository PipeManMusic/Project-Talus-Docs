# Talus Tally: Project Management Specification

## 1. Core Architecture
**Talus Tally** is a standalone Python middleware that decouples project management data from its presentation.
* **Data Store:** `talus_master.json` (Validated by Pydantic Schema).
* **Logic Engine:** Python backend calculating priority based on hierarchy and cost.
* **Presentation:** Markdown files (GitHub) and Android App (Shop Floor).

## 2. Priority Logic (The "Velocity" Algorithm)
Sorting is not date-based. It is calculated dynamically using two metrics:
1.  **Hierarchy Score:** Weighted importance of `SubProject` > `WorkPackage` > `Task`.
2.  **Financial Velocity:** Prioritizes "Quick Wins" to maintain momentum.
    * *Formula:* $Velocity = BudgetPriority / (EstimatedCost + 1)$
    * High Priority + Low Cost = Top of the List.

## 3. Implementation Roadmap & Status

### ✅ Phase 1: The Core Engine (Backend)
* [x] **Project Structure:** Standalone repo with `venv` and `requirements.txt`.
* [x] **Data Models:** Pydantic 4-level hierarchy (Project -> Sub -> WP -> Task).
* [x] **Schema Generator:** Automatic creation of `talus_schema.json` for editor validation.
* [x] **Logic Engine:** Priority sorting algorithm with Financial Velocity implementation.
* [x] **TDD Verification:** `tests/test_logic.py` passing for priority math.
* [x] **API Foundation:** FastAPI endpoints for `GET /tasks` and `POST /complete`.

### 🚧 Phase 2: The Translator (Data -> Docs)
* [ ] **Markdown Generator:** Python script to read `talus_master.json` and render a formatted "Roadmap" string.
* [ ] **Injector Logic:** Ability to target the specific `## Roadmap` section in `README.md` without overwriting other documentation.
* [ ] **TDD:** Verify that JSON changes correctly propagate to text files.

### 📅 Phase 3: The Shop Interface (Android)
* [ ] **App Shell:** Basic Android project setup.
* [ ] **Networking:** Retrofit client to talk to `http://<PC_IP>:8000`.
* [ ] **UI/UX:** High-contrast list view sorted by the Backend's "Global Score".

### 📅 Phase 4: Automation (The "Daily Push")
* [ ] **Git Wrapper:** `GitPython` script to stage changes to `talus_master.json` and `README.md`.
* [ ] **Commit Bot:** Logic to auto-generate commit messages (e.g., *"Completed: Install MapLibre"*).