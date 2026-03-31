sequenceDiagram
    participant User
    participant UI as Portal UI
    participant Laravel
    participant DB
    participant Queue
    participant Salesforce

    User->>UI: Compose / autosave / submit
    UI->>Laravel: POST draft or submit

    Laravel->>Laravel: Validate + Policy + EligibilityService

    Laravel->>DB: Save draft/message + transition
    Laravel->>DB: Create outbox event

    Laravel-->>UI: Success response

    Laravel->>Queue: Dispatch notification + sync jobs
    Queue->>Salesforce: Upsert correspondence

    Salesforce-->>Queue: Success / failure
    Queue->>DB: Update sync state
