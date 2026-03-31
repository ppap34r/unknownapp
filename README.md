# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram

### Flowchart of the main workflow
```mermaid
flowchart TD
    A["Start program"] --> B["Load saved data or seed default data"]
    B --> C["Show login menu"]

    C --> D{"Select option"}
    D -->|Student| E["Enter student ID or create new profile"]
    D -->|Admin| F["Enter admin password"]
    D -->|Exit| Z["Save data and quit"]

    E --> G{"Student found or created?"}
    G -->|No| C
    G -->|Yes| H["Show student menu"]

    H --> I{"Choose student action"}
    I -->|View catalog| J["Display course catalog"]
    I -->|Register course| K["Attempt registration"]
    I -->|Drop course| L["Attempt drop"]
    I -->|View schedule| M["Display enrolled courses"]
    I -->|Billing summary| N["Calculate tuition"]
    I -->|Edit profile| O["Update student profile"]
    I -->|Logout and save| P["Save data and return to login menu"]

    J --> H
    K --> H
    L --> H
    M --> H
    N --> H
    O --> H
    P --> C

    F --> Q{"Password correct?"}
    Q -->|No| C
    Q -->|Yes| R["Show admin menu"]

    R --> S{"Choose admin action"}
    S -->|View course catalog| T["Display course catalog"]
    S -->|View class roster| U["Display roster for selected course"]
    S -->|View all students| V["Display all students"]
    S -->|Add/Edit student| W["Create or update student"]
    S -->|Add/Edit course| X["Create or update course"]
    S -->|View student schedule or billing| Y["Display selected student details"]
    S -->|Logout and save| AA["Save data and return to login menu"]

    T --> R
    U --> R
    V --> R
    W --> R
    X --> R
    Y --> R
    AA --> C
```

### Prompts
- "Write a Python version of the 'View My Schedule' use case from a Java course enrollment system. The Python program should load students and courses from JSON files, ask for a student ID, show all currently enrolled courses, display each course's code, title, credits, and time slot, and print the total enrolled credits. Keep it as a simple standalone command-line script."

